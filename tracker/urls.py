from django.urls import path
from .views import (
    package_container_log_trace,
    state_index,
    state_by_id,
    city_index,
    city_by_id,
    natural_person_index,
    natural_person_by_id,
    legal_person_index,
    legal_person_by_id,
    person_index,
    person_by_id,
    package_container_index,
    package_container_by_id,
    log_trace_index,
    log_trace_by_id
)


urlpatterns = [  
    path('log-traces', log_trace_index),
    path('log-traces/<int:id>', log_trace_by_id),
    path('packages', package_container_index),
    path('packages/<int:id>', package_container_by_id),
    path('packages/<str:unique_identify>/log', package_container_log_trace),
    path('person', person_index),
    path('person/<int:id>', person_by_id),
    path('legal-person', legal_person_index),
    path('legal-person/<int:id>', legal_person_by_id),
    path('natural-person', natural_person_index),
    path('natural-person/<int:id>', natural_person_by_id),
    path('states', state_index),
    path('states/<int:id>', state_by_id),
    path('cities', city_index),
    path('cities/<int:id>', city_by_id),
 ]
