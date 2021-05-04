from helpers import restfy
from .serializers import (
    StateSerializer,
    CitySerializer,
    NaturalPersonSerializer,
    LegalPersonSerializer
)



natural_person_index, natural_person_by_id = restfy.make_rest(NaturalPersonSerializer)
legal_person_index, legal_person_by_id = restfy.make_rest(LegalPersonSerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)