
from django.urls import path, include
from leads import views as lead_view
from django.conf import settings #add this
from django.conf.urls.static import static

urlpatterns = [
    path('', lead_view.app_homepage, name="lead_homepage"),
    path('create/', lead_view.lead_form, name="create_lead"),
    path('<int:pk>/update/', lead_view.update_lead, name="update_lead"),
    path('<int:pk>/delete', lead_view.delete_lead, name="delete_lead"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)