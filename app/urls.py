from django.urls import path
from . import views

urlpatterns = [
    path('',views.test,name='test'),
    path('Register',views.form,name="register"),
    path('result',views.result,name="result"),
    path('Donations',views.Donation,name="donations")
    
]
