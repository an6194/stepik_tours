import random
from math import inf
from django.shortcuts import render
from django.views import View
import mock_data as data


class MainView(View):

    def get(self, request, *args, **kwargs):
        tours_sample = random.sample(list(data.tours), 6)
        tours_sample = dict.fromkeys(tours_sample)
        for tour_id in tours_sample:
            tours_sample[tour_id] = data.tours[tour_id]
        return render(request, 'index.html', context={
            'tours_sample': tours_sample,
            'title': data.title,
            'subtitle': data.subtitle,
            'description': data.description,
            'departures': data.departures
        })


class DepartureView(View):

    def get(self, request, departure, *args, **kwargs):
        tours_filtered = dict()
        tour_count = 0
        price_min = inf
        price_max = 0
        nights_min = inf
        nights_max = 0
        for tour_id, tour_data in data.tours.items():
            if tour_data['departure'] == departure:
                tours_filtered[tour_id] = tour_data
                tour_count += 1
                if tour_data['price'] < price_min:
                    price_min = tour_data['price']
                if tour_data['price'] > price_max:
                    price_max = tour_data['price']
                if tour_data['nights'] < nights_min:
                    nights_min = tour_data['nights']
                if tour_data['nights'] > nights_max:
                    nights_max = tour_data['nights']
        departure = data.departures[departure]
        return render(request, 'departure.html', context={
            'tours_filtered': tours_filtered,
            'departure': departure,
            'tour_count': tour_count,
            'price_min': price_min,
            'price_max': price_max,
            'nights_min': nights_min,
            'nights_max': nights_max,
            'departures': data.departures
        })


class TourView(View):

    def get(self, request, tour_id, *args, **kwargs):
        tour = data.tours[tour_id]
        departure = data.departures[tour['departure']]
        stars = int(tour['stars']) * '★'
        return render(request, 'tour.html', context={
            'tour': tour,
            'departure': departure,
            'stars': stars,
            'departures': data.departures
        })
