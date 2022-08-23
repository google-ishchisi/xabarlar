from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, register, Login, Logout, blog, detail, category, region, Search

urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),

    path('register/', register, name="register"),
    path('login/', Login, name="login"),
    path('logout/', Logout, name="logout"),

    path('detail/<int:id>', detail, name='detail'),
    path('category/<int:id>', category, name='category'),
    path('region/<int:id>', region, name='region'),

    path('search/', Search, name="search")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# <int:id>