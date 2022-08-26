from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='blog_post_detail'),
    path('post/new/', views.BlogCreatePostView.as_view(), name='add_blog_post'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete_blog_post'),
]
