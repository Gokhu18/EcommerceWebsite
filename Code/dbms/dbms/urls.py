from django.conf.urls import patterns, include, url
from django.contrib import admin
from dbms.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$',signup),
    url(r'^login/$',login),
    url(r'^customer_home/$',customer_home),
    url(r'^add_order/$',add_order),
    url(r'^goods/$',goods),
    url(r'^index/$',index),
    url(r'^add_to_cart/$',add_to_cart),
    url(r'^view_cart/$',view_cart),
    url(r'^remove_from_cart/$',remove_from_cart),
    url(r'^buy/$',buy),
    url(r'^confirmOrder/$',confirmOrder),
    url(r'^buy_from_cart/$',buy_from_cart),
)
