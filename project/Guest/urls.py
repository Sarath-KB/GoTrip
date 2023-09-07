from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns=[
    path('custreg/',views.userReg,name="creg"),
    path('ajax_plc/',views.ajax_place,name="Ajax_Place"),
    path('login/',views.userLogin,name="User_Login"),
    path('agencyregister/',views.agencyRegister,name="Agency_Register"),
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),

    path('forgotpass/', views.ForgotPass,name="forgotpass"),
    path('validateotp/', views.ValidateOtp,name="validateotp"),
    path('createpass/', views.CreatePass,name="createpass"),
]

