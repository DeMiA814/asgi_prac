from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html', {})

def room(request, room_name):
    return render(request, 'myapp/room.html', {
        'room_name': room_name
    })