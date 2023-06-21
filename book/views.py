from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Chapter
from .forms import CommentForm


class ChapterList(generic.ListView):
    model = Chapter
    queryset = Chapter.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ChapterDetail(View):

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

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment = chapter.comments.all()
            comment.save()
            return redirect(request, 'chapter_detail.html')
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
