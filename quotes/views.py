from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from quotes.models import Quote
from quotes.forms import NewQuoteForm


def _main(request, template="home.html"):
    try:
        quote = Quote.objects.all().order_by('?')[0]
    except IndexError:
        quote = Quote(
            quote="I don't have any quotes yet",
            speaker="Nobody",
        )
    return render(request, 'home.html', {'quote':quote})


def main(request):
    ''' site homepage '''
    return _main(request, template='home.html')


def autoreload(request):
    ''' cycle through quotes automatically '''
    return _main(request, template='autoreload.html')


def detail(request, quote_id):
    ''' display a specific quote '''
    quote = get_object_or_404(Quote, id=quote_id)
    return render(request, 'home.html', {'quote':quote})


def submit(request):
    ''' submission landing page, redirect back to their new content '''
    if request.method == "POST":
        form = NewQuoteForm(request.POST)
        if form.is_valid():
            newquote = Quote.objects.create(
                quote=form.cleaned_data['quote'],
                speaker=form.cleaned_data['speaker']
            )
            return HttpResponseRedirect('/quotes/%d' % newquote.id)
    else:
        form = NewQuoteForm()
    return render(request, 'submit.html', {'form': form})

