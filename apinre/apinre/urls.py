from django.contrib import admin
from django.urls import path
from rest_framework import routers
from aviso.api.viewsets import MenssagemViewSet
from conta.api.viewsets import UserViewSet
from core.api.viewsets import TurmaViewSet
from django.conf.urls import include
from rest_framework.authtoken import views
from website.views import home, index
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'menssagens', MenssagemViewSet, base_name='Menssagem')
router.register(r'usuarios', UserViewSet, base_name='User')
router.register(r'turmas', TurmaViewSet, base_name='Turma')


urlpatterns = [
	path('core/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),

	#path('website/', include(website.urls)),
	path('home/', home, name='home'),
	path('', index, name='index'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
