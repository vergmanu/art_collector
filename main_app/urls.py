from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('art/', views.art_index, name='index'),
    path('art/<int:a_id>/', views.art_detail, name='detail'),
    path('art/create/', views.ArtCreate.as_view(), name='art_create'),
    path('art/<int:pk>/update/', views.ArtUpdate.as_view(), name='art_update'),
    path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name='art_delete'),
    path('art/<int:a_id>/add_comment/', views.add_comment, name='add_comment'),
    path('art/<int:a_id>/assoc_gallery/<int:gallery_id>/', views.assoc_gallery, name='assoc_gallery'),
    path('art/<int:a_id>/unassoc_gallery/<int:gallery_id>/', views.unassoc_gallery, name='unassoc_gallery'),
    path('galleries/', views.GalleryList.as_view(), name='galleries_index'),
    path('galleries/<int:pk>/', views.GalleryDetail.as_view(), name='galleries_detail'),
    path('galleries/create/', views.GalleryCreate.as_view(), name='galleries_create'),
    path('galleries/<int:pk>/update/', views.GalleryUpdate.as_view(), name='galleries_update'),
    path('galleries/<int:pk>/delete/', views.GalleryDelete.as_view(), name='galleries_delete'),
]