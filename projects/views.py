from django.shortcuts import render
from projects.models import Profile


def index(request):
    profile = Profile.objects.select_related(
        'author'
    ).prefetch_related(
        'projects',
        'skills__icon'
    ).first()

    title = profile.author
    return render(request, 'projects/index.html', {'profile': profile, 'title': f'Protfolio {title}'})
