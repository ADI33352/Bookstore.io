from django.urls import path
from books import views

urlpatterns = [
    path ('',views.index,name='index'),
    path ('about/',views.about,name='about'),
    path ('library/',views.library,name='library'),
    path ('contact/',views.contact,name='contact'),
    path ('books/',views.books,name='books'),
    path ('detail/',views.detail,name='deatil'),
   
]