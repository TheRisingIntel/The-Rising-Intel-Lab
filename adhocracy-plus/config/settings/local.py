# replace 'your.domain' with your desired domain
BASE_URL = ' http://127.0.0.1:8000 '
ALLOWED_HOSTS = [u'eagleabove1.herokuapp.com', u'127.0.0.1']

# database config - we recommend postgresql for production purposes
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'localhost',
    'USER': 'user_1',
    'PASSWORD': '54321',
    'HOST': '127.0.0.1'
  }
} 

# forward outgoing emails to a local email proxy
EMAIL_BACKEND='django.core.mail.backends.smtp.mailcoat.com'
EMAIL_HOST='smtp.mailcoat.com'

# folder for user-uploads, directly served from the webserver (see nginx example below). Must be created manually.
MEDIA_ROOT='/home/azeez/TRI-copy/aplus-media'

# replace the value below with some random value
SECRET_KEY = '8lu*6g0lg)9z!ba+a$ehk)xt)x%rxgb$i1&amp;022shmi1jcgihb*'

# some basic security settings for serving the website over https - see django docu
CSRF_COOKIE_SECURE=True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_HTTPONLY = True

FILE_UPLOAD_PERMISSIONS = 0o644
