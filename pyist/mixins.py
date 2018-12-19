from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured


class SuccessMessageMixin:
    success_message = None

    def form_valid(self, form):
        if not self.success_message:
            raise ImproperlyConfigured(
                'No message to show. Provide a success_message.'
            )
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
