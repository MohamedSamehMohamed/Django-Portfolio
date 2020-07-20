from django.shortcuts import render, get_object_or_404
from .models import Blog
def all_blogs(request):
    Blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'Blogs' : Blogs});

def some_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/some_blog.html', {'blog' : blog})
