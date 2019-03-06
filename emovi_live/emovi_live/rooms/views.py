from django.shortcuts import render
from rooms.models import ChatRoom

# Create your views here.
from django.shortcuts import render_to_response

def search_form(request, t):
    chatRoom = ChatRoom(name=str(t))
    chatRoom.save()
    return render_to_response('rooms/search_form.html')
