from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [ 
    # Django admin
    path('admin/', admin.site.urls),
    
    # User management
    path('', include('accounts.urls')),
    
    
    path('', include('pages.urls')),
    path('', include('project.urls')),
    path('projects/', include('project.urls')),
    path('projects/<uuid:project_id>/', include('todolist.urls')),
    path('projects/<uuid:project_id>/<uuid:todolist_id>/', include('task.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
