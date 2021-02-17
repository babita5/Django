from django.shortcuts import render

# Create your views here.
def home(request):     #function based view
    return render(request,'index.html')      #views index.html on browser
