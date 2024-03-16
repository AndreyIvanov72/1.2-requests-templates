from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 150,
        'сыр, г': 60,
        'сливки, л': 0.08,
        'соль, ч.л.': 1,
        'перец черный молотый, ч.л.': 0.3,

    },
    'hot-dog': {
        'Булочка, шт': 1,
        'сосиска, шт': 1,
        'кетчуп, ст.л.': 2,
        'майонез, ст.л.': 2,
        'горчица, ст.л.': 0.5,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    context = {'recipe': DATA.get('omlet')}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'index.html', context=context)

def pasta(request):
    context = {'recipe': DATA.get('pasta')}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'index.html', context=context)

def hotdog(request):
    context = {'recipe': DATA.get('hot-dog', {})}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'index.html', context=context)


def home(request):
    return render(request, 'main.html')


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
