from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    active_visitors = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visitor in active_visitors:
        non_closed_visits.append({
            'who_entered': visitor.passcard.owner_name,
            'entered_at': visitor.entered_at,
            'duration': visitor.get_duration(),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
