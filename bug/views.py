from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug
from .forms import BugForm


def index(request):
    '''View for the landing page, it returns a simple HttpResponse displaying a message for the landing page.'''
    return HttpResponse("This is the Landing page")


def register_bug(request):
    '''View for registering a new bug, handle POST and GET request'''
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugForm()
    return render(request, 'bug/register_bug.html', {'form': form})


def view_bug(request, bug_id):
    '''retrieves a `Bug` object by its `description` and renders a template to display its details.'''
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug/view_bug.html', {'bug': bug})


def bug_list(request):
    '''retrieves all the Bug objects from the database and renders them in the 'blog/bug_list.html' template'''
    bugs = Bug.objects.all()
    return render(request, 'bug/bug_list.html', {'bugs': bugs})


def bug_link(request):
    '''View function to render a page displaying a list of bug objects with links to their details page'''
    bugs = Bug.objects.all()
    return render(request, 'bug/bug_list_link.html', {'bugs': bugs})


