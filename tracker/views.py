from helpers import restfy
from .serializers import (
    StateSerializer,
    PersonSerializer,
    CitySerializer,
    NaturalPersonSerializer,
    LegalPersonSerializer,
    PackageContainerSerializer
)


(
    package_container_index, 
    package_container_by_id
) = restfy.make_rest(PackageContainerSerializer)
person_index, person_by_id = restfy.make_rest(
    PersonSerializer,
    allow_create=False,
    allow_update=False,
    allow_delete=False
    )
natural_person_index, natural_person_by_id = restfy.make_rest(NaturalPersonSerializer)
legal_person_index, legal_person_by_id = restfy.make_rest(LegalPersonSerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)