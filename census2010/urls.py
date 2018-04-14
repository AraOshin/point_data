from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from census2010 import views

urlpatterns = [
    # url(r'^blockgroups2010/$', views.blockgroup_list),
    url(r'^blockgroups2010/(?P<pk>[0-9]+)/$', views.blockgroup_detail),
    url(r'^blockgroups2010/latlong/(?P<latlong>.+)/$', views.blockgroup_latlong)

]
urlpatterns = format_suffix_patterns(urlpatterns)
