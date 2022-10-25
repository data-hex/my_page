from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def get_week_days(request, days):
    day_list = {
        'monday': 'Пн - работать',
        'tuesday': 'Вт - учиться',
        'wednesday': 'Ср - гладить котов',
        'thursday': 'Чт - питон учить',
        'friday': 'Пт - пиво пить',
        'saturday': 'Сб - болеть',
        'sunday': 'Вс - в лес ходить',
    }
    return HttpResponse(day_list.get(days, f'Не найден день недели {days}'))

# def monday(request):
#     return HttpResponse("Понедельник день тяжелый")
#
# def tuesday(request):
#     return HttpResponse("Вторник: надо пить валерьянку")
