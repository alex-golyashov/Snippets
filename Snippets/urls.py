from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="index-page"),
    path('snippets/add/', views.add_snippet_page, name="add-snippet-page"),
    path('snippets/delete/<int:num>/', views.delete_snippet, name="snippet-delete"),
    path('snippets/list/', views.snippets_page, name="snippets-page"),
    path('snippets/<int:num>/', views.snippets_details_page, name="snippets-details-page"),
    path('snippets/mine/', views.snippets_page_mine, name="snippets-page-mine"),
    # path('snippets/form/', views.create_snippet),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('registration/', views.registration_page, name="registration"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

