# outfit_recommender/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'outfit_recommender.settings')

application = get_wsgi_application()
