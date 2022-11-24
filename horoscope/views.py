from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

zodiac_elements_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiacs = list(zodiac_dict)
    li_elem = ''
    for sign in zodiacs:
        redirect_path = reverse(viewname='horoscope-name', args=[sign])
        li_elem += f"<li> <a target='_blank' href='{redirect_path}'>{sign.title()} </a> </li>"
    response = f"""
    <ol>
        {li_elem}
    </ol>
    """
    return HttpResponse(response)


def get_sign_of_elements(request, types_zodiac: str):
    if zodiac_elements_dict.get(types_zodiac):
        li_elem = ''
        for element in list(zodiac_elements_dict.get(types_zodiac)):
            redirect_path = reverse('horoscope-name', args=[element])
            li_elem += f"<li> <a target='_blank' href='{redirect_path}'>{element.title()} </a> </li>"

        response = f"""
        <ol>
            {li_elem}
        </ol>
        """
        return HttpResponse(response)
    elif zodiac_dict.get(zodiac_elements_dict):
        return HttpResponse(zodiac_dict[zodiac_elements_dict])
    else:
        return HttpResponseNotFound(f"Неверная стихия - {zodiac_elements_dict}")


def get_elements(request, type: str):
    zodiac_elements = list(zodiac_elements_dict.keys())
    li_elem = ''
    for element in zodiac_elements:
        redirect_path = reverse(viewname='element-name', args=[element])
        li_elem += f"<li> <a target='_blank' href='{redirect_path}'>{element.title()} </a> </li>"
    response = f"""
    <ol>
        {li_elem}
    </ol>
    """
    return HttpResponse(response)


def get_horoscope_by_sign(request, sign_of_zodiac: str):
    description = zodiac_dict.get(sign_of_zodiac)
    data = {
        "description_zodiac": description,
        "sign": sign_of_zodiac.title()
    }

    return render(request, 'horoscope/info_zodiac.html', context=data)

    #response = render_to_string('horoscope/info_zodiac.html')
    #if description:
        #return HttpResponse(response)
"""    elif sign_of_zodiac == "type":
        return HttpResponseRedirect('type/')
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_of_zodiac}")"""


def get_horoscope_by_sign_by_number(request, sign_of_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_of_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный номер Зодиака - {sign_of_zodiac}')
    name_zodiac = zodiacs[sign_of_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
