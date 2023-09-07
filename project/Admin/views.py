from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.db.models import Q
# Create your views here.

def adminDashboard(request):
    agcount=tbl_agencyRegister.objects.all().count()
    uscount=tbl_userRegister.objects.all().count()
    pbookings=tbl_packagebooking.objects.all().count()
    bbookings=tbl_busbooking.objects.all().count()
    return render(request,"Admin/AdminDashboard.html",{'AC':agcount,'UC':uscount,'PC':pbookings,'BC':bbookings})

def district(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get('txtDist'))
        return render(request,"Admin/District.html",{'data':districtdata})
    else:
        return render(request,"Admin/District.html",{'data':districtdata})

def deletedis(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:district") #here the admin:name name is path name in url

def editdis(request,did):
    disdata=tbl_district.objects.get(id=did)
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        disdata.district_name=request.POST.get("txtDist")
        disdata.save()
        return redirect("Admin:district")
    else:
        return render(request,"Admin/District.html",{'dis':disdata,'data':districtdata})


        

def place(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        disid=tbl_district.objects.get(id=request.POST.get('district'))
        tbl_place.objects.create(place_name=request.POST.get('txtPlace'),district=disid)
        return render(request,"Admin/Place.html",{'district':districtdata,'place':placedata})
    else:
        return render(request,"Admin/Place.html",{'district':districtdata,'place':placedata})

def deleteplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect("Admin:place")

def editplace(request,pid):
    pladata=tbl_place.objects.get(id=pid)
    placedata=tbl_place.objects.all()
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        districtid=request.POST.get('district')
        pladata.district=tbl_district.objects.get(id=districtid)
        pladata.place_name=request.POST.get("txtPlace")
        pladata.save()
        return redirect("Admin:place")
    else:
        return render(request,"Admin/Place.html",{'district':districtdata,'pla':pladata,'place':placedata})




def packageType(request):
    packagedata=tbl_packagetype.objects.all()
    if request.method=="POST":
        tbl_packagetype.objects.create(packagetype_name=request.POST.get('txtPackage'))
        return render(request,"Admin/PackageType.html",{'DATA':packagedata})
    else:
        return render(request,"Admin/PackageType.html",{'DATA':packagedata})

def deletePackageType(request,pid):
    tbl_packagetype.objects.get(id=pid).delete()
    return redirect("Admin:packagetype")

def editPackageType(request,pid):
    packdata=tbl_packagetype.objects.get(id=pid)
    packagedata=tbl_packagetype.objects.all()
    if request.method=="POST":
        packdata.packagetype_name=request.POST.get("txtPackage")
        packdata.save()
        return redirect("Admin:packagetype")
    else:
        return render(request,"Admin/PackageType.html",{'PACK':packdata,'DATA':packagedata})






def agencyVerification(request):
    agencycount=tbl_agencyRegister.objects.filter(agency_status=0).count()
    if agencycount >0:    
        agency=tbl_agencyRegister.objects.filter(agency_status=0)
        return render(request,"Admin/AgencyVerification.html",{'AGENCY':agency})
    else:
        return render(request,"Admin/AgencyVerification.html")
    

def agencyAccept(request,aid):
    agencydata=tbl_agencyRegister.objects.get(id=aid)
    agencydata.agency_status=1
    agencydata.save()
    return redirect("Admin:agencyacceptedlist")


def agencyReject(request,aid):
    agencydata=tbl_agencyRegister.objects.get(id=aid)
    agencydata.agency_status=2
    agencydata.save()
    return redirect("Admin:agencyrejectedlist")

def agencyAcceptedList(request):
    agency=tbl_agencyRegister.objects.filter(agency_status=1)
    return render(request,"Admin/AgencyAccepted.html",{'AGENCY':agency})

def agencyRejectedList(request):
    agencycount=tbl_agencyRegister.objects.filter(agency_status=2).count()
    if agencycount >0:
        agency=tbl_agencyRegister.objects.filter(agency_status=2)
        return render(request,"Admin/AgencyRejected.html",{'AGENCY':agency})
    else:
        return render(request,"Admin/AgencyRejected.html")

  
def busReport(request):
    if request.method=="POST":
        fdate=request.POST.get('fdate')
        tdate=request.POST.get('tdate')
                # report_data=tbl_packagedetails.objects.filter(agency=agency)
        count=tbl_payement.objects.filter(bbooking__isnull=False,payement_date__range=[fdate,tdate]).count()
        report_data=tbl_payement.objects.filter(bbooking__isnull=False,payement_date__range=[fdate,tdate])
        tamnt=0.0
        for i in report_data:
            tamnt=float(i.host_profit) + tamnt
        return render(request,"Admin/BusReport.html",{'DATA':report_data,'TOTAL':tamnt,'COUNT':count})
    else:
        return render(request,"Admin/BusReport.html")



def packageReport(request):
    if request.method=="POST":
        fdate=request.POST.get('fdate')
        tdate=request.POST.get('tdate')
                # report_data=tbl_packagedetails.objects.filter(agency=agency)
        count=tbl_payement.objects.filter(pbooking__isnull=False,payement_date__range=[fdate,tdate]).count()
        report_data=tbl_payement.objects.filter(pbooking__isnull=False,payement_date__range=[fdate,tdate])
        tamnt=0.0
        for i in report_data:
            tamnt=float(i.host_profit) + tamnt
        return render(request,"Admin/PackageReport.html",{'DATA':report_data,'TOTAL':tamnt,'COUNT':count})
    else:
        return render(request,"Admin/PackageReport.html")

def complaintsRegisteredUsers(request):
    cdata=tbl_complaint.objects.filter(agency__isnull=True,user__isnull=True)
    return render(request,"Admin/viewcomplaintsreg.html",{'DATA':cdata})

def complaintsUnRegisteredUsers(request):
    cdata=tbl_complaint.objects.filter(email__isnull=True,name__isnull=True)
    return render(request,"Admin/viewcomplaintsunreg.html",{'DATA':cdata})