from django.shortcuts import render


# Create your views here.
# Hello view that passes text from the function
# to the template
def hello(request):
    return render(request, "spotify/hello_world.html", {"text": "Hello, world!!!"})
