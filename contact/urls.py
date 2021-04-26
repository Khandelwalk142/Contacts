from django.contrib import admin
from django.urls import path
from Contacts import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Contacts),
    path('delete_contact/<int:contact_id>/', views.delete_contact),
    path('edit_contact/<int:contact_id>/', views.edit_contact),
    path('accounts/', include('accounts.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
