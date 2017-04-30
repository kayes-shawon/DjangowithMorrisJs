from atmosphere.forms import AtmosForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Atmos


class AtmosView(CreateView):
    template_name = 'atmosphere/atmos_form.html'
    form_class = AtmosForm
    success_url = '/atmosphere/atmos_show/'

def get_atmophere_show(request):

    data = Atmos.objects.all()
    return render(request,'atmosphere/atmos_show.html',{'data':data})
    # return render(request, 'atmosphere/atmos_show.html')