from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class ChildRedirectView(RedirectView):
    #url = 'https://www.google.com'
    url = '/'
    
class GeekRedirectView(RedirectView):
    pattern_name='mindex'
    permanent = True
    query_string = True
    
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk'] = 14
        return super().get_redirect_url(*args, **kwargs)