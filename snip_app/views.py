from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Snip
from .forms import snipForm, searchForm
from django.contrib.auth.decorators import login_required


@login_required
def show_snip(request, pk):
    snips = Snip.objects.filter(author=request.user)
    snip = Snip.objects.get(id=pk)
    searchform = searchForm()
    if request.method == "POST":
        try:
            searchform = searchForm(request.POST)
            x = request.POST['search']
            return HttpResponseRedirect("/search/" + x)
        except ValueError:
            pass
    return render(request, "detail.html", {'searchform': searchform, 'snip': snip, 'snips': snips})


@login_required
def index(request):
    snips = Snip.objects.filter(author=request.user)
    form = snipForm(initial={'author': request.user})
    if request.method == "POST":
        try:
            form = snipForm(request.POST)
            form.save()
            return HttpResponseRedirect("/")
        except ValueError:
            pass

    return render(request, "index.html", {'form': form, 'snips': snips})



