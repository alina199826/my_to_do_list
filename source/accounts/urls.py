from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, UserDetailView, UserList
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('list/', UserList.as_view(), name='list_users')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)