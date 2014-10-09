from django.conf.urls import patterns, url

from utility import views

urlpatterns = patterns(
    '',
    url(r'upload/in/bloomington/(?P<bldg_tag>\w+)/$', views.upload_bloomington),
    url(r'upload/in/bloomington/$', views.upload_bloomington),

    #url(r'upload/(?P<state>\w+)/(?P<city_name>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>\w+)/$', views.upload),
    #url(r'upload/(?P<state>\w+)/(?P<city_name>\w+)/(?P<bldg_tag>\w+)/$', views.upload),
    #url(r'upload/(?P<state>\w+)/(?P<city_name>\w+)/$', views.upload),
    
    url(r'upload/(?P<state>\w+)/(?P<city_name>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>[\w#]+)/$', views.upload),
    url(r'upload/(?P<state>\w+)/(?P<city_name>\w+)/(?P<bldg_tag>\w+)/$', views.upload),
    url(r'upload/(?P<state>\w+)/(?P<city_name>\w+)/$', views.upload),
    #url(r'test/$', views.upload_handler),

    ## url(r'(?P<utility_tag>\w+)/(?P<city_tag>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>[\w\%\#]+)/edit/$', views.share),
    ## url(r'(?P<utility_tag>\w+)/(?P<city_tag>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>[\w\%\#]+)/edit$', views.share),
    
    url(r'(?P<city_tag>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>[\w\%\#]+)/edit/$', views.edit),
    url(r'(?P<city_tag>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>[\w\%\#]+)/edit$', views.edit),
    url(r'(?P<city_tag>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>[\w\%\#]+)/$', views.details),
    url(r'(?P<city_tag>\w+)/(?P<bldg_tag>\w+)/(?P<unit_tag>[\w\%\#]+)$', views.details),
    
    url(r'thank_you/$', views.thank_you),
    url(r'secret/$', views.secret),
    url(r'upload/$', views.upload, name='utility_upload'),
    url(r'upload$', views.upload, name='utility_upload'),
    url(r'^$', views.index, name='utility_index')
)