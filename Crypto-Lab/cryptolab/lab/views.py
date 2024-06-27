from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UserProfile


def index(request):
    if 'telegram_id' not in request.session:
        return redirect('login')

    profile, created = UserProfile.objects.get_or_create(telegram_id=request.session['telegram_id'])
    return render(request, 'lab/index.html', {'profile': profile})


def login(request):
    if request.method == 'POST':
        telegram_id = request.POST.get('telegram_id')
        request.session['telegram_id'] = telegram_id
        return redirect('index')
    return render(request, 'lab/login.html')


def earn_tokens(request):
    if 'telegram_id' not in request.session:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    profile = UserProfile.objects.get(telegram_id=request.session['telegram_id'])
    profile.token_balance += 1
    profile.save()
    return JsonResponse({'token_balance': profile.token_balance})
