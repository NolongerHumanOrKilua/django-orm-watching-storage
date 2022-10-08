from .models import Passcard
from .models import Visit
from .models import format_duration
from .models import get_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit, minutes=60)
            }
        )



    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
