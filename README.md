# alx-backend-security Project

## Overview
The `alx-backend-security` project is designed to implement various security features for web applications, focusing on IP tracking and management. This project includes an application named `ip_tracking`, which provides middleware for logging IP addresses, blacklisting, geolocation analytics, rate limiting, and anomaly detection.

## Features
- **IP Logging**: Middleware that logs the IP address, timestamp, and path of every incoming request.
- **Blacklisting**: Middleware to block requests from specified IP addresses, returning a 403 Forbidden response.
- **Geolocation Analytics**: Enhances logging with geolocation data, including country and city information.
- **Rate Limiting**: Implements rate limiting for requests based on user authentication status.
- **Anomaly Detection**: Flags suspicious IPs based on request patterns using Celery tasks.

## Project Structure
```
alx-backend-security
├── ip_tracking
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── middleware
│   │   ├── __init__.py
│   │   ├── ip_logging.py
│   │   ├── blacklist.py
│   │   ├── geolocation.py
│   │   ├── rate_limiting.py
│   │   └── anomaly_detection.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── utils
│       ├── __init__.py
│       ├── geo_utils.py
│       └── anomaly_utils.py
├── alx_backend_security
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd alx-backend-security
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
- The middleware will automatically log incoming requests and apply security measures as configured.
- You can manage blacklisted IPs through the Django admin interface.
- Rate limits and anomaly detection will operate based on the defined logic in the middleware.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.