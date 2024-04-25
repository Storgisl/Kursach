from django.shortcuts import render
from .models import Video
def videos(request):
    video = Video.objects.all()
    context = {"video": video}
    return render(request, "videos/v.html", context=context)