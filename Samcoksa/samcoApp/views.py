from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    obj = About.objects.all().order_by('-id')[:1]
    obj1 = Service.objects.all().order_by('-id')[:6]
    obj2 = ContactU.objects.all().order_by('-id')[:1]
    obj3 = Team.objects.all().order_by('-id')[:1]
    context = {
        "data": obj,
         "data1": obj1,
         "data2": obj2,
         "team": obj3,
    }
    try:
        if request.method == 'POST':
            contact = Contact()
            if request.POST['name'] and request.POST['email'] and request.POST['subject'] and request.POST['message']:
                contact.name = request.POST['name']
                contact.email = request.POST['email']
                contact.subject = request.POST['subject']
                contact.message = request.POST['message']
                contact.save()
                messages.info(request, "Your message has been sent. Thank you!")

            else:
                messages.error(request, "Somethings went Wrong!")
    except:
        messages.info(request,"The requested data is too Big!")

    return render(request,'index.html', context)


# def profile(request,id):
#     obj = Service.objects.get(id = id)
#
#
#     context ={
#         "data":obj,
#
#     }
#     return  render(request,'profile.html',context)
# def profile(request,id):
#
#     # try:
#     #     if request.method == 'POST':
#     #         contact = Contact()
#     #         if request.POST['name'] and request.POST['email'] and request.POST['subject'] and request.POST['message']:
#     #             contact.name = request.POST['name']
#     #             contact.email = request.POST['email']
#     #             contact.subject = request.POST['subject']
#     #             contact.message = request.POST['message']
#     #             contact.save()
#     #             messages.info(request, "Your message has been sent. Thank you!")
#     #         else:
#     #             messages.error(request, "Somethings went Wrong!")
#     #         return redirect('/')
#     # except:
#     #     messages.info(request,"The requested data is too Big!")
#     obj = Service.objects.get(id=id)
#     context = {
#         "data": obj
#     }
#     return  render(request,'profile.html',context)

def profile(request,id):
    obj = Service.objects.get(id = id)
    context ={
        "data":obj
    }
    return  render(request,'profile.html',context)