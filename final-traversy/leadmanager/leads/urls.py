# we will use routers from rest frame work to specify url
from rest_framework import routers
from .api import LeadViewSet

router=routers.DefaultRouter()
router.register('api/leads',LeadViewSet,'leads')

urlpatterns=router.urls 
#all urls that are registerd