from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [
    path('admindashboard/',views.adminDashboard,name="admindashboard"),

    path('Dist/',views.district,name="district"),
    path('deledis/<int:did>',views.deletedis,name="deldis"), #name should be same name as in url
    path('editdis/<int:did>',views.editdis,name="editdis"),

    path('Place/',views.place,name="place"),
    path('delplace/<int:pid>',views.deleteplace,name="delpla"),
    path('editplace/<int:pid>',views.editplace,name="editpla"),
    

    path('PackageType/',views.packageType,name="packagetype"),
    path('delpackage/<int:pid>',views.deletePackageType,name="deletepackage"),
    path('editpackage/<int:pid>',views.editPackageType,name="editpackage"),


    path('agencyverification/',views.agencyVerification,name="agencyverification"),
    path('agencyaccept/<int:aid>',views.agencyAccept,name="agencyaccept"),
    path('agencyreject/<int:aid>',views.agencyReject,name="agencyreject"),

    path('agencyacceptedlist/',views.agencyAcceptedList,name="agencyacceptedlist"),
    path('agencyrejectedlist/',views.agencyRejectedList,name="agencyrejectedlist"),
    path('busreport/',views.busReport,name="busreport"),
    path('packagereport/',views.packageReport,name="packagereport"),
    path('creg/',views.complaintsRegisteredUsers,name="creg"),
    path('cunreg/',views.complaintsUnRegisteredUsers,name="cunreg"),
]

