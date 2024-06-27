from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile

@login_required
def index(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'lab/index.html', {'profile': profile})

@csrf_exempt
@login_required
def earn_tokens(request):
    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        profile.token_balance += 1
        profile.save()
        return JsonResponse({'token_balance': profile.token_balance})
