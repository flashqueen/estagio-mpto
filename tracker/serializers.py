from helpers.serializer import BaseSerializer
from .models import LegalPerson, Person, State, City, NaturalPerson



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



class PersonSerializer(BaseSerializer):
    
    _model = Person

    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
            name=instance.name
        )

        return result



class  NaturalPersonSerializer(PersonSerializer):

    _model = NaturalPerson

    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
            cpf=instance.cpf
        )

        return result

class LegalPersonSerializer(PersonSerializer):

    _model = LegalPerson

    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
            cnpj=instance.cnpj,
            fantasy_name=instance.fantasy_name
        )

        return result