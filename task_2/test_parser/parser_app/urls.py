from django.urls import path

from parser_app.views import APIParse


urlpatterns = [
    path('parse/', APIParse.as_view()),
]
