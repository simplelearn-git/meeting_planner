from django.shortcuts import render
from meetings.models import Meeting
# Create your views here.


def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
