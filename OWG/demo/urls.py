# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('loaddata/', views.LoadData_info, name='mymodel-list'),
    path('states/', views.USAStates_info, name='mymodel-list'),
    path('sitedata/', views.SiteData_info, name='mymodel-list'),
    path('siteenviroment/', views.SiteEnviroment_info, name='mymodel-list'),
    path('wastewater/', views.WasteWater_info, name='mymodel-list'),
    path('naturalgas/', views.NG_info, name='mymodel-list'),
    path('crudeoilnodes/', views.CrudeOilNodes_info, name='mymodel-list'),
    path('users/', views.Users_info, name='mymodel-list'),
]
