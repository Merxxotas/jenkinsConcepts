from django.contrib import admin
from django.urls import path

from jenkinsMain.views import (cos_of_number, create_get_names, delete_name,
                               random_number, sin_of_number, update_name)

urlpatterns = [
    path("name/", create_get_names),
    path("name/<int:name_id>/", update_name),
    path("name/<int:name_id>/delete/", delete_name),
    path("number/sin/", sin_of_number),
    path("number/cos/", cos_of_number),
    path("number/random/", random_number),
]
