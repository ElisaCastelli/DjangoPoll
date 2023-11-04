from django.urls import path

from . import views
# app_name = "polls"
# urlpatterns = [
#     path("", views.index, name="index"),  # route (string that contains a URL pattern. When processing a request,
#     # Django starts at the first pattern in urlpatterns and makes its way down the list,
#     # comparing the requested URL against each pattern until it finds one that matches,
#                                           # view (When Django finds a matching pattern, it calls the specified view
#                                           # function with an HttpRequest object as the first argument and any
#                                           # “captured” values from the route as keyword arguments) kwargs, and name# ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]