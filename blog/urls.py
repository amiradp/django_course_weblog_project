from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('add/', views.PostCreateView.as_view(), name='add_new_post'),
    path('<int:pk>/', views.PostDetailViews.as_view(), name='detail_views'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
]
