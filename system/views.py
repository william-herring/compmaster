from django.views.generic import TemplateView

class ErrorView(TemplateView):
    template_name = 'error.html'

    def get_context_data(self, **kwargs):
        context = super(ErrorView, self).get_context_data(**kwargs)
        status_code = self.request.GET.get('c')
        error_msg = self.request.GET.get('msg')

        context['status_code'] = status_code
        context['error_msg'] = error_msg
        return context
