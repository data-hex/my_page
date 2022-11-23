from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def main(request):
    return render(request, 'week_days/greeting.html')


def get_week_days(request, days: str):
    return HttpResponse(day_list.get(days, f'Не найден день недели {days}'))


def get_week_days_by_number(request, days: int):
    if days in range(1, 8):
        names = list(day_list)
        name_day = names[days - 1]
        redirect_url = reverse("week_days_name", args=[name_day])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {days}")
