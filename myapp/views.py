from django.shortcuts import render

# Create your views here.
def index(request):
    result = ""
    if request.method == "GET":
        if request.GET.get("sub") == "ping":
            result = "pong!"
    return render(request, "myapp/index.html", {'result': result})