DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ✅ must be before auth
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ✅ must be present
    'django.contrib.messages.middleware.MessageMiddleware',     # ✅ must be present
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # you can add template directories later
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'tasks',
]

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                       # your DB name
        'USER': 'postgres',                       # your DB user
        'PASSWORD': 'Disha@19122004',   # exact password from Supabase
        'HOST': 'db.cmawsnkjjgcqeatpjguo.supabase.co',           # exact host from Supabase
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',                 # important for Supabase
        }
    }
}
