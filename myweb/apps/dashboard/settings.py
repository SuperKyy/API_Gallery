SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

STATIC_URL = '/static/'

STATIC_ROOT = 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)