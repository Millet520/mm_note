from django.utils.deprecation import MiddlewareMixin


class Mymw(MiddlewareMixin):

    def process_request(self, request):
        print('mw is process_request---')

    def process_view(self, request, callback, callback_args, callback_kwargs):

        print('mv is process_view---')

    def process_response(self, request, response):

        print('mv is process_response---')

        return response


class VisitLimit(MiddlewareMixin):

    def process_request(self, request):

        ip_address = request.META['REMOTE_ADDR']