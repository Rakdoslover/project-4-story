from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Chapter


class ChapterList(generic.ListView):
    model = Chapter
    queryset = Chapter.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ChapterDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Chapter.objects.filter(status=1)
        chapter = get_object_or_404(queryset, slug=slug)
        comments = chapter.comments.filter(approved=True).order_by("-created_on")
        
        return render(
            request,
            "post_detail.html",
            {
                "chapter": chapter,
                "comments": comments,
            },
        )
