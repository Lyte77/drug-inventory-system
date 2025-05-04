
<<<<<<< HEAD

from django.contrib import admin
from django.urls import path,include
=======
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
>>>>>>> d721a13 (Updated the program)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
<<<<<<< HEAD
]
=======
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> d721a13 (Updated the program)
