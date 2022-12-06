from django.shortcuts import render ,redirect
from .forms import assetfoem ,SignUpForm
from .models import asset 
from . import forms,models
import os
# from curdopt.EmailBackEnd import EmailBackEnd
# from curdopt.emailbackend import EmailBackEnd
from django.contrib.auth import login ,authenticate ,logout
from django.contrib.auth.models import User , AbstractUser ,Group 
from django.contrib.auth.forms import  UserCreationForm ,AuthenticationForm , PasswordChangeForm
from django.contrib import auth ,messages
from django.contrib.auth import authenticate, update_session_auth_hash
from  django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
import csv
import xlwt
import json 
# from django.contrib.auth.models import user
from urllib import response
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

def add(request):
    if request.method=='POST':
        form=assetfoem(request.POST ,request.FILES)
        if form.is_valid():
            form= form.save(commit=False)
            form.save()
            return redirect('view')
    else:        
        form=assetfoem()
    return render(request ,'add.html',{'form':form})


def assetview1(req ,sr_no):
    asset1=asset.objects.get(sr_no=sr_no)
    if req.method=='POST':
        
        return redirect('view1')
    return render(req ,'assetview1.html',{'asset1':asset1})


def assetview(req ,sr_no):
    asset1=asset.objects.get(sr_no=sr_no)
    if req.method=='POST':
        
        return redirect('view')
    return render(req ,'assetview.html',{'asset1':asset1})


def intro(request):
    return render(request ,'intro.html')

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

# @login_required(login_url='adminlogin') 
# @user_passes_test(is_admin)
def view(request):
   
    
    assets=asset.objects.all()
    return render(request , 'view.html',{'assets':assets })

# @login_required(login_url='adminlogin') 
# @user_passes_test(is_admin)
# @login_required
def view1(request):
    if request.user.is_authenticated:
        assets=asset.objects.all()
    else:
        return redirect('studentlogin')
    return render(request , 'view1.html',{'assets':assets})

def studentclick(request):
    return render(request ,'studentclick.html')

def adminclick(request):
    return render(request ,'adminclick.html')

def adminlogin(request):
    # if request.method != "POST":
    #     return HttpResponse("<h2>Method Not Allowed</h2>")
    # else:
    # if request.user.is_superuser==True:
    if request.method=='POST':
    #         username=request.POST.get('username')
    #         password=request.POST.get('pswd')
    #         user=authenticate(email=username ,password=password)
        
    #     if user is not None :
    #         login(request ,user)
    #         messages.info(request , 'login sucessfully')
    #         return redirect('view')
        
    #     else:
    #         messages.info(request ,'invalid credentials')
    #         return render(request ,'adminsignup.html')
    #     return redirect('view')
    # if request.method=='POST':
        return redirect('view')
    return render(request ,'adminlogin.html')

# def adminlogin(request):
#     if request.method != "POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
#         if user != None:
#             login(request, user)
#             user_type = user.user_type
#             #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
#             if user_type == '1':
#                 return redirect('view')
#             elif user_type == '2':
#                 return redirect('view1')
#             elif user_type == '3':
#                 pass
#             else:
#                 messages.error(request, "Invalid Login!")
#                 return redirect('adminlogin')
#         else:
#             messages.error(request, "Invalid Login Credentials!")
#             #return HttpResponseRedirect("/")
#             return redirect('adminlogin')


# @unauthentocated_user
def studentlogin(request):
    
    # if request.method=='POST':
    #     fm=AuthenticationForm(request=request ,data=request.POST)
    #     if fm.is_valid():
    #         uname=fm.cleaned_data['username']
    #         upass=fm.cleaned_data['password']
    #         user=authenticate(username=uname ,password=upass)
    #         if user is not None:
    #             login(request ,user)
    #             return redirect('view1')
    # else:           
    #     fm=AuthenticationForm()
    if not request.user.is_authenticated:      
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('pswd')
            user=authenticate(username=username ,password=password)
            
            if user is not None :
                login(request ,user)
                messages.info(request , 'login sucessfully')
                return redirect('view1')
            
            else:
                messages.info(request ,'invalid credentials')
                return render(request ,'studentlogin.html')
            
        return render(request ,'studentlogin.html')
    else:
        return redirect('view1')

