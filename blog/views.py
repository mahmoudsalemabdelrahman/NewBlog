from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Post
from .forms import PostForm



def post_list(request):
    post_list= Post.objects.filter(active=True)

    context ={'post_list':post_list}
    return render(request, 'post_list.html', context)


def post_detail(request, slug):
    post_detail= get_object_or_404(Post, slug=slug)
    
    context = {'post_detail':post_detail}
    return render(request, 'post_detail.html', context)


@login_required
def create_post(request):

    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():        
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('blog:post_list')


    else:
        form =PostForm()

    context = {'form':form}
    return render(request, 'create_post.html', context)


def edit_post(request, slug):
     edit_post = get_object_or_404(Post, slug=slug)
     if request.method=='POST':
        form = PostForm(request.post, request.FILES, instance= edit_post)
        if form.is_valid():
            
            form.save()


     else:
        form =PostForm(instance= edit_post)

     context = {'form':form}
     return render(request, 'edit_post.html', context)


