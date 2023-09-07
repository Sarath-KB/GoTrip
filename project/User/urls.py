from django.urls import path
from User import views
app_name="User"

urlpatterns=[
    path('userhome/',views.userHome,name="userhome"),
    path('userprofile/',views.userProfile,name="userprofile"),
    path('editprofile/',views.editProfile,name="editprofile"),
    path('changepasswd/',views.changePasswd,name="changepasswd"),
    path('searchpackages/',views.searchPackages,name="searchpackages"),
    path('ajax_package/',views.ajax_package,name="AjaxPackage"),
    path('viewdetails/<int:pid>',views.viewDetails,name="viewdetails"),
    path('packagebooking/<int:pid>',views.packageBooking,name="packagebooking"),
    path('viewbookingstatus/',views.viewBookingStatus,name="viewbookingstatus"),

    # path('hotels/<int:pid>',views.hotels,name="hotels"),
    # path('meals/<int:pid>',views.meal,name="meals"),
    # path('day/<int:pid>',views.day,name="day"),
    # path('bus/<int:pid>',views.bus,name="bus"),

    path('payment/<int:bid>',views.payment,name="payment"),
    path('processingpayment/',views.processingpayment,name="processingpayment"),
    path('patmentsucessful/',views.paysucess,name="patmentsucessful"),
    
    path('paymentbus/<int:bid>',views.paymentbus,name="paymentbus"),
    path('processingpaymentbus/',views.processingpaymentbus,name="processingpaymentbus"),
    path('paymentsucessfulbus/',views.paysucessbus,name="paymentsucessfulbus"),
    

    path('packagebill/',views.PackageBilling,name="PackageBill"),
    path('busbill/',views.BusBilling,name="BusBill"),

    path('searchbus/',views.searchBus,name="searchbus"),
    path('ajax_bus/',views.ajax_bus,name="Ajax_Bus"),
    # path('bookbus/<int:bid>',views.bookBus,name="bookbus"),
    path('bookbus/',views.bookBus,name="bookbus"),
    path('burl/',views.burl,name="burl"),

    path('viewbusbookingstatus/',views.viewBusBookingStatus,name="viewbusbookingstatus"),
    

    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),

    # path('complaint/',views.addComplaint,name="complaint"),
    
    path('myhistory/',views.myHistory,name="myhistory"),
   

    path('viewagencyprofile/<int:aid>',views.viewAgencyProfile,name="viewagencyprofile"),
    # path('viewreviews/<int:pid>',views.viewReview,name="viewreviews"),


    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),

    path('cancelbooking/<int:bid>',views.cancelBooking,name="cancelbooking"),
    path('cancelbookingrefund/<int:bid>',views.cancelBookingRefund,name="cancelbookingrefund"),
    path('logout/',views.logout,name="logout"),

    path('star/<int:mid>',views.starrating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('terms/',views.terms,name="terms"),


]