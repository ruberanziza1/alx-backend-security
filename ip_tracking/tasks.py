from celery import shared_task
from .models import SuspiciousIP, RequestLog
from django.utils import timezone

@shared_task
def detect_anomalies():
    # Fetch request logs from the last hour
    one_hour_ago = timezone.now() - timezone.timedelta(hours=1)
    recent_logs = RequestLog.objects.filter(timestamp__gte=one_hour_ago)

    # Analyze logs for suspicious patterns
    ip_request_count = {}
    sensitive_paths = ['/admin', '/login']
    for log in recent_logs:
        ip_request_count[log.ip_address] = ip_request_count.get(log.ip_address, 0) + 1
        if log.path in sensitive_paths:
            SuspiciousIP.objects.get_or_create(ip_address=log.ip_address, reason=f'Access to sensitive path: {log.path}')

    # Flag suspicious IPs based on request count threshold
    threshold = 100  # Example threshold
    for ip, count in ip_request_count.items():
        if count > threshold:
            SuspiciousIP.objects.get_or_create(ip_address=ip, reason='Excessive requests in a short time frame')
