from django.shortcuts import render, get_object_or_404

from blog.models import Post
import datetime

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(published_date__lte=datetime.datetime.now())
    context={'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test(request,pid):
    post=get_object_or_404(Post,pk=pid)
    post.counted_view=post.counted_view+1
    post.save()
    context={'post': post}
    return render(request,'test.html',context)