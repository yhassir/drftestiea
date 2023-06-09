from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views

# api versioning
router = routers.DefaultRouter()
# ---
# router.register(r'tasks', views.TaskViews, 'Tasks')
router.register(r'devices', views.DevicesViews, 'Devices')
router.register(r'schedules', views.ScheduleViews, 'Schedules')
router.register(r'userdevices', views.UserDevicesViews, 'UserDevices')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Task API'))
]