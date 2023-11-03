from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # route (string that contains a URL pattern. When processing a request,
    # Django starts at the first pattern in urlpatterns and makes its way down the list,
    # comparing the requested URL against each pattern until it finds one that matches,
                                          # view (When Django finds a matching pattern, it calls the specified view
                                          # function with an HttpRequest object as the first argument and any
                                          # “captured” values from the route as keyword arguments) kwargs, and name
]