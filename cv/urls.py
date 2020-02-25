from django.contrib import admin
from django.urls import path
from authentication.views import LoginView, SignUpView
from basicInfo.views import BasicInfoView
from education.views import EducationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view()),
    path('accounts/register/', SignUpView.as_view()),
    path('builder/basicInfo/', BasicInfoView.as_view()),
    path('builder/education/', EducationView.as_view())
]
