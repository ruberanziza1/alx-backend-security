# IP Tracking Implementation Plan

## Task 0: Basic IP Logging Middleware
- [x] Update models.py to ensure RequestLog has ip_address, timestamp, path
- [x] Create ip_tracking/middleware.py with IPLoggingMiddleware class
- [x] Register the middleware in settings.py
- [ ] Fix imports in middleware files

## Task 1: IP Blacklisting
- [x] Ensure BlockedIP in models.py
- [x] Update ip_tracking/middleware.py to include blocking logic
- [x] Create ip_tracking/management/commands/block_ip.py

## Task 2: IP Geolocation Analytics
- [ ] Install django-ipgeolocation
- [x] Add country and city fields to RequestLog in models.py
- [x] Update middleware to populate geolocation data

## Task 3: Rate Limiting by IP
- [ ] Install django-ratelimit
- [x] Configure rate limits in settings.py
- [x] Create login view in views.py and apply rate limiting
- [x] Update urls.py

## Task 4: Anomaly Detection
- [ ] Install Celery
- [x] Create ip_tracking/tasks.py with anomaly detection task
- [x] Update the task to check for sensitive paths

## General
- [ ] Fix middleware class names and imports
- [x] Run migrations
- [ ] Test the implementation
