from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_cv/',views.create_cv, name='create_cv'),
    path('view_cv_database/',views.view_cv_database, name='view_cv_database'),
    path('render_context_to_cv/<int:id>/',views.render_context_to_cv, name='render_context_to_cv'),
    path('download_pdf/<int:id>/',views.download_pdf,name='download_pdf'),
    path('delete_cv/<int:id>/',views.delete_cv, name='delete_cv'),
    path('contact_developer/', views.contact_developer, name='contact_developer'),
    #path('print_radio/',views.print_radio, name='print_radio'),
    
]