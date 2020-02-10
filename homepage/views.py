from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Member, Value, Event
from .forms import PostForm

def event_list(request):
    upcoming_events = Event.objects.filter(ate__lte=timezone.now()).order_by('date')
    return render(request, 'homepage/event_list.html', {'events': upcoming_events})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # We only want to show board members in this view
    members = Member.objects.filter(is_board_member=True)
    return render(request, 'homepage/post_list.html', {
        'posts': posts,
        'members': members,
        })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'homepage/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'homepage/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'homepage/post_edit.html', {'form': form})