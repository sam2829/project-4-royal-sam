from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, ReviewForm
from django.contrib import messages

# This class is to create a view to display posts on the reviews page


class PostList(generic.ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews.html'
    paginate_by = 4


# This class is to create a view so the user can see the entire post / review when clicked

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    # This is the view to post our comment form

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'You have succesfully left a comment.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

# This view is for being able to like posts / reviews


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_details', args=[slug]))


# This class is to view for the user to post a review


class LeaveReview(View):

    def get(self, request):

        return render(request, 'leave_review.html',
                      {
                          "review_form": ReviewForm(),
                      })

    def post(self, request):

        review_form = ReviewForm(data=request.POST, files=request.FILES)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.email = request.user.email
            review.name = request.user.username
            review.author = request.user
            review.slug = review_form.cleaned_data['title'].replace(' ', '-')

            if 'featured_image' in request.FILES:
                review.featured_image = request.FILES['featured_image']

            review.save()
            messages.success(request, 'You have succesffully left a review and '
                             'is awaiting approval.')
            return redirect('reviews')
        else:

            messages.warning(request, 'Something went wrong, please try again.')
            return render(
                request,
                "leave_review.html",
                {
                    "review_form": ReviewForm(),
                },
            )
