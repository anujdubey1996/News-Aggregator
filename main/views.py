from django.shortcuts import  render, redirect
from .forms import NewUserForm
from .models import News, Category
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .models import Like
from django.contrib.auth.models import User
import random
import requests


#Like.objects.create(user= User.objects.get(username='anuj04').username, article_id='Technology Breaking!')
# Create your views here.
def home(request):
    top_three_news = News.objects.all()
    rows = len(top_three_news)
    top_three_news = top_three_news[(rows-10):(rows-7)]     
    return render(request, 'home.html', {'top_three_news':top_three_news})


def for_you(request):
    top_three_news = News.objects.all()[10:16] 
    return render(request, 'for_you.html', {'top_three_news':top_three_news})

def top_trending(request):
    top_three_news = News.objects.order_by('?')
    top_three_news = top_three_news.all()[0:6] 
    top_three_news = top_three_news
    return render(request, 'top_trending.html', {'top_three_news':top_three_news})

def bookmarks(request):
    top_three_news = News.objects.all()[1:3] 
    return render(request, 'bookmarks.html', {'top_three_news':top_three_news})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
                return redirect("login", permanent=True)
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main_login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("home")


def category_request(request,cat):
    try:
        category_news = Category.objects.get(title=cat)  
        category_news = News.objects.filter(category=category_news)[0:6] 
    except:
        category_news = []
    return render(request, 'category.html', {'category_news':category_news})

def detail(request,id):
    news=News.objects.get(pk=id)
    category=Category.objects.get(id=news.category.id)
    try:
        user_articles = Like.objects.get(user=User.username).title
        return render(request=request,template_name='article.html',context={
        'news':news,
        'category':category,
        'liked_articles':user_articles})
    except Like.DoesNotExist:
        user_articles = None
        return render(request=request,template_name='article.html',context={
        'news':news,
        'category':category,
        'liked_articles':user_articles})
   
def headlines(request):
    API_KEY = "14a8cdb3b4274fecabb4e1e67716248e"
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={key}'.format(key = API_KEY)
    response = requests.get(url)
    data = response.json()
    print(data)
    count = 0
    for news in data['articles']:
        newsData = News()
        newsData.title = news['title'] 
        newsData.article_image = news['urlToImage']
        newsData.details = news['description']
        newsData.url = news['url']
        newsData.likes = 0
        newsData.category = Category.objects.get(title = 'Headlines')
        if newsData.details is None:
            continue
        newsData.save()
        count += 1
    
    top_three_news = News.objects.all()[0:3]
    context = {
        'top_three_news':top_three_news
    }
    return render(request, 'home.html', context)

def category_headlines(request):
    API_KEY = "14a8cdb3b4274fecabb4e1e67716248e"
    url = 'https://newsapi.org/v2/top-headlines?country=us&category={cat}&apiKey={key}'.format(cat='general', key = API_KEY)
    response = requests.get(url)
    data = response.json()
    count = 0
    for news in data['articles']:
        newsData = News()
        newsData.title = news['title'] 
        newsData.article_image = news['urlToImage']
        newsData.details = news['description']
        newsData.url = news['url']
        newsData.likes = 0
        newsData.category = Category.objects.get(title = 'International')
        print("READ HERE !!!!!!!",newsData.title, newsData.details)
        if newsData.details is None:
            continue
        newsData.save()
        count += 1
    
    top_three_news = News.objects.all()[0:3]
    context = {
        'top_three_news':top_three_news
    }

    return render(request, 'get_top_headlines.html', context)