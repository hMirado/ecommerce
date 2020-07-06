from .models import MarketingMessage

class DisplayMarketing:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.session['marketing_message'] = MarketingMessage.objects.get_featured_item().message
        except:
            request.session['marketing_message'] = False

        response = self.get_response(request)

        return response
        