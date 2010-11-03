from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('welcome/index.html', {
        'sup': "What's up"
    }, context_instance=RequestContext( request ))
