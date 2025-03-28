from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    path('about_us/', views.about_us, name='about_us'),

    # path for contact us view

    path('contact_us/', views.contact_us, name='contact_us'),

    # path for registration

     path('registration/', views.registration_view, name='registration'),

    # path for login

    path('login/', views.login_view, name='login'),

    # path for logout

    path('logout/', views.logout_view, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)