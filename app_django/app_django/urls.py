
from django.contrib import admin
from django.urls import path, include # Se importa el include para agregar las urls de otras app.

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #   De esta forma se agrega las urls que estan dentro de app_user
    path('api/v1.0/user/', include('app_user.urls'))
]
