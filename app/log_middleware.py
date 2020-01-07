import logging.config


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.config.fileConfig("")

    def __call__(self, request):
        response = self.get_response(request)

        logging.debug("hh")
        print("hi")

        return response
