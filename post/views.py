from django.shortcuts import render , redirect
from .models import Post
from .forms import Post_form
# Create your views here.


def post_list(request):
    
    all_posts= Post.objects.all()

    return render(request,'registration/Post_list.html',{'postlist':all_posts})


def post_details(request,post_id):
    
    post= Post.objects.get(id = post_id)

    return render(request,'registration/post_details.html',{'singlepost':post})


def new_post(request):
    if request.method=='POST':
        form=Post_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/posts")
    
    else :
        form=Post_form
        return render(request,'registration/newpost.html',{'form':form})


def edite_post(request,post_id):
    post=post.objects.get(id=post_id)
    if request.method=='POST':
        form=Post_form(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            
    
    else :
        form=Post_form(instance=post)
        return render(request,'registration/editepost.html',{'form':form})
