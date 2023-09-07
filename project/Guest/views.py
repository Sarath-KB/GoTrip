from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

import random


# Create your views here.


def index(request):
    return render(request,"Guest/Index.html")

def about(request):
    return render(request,"Guest/about.html")

def contact(request):
    if request.method=="POST":
        tbl_complaint.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            complaint_title=request.POST.get('subject'),
            complaint_content=request.POST.get('message')
        )
        return render(request,"Guest/Contact.html",{'msg':"Complaint send Successfully"})
    else:
        return render(request,"Guest/Contact.html")

def userReg(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get('txtName')
        contact=request.POST.get('txtPhno')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        photo=request.FILES.get('photo')
        password=request.POST.get('passwd')
        cpassword=request.POST.get('cpasswd')
        plc_id=tbl_place.objects.get(id=request.POST.get('sel_place'))
        if password==cpassword:    
            tbl_userRegister.objects.create(user_name=name,user_contact=contact,user_email=email,user_gender=gender,user_address=address,user_photo=photo,user_password=password,place_id=plc_id)
            return render(request,"Guest/userreg.html",{'district':districtdata})
        else:
            return render(request,"Guest/userreg.html",{'district':districtdata,'msg':"Password Doesn't match!!!"})
        
    else:
        return render(request,"Guest/userreg.html",{'district':districtdata})

def ajax_place(request):
    dis=tbl_district.objects.get(id=request.GET.get('DIST'))
    plc=tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{'PLC':plc})


def userLogin(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get('txtName')
        contact=request.POST.get('txtPhno')
        email=request.POST.get('email')
        address=request.POST.get('address')
        photo=request.FILES.get('photo')
        password=request.POST.get('passwd')
        cpassword=request.POST.get('cpasswd')
        plc_id=tbl_place.objects.get(id=request.POST.get('sel_place'))
        if password==cpassword:    
            tbl_userRegister.objects.create(user_name=name,user_contact=contact,user_email=email,user_address=address,user_photo=photo,user_password=password,place_id=plc_id)
            return render(request,"Guest/Login.html",{'district':districtdata})
        else:
            return render(request,"Guest/Login.html",{'district':districtdata,'msg':"Password Doesn't match!!!"}) 
    elif request.method=="POST":
        Email=request.POST.get('email')
        Password=request.POST.get('passwd')
        
        ulog=tbl_userRegister.objects.filter(user_email=Email,user_password=Password).count()
        alog=tbl_agencyRegister.objects.filter(agency_email=Email,agency_password=Password,agency_status=1).count()
        adlog=tbl_admin.objects.filter(admin_mail=Email,admin_passwd=Password).count()
        if ulog > 0:
            user=tbl_userRegister.objects.get(user_email=Email,user_password=Password)
            request.session['uid']=user.id
            request.session['uname']=user.user_name
            return redirect('User:userhome')
        elif alog > 0:
            agency=tbl_agencyRegister.objects.get(agency_email=Email,agency_password=Password,agency_status=1)
            request.session['aid']=agency.id
            request.session['aname']=agency.agency_name
            return redirect('Agency:agencyhome')
        elif adlog > 0:
            return redirect('Admin:admindashboard')
        else:
            return render(request,"Guest/Login.html",{'msgg':"Invalid credentials"}) 
    else:
        return render(request,"Guest/Login.html",{'district':districtdata})
    


def agencyRegister(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        password=request.POST.get('passwd')
        cpassword=request.POST.get('cpasswd')
        plc_id=tbl_place.objects.get(id=request.POST.get('sel_place'))
        if password==cpassword: 
            tbl_agencyRegister.objects.create(agency_name=request.POST.get('txtAgName'),agency_ownername=request.POST.get('txtOwName'),
            agency_contact=request.POST.get('txtContact'),agency_email=request.POST.get('txtEmail'),agency_address=request.POST.get('txtAddress'),place=plc_id,
            agency_ownerproof=request.FILES.get('imgProof'),agency_license=request.FILES.get('imgLicense'),agency_password=password) 
            return render(request,"Guest/AgencyRegister.html",{'district':districtdata})
        else:
            return render(request,"Guest/AgencyRegister.html",{'district':districtdata,'msg':"Password Doesn't match!!!"})
    else:
        return render(request,"Guest/AgencyRegister.html",{'district':districtdata})




#--------------Forgot Password--------------#


def ForgotPass(request):
    if request.method=="POST":
        otp=(random.randint(100000,999999))
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txt_email')
        send_mail(
            'Respected Sir/Madam '+" ",#subject
            "Your Otp is "+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txt_email')],
        )
        return redirect('Guest:validateotp')
    else:
        return render(request,"Guest/ForgotPassword.html")
    
def ValidateOtp(request):
    if request.method=="POST":
        otp=request.POST.get("txt_otp")
        ce=str(request.session["otp"])
        if otp==ce:
            return redirect("Guest:createpass")
    return render(request,"Guest/ValidateOTP.html")

def CreatePass(request):
    if request.method=="POST":
        if request.POST.get("txt_pass")==request.POST.get("txt_confirm"):
            usercount=tbl_userRegister.objects.filter(user_email=request.session["femail"]).count()
            agencycount=tbl_agencyRegister.objects.filter(agency_email=request.session["femail"]).count()
            
            if usercount>0:
                user=tbl_userRegister.objects.get(user_email=request.session["femail"])
                user.user_password=request.POST.get("txt_pass")
                user.save()
                return render(request,"Guest/CreatePassword.html",{'msg':"User Password Changed Successfully"})
            elif agencycount>0:
                  agency=tbl_agencyRegister.objects.get(agency_email=request.session["femail"])
                  agency.agency_password=request.POST.get("txt_pass")
                  agency.save()
                  return render(request,"Guest/CreatePassword.html",{'msg':"Agency Password Changed Successfully"})     
        else:
            return render(request,"Guest/CreatePassword.html",{'msg':" Passwords are not same"})
    else:
        return render(request,"Guest/CreatePassword.html")
