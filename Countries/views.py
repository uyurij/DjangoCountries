from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import country
from django.core.exceptions import ObjectDoesNotExist

Countries = [
    {"id": 1, "country": "Aruba", "languages": "Dutch"},
    {"id": 1, "country": "Afghanistan", "languages": "Balochi"},
    ]

def home(request):
    context = {
        "name": "Горбунов Юрий Геннадьевич",
        "email": "uyurij@yandex.ru"
    }
    return render(request, 'index.html', context)

def about(request):
    text = """
    <p>Имя: <b>Юрий</b><br>
    Отчество: <b>Геннадьевич</b><br>
    Фамилия: <b>Горбунов</b><br>
    Телефон: <b>+7 (906)715-29-02</b><br>
    email: <b>uyurij@yandex.ru</b></p>
    <nav>
    <ul>
      <li><a href="countries">Страны</a></li>
      <li><a href="/">Главная</a></li>
    </ul>
  </nav>
    """
    return HttpResponse(text)

def get_country(request, country_id: int):
    try:
        country = country.objects.get(id=country_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"country with id={country_id} not found")
    else:
        context = {"country": country}
        return render(request, "country.html", context)
    
def get_countries(request):
    countries = country.objects.all()
    context = {
        "countries": countries
    }
    return render(request, "countries.html", context)


