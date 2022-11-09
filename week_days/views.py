from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.
day_list = {
        'monday': 'Пн - работать',
        'tuesday': 'Вт - учиться',
        'wednesday': 'Ср - гладить котов',
        'thursday': 'Чт - питон учить',
        'friday': 'Пт - пиво пить',
        'saturday': 'Сб - болеть',
        'sunday': 'Вс - в лес ходить',
    }


def get_week_days(request, days: str):
    return HttpResponse(day_list.get(days, f'Не найден день недели {days}'))


def get_week_days_by_number(request, days: int):
    if days in range(1, 8):
        names = list(day_list)
        name_day = names[days - 1]
        return HttpResponseRedirect(f"/todo_week/{name_day}")
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {days}")
