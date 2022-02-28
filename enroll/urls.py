
from . import views
from django.urls import path

urlpatterns = [
    path('',views.ViewData.as_view(),name='getdata'),
    path('delete/<int:id>/',views.ViewDelete.as_view(),name='delete'),
    path('update/<int:id>/',views.ViewUpdate.as_view(),name='update'),

]
