from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static  
from django.urls.conf import re_path
from django.views.static import serve
urlpatterns = [
    
    path('',views.intro ,name="intro"),
    path('studentclick/',views.studentclick,name = "studentclick"),
    path('adminclick/',views.adminclick ,name="adminclick"),
    
    path('adminlogin/' ,views.adminlogin ,name="adminlogin"),
    path('studentlogin/' ,views.studentlogin ,name="studentlogin"),
    
    path('adminsignup/' ,views.adminsignup ,name="adminsignup"),
    path('studentsignup/' ,views.studentsignup ,name="studentsignup"),
    
    # path('studentlogin/studentlogin/studentlogin/' ,views.studentlogin  , name="studentlogin"),
    # path('studentsignup/signup/',views.signup ,name="signup"),
    # path('studentlogin/studentlogin/' ,views.studentlogin ,name="studentlogin"),
    path('view1/',views.view1 ,name="view1"),
    path('view/', views.view ,name='view'),
    
    # path('view/add/asset_form/', views.asset_form ,name='asset_form'),
    path('view/assetview/edit/update/<int:sr_no>',views.edit ,name="edit"),
    # path('add/',views.add,name = "add"),
    path('view/add/',views.add,name = "add"),
    path('view/delete/<int:sr_no>', views.delete ,name='delete'),
    
    # path('view/edit/<int:sr_no>' ,views.edit ,name="edit"),
    path('view1/assetview1/<int:sr_no>',views.assetview1 ,name="assetview1"),
    # path('view/assetview/assetview/<int:sr_no>',views.assetview ,name="assetview"),
    path('assetview/<int:sr_no>',views.assetview ,name="assetview"),
    path('view/assetview/delete/<int:sr_no>', views.delete ,name='delete'),
    path('view/assetview/edit/<int:sr_no>', views.edit ,name='edit'),
    path('edit/' ,views.edit ,name="edit"),
    # path('view/view3/<int:sr_no>' ,views.view3 ,name="view3"),
    # path('view/view2/<int:sr_no>' ,views.view2 ,name="view2"),
    # path('update/<int:sr_no>' ,views.update ,name="update"),
    
    path('changepass/',views.changepass ,name="changepass"),
    
    path('export_csv/', views.export_csv, name="export_csv"),
    path('export_excel/', views.export_excel, name="export_excel"),
    path('view/assetview/<int:sr_no>',views.assetview ,name="assetview"),
    path('logout/',views.logout ,name="logout"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    