from django.shortcuts import render
from .models import Contact, ContactInformation, HomeInformation, Testimonial


# Create your views here.
def home(request):     #function based view
    view ={}
    view['welcome'] = HomeInformation.objects.all()
    view['test'] = Testimonial.objects.all()
    return render(request,'index.html',view)      #views index.html on browser



def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request,'services.html')

def blog_home(request):
    return render(request,'blog-home.html')

def blog_single(request):
    return render(request,'blog-single.html')

def elements(request):
    return render(request,'elements.html')

def contact(request):
    view = {}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        data=Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
        view['success']= "The message is submitted."


    view['info']= ContactInformation.objects.all()

    return render(request,'contact.html',view)