from django.contrib import admin
from django.urls import path, include
from wrap_gpt.core.views import index, console, case, lab, \
    upload_content, upload_excel, download_excel, delete_excel, do_lab

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # pages
    path('', index, name='index'),
    path('console', console, name='console'),
    path('case', case, name='case'),
    path('lab', lab, name='lab'),
    # functions
    path('upload_content', upload_content, name='upload_content'),
    path('upload_excel', upload_excel, name='upload_excel'),
    path('download/<str:file_name>/', download_excel, name='download_excel'),
    path('delete_excel', delete_excel, name='delete_excel'),
    path('do_lab', do_lab, name='do_lab'),
]