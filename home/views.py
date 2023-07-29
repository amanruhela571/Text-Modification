from cgitb import html
from dataclasses import field
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from home.models import Regular_user
from django.contrib import messages
from templates import *
# Create your views here.

#crete by aman to handle date of models.py          # it is not working 
# class Regular_userform(forms.modelform):
#     class  Meta:
#         model = Regular_user
#         field = "__all__"




def Regular_user(request):
    if request.method == "POST":
        id = request.POST.get('id')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        profession = request.POST.get('profession')
        github = request.POST.get('github')
        active_coding_platfor = request.POST.get('active_coding_platfor')
        from_date = request.POST.get('from_date')
        Regular_user = Regular_user(id=id, email=email, phone_number=phone_number, from_date=from_date,
        profession=profession,github=github,active_coding_platfor=active_coding_platfor)
        Regular_user.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'Regular_user.html')

# this is adding by aman for understanding pipeline concept in django
# pipeline is nothing just adding fuction(def) in views.py and join/link them
# in urls.py with path okkkk


# def index(request):
#     return HttpResponse('''home page <br>
    
#     <a href="http://127.0.0.1:8000/home">index/home</a><br>
#     <a href="http://127.0.0.1:8000/about">about</a><br>
#     <a href="http://127.0.0.1:8000/admin">admin</a><br>
#     <a href="http://127.0.0.1:8000/contact">contact</a><br>
#     <a href="http://127.0.0.1:8000/newpage">newpage</a>

#     ''')


def index(request):
    return render(request,'demo2.html')     

#demo 2 is the main file and other is only for demo

def contact(request):
 
    return HttpResponse('''<a href='http://127.0.0.1:8000/home'>home</a><br>it is contact page,''')


def about(request):
    return HttpResponse('''<h1>you are in about</h1> <a href="/home" >back to home </a>''')     
    #       we can do this by this way also href='/home'  or if you dont give any name to your home page then href = '/' this also works 

# below code is just for understanding templates and sending variables in temp 
# and render used for temp(not httpresponse) and using html file from temp

def newpage(request):
    variable = {'name':'aman','place':'mars'}
    return render(request,'demo2.html',variable)

def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')
    # print(djtext)             # dont need to print this (it is just for fun)

    # get the value of checkbox
    removepunc = request.GET.get('remove punc','off/empty')
    capitalize = request.GET.get('capitalize','off')
    removeNewLIne= request.GET.get('remove new line','default')
    removeExtraSpace=request.GET.get('remove_extra_space','off')
    
# below code check the value of checkbox/variable (if it on then work accordingly)

    if (removepunc == "on"):        # it is first if which remove punctuation 
        analyzed_text = ""

        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuation:
                analyzed_text = analyzed_text + char
        
        params = {'purpose':'remove punc','analyzed_result':analyzed_text}

        return render(request,'analyzed.html',params)

    elif(capitalize == 'on'):       # it is second condition which check it is on and then capitalize it
        analyzed_text = ""

        for char in djtext:
            analyzed_text = analyzed_text + char.upper()
        
        params = {'purpose':'capitalizing text','analyzed_result':analyzed_text}
        return render(request,'analyzed.html',params)
        
    elif(removeNewLIne == "on"):        # if you simple write (removeNewLIne) then it also work
        analyzed_text = ""

        for char in djtext:
            if(char != '\n' and char !='\r'):
                analyzed_text = analyzed_text + char
        
        params = {'purpose':'Removing New Line','analyzed_result':analyzed_text}
        return render(request,'analyzed.html',params)

    elif(removeExtraSpace=="on"):
        # pass                          #it is used for emptiness

        analyzed_text=""

        for index,char in enumerate(djtext):            # enumerate used for getting index of our text/string
            if not (djtext[index]==" " and djtext[index+1]=="  "):
                analyzed_text= analyzed_text + char
        
        params = {'purpose':'Removing Extra space','analyzed_result':analyzed_text}
        return render(request,'analyzed.html',params)

        

    else:
        return HttpResponse("<a href='http://127.0.0.1:8000/newpage'>back to text page</a><br>error click the check box")

