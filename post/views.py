from django.shortcuts import render, redirect
from .forms import NewPostForm
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.
def home(request):
    # posts = Post.objects.all()
    # context = {
    #     'posts' : posts
    # }
    return render(request, 'post/home.html',)


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
