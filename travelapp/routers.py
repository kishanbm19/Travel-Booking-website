from rest_framework.routers import DefaultRouter
# from .models import *
# from .serializers import *
from .viewsets import *

routers=DefaultRouter()
routers.register('modes/',Modeviewset),
routers.register('modetype/',ModeTypeviewset),
routers.register('routes/',Routeviewset),
routers.register('bookings/',Bookviewset)
routers.register('Seats/',Seatviewset)

urlpatterns=routers.urls