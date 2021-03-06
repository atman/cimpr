from django.contrib import admin
from django.urls import path
from .views import (ContactAPIView,
                    ContactDetailAPIView,
                    )

app_name = 'relations'

urlpatterns = [

    path('', ContactAPIView.as_view(), name="contact"),
    path('<int:pk>/', ContactDetailAPIView.as_view(), name="contact-detail"),
    #path('create/', ContactCreateAPIView.as_view(), name="contact-create"),
    #path('<int:pk>/update/', ContactUpdateAPIView.as_view(), name="contact-update"),
    #path('<int:pk>/delete/', ContactDeleteAPIView.as_view(), name="contact-delete"),

]

# Start With

# /api/contact/ --> LIST
# /api/contact/create/ --> LIST
# /api/contact/12/update --> LIST
# /api/contact/12/delete --> LIST

# End with

# /api/contact/--> List / CRUD
# /api/contact/1 --> Detail / CRUD

# Final

# /api/contact/ --> CRUD LS
