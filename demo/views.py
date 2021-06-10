from django.shortcuts import render

from customusers.forms import CustomUserForm


def home(request, error=False):
    if request.user.is_authenticated:
        authmessage = f'You are logged in as "{request.user.username}" (id={request.user.id}).'
        userform = CustomUserForm(instance=request.user)
    else:
        authmessage = "You are not logged in."
        userform = None
    viewmessage = (
        authmessage +
        " This paragraph has been generated in the view, " +
        "and changes based on request.user.is_authenticated."
    )
    context = {
        'user': request.user,
        'error': error,
        'viewmessage': viewmessage,
        'userform': userform,
    }
    return render(request, 'home.html', context)
