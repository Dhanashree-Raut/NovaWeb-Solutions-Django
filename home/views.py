from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact

def default(request):
    # return HttpResponse("Hello, world. You're at the hoem/user index.")
    # return HttpResponse("<h1>Hello Home</h1")
    context = {
        "name" : "Dhanashree",
        "course" : "Django",
    }
    return render(request,'home.html' , context)


def project(request):
    # return HttpResponse("Hello, world. You're at the hoem/user index.")
    # return HttpResponse("<h1>Project</h1")
    return render(request,'project.html')


def about(request):
    # return HttpResponse("Hello, world. You're at the hoem/user index.")
    # return HttpResponse("<h1>About</h1")
    return render(request,'about.html')

def services(request):
    return render(request, "services.html")

def portfolio(request):
    return render(request, "portfolio.html")



def contact(request):

    # Check Type of Request
    if request.method=="POST":
        # print (request.POST)
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['desc']
        phone = request.POST['phone']
        
        entry = Contact(name=name , phone =phone , email=email , message=msg)
        entry.save()
        
        print("DATA IS SAVED")
        print( name , email  , phone , msg )
        


    return render(request,'contact.html')


