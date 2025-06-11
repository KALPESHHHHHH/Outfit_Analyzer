from django.utils import translation
from django.conf import settings
from django.urls import reverse

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get language from session or cookie
        language = request.session.get('language') or \
                   request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME) or \
                   settings.LANGUAGE_CODE
        
        # Set the language
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
        
        response = self.get_response(request)
        
        # Set language cookie if not already set
        if not request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME):
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME,
                language,
                max_age=365*24*60*60,
                httponly=True
            )
        
        return response