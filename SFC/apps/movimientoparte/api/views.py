from rest_framework.viewsets import ModelViewSet
from apps.movimientoparte.api.serializers import MovimientoParteSerializer
from apps.movimientoparte.models import MovimientoParte


class MovimientoParteViewSet(ModelViewSet):
    serializer_class = MovimientoParteSerializer
    queryset = MovimientoParte.objects.all()

    



""" from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 


class MovimientoParteAPIview(APIView):
    def get(self, request):
        data = MovimientoParte.objects.all()
        serializador = MovimientoParteSerializer(data, many=True)
        
        return Response(status=status.HTTP_200_OK, data=serializador.data)    """