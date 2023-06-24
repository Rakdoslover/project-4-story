from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Chapter, Review
from .forms import ReviewForm


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
        reviews = chapter.reviews.filter(approved=True).order_by(
            "-created_on"
        )

        if request.method == 'GET':

            return render(
                request,
                "chapter_detail.html",
                {
                    "chapter": chapter,
                    "reviews": reviews,
                    "reviewed": False,
                    "review_form": ReviewForm()
                },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Chapter.objects.filter(status=1)
        chapter = get_object_or_404(queryset, slug=slug)
        reviews = chapter.reviews.filter(approved=True).order_by(
            "-created_on"
        )

        review_form = ReviewForm(request.POST, request.FILES)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            # comment = chapter.comments.all()
            review.post = chapter

            review.save()

        else:
            review_form = ReviewForm()

        return render(
            request,
            "chapter_detail.html",
            {
                "chapter": chapter,
                "reviews": reviews,
                "reviewed": True,
                "review_form": ReviewForm()
            },
        )


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, View):
    """ Delete a review """
    model = Review
    success_url = '/chapter_detail/'

    def test_func(self):
        return self.request.user == self.get_object().user
