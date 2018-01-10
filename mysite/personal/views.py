from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')
def addpost(request):
    return  render(request,'personal/post/addpost.html')
def postlist(request):
    return render(request,'personal/post/postlist.html')
def inbox (request):
    return render(request,'personal/inbox/inbox.html')