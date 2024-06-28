from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User

def index(request):
    user_id = request.GET.get('user_id')
    user, created = User.objects.get_or_create(telegram_id=user_id)
    return render(request, 'lab/index.html', {'user': user})

def collect_dust(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, telegram_id=user_id)
        user.tokens += 1
        user.save()
        return JsonResponse({'tokens': user.tokens})

def page1(request):
    return render(request, 'lab/page1.html')

def page2(request):
    return render(request, 'lab/page2.html')
