from django.urls import path
from .views import enquiry_viewset

urlpatterns = [
    # path('', enquiry_viewset.as_view()),
    path('enquiry/', enquiry_viewset.as_view()),
    path('enquiry/<int:id>', enquiry_viewset.as_view()),
]