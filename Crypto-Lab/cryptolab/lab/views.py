from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import User

def index(request):
    if settings.USE_TELEGRAM_ID:
        user_id = request.GET.get('user_id')
        user, created = User.objects.get_or_create(telegram_id=user_id)
    else:
        user, created = User.objects.get_or_create(telegram_id='default_user')
    
    return render(request, 'lab/index.html', {'user': user})

def collect_dust(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(telegram_id=user_id)
        user.tokens += 1
        user.save()
        return JsonResponse({'tokens': user.tokens})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def page1(request):
    return render(request, 'lab/page1.html')

def page2(request):
    return render(request, 'lab/page2.html')
