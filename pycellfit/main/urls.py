from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views as pycellfit_views

urlpatterns = [
                  # view for the 'home' url is defined in views.py
                  path('', pycellfit_views.index, name='home'),
                  path('about', pycellfit_views.about, name='about'),
                  # url for all the files in the `media/` folder are here:
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
