from django.shortcuts import render
from django.views import generic
from .models import Post

# This class is to create a view to display posts on the reviews page

class PostList(generic.ListView):
    
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews.html'
    paginate_by = 4
