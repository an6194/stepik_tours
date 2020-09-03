from mock_data import departures


def departures_menu(request):
    return {
        'departures': departures
    }
