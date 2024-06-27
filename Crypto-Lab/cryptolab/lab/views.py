from django.shortcuts import render, redirect
from .models import User, UserIP
from django.views.decorators.csrf import csrf_exempt

def index(request):
    user_id = request.GET.get('user_id')
    if user_id:
        user, created = User.objects.get_or_create(telegram_id=user_id)
        return render(request, 'lab/index.html', {'user': user})
    else:
        return render(request, 'lab/index.html', {'error': 'User ID not provided'})

@csrf_exempt
def collect_dust(request):
    user_id = request.POST.get('user_id')
    if user_id:
        try:
            user = User.objects.get(telegram_id=user_id)
            user.balance += 10  # Добавляем условные 10 токенов
            user.save()
            return render(request, 'lab/update_balance.html', {'user': user})
        except User.DoesNotExist:
            return render(request, 'lab/update_balance.html', {'error': 'User does not exist'})
    return render(request, 'lab/update_balance.html', {'error': 'User ID not provided'})
