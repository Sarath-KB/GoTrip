from django.shortcuts import render,redirect
from Admin.models import *
from Agency.models import  *
from Guest.models import *
from User.models import *
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Sum

# Create your views here.


def agencyHome(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    income1=tbl_payement.objects.filter(bbooking__bus__agency=agency)
    s1=0
    for i in income1:
        s1+=float(i.agency_profit)
    income2=tbl_payement.objects.filter(pbooking__package__agency=agency)
    s2=0
    for i in income2:
        s2+=float(i.agency_profit)
    tincome=s1+s2
    busbookings=tbl_busbooking.objects.filter(bus__agency=agency).count()
    packagebookings=tbl_packagebooking.objects.filter(package__agency=agency).count()
    return render(request,"Agency/AgencyHome.html",{'AGENCY':agency,'count':count,'notifications':notifications,'P':packagebookings,'B':busbookings,'I':tincome})


def agencyProfile(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    return render(request,"Agency/AgencyProfile.html",{'AGENCY':agency})


def editAgencyProfile(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    if request.method=="POST":
        agency.agency_contact=request.POST.get('txtContact')
        agency.agency_address=request.POST.get('txtAddress')
        agency.save()
        return redirect("Agency:agencyhome")
    else:
        return render(request,"AGENCY/AgencyEditProfile.html",{'AGENCY':agency})


def changeAgencyPasswd(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    if request.method=="POST":
        psw=agency.agency_password
        curpass=request.POST.get('curPasswd')
        if psw == curpass:
            newpass=request.POST.get('newPasswd')
            cpass=request.POST.get('conPasswd')
            if newpass==cpass:
                agency.agency_password=newpass
                agency.save()
                return redirect("Agency:agencyhome")
            else:
                return render(request,"Agency/AgencyChangePassword.html",{'msg':"Password Mismatch!!"})
        else:
            return render(request,"Agency/AgencyChangePassword.html",{'msg':"Password Incorrect!!"})
    else:
        return render(request,"Agency/AgencyChangePassword.html")


def hotelDetails(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    if request.method=="POST":
        tbl_hoteldetails.objects.create(hotel_name=request.POST.get('txtName'),hotel_address=request.POST.get('txtAddress'),
            hotel_phno=request.POST.get('txtPhno'),agency=agency)
        return render(request,"Agency/HotelDetails.html",{'AGENCY':agency,'count':count,'notifications':notifications})
    else:
        return render(request,"Agency/HotelDetails.html",{'AGENCY':agency,'count':count,'notifications':notifications})

def mealDetails(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    mealsdata=tbl_mealdetails.objects.filter(agency=agency)
    if request.method=="POST": 
        tbl_mealdetails.objects.create(meal_name=request.POST.get('txtName'),agency=agency)
        return render(request,"Agency/MealDetails.html",{'MEALS':mealsdata,'AGENCY':agency,'count':count,'notifications':notifications})
    else:
        return render(request,"Agency/MealDetails.html",{'MEALS':mealsdata,'AGENCY':agency,'count':count,'notifications':notifications})

def editMealDetails(request,mid):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    meal=tbl_mealdetails.objects.get(id=mid)
    mealsdata=tbl_mealdetails.objects.all()
    if request.method=="POST" and request.FILES:
        meal.meal_name=request.POST.get('txtName')
        meal.save()
        return redirect("Agency:mealdetails")
    elif request.method=="POST":
        meal.meal_name=request.POST.get('txtName')
        meal.save()
        return redirect("Agency:mealdetails")
    else:
        return render(request,"Agency/MealDetails.html",{'MEALS':mealsdata,'MEAL':meal,'count':count,'notifications':notifications})
def deletePackage(request,pid):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    tbl_packagedetails.objects.get(id=pid).delete()
    return redirect("Agency:mypackages")

def deleteMealDetails(request,mid):
    meal=tbl_mealdetails.objects.get(id=mid)
    mealsdata=tbl_mealdetails.objects.all()
    tbl_mealdetails.objects.get(id=mid).delete()
    return redirect("Agency:mealdetails")

def packageDetails(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    hoteldata=tbl_hoteldetails.objects.filter(agency=agency)
    mealdata=tbl_mealdetails.objects.filter(agency=agency)
    busdata=tbl_busdetails.objects.filter(agency=agency,package__isnull=True)
    if request.method=="POST" and request.FILES:
        #print(request.POST.getlist('txt_hotel'))
        agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
        hotel=request.POST.getlist('txt_hotel')
        
        std=""
        for i in hotel:
            std=std+str(i)+","
        meal=request.POST.getlist('txt_meal')
        mealdata=""
        for i in meal:
            mealdata=mealdata+str(i)+","
        
        bus=request.POST.getlist('txt_bus')
        busdata=""
        for i in bus:
            busdata=busdata+str(i)+","
        tbl_packagedetails.objects.create(
            package_name=request.POST.get('txtName'),
            package_description=request.POST.get('txtDesc'),
            package_cover=request.FILES.get('Cimage'),
            package_locations=request.POST.get('txtLoc'),
            package_days=request.POST.get('txtDay'),
            package_nights=request.POST.get('txtNight'),
            package_persons=request.POST.get('txtNo'),
            package_price=request.POST.get('txtRate'),
            agency=agency,
            hotel=std,
            meal=mealdata,
            bus=busdata)
        pack=tbl_packagedetails.objects.filter(agency=request.session["aid"]).last()
        pac=pack.package_days
        pa=pack.id
        for i in bus:
            bsda=tbl_busdetails.objects.get(id=i)
            bsda.package=pack
            bsda.save()
        request.session["pac"]=pac
        request.session["pa"]=pa
        return  redirect("Agency:dayhighlights")
    else:
        return render(request,"Agency/PackageDetails.html",{'HOTEL':hoteldata,'MEAL':mealdata,'BUS':busdata,'AGENCY':agency,'count':count,'notifications':notifications})

def dayHighlights(request):
    pac=int(request.session["pac"])
    parray=[i for i in range(1,pac+1)]
    package=tbl_packagedetails.objects.get(id=request.session["pa"])
    if request.method=="POST" and request.FILES:
        day=request.POST.getlist('txtDay')  # Get the list of textarea values
        high=request.POST.getlist('txtHigh')
        img=request.FILES.getlist('fday')
        for i,j,k in zip(day, high, img):
            tbl_dayhighlights.objects.create(day_no=i,day_highlights=j,package=package,day_image=k)
        return redirect("Agency:agencyhome")
    else:    
        return render(request,"Agency/DayHighlights.html",{'array':parray})


def busDetails(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])  
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    if request.method=="POST" and request.FILES:
        tbl_busdetails.objects.create(
            bus_regno=request.POST.get('txtNo'),
            bus_type=request.POST.get('bustype'),
            bus_seatcapacity=request.POST.get('scap'),
            bus_image=request.FILES.get('busimage'),
            agency=agency
        )
        return render(request,"Agency/BusDetails.html",{'AGENCY':agency,'count':count,'notifications':notifications})
    else:
        return render(request,"Agency/BusDetails.html",{'AGENCY':agency,'count':count,'notifications':notifications})


def pBookingVeri(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"]) 
    bookingdatacount=tbl_packagebooking.objects.filter(pbooking_status=0,package__agency=agency).count()
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    if bookingdatacount >0:
        bookingdata=tbl_packagebooking.objects.filter(pbooking_status=0,package__agency=agency)
        return render(request,"Agency/PbookingVeri.html",{'DATA':bookingdata,'AGENCY':agency,'notifications':notifications})
    else:
        return render(request,"Agency/PbookingVeri.html",{'AGENCY':agency,'count':count,'notifications':notifications})


def acceptBooking(request,bid):
    bdata=tbl_packagebooking.objects.get(id=bid)
    bdata.pbooking_status=1

    ag_name=bdata.package.agency.agency_name
    name=bdata.user.user_name
    email=bdata.user.user_email
    pname=bdata.package.package_name
    bdate=str(bdata.pbooking_fordate)

    send_mail(
            "Rejection of the Tour Package booking",
            "\rRespected sir/madam "+ name +",\nYour booking of the travel package "+ pname +" for the date "+ bdate + " has been accepted  by the agency "+ ag_name +".\nThis is a system generated email.So no need to reply.\n\n\nWith Regards,\n\nVoyagecom.",
            settings.EMAIL_HOST_USER,
            [email],

        )
        


    bdata.save()
    pkid=bdata.package.id
    pack=tbl_packagedetails.objects.get(id=pkid)
    bus=pack.bus
    bsdata=bus.split(",")
    bus_ids = [int(id_str) for id_str in bsdata if id_str.strip().isdigit()]
    busdata=tbl_busdetails.objects.filter(id__in=bus_ids)
    for i in busdata:
        i.bus_status=1
        i.save()
    pack.package_status=1
    pack.save()
    return redirect("Agency:pbookingveri")


   

def rejectBooking(request,bid):
    bdata=tbl_packagebooking.objects.get(id=bid)
    bdata.pbooking_status=2

    ag_name=bdata.package.agency.agency_name
    name=bdata.user.user_name
    email=bdata.user.user_email
    pname=bdata.package.package_name
    bdate=str(bdata.pbooking_fordate)
    send_mail(
            "Rejection of the Tour Package booking",
            "\rRespected sir/madam "+ name +",\nYour booking of the travel package "+ pname +" for the date "+ bdate + " has been rejceted due to some reason by the agency "+ ag_name +".\nThis is a system generated email.So no need to reply.\n\n\nWith Regards,\n\nVoyagecom.",
            settings.EMAIL_HOST_USER,
            [email],

        )

    bdata.save()
    return redirect("Agency:pbookingveri")


def bBookingVeri(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"]) 
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    bbookingdata=tbl_busbooking.objects.filter(bbooking_status=0,bus__agency=agency)
    return render(request,"Agency/BbookingVeri.html",{'DATA':bbookingdata,'AGENCY':agency,'count':count,'notifications':notifications})

    
def acceptBusBooking(request,bid):
    bodata=tbl_busbooking.objects.get(id=bid)
    if request.method=="POST":
        bodata.bbooking_status=1
        amnt=request.POST.get('txtRate')
        bmnt=int(amnt)/2
        bodata.btotal_amount=amnt
        bodata.bbooking_amount=bmnt
        bodata.save()
        busid=bodata.bus.id
        bus=tbl_busdetails.objects.get(id=busid)
        bus.bus_status=1
        bus.save()
        return redirect("Agency:bbookingveri")
    else:
        return render(request,"Agency/AcceptBus.html")

def rejectBusBooking(request,bid):
    bodata=tbl_busbooking.objects.get(id=bid)
    bodata.bbooking_status=2
    bodata.save()
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"]) 
    return redirect("Agency:bbookingveri")
   




#---------Chat-----------#




def chat(request, cid):
    chatobj = tbl_userRegister.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_userRegister.objects.get(id=cied)
        sobj = tbl_agencyRegister.objects.get(id=request.session["aid"])
        content = request.POST.get("msg")
        # print(cied)
        print(content)
        Chat.objects.create(
            from_agency=sobj, to_user=ciedobj, content=content, from_user=None, to_agency=None)
        return render(request, 'Agency/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'Agency/Chat.html', {"chatobj": chatobj})


def loadchat(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    
    shopobj = tbl_userRegister.objects.get(id=cid)
   
    sid = request.session["aid"]
    
    suserobj = tbl_agencyRegister.objects.get(id=request.session["aid"])
   
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_tbl_agencyregister u on (u.id=c.from_agency_id) or (u.id=c.to_agency_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'Agency/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})



def addComplaint(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"]) 
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    if request.method=="POST":
        tbl_complaint.objects.create(
            agency=agency,
            complaint_title=request.POST.get('txtTitle'),
            complaint_content=request.POST.get('txtContent')
        )
        return render(request,"Agency/Complaint.html",{'msg':"Complaint send Successfully"})
    else:
        return render(request,"Agency/Complaint.html",{'count':count,'notifications':notifications})


def myPackages(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"]) 
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    pdata=tbl_packagedetails.objects.filter(agency=agency)
    return render(request,"Agency/MyPackagesList.html",{'DATA':pdata,'AGENCY':agency,'count':count,'notifications':notifications})


def Schedules(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    data=tbl_packagebooking.objects.filter(Q(pbooking_status=1) | Q(pbooking_status=3)| Q(pbooking_status=4),package__agency=agency)
    
    return render(request,"Agency/Schedules.html",{'DATA':data,'AGENCY':agency,'count':count,'notifications':notifications})

def BusSchedules(request):
    agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
    count = Chat.objects.filter(to_agency=agency).count()
    notifications = Chat.objects.filter(to_agency=agency)
    bus=tbl_busbooking.objects.filter(Q(bbooking_status=1) | Q(bbooking_status=3) | Q(bbooking_status=4),bus__agency=agency)
    return render(request,"Agency/BusSchedules.html",{'BUS':bus,'AGENCY':agency,'count':count,'notifications':notifications})


def packageCompletd(request,bid):
    dat=tbl_packagebooking.objects.get(id=bid)
    dat.pbooking_status=4
    dat.save()
    pid=dat.package.id
    pck=tbl_packagedetails.objects.get(id=pid)

    bus=pck.bus
    bsdata=bus.split(",")
    bus_ids = [int(id_str) for id_str in bsdata if id_str.strip().isdigit()]
    busdata=tbl_busdetails.objects.filter(id__in=bus_ids)
    for i in busdata:
        i.bus_status=0
        i.save()

    pck.package_status=0
    pck.save()
    return redirect('Agency:schedules')

def busCompletd(request,bid):
    dat=tbl_busbooking.objects.get(id=bid)
    dat.bbooking_status=4
    dat.save()
    busid=dat.bus.id
    bdata=tbl_busdetails.objects.get(id=busid)
    bdata.bus_status=0
    bdata.save()
    return redirect('Agency:schedules')

def logOut(request):
    del request.session['aid']
    return redirect('Guest:index')


def generateReport(request):
    if 'aid' in request.session:
        agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
        if request.method=="POST":
            fdate=request.POST.get('fdate')
            tdate=request.POST.get('tdate')
                
            count=tbl_payement.objects.filter(pbooking__package__agency=agency,payement_date__range=[fdate,tdate]).count()
            report_data=tbl_payement.objects.filter(pbooking__package__agency=agency,payement_date__range=[fdate,tdate])
            tamnt=0.0

            for i in report_data:

                tamnt=float(i.agency_profit) + tamnt
            
            

            return render(request,"Agency/Report.html",{'DATA':report_data,'TOTAL':tamnt,'COUNT':count})
        else:
            return render(request,"Agency/Report.html")
    else:
        return redirect('Guest:index')

def generateReportBus(request):
    if 'aid' in request.session:
        agency=tbl_agencyRegister.objects.get(id=request.session["aid"])
        if request.method=="POST":
            fdate=request.POST.get('fdate')
            tdate=request.POST.get('tdate')
                
            count=tbl_payement.objects.filter(bbooking__bus__agency=agency,payement_date__range=[fdate,tdate]).count()
            report_data=tbl_payement.objects.filter(bbooking__bus__agency=agency,payement_date__range=[fdate,tdate])
            tamnt=0.0

            for i in report_data:

                tamnt=float(i.agency_profit) + tamnt
            
            

            return render(request,"Agency/BusReport.html",{'DATA':report_data,'TOTAL':tamnt,'COUNT':count})
        else:
            return render(request,"Agency/BusReport.html")
    else:
        return redirect('Guest:index')





