from django.shortcuts import render
from .models import User


def index(request):
    user_id = request.GET.get('user_id')
    if not user_id:
        return render(request, 'lab/error.html', {'message': 'User ID not provided'})

    user, created = User.objects.get_or_create(telegram_id=user_id)
    return render(request, 'lab/index.html', {'user': user})


def collect_dust(request):
    if request.method == 'POST':
        user_id = json.loads(request.body).get('user_id')
        user = User.objects.get(telegram_id=user_id)
        user.tokens += 1
        user.save()
        return JsonResponse({'tokens': user.tokens})


def page1(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(telegram_id=user_id)
    return render(request, 'page1.html', {'user': user})


def page2(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(telegram_id=user_id)
    return render(request, 'page2.html', {'user': user})
