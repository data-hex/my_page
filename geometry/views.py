from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi
from django.urls import reverse


# Create your views here.
def get_rectangle_area(request, width: int, height: int):
    if 'get_' in request.path:
        redirect_url = reverse('name-rectangle', args=(width, height))
        return HttpResponseRedirect(redirect_url)
    area = width * height
    answer = f"Площадь прямоугольника размером {width}x{height} равна {area}"
    return HttpResponse(answer)


def get_square_area(request, side: int):
    if 'get_' in request.path:
        redirect_url = reverse('name-square', args=[side])
        return HttpResponseRedirect(redirect_url)
    area = side ** 2
    answer = f"Площадь квадрата размером {side}x{side} равна {area}"
    return HttpResponse(answer)


def get_circle_area(request, radius: int):
    if 'get_' in request.path:
        redirect_url = reverse('name-circle', args=[radius])
        return HttpResponseRedirect(redirect_url)
    area = pi * radius ** 2
    answer = f"Площадь круга радиуса {radius} равна {area}"
    return HttpResponse(answer)