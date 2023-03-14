from django.shortcuts import render, HttpResponse

# Create your views here.

from .models import Student
# View
# class based view
# function based view

# view - function based view
# def welcome(request):           #reserved keyword #business logic
#     studs = Student.objects.get(id = 1)
#     return HttpResponse(f"Welcome to Django Application...!!, {studs}")

# studs = Student.objects.all()     #this will not work as HttpResponse respons to string
# def welcome(request):
#     print(request.method)               # GET
#     print(request.user)                 # Rajendra
#     print(request.GET)
#     print(type(request.GET["age"]))
#     studs = list(Student.objects.values("name"))
#     final_studs = list(map(lambda x: x["name"], studs))
#     return HttpResponse(f"Welcome to Django Application..!!, {final_studs}")

# output
# GET
# AnonymousUser
# <QueryDict: {'name': ['abc'], 'surname': ['pqr'], 'age': ['28']}>
# 28

def welcome(request):
    return render(request,"home.html")      # hyper text markup language

# query params - Query Parameters
# afetr url http://127.0.0.1:8000/home/?name=abc&surname=pqr&age=28
# query set to client side & to access from server side write a statement print(request.GET) 
# then click on send button to postman application then in vs code we will get output in dictionary format.
# <QueryDict: {'name': ['abc'], 'surname': ['pqr'], 'age': ['28']}>
# print(request.GET)
# print(request.GET["age"])
# <QueryDict: {'name': ['abc'], 'surname': ['pqr'], 'age': ['28']}>
# 28        # to get age 