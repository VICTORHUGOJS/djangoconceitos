from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Person
from.forms import PersonForm

def persons_list(request):
    persons = Person.objects.all()              #Lista dados do banco
    return render(request, 'person.html', {'persons': persons}) #List


def persons_new(request):
    form = PersonForm(request.POST or None)   #instancia os dados preenchido no bd
    if form.is_valid():
        form.save()
        return  redirect('person_list')
    return render(request,'person_form.html', {'form': form})


def persons_update(request,id):
    person = get_object_or_404(Person, pk=id) #Buscar no bd pelo id
    form = PersonForm(request.POST or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form}) #se nao for valido ou 1 vez

def persons_delete(request,id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})

