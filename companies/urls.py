from django.urls import path
from companies.views.employees import Employees, EmployeesDetail

urlpatterns = [
    # Employees Endpoints
    path('employees', Employees.as_view()),
    path('employees/<int:employee_id>', EmployeesDetail.as_view()),
]
