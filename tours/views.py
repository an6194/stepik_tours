from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'


class DepartureView(TemplateView):
    template_name = 'departure.html'


class TourView(TemplateView):
    template_name = 'tour.html'
