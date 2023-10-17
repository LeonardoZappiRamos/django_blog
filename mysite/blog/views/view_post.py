from django.views import generic
from django.http import HttpResponse

import datetime


class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        html = "<html><body>Hello !! It %s now.</body></html>" % now
        return HttpResponse(html)