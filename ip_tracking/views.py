from django.shortcuts import render
from django.http import JsonResponse
from .models import RequestLog, BlockedIP
from django.utils.decorators import method_decorator
from django.views import View
from django_ratelimit.decorators import ratelimit
from django.contrib.auth.views import LoginView
from django.utils import timezone

class LoginView(LoginView):
    @method_decorator(ratelimit(key='ip', rate='5/m', method='POST'))
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SensitiveView(View):
    @method_decorator(ratelimit(key='ip', rate='10/m'))
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "This is a sensitive view."})

class LogRequestView(View):
    def post(self, request, *args, **kwargs):
        ip_address = request.META.get('REMOTE_ADDR')
        path = request.path
        timestamp = timezone.now()

        # Log the request
        RequestLog.objects.create(ip_address=ip_address, path=path, timestamp=timestamp)

        return JsonResponse({"message": "Request logged."})

class BlockedIPView(View):
    def get(self, request, *args, **kwargs):
        blocked_ips = BlockedIP.objects.values_list('ip_address', flat=True)
        return JsonResponse({"blocked_ips": list(blocked_ips)})
