from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def get_week_days(request, days: str):
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


def get_week_days_by_number(request, days: int):
    if days in range(1, 8):
        return HttpResponse(f"Сегодня {days} день недели")
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {days}")
