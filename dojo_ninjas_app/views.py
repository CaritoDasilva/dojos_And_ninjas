from django.shortcuts import render, redirect
from . import models
# Create your views here.


def index(request):
    ninjas_by_dojo = models.Dojos.objects.all()
    # for dojo in models.Dojos.objects.all():
    #     ninjas = dojo.dojos.all()
    #     print('hola', dojo.dojos.all())
    #     for ninja in dojo.dojos.all():
    #         print('ninja', ninja.first_name, dojo.name)

    context = {
        'dojos': models.Dojos.objects.all(),
        'ninjas_by_dojo': ninjas_by_dojo
    }
    return render(request, 'index.html', context)


def add_ninja(request):
    dojo_id = models.Dojos.objects.get(id=request.POST.get('dojo_id'))
    print(dojo_id)
    models.Ninjas.objects.create(
        dojo_id=dojo_id,
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
    )
    return redirect('/')


def add_dojo(request):
    models.Dojos.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
        desc=int(request.POST['desc'])
    )
    return redirect('/')
