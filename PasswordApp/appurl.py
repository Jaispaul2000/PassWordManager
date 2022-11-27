from django.urls import path
from PasswordApp.views import UserView,PassWordView,OrganizationView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("accounts/signup",UserView,basename="signup"),
router.register("password",PassWordView,basename="password")
router.register("organization",OrganizationView,basename="organization")
urlpatterns = [
    path("token/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
]+router.urls