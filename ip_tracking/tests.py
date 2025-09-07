from django.test import TestCase
from .models import RequestLog, BlockedIP, SuspiciousIP
from django.urls import reverse
from django.utils import timezone

class IPTrackingTests(TestCase):

    def setUp(self):
        self.valid_ip = '192.168.1.1'
        self.blocked_ip = BlockedIP.objects.create(ip_address='192.168.1.2')
        self.suspicious_ip = SuspiciousIP.objects.create(ip_address='192.168.1.3', reason='Too many requests')

    def test_request_logging(self):
        response = self.client.get(reverse('some_view_name'))  # Replace with an actual view name
        log_entry = RequestLog.objects.filter(ip_address=self.valid_ip).first()
        self.assertIsNotNone(log_entry)
        self.assertEqual(log_entry.path, '/some-path/')  # Replace with actual path
        self.assertTrue(log_entry.timestamp <= timezone.now())

    def test_blocked_ip_access(self):
        self.client.cookies['ip_address'] = self.blocked_ip.ip_address
        response = self.client.get(reverse('some_view_name'))  # Replace with an actual view name
        self.assertEqual(response.status_code, 403)

    def test_suspicious_ip_logging(self):
        response = self.client.get(reverse('some_view_name'))  # Replace with an actual view name
        suspicious_entry = SuspiciousIP.objects.filter(ip_address=self.suspicious_ip.ip_address).first()
        self.assertIsNotNone(suspicious_entry)

    def test_rate_limiting(self):
        # Simulate multiple requests from the same IP
        for _ in range(10):
            self.client.get(reverse('some_view_name'))  # Replace with an actual view name
        # Check if the rate limiting logic is triggered (this will depend on your implementation)
        # You may need to check the response or the database for rate limiting effects

    def test_geolocation_logging(self):
        # Assuming geolocation middleware is in place and working
        response = self.client.get(reverse('some_view_name'))  # Replace with an actual view name
        log_entry = RequestLog.objects.filter(ip_address=self.valid_ip).first()
        self.assertIsNotNone(log_entry)
        self.assertIsNotNone(log_entry.country)  # Assuming country field exists
        self.assertIsNotNone(log_entry.city)     # Assuming city field exists