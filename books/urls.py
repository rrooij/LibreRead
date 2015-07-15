from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.BookCreate.as_view(), name='add'),
    # example:  /books/5/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]
