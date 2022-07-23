from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    pk = passcard[0].id
    all_visits = Visit.objects.filter(passcard=pk)
    this_passcard_visits = []

    for visit in all_visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': visit.leaved_at - visit.entered_at,
            'is_strange': visit.is_visit_long()
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
