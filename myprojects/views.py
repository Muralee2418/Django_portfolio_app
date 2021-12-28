from django.shortcuts import render, redirect
from myprojects.models import myprojects
from django.http import HttpResponseRedirect
from django.urls import reverse
from myprojects.models import comments
from myprojects.forms import commentforms
from myprojects.models import profile



# Create your views here.
def projects_index(request):
    projects=myprojects.objects.all()
    user=request.user
    if user.is_authenticated:
        print(user.profile.likedprojects.all())
    context={
        'projects':projects
    }
    return render(request,"index.html",context)

def project_details(request,pk):
    print("inside project details")
    project=myprojects.objects.get(pk=pk)
    if request.method=="POST":
        form=commentforms(data=request.POST)
        if form.is_valid():
            newcomment=form.save(commit=False)
            newcomment.myprojects=project
            newcomment.save()
    else:
        form=commentforms()    
    comments_connected=comments.objects.filter(myprojects__pk=pk)
    for comment in comments_connected:
        print(comment.comment_info)
    context={
        'project':project,
        'author':project.author,
        'form':form,
        'comments':comments_connected
    }

    return render(request,"projectdetail.html",context)

def logout(request):
    auth.logout(request)
    return redirect("/")

def likeproject(request, pk):
    project=myprojects.objects.get(pk=pk)
    user=request.user
    if user.is_authenticated:
        print("user authenticated")
        print("request method is:"+request.method)
        print(hasattr(user,'profile'))
        if request.method=="GET":
            if hasattr(user,'profile')==False:
                proj=None
                userprofile=profile.objects.create(user=user)
                userprofile.save()
                userprofile.likedprojects.add(proj)
            else:
               userprofile=profile.objects.get(user=user)
               userprofile.likedprojects.add(project)
               userprofile.save()
               print("has attribute profile")
               return HttpResponseRedirect(reverse('projects_index'))
        else:
            print("Not GET method")
            return HttpResponseRedirect(reverse('projects_index'))
        
    else:
        print("user is not authenticated")
        return HttpResponseRedirect(reverse('projects_index'))

    

        
