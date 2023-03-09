from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Main, Dashboard, Production, Quality, Cooperative, Business, Okr, Crew
from .views import Overview, Location, Inquiry, Login, Register, Forgot_password, My_page, My_account, Error404



urlpatterns = [
    path('', Main.as_view()),
    path("admin/", admin.site.urls),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('production/', Production.as_view(), name='production'),
    path('quality/', Quality.as_view(), name='quality'),
    path('cooperative/', Cooperative.as_view(), name='cooperative'),
    path('business/', Business.as_view(), name='business'),
    path('okr/', Okr.as_view(), name='okr'),
    path('overview/', Overview.as_view(), name='overview'),
    path('crew/', Crew.as_view(), name='crew'),
    path('location/', Location.as_view(), name='location'),
    path('inquiry/', Inquiry.as_view(), name='inquiry'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('forgot_password/', Forgot_password.as_view(), name='forgot_password'),
    path('my_account/', My_account.as_view(), name='my_account'),
    path('my_page/', My_page.as_view(), name='my_page'),
    path('404/', Error404.as_view(), name='404'),
    path('auth/', include('users.urls')),
    path('todos/',include('todos.urls')),
    path('business_management/', include('business_management.urls')),
    path('single_pages/', include('single_pages.urls')),
   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)