from django.contrib import messages


class SuccessMessageMixin(object):
    success_message = None

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
