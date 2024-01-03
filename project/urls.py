from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import ConfirmAuditoriumAndREGView, ConfirmPresentView, UserEvents, UpdateRegistrationView

urlpatterns = [
    path("api/<str:id>/userevents", UserEvents.as_view(), name="userevents"),
    path(
        "api/<str:user_id>/<int:event_id>/confirm",
        ConfirmPresentView.as_view(),
        name="confirm",
    ),
    path("admin/", admin.site.urls, name="admin"),
    path(
        "api/<str:user_id>/<int:event_id>/audit-reg",
        ConfirmAuditoriumAndREGView.as_view(),
        name="audit-reg",
    ),
    path('api/update-registration/<str:id>/', UpdateRegistrationView.as_view(), name='update-event-registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Anubhuti Events"
admin.site.site_title = "Anubhuti Events"
admin.site.index_title = "Anubhuti Events"