from django.shortcuts import render, get_object_or_404
from .models import Artist,Song

# Create your views here.
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'TuneTracker/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'TuneTracker/song_detail.html', {'song': song})


