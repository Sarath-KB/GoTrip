from django.urls import path
from Agency import views
app_name="Agency"
urlpatterns = [
    path('agencyhome/',views.agencyHome,name="agencyhome"),
    path('agencyprofile/',views.agencyProfile,name="agencyprofile"),
    path('editagencyprofile/',views.editAgencyProfile,name="editagencyprofile"),
    path('changeagencypasswd/',views.changeAgencyPasswd,name="changeagencypasswd"),

    path('hoteldetails/',views.hotelDetails,name="hoteldetails"),

    path('mealdetails/',views.mealDetails,name="mealdetails"),
    path('editmeal/<int:mid>',views.editMealDetails,name="editmeal"),
    path('deletemeal/<int:mid>',views.deleteMealDetails,name="deletemeal"),

    path('packagedetails/',views.packageDetails,name="packagedetails"),
    path('dayhighlights/',views.dayHighlights,name="dayhighlights"),

    path('busdetails/',views.busDetails,name="busdetails"),

    path('pbookingveri/',views.pBookingVeri,name="pbookingveri"),
    path('accept/<int:bid>',views.acceptBooking,name="accept"),
    path('reject/<int:bid>',views.rejectBooking,name="reject"),
    # path('rejectreason/<int:bid>',views.rejectReason,name="rejectreason"),

    path('bbookingveri/',views.bBookingVeri,name="bbookingveri"),
    path('acceptbus/<int:bid>',views.acceptBusBooking,name="acceptbus"),
    path('rejectbus/<int:bid>',views.rejectBusBooking,name="rejectbus"),



    path('Chat/<int:cid>/', views.chat, name="Chat-agency"),
    path('loadchat/', views.loadchat, name="load-chat"),

    path('complaint/',views.addComplaint,name="complaint"),

    path('mypackages/',views.myPackages,name="mypackages"),

    path('schedules/',views.Schedules,name="schedules"),
    path('busschedules/',views.BusSchedules,name="busschedules"),
    path('pcompleted/<int:bid>',views.packageCompletd,name="pcompleted"),
    path('bcompleted/<int:bid>',views.busCompletd,name="bcompleted"),

    path('deletepackage/<int:pid>',views.deletePackage,name="deletepackage"),


    path('report/',views.generateReport,name="report"),
    path('reportbus/',views.generateReportBus,name="reportbus"),

    path('logout/',views.logOut,name="logout"),
]