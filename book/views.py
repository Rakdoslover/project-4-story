from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Chapter, Comment
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


class ChapterList(generic.ListView):
    model = Chapter
    queryset = Chapter.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ChapterDetail(View):

    """ Post/get function for reviews """
    def get(self, request, slug, *args, **kwargs):
        queryset = Chapter.objects.filter(status=1)
        chapter = get_object_or_404(queryset, slug=slug)
        comments = chapter.comments.filter(approved=True).order_by(
            "-created_on"
        )

        if request.method == 'GET':

            return render(
                request,
                "chapter_detail.html",
                {
                    "chapter": chapter,
                    "comments": comments,
                    "commented": False,
                    "comment_form": CommentForm()
                },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Chapter.objects.filter(status=1)
        chapter = get_object_or_404(queryset, slug=slug)
        comments = chapter.comments.filter(approved=True).order_by(
            "-created_on"
        )

        comment_form = CommentForm(request.POST, request.FILES)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = chapter
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "chapter_detail.html",
            {
                "chapter": chapter,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm()
            },
        )


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, View):
    """ Delete a comment """
    model = Comment
    success_url = '/chapter_detail/'
