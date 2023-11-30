from django.urls import reverse

class ExcludeContextProcessorMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        current_path = request.path

        excluded_paths = [
            reverse('logout'),
        ]

        exclude_context_processor = any(current_path.startswith(path) for path in excluded_paths)

        request.exclude_context_processor = exclude_context_processor
