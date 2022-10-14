
from django.contrib import admin
from django.urls import path, include

from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('bookstore/', include('bookstore.urls')),
    path('accounts/', include('accounts.urls')),
    #path('socialaccounts/', include('allauth .urls')),
    path('cart/',include('carts.urls')),


    #bookloan
    path('bookloan/',include('bookloan.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Welcome, Librarian'        # default: "Django Administration"
admin.site.index_title = 'Cardiff Library'                 # default: "Site administration"
admin.site.site_title = 'Cardiff Library' # default: "Django site admin"