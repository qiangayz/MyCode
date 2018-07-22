from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        return HttpResponse(username+pwd)
    return  render(request,'index.html')