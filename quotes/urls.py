from django.conf.urls.defaults import *

urlpatterns = patterns('quotes.views',
    (r'^$', 'main'),
    (r'^r.$', 'autoreload'),
    (r'^quotes/(?P<quote_id>\d+)/$', 'detail'),   # quote permalinks
    (r'^quotes/submit/$', 'submit'),	# quote submission form
)
