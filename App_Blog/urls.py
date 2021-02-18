from django.urls import path
app_name = 'App_Blog'
from App_Blog import views
urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>',views.blog_details, name='blog_details'),
    path('liked/<pk>/',views.liked, name='liked_post'),
    path('unliked/<pk>/',views.unliked, name='unliked_post'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blog'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
]