from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from demo1.form import RegisterForm,ProfileForm,UserImageForm
from demo1.models import ProjectData,Profile,UserBlog

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
          print(res)
          if res['Status'] == 'Success':
            return redirect(Userlogin)
        else:
            return HttpResponse('verification failed')

    return render(request,'Resetpass.html')



"""def CreateBlog(request):
    if request.method == "POST":
         Topic = request.POST['Topic']
         caption = request.POST['caption']
         blog_data = request.POST['blog_data']
         data = UserBlog.objects.create(Topic=Topic,caption=caption,images=url('indian.jpeg'),user=request.user.id)
         data.save()
         return redirect(home)
    return render(request,'createblog.html')"""


def CreateBlog(request):
    form = UserImageForm()
    if request.method == 'POST':
        form = UserImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            img_object = form.instance
            return render(request,'createblog.html',{'form':form,'img_object':img_object})

    return render(request,'createblog.html',{'form':form})


def ViewBlog(request):
    context = {
        'user': request.user
    }
    return render(request,'viewblog.html',context)


def createprofile(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        DOB = request.POST['DOB']
        city = request.POST['city']
        address = request.POST['address']
        data =Profile.objects.create(phone=phone,DOB=DOB,city=city,address=address),ProjectData.objects.create(first_name=first_name,last_name=last_name,email=email)
    return render(request,'createpro.html')










