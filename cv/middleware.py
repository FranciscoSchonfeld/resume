from .models import Visitor

#keep track of the number of visits of the site
class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        #visitor information
        if request.session.get('visited', False) is False:
            visitor = Visitor(
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT')
            )
            visitor.save()
            request.session['visited'] = True

        return response
