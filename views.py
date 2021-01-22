from django.shortcuts import render, get_object_or_404

from .models import Photo


def album(request):
    photos = Photo.objects
    return render(request, 'album.html', {'photos': photos})


async def details(request, photo_id):
    photo_detail = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'details.html', {'photo': photo_detail})
