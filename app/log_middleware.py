import logging.config
import socket
import time


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.config.fileConfig(".//logging_configuration.conf")

    def __call__(self, request):
        response = self.get_response(request)
        log_data = {
            'user': request.user.pk,

            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),

            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request.body,

            'response_status': response.status_code,

        }
        logging.debug(log_data)

        return response
