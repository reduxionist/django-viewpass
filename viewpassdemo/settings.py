# Django settings for testtinymce project.

from os.path import join, dirname, realpath

ROOT_PATH = dirname(realpath(__file__))
DEBUG = True

TEMPLATE_DIRS = (join(ROOT_PATH, "templates"),)

AUTHENTICATION_BACKENDS = [
    'viewpass.backends.ViewPassBackend',
    'django.contrib.auth.backends.ModelBackend',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(ROOT_PATH, "viewpass.sqlite"),
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'viewpass.middleware.ViewPassMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = 'w4o4x^&b4h4zne9&3b1m-_p-=+&n_i_sdf@oz=gd+6h6v1$sd9'

ROOT_URLCONF = 'viewpassdemo.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.admin',
    'viewpass',
)
