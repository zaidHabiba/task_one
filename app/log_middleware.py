import logging.config


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.config.fileConfig(".//logging_configuration.conf")

    def __call__(self, request):
        response = self.get_response(request)
        try:
            logging.debug({"response_data": response.data, "status_code": response.status_code})
        except Exception:
            logging.debug({"status_code": response.status_code})
        return response
