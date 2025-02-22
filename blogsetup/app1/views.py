from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import *
from django.contrib import messages
import os,time
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home1(request):
    # for latest 1 we use [::-1]
    home = Home.objects.all()
    cat = Catagory.objects.all()
    allpost = Post.objects.all()[0:7]
    recentpost = Post.objects.all()[0::-1]

    sort = request.GET.get("catagories")
    if sort:
        home = Home.objects.all()
        cat = Catagory.objects.all()
        sortedpost = Post.objects.filter(category = sort )
        return render(request, "index.html", {"post1": sortedpost, "home": home, "cat": cat})
    else:
        return render(request,"index.html",{"rcposts":recentpost,"post":allpost,"home":home,"cat":cat})

def home(request):
    home = Home.objects.all()
    cat = Catagory.objects.all()
    allpost = Post.objects.all()[0:7]
    recentpost = Post.objects.all()[0::-1]
    sort = request.GET.get("catagories")
    if sort:
        home = Home.objects.all()
        cat = Catagory.objects.all()
        sortedpost = Post.objects.filter(category=sort)
        return render(request, "index.html", {"post1": sortedpost, "home": home, "cat": cat})
    else:
        return render(request, "index.html", {"rcposts": recentpost, "post": allpost, "home": home, "cat": cat})

def all_blogs(request):
    home = Home.objects.all()
    cat = Catagory.objects.all()
    allpost = Post.objects.all()[::-1]
    return render(request,"blog.html",{"home":home,"cat":cat,"allpost":allpost})

def contact(request):
    if request.method == "GET":
        home = Home.objects.all()
        cat = Catagory.objects.all()
        return render(request,"contact.html",{"home":home,"cat":cat})
    else:
        fnm = request.POST["T1"]
        lnm = request.POST["T2"]
        em = request.POST["T3"]
        sbj = request.POST["T4"]
        ms = request.POST["T5"]

        obj = Contact()
        obj.first_name = fnm
        obj.last_name = lnm
        obj.email = em
        obj.subject = sbj
        obj.message = ms

        obj.save()

        messages.success(request,"Message Sent Sucessfully")

        return redirect("../contact/")

def catagories(request):
    home = Home.objects.all()
    cat = Catagory.objects.all()
    return render(request, "category.html",{"home":home,"cat":cat})

def this_blog(request,slug):
    home = Home.objects.all()
    cat = Catagory.objects.all()
    post = Post.objects.filter(slug=slug).first()
    cmnts = Comment.objects.all()

    if request.method == "POST":
        nm = request.POST["T1"]
        em = request.POST["T2"]
        web = request.POST["T3"]
        msg = request.POST["T6"]
        cmnt = Comment(name=nm,email=em,website=web,message=msg)
        cmnt.save()
        messages.success(request,"Comment Successfully Added")
        return redirect("../home/")
    return render(request, "single.html",{"home":home,"cat":cat,"post":post,"comments":cmnts})



