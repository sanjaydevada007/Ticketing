from django.conf.urls import url
from . import views

app_name='complaint'


urlpatterns=[
url(r'^alltics/$',views.DetailView.as_view(),name='detail'),
url(r'^$',views.Index,name='index'),
url(r'^createtic/$',views.TicketCreate.as_view(),name='create'),
url(r'^alltics/(?P<pk>[0-9]+)/$',views.TicketUpdate.as_view(),name='update'),
url(r'^alltics/(?P<pk>[0-9]+)/del/$',views.TicketDelete.as_view(),name='del'),


]