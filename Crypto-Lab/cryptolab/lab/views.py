from django.shortcuts import render
from django.http import JsonResponse
from .models import User
import json  # Импорт библиотеки json

def index(request):
    user_id = request.GET.get('user_id')
    if user_id:
        user, created = User.objects.get_or_create(telegram_id=user_id)
        return render(request, 'lab/index.html', {'user': user})
    return render(request, 'lab/index.html')

def collect_dust(request):
    data = json.loads(request.body)
    user_id = data.get('user_id')
    if user_id:
        user = User.objects.get(telegram_id=user_id)
        user.tokens += 1
        user.save()
        return JsonResponse({'status': 'success', 'tokens': user.tokens})
    return JsonResponse({'status': 'error', 'message': 'User ID not provided'}, status=400)
