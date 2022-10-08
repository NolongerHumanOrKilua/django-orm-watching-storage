from .models import Passcard
from .models import Visit
from .models import format_duration
from .models import get_duration, is_visit_long
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits=[]
    passcard = Passcard.objects.all()[0]
    user = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=user)
    # Программируем здесь
    for visit in visits:
        this_passcard_visits.append(
                {
                    'entered_at': visit.entered_at,
                    'duration': format_duration(get_duration(visit)),
                    'is_strange': is_visit_long(visit, minutes=60)
                },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
