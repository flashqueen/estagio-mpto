from helpers import restfy
from .serializers import (
    StateSerializer,
    CitySerializer,
    NaturalPersonSerializer
)



natural_person_index, natural_person_by_id = restfy.make_rest(NaturalPersonSerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)