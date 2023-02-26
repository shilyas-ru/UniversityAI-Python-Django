from django.urls import path

from app_blog import views

app_name = 'my_blog_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('post/<int:id>/', views.post_view, name='post'),
    path('empty/', views.main_empty_view, name='empty_index'),
    path('empty/about/', views.about_empty_view, name='empty_about'),
    path('empty/contact/', views.contact_empty_view, name='empty_contact'),
    path('empty/post/', views.post_empty_view, name='empty_post'),
    path('cat/list/', views.Categories_ListView.as_view(), name='cat_list'),
    path('cat/detail/<int:pk>/', views.Categories_DetailView.as_view(), name='cat_detail'),
    path('cat/create/', views.Categories_CreateView.as_view(), name='cat_create'),
    path('cat/update/<int:pk>/', views.Categories_UpdataView.as_view(), name='cat_update'),
    path('cat/delete/<int:pk>/', views.Categories_DeleteView.as_view(), name='cat_delete'),
]
