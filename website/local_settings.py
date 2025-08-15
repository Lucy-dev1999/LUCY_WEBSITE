# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ainembabaziluciarachel02@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'iloveyoujesus'  # Replace with your Gmail app password
DEFAULT_FROM_EMAIL = 'ainembabaziluciarachel02@gmail.com'  # Replace with your Gmail address
CONTACT_EMAIL = 'ainembabaziluciarachel02@gmail.com'  # Replace with your contact email

# Security settings
SECURE_SSL_REDIRECT = False  # Set to True in production
SESSION_COOKIE_SECURE = False  # Set to True in production
CSRF_COOKIE_SECURE = False  # Set to True in production
