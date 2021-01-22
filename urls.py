from django.urls import path

from .import views


urlpatterns = [
    path('photos', views.album, name='album'),
    path('photos/<int:photo_id>', views.details, name='details')
]
