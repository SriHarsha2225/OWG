from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(LoadData)
admin.site.register(USAStates)
admin.site.register(SiteData)
admin.site.register(SiteEnviroment)
admin.site.register(WasteWater)
admin.site.register(NG)
admin.site.register(CrudeOilNodes)
admin.site.register(Users)