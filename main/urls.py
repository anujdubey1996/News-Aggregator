from django.urls import path, re_path
from . import views

#to add media/static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('headlines', views.headlines, name='headlines'),   
    path('login', views.login_request, name='login'),
    path("register", views.register_request, name="register"),
    path("for-you", views.for_you, name="for-you"),
    path("top-trending", views.top_trending, name="top-trending"),
    path("bookmarks", views.bookmarks, name="bookmarks"),
    path("logout", views.logout_request, name= "logout"),
    path('<int:id>',views.detail,name='article'),
    path('<str:cat>',views.category_request,name='category'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
