from django.urls import path,include
from .import views
urlpatterns = [
   path("details/<int:id>", views.DetailsBook.as_view(), name="details_book")
]
