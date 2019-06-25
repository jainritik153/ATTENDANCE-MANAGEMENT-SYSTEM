from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from  django.template.context import RequestContext
from django.http import *
from django import forms
from student.forms import *
from .models import *
date=''
s=''
subject=''
e=''
teacher=[]
student=[]
# Create your views here.

def update(request):
    global date
    a = Teacherreg.objects.filter(username=request.user.username)
    y = a[0].subject
    print(y)
    x = Studentreg.objects.all()
    
    if request.method=='POST':

       for i in range(1,16):
         d=request.POST.get(str(i))

         if d==None:
           if y=='aoa':
              if date=='_1':
                 Aoa.objects.filter(roll=i).update(_1="Absent")
              if date=='_2':
                 Aoa.objects.filter(roll=i).update(_2="Absent")
                 print("in if")
              if date=='_3':
                 Aoa.objects.filter(roll=i).update(_3="Absent")
              if date=='_4':
                 Aoa.objects.filter(roll=i).update(_4="Absent")
              if date=='_5':
                 Aoa.objects.filter(roll=i).update(_5="Absent")
              if date=='_6':
                 Aoa.objects.filter(roll=i).update(_6="Absent")
              if date=='_7':
                 Aoa.objects.filter(roll=i).update(_7="Absent")
           if y=='maths':
              if date=='_1':
                 Maths.objects.filter(roll=i).update(_1="Absent")
              if date=='_2':
                 Maths.objects.filter(roll=i).update(_2="Absent")

              if date=='_3':
                 Maths.objects.filter(roll=i).update(_3="Absent")
              if date=='_4':
                 Maths.objects.filter(roll=i).update(_4="Absent")
              if date=='_5':
                 Maths.objects.filter(roll=i).update(_5="Absent")
              if date=='_6':
                 Maths.objects.filter(roll=i).update(_6="Absent")
              if date=='_7':
                 Maths.objects.filter(roll=i).update(_7="Absent")
           if y == 'ostl':
               if date == '_1':
                   Ostl.objects.filter(roll=i).update(_1="Absent")
               if date == '_2':
                   Ostl.objects.filter(roll=i).update(_2="Absent")
                   print("in if")
               if date == '_3':
                   Ostl.objects.filter(roll=i).update(_3="Absent")
               if date == '_4':
                   Ostl.objects.filter(roll=i).update(_4="Absent")
               if date == '_5':
                   Ostl.objects.filter(roll=i).update(_5="Absent")
               if date == '_6':
                   Ostl.objects.filter(roll=i).update(_6="Absent")
               if date == '_7':
                   Ostl.objects.filter(roll=i).update(_7="Absent")
         else:
           if y=='aoa':
              if date=='_1':
                 Aoa.objects.filter(roll=i).update(_1=d)
              if date=='_2':
                 Aoa.objects.filter(roll=i).update(_2=d)
                 print("in if")
              if date=='_3':
                 Aoa.objects.filter(roll=i).update(_3=d)
              if date=='_4':
                 Aoa.objects.filter(roll=i).update(_4=d)
              if date=='_5':
                 Aoa.objects.filter(roll=i).update(_5=d)
              if date=='_6':
                 Aoa.objects.filter(roll=i).update(_6=d)
              if date=='_7':
                 Aoa.objects.filter(roll=i).update(_7=d)
           if y=='maths':

              if date=='_1':
                 Maths.objects.filter(roll=i).update(_1=d)
                 print('in if')
              if date=='_2':
                 Maths.objects.filter(roll=i).update(_2=d)
                 print("in if")
              if date=='_3':
                 Maths.objects.filter(roll=i).update(_3=d)
              if date=='_4':
                 Maths.objects.filter(roll=i).update(_4=d)
              if date=='_5':
                 Maths.objects.filter(roll=i).update(_5=d)
              if date=='_6':
                 Maths.objects.filter(roll=i).update(_6=d)
              if date=='_7':
                 Maths.objects.filter(roll=i).update(_7=d)
           if y=='ostl':

              if date=='_1':
                 Ostl.objects.filter(roll=i).update(_1=d)
              if date=='_2':
                 Ostl.objects.filter(roll=i).update(_2=d)

              if date=='_3':
                 Ostl.objects.filter(roll=i).update(_3=d)
              if date=='_4':
                 Ostl.objects.filter(roll=i).update(_4=d)
              if date=='_5':
                 Ostl.objects.filter(roll=i).update(_5=d)
              if date=='_6':
                 Ostl.objects.filter(roll=i).update(_6=d)
              if date=='_7':
                 Ostl.objects.filter(roll=i).update(_7=d)

    return render(request,'update.html',{'x':x})





def Teacher1(request):
        global date
        if request.method=='POST':
            date=request.POST.get('date')
            print(date)
            date='_'+date[-1]

        return render(request ,'Teacher.html')

def Student1(request):
  global s,e,subject
  print(subject)
  if request.user.username in student:
       print("true")

       if request.method=='POST':
         start=request.POST.get('start')
         end=request.POST.get('end')
         subject=request.POST.get('subject')
         print(subject)
         s='_'+start[-1]
         e='_'+end[-1]
       return render(request,'student1.html')
  else:
       return HttpResponse("You are unauthorised to access this page")

def Student2(request):
     global subject

     u=request.user.username
     a = Studentreg.objects.filter(username=request.user.username)
     y=a[0].roll
     if subject=='aoa':
          b=Aoa.objects.filter(roll=y)
     elif subject=='maths':
          b = Maths.objects.filter(roll=y)
     elif subject=='ostl':
          b = Ostl.objects.filter(roll=y)

     x=[b[0]._1,b[0]._2,b[0]._3,b[0]._4,b[0]._5,b[0]._6,b[0]._7]
     total=abs(int(e[-1])-int(s[-1]))+1
     present=0
     absent=0
     for i in range(int(s[-1])-1,int(e[-1])):
         if x[i]=='Present':
               present+=1
         elif x[i]=='Absent':
             absent+=1
         else:
             total-=1
     if present>0:
        per=(present/total)*100
     else:
         per=0
     return render(request, 'student.html',locals())

def Time(request):
    if request.method=='POST':
         firstname=request.POST.get("gender")
         print(firstname)
    return render(request,'time.html')
def Success(request):
    return render(request,'success.html')
def home(request):
    global student,teacher
    x=Studentreg.objects.all()
    for i in x:
        student.append(i.username)
    y = Teacherreg.objects.all()
    for i in y:
        teacher.append(i.username)
    return render(request,'h.html')

def Tregister(request):
    if request.method == 'POST':
        form = TeacherReg(request.POST)
        if form.is_valid():
            form.save()
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            subject= userObj['subject']
            form.save()
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password,subject= subject)
                login(request, user)
                form.save()
                return HttpResponseRedirect('/success/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form=TeacherReg()
        return render(request, 'mysite/tregister.html', {'form': form})

def Sregister(request):
    if request.method == 'POST':
        form = StudentReg(request.POST)
        if form.is_valid():
            form.save()
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            roll=userObj['roll']
            form.save()
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password,roll=roll)
                login(request, user)
                form.save()
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form=StudentReg()
        return render(request, 'mysite/sregister.html', {'form': form})


def login(request):
    global student,teacher
    print(request.user.username)
    if request.user.username in student:
        a='/student1'
    if request.user.username in teacher:
        a="/thome"
    return render(request,'home.html',locals())