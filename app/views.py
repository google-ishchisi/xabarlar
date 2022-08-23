from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import New, Category, Region
from django.views.generic import ListView

def index(request):
    latest_new = New.objects.filter().order_by('-id')[0:1]
    other_new = New.objects.filter().order_by('-id')[1:10]
    categorys = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'latest_new': latest_new,
        'other_new':other_new,
        'categorys': categorys,
        'regions':regions,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    news= New.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = New.objects.filter(category=category).exclude(id=id)
    other_news = New.objects.filter().order_by('-id')[0:9]
    regions = Region.objects.all()
    categorys = Category.objects.all()
    context = {
        'news':news,
        'category':category,
        'rel_news':rel_news,
        'other_news':other_news,
        'categorys': categorys,
        'regions':regions,
    }
    return render(request, 'detail.html', context)


def region(request, id):
    region = Region.objects.get(id=id)
    new = New.objects.filter(region=region)
    categorys = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'region':region,
        'news': new,
        'categorys': categorys,
        'regions':regions,
    }
    return render(request, 'region.html', context)

def category(request, id):
    category = Category.objects.get(id=id)
    new = New.objects.filter(category=category)
    categorys = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'category':category,
        'news': new,
        'categorys': categorys,
        'regions':regions,
    }
    return render(request, 'category.html', context)


def blog(request):
    news = New.objects.order_by('-id')[0:]
    categorys = Category.objects.all()
    regions = Region.objects.all()
    context={
        'new': news,
        'categorys': categorys,
        'regions':regions,
    }
    return render(request, 'blog.html', context)


# --------------------------------------------------
def register(request):
    if request.method == "POST":
        first_name = request.POST['ism']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username bazada bor !!!")#  username bazada bor
                redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email royhatdan otgan !!!")# email royhatdan otgan
                redirect('register/')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password1)
                user.save()
                messages.success(request, "Royhatdan o'tdingiz !!!")
                return redirect('index')
        else:
            messages.info(request, "Parollar bir xil emas !!!")
            redirect('register/')

    return render(request, 'register.html')


def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga kirdingiz !!!")
            return redirect('index')
    context = {}
    return render(request, 'login.html', context)

def Logout(request):
    logout(request)
    return redirect('login')
        
def Search(request):
    if request.method == 'POST':
        search_txt = request.POST['q']
        categorys = Category.objects.all()
        regions = Region.objects.all()
        if search_txt:
            post = New.objects.filter(Q(title__icontains=search_txt) | Q(body__icontains=search_txt) | Q(sumary__icontains=search_txt))
            context = {
                'post': post,
                'categorys': categorys,
                'regions':regions,
            }
            return render(request, 'search.html', context)
        else:
            messages.error(request, 'Malumot topilmadi')
            return redirect('index')
    else:
        return redirect('index')



