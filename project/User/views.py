from django.shortcuts import render,redirect

from django.core.paginator import Paginator
from Admin.models import *
from User.models import  *
from Guest.models import *
from Agency.models import *
import random
from datetime import datetime
from datetime import date

from django.db.models import Q
from django.db.models import F, ExpressionWrapper, fields

# Create your views here.

def userHome(request):
    if 'uid' in request.session:
        user=tbl_userRegister.objects.get(id=request.session["uid"])
        chatob=Chat.objects.filter(to_user=user)
        return render(request,"User/UserHome.html",{'Chat':chatob})
    else:
         return redirect("Guest:login")



def userProfile(request):
    if 'uid' in request.session:
        user=tbl_userRegister.objects.get(id=request.session["uid"])
        return render(request,"User/MyProfile.html",{'USER':user})
    else:
         return redirect("Guest:login")



def editProfile(request):
    if 'uid' in request.session:
        user=tbl_userRegister.objects.get(id=request.session["uid"])
        if request.method=="POST" and request.FILES:
            user.user_photo=request.FILES.get('img_file')
            user.user_name=request.POST.get('txtName')
            user.user_contact=request.POST.get('txtContact')
            user.user_address=request.POST.get('txtAddress')
            user.save()
            return redirect("User:userhome")
        elif request.method=="POST":
            user.user_name=request.POST.get('txtName')
            user.user_contact=request.POST.get('txtContact')
            user.user_address=request.POST.get('txtAddress')
            user.save()
            return redirect("User:userhome")
        else:
            return render(request,"User/EditProfile.html",{'USER':user})
    else:
        return redirect("Guest:login")


def changePasswd(request):
    if 'uid' in request.session:
        user=tbl_userRegister.objects.get(id=request.session["uid"])
        if request.method=="POST":
            psw=user.user_password
            curpass=request.POST.get('curPasswd')
            if psw == curpass:
                newpass=request.POST.get('newPasswd')
                cpass=request.POST.get('conPasswd')
                if newpass==cpass:
                    user.user_password=newpass
                    user.save()
                    return redirect("User:userhome")
                else:
                    return render(request,"User/ChangePassword.html",{'msg':"Password Mismatch!!"})
            else:
                return render(request,"User/ChangePassword.html",{'msg':"Password Incorrect!!"})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return redirect("Guest:login")

def searchPackages(request):
    if 'uid' in request.session:
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        dis=tbl_district.objects.all()
        package=tbl_packagedetails.objects.filter(Q(package_status=0) | Q(package_status=2))
        page = request.GET.get('page', 1)  
        paginator = Paginator(package, 3)  
        page_obj = paginator.get_page(page)
        for i in package:
            wdata=tbl_packagedetails.objects.get(id=i.id)
            tot=0
            ratecount=tbl_rating.objects.filter(package=wdata).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(package=wdata)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            print(parry)
        
        datas=zip(page_obj,parry)
        
        if request.method=="POST":
            pack=tbl_packagedetails.objects.filter(Q(package_locations__icontains=request.POST.get('search')) | Q(agency__place__district__district_name__icontains=request.POST.get('search')),Q(package_status=0) | Q(package_status=2))
            for i in pack:
                wdata=tbl_packagedetails.objects.get(id=i.id)
                tot=0
                ratecount=tbl_rating.objects.filter(package=wdata).count()
                if ratecount>0:
                    ratedata=tbl_rating.objects.filter(package=wdata)
                    for j in ratedata:
                        tot=tot+j.rating_data
                        avg=tot//ratecount
                        #print(avg)
                    parry.append(avg)
                else:
                    parry.append(0)
                print(parry)
            datas=zip(pack,parry)
            return render(request,"User/SearchPackage.html",{'page_obj':page_obj,'page_objj':datas,'DIS':dis,'ar':ar})
        else:
            return render(request,"User/SearchPackage.html",{'page_obj':page_obj,'DIS':dis,'page_objj':datas,'ar':ar})
    else:
        return redirect("Guest:User_Login")



