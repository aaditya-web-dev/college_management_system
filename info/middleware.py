import datetime
from django.conf import settings
from django.shortcuts import redirect

class AutoLogout:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                elapsed_time = (datetime.datetime.now() - datetime.datetime.fromisoformat(last_activity)).total_seconds()
                if elapsed_time > settings.SESSION_COOKIE_AGE:
                    del request.session['last_activity']
                    return redirect('logout')  # Redirect to logout view

            request.session['last_activity'] = datetime.datetime.now().isoformat()

        return self.get_response(request)
