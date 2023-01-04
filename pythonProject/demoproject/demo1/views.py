from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from demo1.form import RegisterForm,ProfileForm
from demo1.models import ProjectData

import requests
# Create your views here.

def home(request):
        return render(request,'home.html')
def testing(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))


def UserRegister(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Userlogin)
    return render(request,'register.html',{"form":form})


def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(username=username,password=passwd)
        if user is not None:
            login(request,user)
            print(request.user.username)
            return redirect(home)
        else:
            return redirect(Userlogin)
            return HttpResponse('<h1> invalid username and password</h1>')
    return render(request,'login.html')

def User_logout(request):
    logout(request)
    return redirect(Userlogin)


def Forgot_Password(request):
    if request.method == "POST":
        mobile = request.POST['phone']
        userdata = profile.objects.get(phone=mobile)
        if userdata:
          url = "https://2factor.in/API/V1/e102c85c-7c4d-11ed-9158-0200cd936042/SMS/{}/AUTOGEN".format(str(mobile))

          payload = ""
          headers = {}
          response = requests.request('GET',url,headers=headers,data=payload)
          res = response.json()
          if res['Status'] == 'Success':
            return redirect(Userlogin)
        else:
            return HttpResponse('verification failed')

    return render(request,'Resetpass.html')





"""def upload_image(request):
    if request.method == "POST" and request.FILES['images']:
        upload = request.FILES['images']
        fss = FileSystemStorage()
        file = fss.save(upload.name,upload)
        file_url = fss.url(file)
        profile.objects.filter(user_id=request.user.id.update(profile_pic=file_url))
        return redirect('home')
    
    return render(request,'propic.html')"""

