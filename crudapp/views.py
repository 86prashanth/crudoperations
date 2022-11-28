from django.shortcuts import render,HttpResponseRedirect
from .forms import Studentregistartion
from .models import User
# Create your views here.
# this function will add new item and show all items
def add_show(request):
    if request.method=='POST':
        fm=Studentregistartion(request.POST,request.FILES)
        if fm.is_valid():
            #fm.save()
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            image=fm.cleaned_data['image']
            reg=User(name=name,email=email,password=password,image=image)
            reg.save()
            fm=Studentregistartion()
    else:
        fm=Studentregistartion()   
    stud=User.objects.all()
    return render(request,'app/addandshow.html',{'form':fm,'stu':stud}) 

# this function will update/edit
def update_data(request,id):
    if request.method=='POST':
     pi=User.objects.get(pk=id)
     fm=Studentregistartion(request.POST,instance=pi)
     if fm.is_valid():
        fm.save()
    else:
     pi=User.objects.get(pk=id)
     fm=Studentregistartion(instance=pi)
    return render(request,'app/update.html',{'form':fm})

# this function will delete

def delete_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
