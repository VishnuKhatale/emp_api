from django.urls import path
from .views import employee_viewset

urlpatterns = [
    path('', employee_viewset.as_view()),
    path('emp/', employee_viewset.as_view()),
    path('emp/<int:id>', employee_viewset.as_view()),
]