from django.shortcuts import render, get_object_or_404

from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    context={'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    post=get_object_or_404(posts ,pk=pid)
    
    previous_post=Post.objects.filter(created_date__gt=post.created_date,published_date__lte=timezone.now(),status=1 ).order_by('created_date').first()
    next_post=Post.objects.filter(created_date__lt=post.created_date,published_date__lte=timezone.now(),status=1 ).order_by('-created_date').first()
    
    post.counted_view=post.counted_view+1
    post.save()
    context={'post': post, 'previous_post':previous_post , 'next_post':next_post}
    
    return render(request,'blog/blog-single.html',context)

