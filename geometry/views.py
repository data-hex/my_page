from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi


# Create your views here.
def get_rectangle_area(request, width: int, height: int):
    area = width * height
    answer = f"Площадь прямоугольника размером {width}x{height} равна {area}"
    return HttpResponse(answer)


def rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(f"/rectangle/{width}/{height}")


def get_square_area(request, side: int):
    area = side ** 2
    answer = f"Площадь квадрата размером {side}x{side} равна {area}"
    return HttpResponse(answer)


def square_area(request, side: int):
    return HttpResponseRedirect(f"/square/{side}")


def get_circle_area(request, radius: int):
    area = pi * radius ** 2
    answer = f"Площадь круга радиуса {radius} равна {area}"
    return HttpResponse(answer)


def circle_area(request, radius: int):
    return HttpResponseRedirect(f"/circle/{radius}")