def adminsignup(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        password1=request.POST.get('pswd1')
        user=customers.objects.create_user()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return render('adminlogin')
    return render(request ,'adminsignup.html',{'form':form})

# def studentsignup(request):
    # if request.method == "POST":
    #     # check if user has entered correct credientials
    #     username = request.POST.get('username')
    #     email=request.POST.get('email')
    #     password = request.POST.get('pswd')
    #     Confirm_Password=request.POST.get('pswd1')
    #     user = authenticate(username=username, password=password ,password=password )
    #     if user is not None:
    #         # A backend authenticated the credentials
    #         if user.is_user == True:
    #             login(request, user)
    #             return redirect("sginpg_user")
    #         else:
    #             messages.error(request, 'You are not authorized to access this page!')
    #     else:
    #         # No backend authenticated the credentials
    #         messages.error(request, 'Invalid username or password!')    
    #         return render(request, 'sgin_user.html')
    # if request.user.is_authenticated :
    #     return redirect('intro')
    # else:
    #     if request.method == 'POST':
    #         username = request.POST.get('username')
    #         email=request.POST.get('email')
    #         password = request.POST.get('pswd')
    #         Confirm_Password=request.POST.get('pswd1')
    #         if password==Confirm_Password:
    #             if User.objects.filter(email=email).exists():
    #                 messages.info(request ,'email taken')
    #                 return redirect('studentsignup')
    #             elif User.objects.filter(username=username).exists():
    #                 messages.info(request ,'username taken')
    #                 return redirect('studentsignup')
    #             else:
    #                 user1=User.objects.create_user(email=email ,password=password ,username=username)
    #                 user1.save()
    #                 return redirect('view1')
                    
    #         else:
    #                 messages.error(request, ' password is not matching!')  
    #                 return redirect('studentsignup')  
    # return render(request ,'studentsignup.html')

# def studentsignup(request):
    
#     form=forms.StudentUserForm()
#     if request.method=='POST':
#         form=forms.StudentUserForm(request.POST)
        
#         if form.is_valid():
#             user=form.save()
#             user.set_password(user.password)
#             user.save()
           

#             my_student_group = Group.objects.get_or_create(name='STUDENT')
#             my_student_group[0].user_set.add(user)

#         return render('studentlogin')
#     return render(request,'studentsignup.html',{'form':form})


def studentsignup(request):
    if request.user.is_authenticated:  
        if request.method == 'POST':
            form = SignUpForm(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request ,"user is created sucessfully")
                form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('view1')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    
    return render(request, 'studentsignup.html', {'form': form})



def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def export_csv(request):

    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;fileName=Asset'+ '.csv'
    writer=csv.writer(response)
    writer.writerow(['Sr. No.','Name of the Equipment Machinary','Vr. No.','Date','Make','identification mark','Name of the party from whome purchesed','VALUE','Wether our own funds/ capital Grants','Dept stock register folio number','Varified by','Date of verification','Remark','Image','Laboratory'])


    asset1 =asset.objects.all()
    for i in asset1:

        writer.writerow([i.sr_no, i.name,i.vr_no,i.Date ,i.make ,i.identification_mark ,i.Name_of_the_party_from_whome_purchesed ,i.value ,i.funds ,i.Dept_stock_register_folio_number ,i.Varified_by,i.Date_of_verification,i.Remark ,i.Image ,i.Laboratory])
    return response

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Asset')
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Sr. No.','Name of the Equipment Machinary','Vr. No.','Date','Make','identification mark','Name of the party from whome purchesed','VALUE','Wether our own funds/ capital Grants','Dept stock register folio number','Varified by','Date of verification','Remark','Image','Laboratory' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = asset.objects.all().values_list('sr_no', 'name','vr_no','Date' ,'make' ,'identification_mark','Name_of_the_party_from_whome_purchesed' ,'value' ,'funds' ,'Dept_stock_register_folio_number' ,'Varified_by','Date_of_verification','Remark' ,'Image' ,'Laboratory')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response      




def delete(request ,sr_no):
    a=asset.objects.filter(sr_no=sr_no)
    a.delete()
    return redirect('view')

def edit(request,sr_no ):
    asset1=asset.objects.get(sr_no=sr_no)
    form=assetfoem(instance=asset1)
    if request.method=='POST':
        form=assetfoem(request.POST,request.FILES, instance=asset1 )
        
        
        if form.is_valid():
            # form= form.save(commit=False)
            form.save()
            return redirect('view')
    return render(request ,'edit.html' ,{'form':form})


def logout(request):
    auth.logout(request)
    messages.info(request ,'Logout sucessfully')
    return redirect('/')
            
def changepass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                messages.success(request ,"password changed sucessfully")
                fm.save()
                update_session_auth_hash(request ,fm.user)
                return redirect('view1')
        else:
            fm= PasswordChangeForm(request.user)
        return render(request ,'changepass.html',{'fm':fm})
    else:
        return redirect('intro')
                
            

