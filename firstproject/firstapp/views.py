from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import Reservation



# function based-view 
def hello_world(request): 
    return HttpResponse ("Hello World!")

# class based view
class HelloEthiopia(View): 
    def get (self, request):
        return HttpResponse("Hello Ethiopia")
    
def home(request): 
    form = Reservation()

    if request.method == 'POST': 
        form = Reservation(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse ("Success")

    return render(request, 'index.html', {'form' : form})    