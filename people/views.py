from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
people = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]

def get_people(request):
    context = {
        'people': people
    }
    return render(request, 'people/index.html', context=context)