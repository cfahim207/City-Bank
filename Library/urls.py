
from django.contrib import admin
from django.urls import path,include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('category/<slug:Brand_slug>/', home, name='brand_wise_post'),
    path('account/', include("accounts.urls")),
    path('books/', include("books.urls")),
    path('transaction/', include("Transaction.urls")),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


