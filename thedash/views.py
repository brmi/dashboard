from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from .models import Table
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def target_list(request):
    targets = Table.objects.filter(days_back=1)

    args = {}
    args.update(csrf(request))
    args['targets'] = targets

    return render(request, 'thedash/target_list.html', args)


def day_update(request):
    if request.method == 'POST':
        day = request.POST['search_day'] #day variable should be in post
    else:
        day = 1
    entries = Table.objects.filter(days_back__lte=day)

    return render(request, 'thedash/ajax_search.html', {'entries' : entries})


def dashboard(request, pk):
    target = get_object_or_404(Table, target=pk)
    # target = Table.object.filter(target = targetnum)
    args = {}
    args['target'] = target
    return render(request, 'thedash/dashboard.html', args)
