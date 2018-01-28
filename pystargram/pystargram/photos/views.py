from django.shortcuts import render
from .models import Photo
from django.shortcuts import get_object_or_404

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    context = dict()
    context['photo'] = photo
    return render(request, 'photos/detail.html', context)