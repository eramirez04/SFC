from rest_framework.routers import DefaultRouter

from apps.movimientoparte.api.views import MovimientoParteViewSet

router_movimientoParte = DefaultRouter()
router_movimientoParte.register(prefix="movimientoParte", basename="MovimientoParte", viewset=MovimientoParteViewSet)

""" from rest_framework.routers import DefaultRouter

from apps.movimientoparte.api.views import MovimientoParteViewSet,MovimientoParteAPIview

from django.urls import path, include

router_movimientoParte = DefaultRouter
router_movimientoParte.register(r'movimientoPaete', MovimientoParteViewSet)


urlpatterns = [
    path('', include(router_movimientoParte.urls)),
    path('',MovimientoParteAPIview.as_view())
] """