from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    all_post = Post.objects.all()
    
    context = {"all_post": all_post}
    return render(request, "myapp/home.html",context)


def contact(request):
    return render(request, "myapp/contact.html")

def about(request):
    return render(request, "myapp/about.html")

def Regidter(request):

    context = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        check = User.objects.filter(username=email)

        if len(check) == 0:
           newuser=User()
           newuser.username = email
           newuser.first_name = name
           newuser.set_password(password)
           newuser.save()
           context['success'] = 'success'
        else:
            context['usertaken'] = 'usertaken'



    return render(request,'myapp/register.html',context)

def Login(request):

    context = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        email = data.get('email')
        password = data.get('password')

        check = User.objects.filter(username=email)

        if len(check) == 0:
           context['nouser'] = 'nouser'
        else:
            try:
                user = authenticate(username=email,password=password)
                login(request,user)
                print('login completed')
                return redirect('home-page')
            except:
                context['wrongpassword'] = 'wrongpassword'



    return render(request,'myapp/login.html',context)