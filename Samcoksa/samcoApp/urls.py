
from django.urls import path,include
from .views import *
from rest_framework import routers
from .viewset import *

router = routers.DefaultRouter()
router.register(r'author',AuthorViewSet)
router.register(r'contact',ContactViewSet)
router.register(r'contactu',ContactUViewSet)
router.register(r'about',AboutViewSet)
router.register(r'team',TeamViewSet)
router.register(r'service',ServiceViewSet)

urlpatterns = [
    path('',index,name = "index"),
    path('profile/<id>',profile, name="profile"),
    path('api', include(router.urls)),
    # path('profile',profile, name="profile")

]