def ajax_package(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    dist=tbl_district.objects.get(id=request.GET.get('DIS'))
    package=tbl_packagedetails.objects.filter(agency__place__district=dist)
    for i in package:
        wdata=tbl_packagedetails.objects.get(id=i.id)
        tot=0
        ratecount=tbl_rating.objects.filter(package=wdata).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(package=wdata)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        print(parry)
    datas=zip(package,parry)
    return render(request,"User/AjaxPackage.html",{'page_obj':datas,'ar':ar})





def viewDetails(request,pid):

    pack=tbl_packagedetails.objects.get(id=pid)
    hotel=pack.hotel
    meal=pack.meal
    bus=pack.bus
    agency=pack.agency
    bdata=bus.split(",")
    hdata=hotel.split(",")
    mdata=meal.split(",")
    hotel_ids = [int(id_str) for id_str in hdata if id_str.strip().isdigit()]
    meal_ids = [int(id_str) for id_str in mdata if id_str.strip().isdigit()]
    bus_ids = [int(id_str) for id_str in bdata if id_str.strip().isdigit()]
    busdata=tbl_busdetails.objects.filter(id__in=bus_ids,agency=agency) 
    mealdata=tbl_mealdetails.objects.filter(id__in=meal_ids,agency=agency)

    hoteldata=tbl_hoteldetails.objects.filter(id__in=hotel_ids,agency=agency) 
    rdata=tbl_rating.objects.filter(package=pack)
    dayh=tbl_dayhighlights.objects.filter(package=pid) 
    
    return render(request,"User/ViewDetails.html",{'PACK':pack,'HOTEL':hoteldata,'DAY':dayh,'MEAL':mealdata,'BUS':busdata,'RV':rdata})
    


    
def packageBooking(request,pid):
    pack=tbl_packagedetails.objects.get(id=pid)
    user=tbl_userRegister.objects.get(id=request.session["uid"])
    am=int(pack.package_price)/2
    if request.method=="POST":
        pack=tbl_packagedetails.objects.get(id=pid)
        am=int(pack.package_price)/2
        tbl_packagebooking.objects.create(
            package=pack,
            user=user,
            pbooking_amount=am,
            pbooking_loc=request.POST.get('txtLoc'),
            pbooking_fordate=request.POST.get('tdate'),
            ppassengers=request.POST.get('passengers')
        )
        return render(request,"User/PackageBooking.html",{'PACK':pack,'msg':"Package Booking  Request Send SuccessFully   Wait for the confirmation mail"})
    else:
        return render(request,"User/PackageBooking.html",{'PACK':pack,'am':am})



def viewBookingStatus(request):
    user=tbl_userRegister.objects.get(id=request.session["uid"]) 
    bookingdata=tbl_packagebooking.objects.filter(user=user,pbooking_status__lt=4)
    today = date.today()
    target_dates = tbl_packagebooking.objects.filter(user=user,pbooking_status__lt=4).values_list('pbooking_fordate', flat=True,)
    day_differences = [(target_date - today).days for target_date in target_dates]
    datas=zip(bookingdata,day_differences)
    return render(request,"User/BookingStatus.html",{'DATA':datas})



def payment(request,bid):
    if 'uid' in request.session:
        book=tbl_packagebooking.objects.get(id=bid)
        user=tbl_userRegister.objects.get(id=request.session["uid"]) 
        if request.method=="POST": 
            ids=tbl_packagebooking.objects.get(id=bid)
            ids.pbooking_status=3
            ids.save()
            amount=float(book.pbooking_amount)
            adamnt=(amount*5)/100
            agamnt=amount-adamnt
            tbl_payement.objects.create(
                pbooking=book,
                payement_amount=book.pbooking_amount,
                host_profit=adamnt,
                agency_profit=agamnt
            )
            return redirect("User:processingpayment")
        else:
            return render(request,"User/Payment.html",{'USER':user,'DATA':book})
    else:
        return redirect("Guest:User_Login")
    



def processingpayment(request):
    if 'uid' in request.session:
        return render(request,"User/runpayment.html")
    else:
        return redirect("Guest:User_Login")
    

def paysucess(request):
    if 'uid' in request.session:
        return render(request,"User/paysucessful.html")
    else:
        return redirect("Guest:User_Login")

def processingpaymentbus(request):
    if 'uid' in request.session:
        return render(request,"User/runpaymentbus.html")
    else:
        return redirect("Guest:User_Login")

def paysucessbus(request):
    if 'uid' in request.session:
        return render(request,"User/paysuccessfulbus.html")
    else:
        return redirect("Guest:User_Login")


def PackageBilling(request):
    if 'uid' in request.session:
        billno=random.randint(10000,99999)
   
        today = datetime.now()
        today=today.strftime("%d-%m-%Y")
   
        userid=tbl_userRegister.objects.get(id=request.session["uid"])
        uobj=tbl_packagebooking.objects.filter(user=userid).last()
        return render(request,"User/PackageBill.html",{'billno':billno,'today':today,'userdata':userid,'data':uobj})
    else:
        return redirect("Guest:User_Login")

def BusBilling(request):
    if 'uid' in request.session:
        billno=random.randint(10000,99999)
   
        today = datetime.now()
        today=today.strftime("%d-%m-%Y")
   
        userid=tbl_userRegister.objects.get(id=request.session["uid"])
        uobj=tbl_busbooking.objects.filter(user=userid).last()
        return render(request,"User/BusBill.html",{'billno':billno,'today':today,'userdata':userid,'data':uobj})
    else:
        return redirect("Guest:User_Login")

def searchBus(request):
    if 'uid' in request.session:
        dis=tbl_district.objects.all()
        bus=tbl_busdetails.objects.filter(Q(bus_status=0) | Q(bus_status=2))
        return render(request,"User/SearchBus.html",{'BUS':bus,'DIS':dis})
    else:
        return redirect("Guest:User_Login")


def bookBus(request):
    
    user=tbl_userRegister.objects.get(id=request.session["uid"])
    bus=tbl_busdetails.objects.get(id=request.GET.get('ID'))
    return render(request,"User/BookBus.html",{'BUS':bus})

def burl(request):
    user=tbl_userRegister.objects.get(id=request.session["uid"])
    BUS=tbl_busdetails.objects.get(id=request.GET.get('bid'))
    tbl_busbooking.objects.create(
            bus=BUS,
            user=user,
            start_date=request.GET.get('fdate'),
            end_date=request.GET.get('edate'),
            from_loc=request.GET.get('ftime'),
            to_loc=request.GET.get('eloc'),
            passengers=request.GET.get('nn'),
            purpose=request.GET.get('pur')
        )
    return redirect("User:searchbus")
def ajax_bus(request):
    if request.GET.get('place')!="":
        plc=tbl_place.objects.get(id=request.GET.get('place'))
        bus=tbl_busdetails.objects.filter(agency__place=plc,bus_status=0)
        return render(request,"User/AjaxBus.html",{'BUS':bus})
    else:
        dist=tbl_district.objects.get(id=request.GET.get('DIST'))
        bus=tbl_busdetails.objects.filter(agency__place__district=dist,bus_status=0)
        return render(request,"User/AjaxBus.html",{'BUS':bus})



def viewBusBookingStatus(request):
    if 'uid' in request.session:

        user=tbl_userRegister.objects.get(id=request.session["uid"])
        bodata=tbl_busbooking.objects.filter(user=user)
        return render(request,"User/ViewBusBookingStatus.html",{'DATA':bodata})
    else:
        return redirect("Guest:User_Login")


def paymentbus(request,bid):
    if 'uid' in request.session:
        book=tbl_busbooking.objects.get(id=bid)
        user=tbl_userRegister.objects.get(id=request.session["uid"]) 
        if request.method=="POST": 
            ids=tbl_busbooking.objects.get(id=bid)
            ids.bbooking_status=3
            ids.save()
            amount=float(book.bbooking_amount)
            adamnt=(amount*5)/100
            agamnt=amount-adamnt
            tbl_payement.objects.create(
                bbooking=book,
                payement_amount=book.bbooking_amount,
                host_profit=adamnt,
                agency_profit=agamnt
            )
            return redirect("User:processingpaymentbus")
        else:
            return render(request,"User/PaymentBus.html",{'USER':user,'DATA':book})
    else:
        return redirect("Guest:User_Login")


#----------Chat---------#


def chatuser(request, cid):
    chatobj = tbl_agencyRegister.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_agencyRegister.objects.get(id=cied)
        sobj = tbl_userRegister.objects.get(id=request.session["uid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        Chat.objects.create(
            from_user=sobj, to_agency=ciedobj, content=content, from_agency=None, to_user=None)
        return render(request, 'User/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = tbl_agencyRegister.objects.get(id=cid)
    # print(userobj)
    sid = request.session["uid"]
    # print(sid)
    suserobj = tbl_userRegister.objects.get(id=request.session["uid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_tbl_userregister u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_agency_id=%s or c.to_agency_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})






def myHistory(request):
    if 'uid' in request.session:
        user=tbl_userRegister.objects.get(id=request.session["uid"])
        data=tbl_packagebooking.objects.filter(pbooking_status=4,user=user)
        return render(request,"User/MyHistory.html",{'DATA':data})
    else:
        return redirect("Guest:User_Login")




def viewAgencyProfile(request,aid):
    adata=tbl_agencyRegister.objects.get(id=aid)
    pdata=tbl_packagedetails.objects.filter(agency=aid)
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    for i in pdata:
        wdata=tbl_packagedetails.objects.get(id=i.id)
        tot=0
        ratecount=tbl_rating.objects.filter(package=wdata).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(package=wdata)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
        else:
            parry.append(0)
            print(parry)
            datas=zip(pdata,parry)
    return render(request,"User/AgencyProfile.html",{'AGENCY':adata,'PACK':datas,'ar':ar})




def about(request):
    return render(request,"User/about.html")


def contact(request):
    user=tbl_userRegister.objects.get(id=request.session["uid"]) 
    if request.method=="POST":
        tbl_complaint.objects.create(
            user=user,
            complaint_title=request.POST.get('txtTitle'),
            complaint_content=request.POST.get('txtContent')
        )
        return render(request,"User/Contact.html",{'msg':"Complaint send Successfully"})
    else:
        return render(request,"User/Contact.html")




def cancelBooking(request,bid):
    data=tbl_packagebooking.objects.get(id=bid)
    pid=data.package.id
    pdata=tbl_packagedetails.objects.get(id=pid)
    pdata.package_status=0
    pdata.save()
    tbl_packagebooking.objects.get(id=bid).delete()
    return redirect("User:viewbookingstatus")


def cancelBookingRefund(request,bid):
    bdata=tbl_packagebooking.objects.get(id=bid)
    bdata.pbooking_status=5
    bdata.save()
    

    pacdata=tbl_packagedetails.objects.get(id=bdata.package.id)
    bus=pacdata.bus
    bsdata=bus.split(",")
    bus_ids = [int(id_str) for id_str in bsdata if id_str.strip().isdigit()]
    busdata=tbl_busdetails.objects.filter(id__in=bus_ids)
    for i in busdata:
        i.bus_status=0
        i.save()

    pacdata.package_status=0
    pacdata.save()

    pdata=tbl_payement.objects.get(pbooking=bid)
    pdata.payement_amount=float(pdata.payement_amount)/2
   
    pdata.agency_profit=float(pdata.agency_profit)/2
    pdata.host_profit=float(pdata.host_profit)/2
    pdata.save()
    return render(request,"User/BookingStatus.html",{'msg':"Booking Canceled,Money will be refunded within days"})




#-----Review & Rating-----#

def starrating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    wdata=tbl_packagedetails.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(package=wdata).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(package=wdata).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_packagedetails.objects.get(id=workid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,package=wdata)
    stardata=tbl_rating.objects.filter(package=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})



def logout(request):
    del request.session['uid']
    return redirect("Guest:User_Login")


def terms(request):
    return render(request,"User/Terms.html")

