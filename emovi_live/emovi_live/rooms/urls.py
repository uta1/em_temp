from django.urls import path, re_path

from emovi_live.rooms.views import search_form

app_name = "rooms"
urlpatterns = [
    # ...
    path("search-form/<t>/", view=search_form, name="sf"),
    # ...
]

