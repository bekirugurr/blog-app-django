from msilib.schema import PublishComponent
from django.shortcuts import render, redirect
from .forms import NewPostForm
from .models import Post, Category, Comment, Like, PostView
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from .functions import elapsed_time

def home(request):
    posts = Post.objects.all()
    for post in posts:
        post.writer_name = User.objects.get(id=post.writer_id).username
        publish_time = post.publish_date
        post.elapsed_time = elapsed_time(publish_time)
        if Profile.objects.get(user_id=post.writer_id).profile_pic:
            post.writer_pic = Profile.objects.get(user_id=post.writer_id).profile_pic
        else:
            post.writer_pic = False
        post.comment_num = Comment.objects.filter(post_id=post.id).count()
        post.view_num = PostView.objects.filter(post_id=post.id).count()
        post.like_num = Like.objects.filter(post_id=post.id).count()
        post.who_liked_id_arr = []
        for i in Like.objects.filter(post_id=post.id):
            post.who_liked_id_arr.append(i.who_liked_id)

    context = {
        'posts' : posts,
    }
    return render(request, 'post/home.html', context)


def new_entry(request):
    form = NewPostForm()
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save()
            entry.writer_id = request.user.id
            if "post_pic" in request.FILES:
                entry.post_pic = request.FILES.get('post_pic') 
            entry.save()
            messages.success(request, "New Post Added Succesfully")
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'post/new_entry.html', context)
