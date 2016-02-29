from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from .forms import PollCreationForm, DateChoiceCreationForm, UniversalChoiceCreationForm
from .models import Poll, Choice

# Create your views here.


def poll(request, poll_url):
    poll = get_object_or_404(Poll, url=poll_url)
    return TemplateResponse(request, "poll/poll.html", {
        'poll': poll
    })


def index(request):
    if request.method == 'POST':
        form = PollCreationForm(request.POST)
        if form.is_valid():
            poll = form.save()

            if poll.type == 'universal':
                return redirect('poll_editUniversalChoice', poll.url)
            elif poll.type == 'date':
                return redirect('poll_editDateChoice', poll.url)
            else:
                return redirect('poll_editDateTimeChoice', poll.url)
    else:
        form = PollCreationForm()
    return TemplateResponse(request, "poll/index.html", {
        'new_Poll': form
    })


def delete_comment(request, comment_id):
    pass


def edit(request, poll_id):
    pass


def watch(request, poll_id):
    pass


def edit_choice(request, poll_id):
    pass


def edit_date_choice(request, poll_url):
    poll = get_object_or_404(Poll, url=poll_url)
    if request.method == 'POST':
        form = DateChoiceCreationForm(request.POST)
        if form.is_valid():
            for datum in form.cleaned_data['date'].split(";"):
                choice = Choice(text="", date=datum, poll=poll)
                choice.save()
            return redirect('poll', poll_url)
    else:
        form = DateChoiceCreationForm()
    return TemplateResponse(request, "poll/DateChoiceCreation.html", {
        'new_Choice': form
    })


def edit_date_time_choice(request, poll_url):
    pass


def edit_universal_choice(request, poll_url):
    poll = get_object_or_404(Poll, url=poll_url)
    if request.method == 'POST':
        form = UniversalChoiceCreationForm(request.POST)
        if form.is_valid():
            choice = Choice(text=form.cleaned_data['text'], date='1970-01-01', poll=poll)
            choice.save()
            return redirect('poll', poll_url)
    else:
        form = UniversalChoiceCreationForm()
    return TemplateResponse(request, "poll/UniversalChoiceCreation.html", {
        'new_Choice': form
    })


def values(request, poll_id):
    pass


def delete(request, poll_id):
    pass


def vote(request, poll_id):
    pass


def vote_assign(request, poll_id, vote_id):
    pass


def vote_edit(request, poll_id, vote_id):
    pass


def vote_delete(request, poll_id, vote_id):
    pass


def copy(request, poll_id):
    pass