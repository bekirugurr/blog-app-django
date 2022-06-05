from django.shortcuts import render, redirect
from .forms import NewPostForm, CommentForm
from .models import Post, Category, Comment, Like, PostView
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
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
        if  PostView.objects.filter(post_id=post.id):
            post.view_num  = PostView.objects.get(post_id=post.id).time_tamp 
        else:
            post.view_num = 0
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
            messages.success(request, "New post added succesfully")
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'post/new_entry.html', context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    post.writer_name = User.objects.get(id=post.writer_id).username
    publish_time = post.publish_date
    post.elapsed_time = elapsed_time(publish_time)
    post.comment_num = Comment.objects.filter(post_id=post.id).count()  
    if  PostView.objects.filter(post_id=post.id):
        view_ins = PostView.objects.get(post_id=post.id)
        view_ins.time_tamp += 1
        view_ins.save() 
    else:
        view_ins = PostView(post_id=post.id, time_tamp=1)
        view_ins.save()
    post.view_num = view_ins.time_tamp
    post.like_num = Like.objects.filter(post_id=post.id).count()
    post.comments = Comment.objects.filter(post_id=post.id) 
    post.who_liked_id_arr = []
    for i in Like.objects.filter(post_id=post.id):
        post.who_liked_id_arr.append(i.who_liked_id)  
    for comment in post.comments:
        comment.elapsed_time = elapsed_time(comment.date_stamp)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_data = form.save()
            comment_data.post_id = post.id
            comment_data.commenter_id = request.user.id
            comment_data.save()
            messages.success(request, 'New comment added succesfully')
            return redirect('detail', slug=slug)
            #return redirect(f'/detail/{slug}/')
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'post/detail.html', context)

def post_delete(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted succesfully')
        return redirect('home')
    context= {
        'post' : post
    }
    return render(request, 'post/post_delete.html', context)

def change_like(request, slug):
    post = Post.objects.get(slug=slug) 
    liked_id = 0
    for i in  Like.objects.filter(post_id=post.id):
        if i.who_liked_id ==  request.user.id: 
            liked_id = i.id
    if liked_id:
        instance = Like.objects.get(id=liked_id)
        instance.delete()
    else:
        instance = Like(post_id=post.id, who_liked_id=request.user.id)
        instance.save()
    #* alttaki redirect satırıyla detail sayfasını yeniden yüklüyeceği için görülme saysını bir artıracak, alttaki üç satırla okundu sayısının gereksiz artması engelleniyor
    view_ins = PostView.objects.get(post_id=post.id)
    view_ins.time_tamp -= 1
    view_ins.save()
    return redirect('detail', slug=slug)
    #return redirect(f'/detail/{slug}/')
    
def post_update(request, slug):
    post = Post.objects.get(slug=slug) 
    form = NewPostForm(instance=post)
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            entry = form.save()
            if "post_pic" in request.FILES:
                entry.post_pic = request.FILES.get('post_pic') 
            entry.save()
            messages.success(request, "Post updated succesfully")
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'post/update.html', context)

