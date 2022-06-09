from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewPostForm, CommentForm
from .models import Post, Category, Comment, Like, PostView
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    for post in posts:
        post.writer_name = User.objects.get(id=post.writer_id).username
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

@login_required(login_url='user_login')
def new_entry(request):
    form = NewPostForm()
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
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
    post = get_object_or_404(Post, slug=slug)
    #post = Post.objects.get(slug=slug) 
    post.writer_name = User.objects.get(id=post.writer_id).username
    publish_time = post.publish_date
    post.comment_num = Comment.objects.filter(post_id=post.id).count()  
    post.who_viewed_id_arr = []
    for i in PostView.objects.filter(post_id=post.id):
        post.who_viewed_id_arr.append(i.who_viewed_id)
    if not request.user.id in post.who_viewed_id_arr: 
        view_ins = PostView(post_id=post.id, who_viewed_id=request.user.id)
        view_ins.save()
    post.view_num = PostView.objects.filter(post_id=post.id).count()
    post.like_num = Like.objects.filter(post_id=post.id).count()
    post.comments = Comment.objects.filter(post_id=post.id) 
    post.who_liked_id_arr = []
    for i in Like.objects.filter(post_id=post.id):
        post.who_liked_id_arr.append(i.who_liked_id)  
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_data = form.save(commit=False)
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


@login_required(login_url='user_login')
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

@login_required(login_url='user_login')
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
    return redirect('detail', slug=slug)
    #return redirect(f'/detail/{slug}/')

@login_required(login_url='user_login')
def post_update(request, slug):
    post = Post.objects.get(slug=slug) 
    form = NewPostForm(instance=post)
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            if "post_pic" in request.FILES:
                entry.post_pic = request.FILES.get('post_pic') 
            entry.save()
            messages.success(request, "Post updated succesfully")
            return redirect('home')
    context = {
        'form' : form,
        'post' : post,
    }
    return render(request, 'post/update.html', context)

def about_me(request):
    return render(request, 'about.html')
    