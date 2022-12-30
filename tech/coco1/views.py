from django.shortcuts import render,redirect
from django.http import HttpResponse
from coco1.form import ProfileForm,StudentForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        fname = request.POST['first name']
        lname = request.POST['last name']
        username = request.POST['user name']
        email = request.POST['email']
        passwd = request.POST['password']
        cpasswd = request.POST['conform password']

        data = member.objects.filter(username = username)

        if data:
                 return HttpResponse("user already exist")
        else:
               if passwd == cpasswd:
                   user_data = member.objects.create(f_name=fname,l_name=lname,username=username,email=email,passwd=passwd)
                   user_data.save()
                   return redirect(login)
               else:
                     return HttpResponse("password and conform password are not matching")
    return render(request,"registration.html")

def login(request):
    if request.method == 'POST':
        username =request.POST['user name']
        passwd = request.POST['password']

        data = member.objects.filter(username=username,passwd=passwd)
        if data:
            return redirect('/')
        else:
            return HttpResponse('please enter a valid user name and password')
    return render(request,'login.html')

def profile(request):
    form = ProfileForm()
    return render(request,"profile.html",{'form':form})

def profile(request):
    form = StudentForm()
    print(form)
    return render(request,"profile.html",{"form":form})
