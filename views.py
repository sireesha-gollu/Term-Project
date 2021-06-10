from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
from . forms import ExamForm
from .models import exam_table
# Create your views here.

def home(request):
    return render(request, 'home.htm')
def stu_pg(request):
    return render(request, 'stu_pg.htm')
def fac_pg(request):
    return render(request, 'fac_pg.htm')
def ssignin(request):
    if request.method == 'POST':
        username1=request.POST.get('username',False)
        password1 = request.POST.get('password',False)

        x=auth.authenticate(username=username1,password=password1,is_staff=True)
        if x is None:
            messages.info(request,'!!!Incorrect username or password entered!!! Try again')
            return redirect('ssignin')
        else:
            return redirect('stu_pg')
    else:
        return render(request, 'ssignin.htm')

def fsignin(request):
    if request.method == 'POST':
        username1=request.POST.get('username',False)
        password1 = request.POST.get('password',False)
        x=auth.authenticate(username=username1,password=password1)
        if x is None:
            messages.info(request,'!!!Incorrect username or password entered!!! Try again')
            return redirect('fsignin')
        else:
            return redirect('fac_pg')
    else:
        return render(request, 'fsignin.htm')

def ssignup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name',False)
        email = request.POST.get('email',False)
        password1 = request.POST.get('password1',False)
        password2 = request.POST.get('password2',False)
        username=request.POST.get('username',False)
        Is_Faculty=request.POST.get('is_staff',False)
        
        if password1==password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'Entered username alread taken')
                return redirect('ssignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Entered email alread taken')
                return redirect('ssignup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name, password= password1, email= email,is_staff=Is_Faculty)
                user.save()
                return redirect('ssignin')
            
        else:
            messages.info(request,'Password enterd is not same!!!')
            return redirect('ssignup')
        return redirect('/')
        
    else:  
        return render(request , 'ssignup.htm')

def fsignup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name',False)
        email = request.POST.get('email',False)
        password1 = request.POST.get('password1',False)
        password2 = request.POST.get('password2',False)
        username=request.POST.get('username',False)
        
        if password1==password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'Entered username alread taken')
                return redirect('fsignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Entered email alread taken')
                return redirect('fsignup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name, password= password1, email= email)
                user.save()
                return redirect('fsignin')
            
        else:
            messages.info(request,'Password enterd is not same!!!')
            return redirect('fsignup')
        return redirect('/')
        
    else:
        return render(request , 'fsignup.htm')
def upload(request):
    context = {}
    if request.method =='POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.htm', context)      
    
def exam_list(request):
    exams = exam_table.objects.all()
    return render(request,'exam_list.htm',{
        'exams':exams
    } )
def upload_exam(request):
    if request.method =='POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fac_pg')
    else:
        form = ExamForm()
    return render(request, 'upload_exam.htm', {
       'form':form 
    })
