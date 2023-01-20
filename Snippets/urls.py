from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="index-page"),
    path('snippets/add/', views.add_snippet_page, name="add-snippet-page"),
    path('snippets/list/', views.snippets_page, name="snippets-page"),
    path('snippets/<int:num>/', views.snippets_details_page, name="snippets-details-page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

