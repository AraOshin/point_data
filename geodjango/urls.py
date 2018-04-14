from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from geodjango import views

urlpatterns = [
    # url(r'^blockgroups2010/$', views.blockgroup_list),
    # url(r'^test/(?P<pk>[0-9]+)/$', views.blockgroup_detail),
    url(r'^pointdata/latlong/(?P<latlong>.+)/$', views.latlong_search)

]
urlpatterns = format_suffix_patterns(urlpatterns)



# from django.conf.urls import url, include
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


# schema_view = get_swagger_view(title='blockgroups2010') 

# urlpatterns = [
#     url(r'^', include('census2010.urls')),
#     url(r'^schema/', schema_view)
# ]

