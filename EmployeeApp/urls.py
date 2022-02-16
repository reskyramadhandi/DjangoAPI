from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department$', views.department_api),
    url(r'^department/([0-9]+)$', views.department_api),

    url(r'^grade$', views.grade_api),
    url(r'^grade/([0-9]+)$', views.grade_api),

    url(r'^employee$', views.employee_api),
    url(r'^employee/([0-9]+)$', views.employee_api),

    url(r'^employee/savefile', views.save_file)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
