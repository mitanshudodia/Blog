from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name = 'article'),
    path('add_post', login_required(views.AddPostView.as_view()), name = 'add_post'),
    path('article/edit/<int:pk>', login_required(views.UpdatePost.as_view()), name='update_post'),
    path('article/<int:pk>/delete', login_required(views.DeletePostView.as_view()), name='delete_post'),
    path('add_category',views.AddCategoryView.as_view(),name = 'add_category'),
    path('category/<str:cats>/',views.categoryView,name = 'category'),
    path('category-list/',views.categoryListView,name = 'category-list'),
    path('like/<int:pk>', views.LikeView, name = 'like_post'),
    path('article/<int:pk>/comment', views.AddCommentView.as_view(), name='add_comment')
]