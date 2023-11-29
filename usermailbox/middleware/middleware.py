from django.urls import reverse

class ExcludeContextProcessorMiddleware():
    def __init__(self, get_response):
        # Middleware initialization code goes here, if needed
        self.get_response = get_response

    def __call__(self, request):
        # Middleware processing code goes here
        response = self.get_response(request)
        return response

    def process_request(self, request):
        # Get the path of the current request
        current_path = request.path

        # List of paths where you want to exclude the context processor
        excluded_paths = [
            # reverse('create_user_profile'),
            # reverse('userprofile_detail'),
            reverse('logout'),
            # Add other paths as needed
        ]

        # Check if the current path is in the excluded paths
        exclude_context_processor = any(current_path.startswith(path) for path in excluded_paths)

        # Set a flag in the request to indicate whether to exclude the context processor
        request.exclude_context_processor = exclude_context_processor
