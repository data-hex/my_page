from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def aries(request):
    return HttpResponse("[ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")


def taurus(request):
    return HttpResponse("['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")


def gemini(request):
   return HttpResponse("['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")


def cancer(request):
    return HttpResponse("['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")


def leo(request):
    return HttpResponse("['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).")


def virgo(request):
    return HttpResponse("['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).")


def libra(request):
    return HttpResponse("['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")


def scorpio(request):
    return HttpResponse("['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).")


def sagittarius(request):
    return HttpResponse("[sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).")


def capricorn(request):
    return HttpResponse("['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).")


def aquarius(request):
    return HttpResponse("[ə'kwɛəriəs] Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).")


def pisces(request):
    return HttpResponse("['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")
