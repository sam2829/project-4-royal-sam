from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

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
                "liked": liked
            },
        )
