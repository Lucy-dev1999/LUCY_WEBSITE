# Local settings for email configuration
# Keep this file secure and don't commit it to version control

# Email Configuration for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ainembabaziluciarachel02@gmail.com' 
EMAIL_HOST_PASSWORD = 'zfjbuyxvedjpjuxb'  # Gmail App Password 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# To get your Gmail App Password:
# 1. Go to your Google Account settings
# 2. Enable 2-Step Verification if not already enabled
# 3. Go to Security > 2-Step Verification > App passwords
# 4. Generate a new app password for "Mail"
# 5. Copy the 16-character password and paste it above
