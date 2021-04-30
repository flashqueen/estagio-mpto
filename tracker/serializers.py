from helpers.serializer import BaseSerializer
from .models import State, City



class StateSerializer(BaseSerializer):
    
    _model = State

    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
            name=instance.name,
            abbreviation=instance.abbreviation

        )
        return result



class CitySerializer(BaseSerializer):
    
    _model = City

    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
            name=instance.name,
            state=StateSerializer.encode(instance.state)
        )
        return result
