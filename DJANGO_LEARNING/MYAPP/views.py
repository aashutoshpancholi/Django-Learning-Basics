from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

def error_404_view(request,exception):
    return render(request,'error404page.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    return HttpResponse("<h1>INDEX FUNCTION</h1>")

def second(request):
    return HttpResponse("<h1>ABOUT FUNCTION</h1>")

def add(request, a, b):
    return HttpResponse(a + b)

def intro(request, name, age):
    dict1 = {
        "name": name,
        "age": age
    }
    return JsonResponse(dict1)

def myfirstpage(request):
    return render(request, 'index.html')

def mysecondpage(request):
    return render(request, 'second.html')

def mythirdpage(request):
    var = "Hello, My Name is Aashutosh.."
    greeting = "My Subjects are as below : ?"
    subjects = ["Python", "HTML", "CSS", "JavaScript"]
    num1, num2 = 10, 20
    ans = num1 > num2
    # print(ans)
    dict2 = {
        "var": var,
        "msg": greeting,
        "subjects": subjects,
        "num1": num1,
        "num2": num2,
        "ans": ans,
    }
    return render(request, 'add.html', context=dict2)

def myimagepage1(request):
    return render(request, 'myimagepage1.html')

def myimagepage2(request):
    return render(request, 'myimagepage2.html')

def myimagepage3(request):
    return render(request, 'myimagepage3.html')

def myimagepage4(request):
    return render(request, 'myimagepage4.html')

def myimagepage5(request,imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var=True
    elif myimagename == "python":
        var=False
    mydictionary ={
        "var":var
    }
    return render(request,'myimagepage5.html',context=mydictionary)

def myform1(request):
    return render(request, 'myform1.html')

def submitmyform(request):
    dict3 = {
        "E Mail ID": request.POST['E Mail ID'],
        "Description": request.POST['Description'],
        "method": request.method
    }
    return JsonResponse(dict3)

def myform2(request):
    if request.method == 'POST':
        form = feedbackform(request.POST)
        if form.is_valid():
            email = request.POST['email']
            subject = request.POST['subject']
            description = request.POST['description']
            dict4 = {
                "form": feedbackform()
            }
            errorflag = False
            Errors = []
            if subject != subject.upper():
                errorflag = True
                errormsg = "Subject should be in Capital.."
                Errors.append(errormsg)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)
            if errorflag != True:
                dict4["success"] = True
                dict4["successmsg"] = "Form Submitted"
            dict4["error"] = errorflag
            dict4["errors"] = Errors
            print(dict4)
            return render(request,'myform2.html',context=dict4)

    elif request.method == "GET":
        form = feedbackform # FeedbackForm(None)
        dict4 = {
            "form" : form
        }
        return render(request,'myform2.html',context=dict4)