from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("nonhome",views.nonhome,name = "nonhome"),
    path("AddMedicine",views.AddMedicine,name = "addMedicine"),
    path("UpdateMedicine/<int:medicine_id>",views.UpdateMedicine,name = "UpdateMedicine"),
    path("DeleteMedicine/<int:medicine_id>",views.DeleteMedicine,name = "DeleteMedicine"),
]
