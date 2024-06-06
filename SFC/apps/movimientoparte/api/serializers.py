from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from apps.movimientoparte.models import MovimientoParte

from apps.movimiento.api.serializers import MovimientoSerializer
from apps.parteevento.api.serializers import ParteEventoSerializer


#modelos de los otros 
from apps.parteevento.models import ParteEvento
from apps.movimiento.models import Movimiento


class MovimientoParteSerializer(ModelSerializer):
    
    # poder concultar a el modelo 
    fk_parte_evento =PrimaryKeyRelatedField(queryset=ParteEvento.objects.all())
    fk_movimiento = PrimaryKeyRelatedField(queryset=Movimiento.objects.all())

    class Meta:
        model = MovimientoParte
        fields = ['id', 'fk_parte_evento', 'fk_movimiento', 'repeticiones', 'orden','date_created' ]
        
        
     ## solo poder crear un registro    
    def create(self, validated_data):
        
        parte_evento_data= validated_data.pop('fk_parte_evento')
        movimiento_data = validated_data.pop('fk_movimiento')
        
        validated_data['fk_movimiento'] = movimiento_data
        
        movimiento = MovimientoParte.objects.create(
            fk_parte_evento=parte_evento_data,
            **validated_data)
       
        return  movimiento
     
     
    def get_parte_evento(self, obj):
        parte_evento = obj.fk_parte_evento
        serializador = ParteEventoSerializer(parte_evento)

        return serializador.data
        
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['parte_evento'] = self.get_parte_evento(instance) 
        print(self.get_parte_evento(instance))
        print("hola emer")
        return representation