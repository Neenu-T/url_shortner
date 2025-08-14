from urllib import request
from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from shortner.forms import UrlForm

# Create your views here.
def home(request):
    short_url = None
    if request.method == 'POST':
        form=UrlForm(request.POST)
        if form.is_valid():
            url_obj=form.save()
            short_url = request.build_absolute_uri(url_obj.short_code)
    else:
        form = UrlForm()
    return render(request, 'shortner/home.html', {'form': form, 'short_url': short_url})

def redirect_url(request, short_code):
    url_obj = get_object_or_404(Url, short_code=short_code)
    return redirect(url_obj.original_url)
