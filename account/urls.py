from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^sign_in$', views.sign_in),
    url(r'^sign_up$', views.sign_up),
    url(r'^logout$', views.log_out),
    url(r'^create_account$', views.create_account),
    url(r'^verify_email$', views.verify_email),
    url(r'^resend_verify_email$', views.resend_verify_email),
    url(r'^modify$', views.modify),
    url(r'^reset_password$', views.reset_password),
]
