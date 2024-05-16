from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render

from core.forms import LoginForm
from openmu.accounts import Account

# Create your views here.


def home(request):
    """
    Home page
    :param request:
    :return:
    """

    requested_name = request.GET.get("name", "")
    title = "Hello world"

    if requested_name:
        try:
            account = Account(requested_name).account

            return render(
                request,
                "home.html",
                context={
                    "title": title,
                    "account": account,
                },
            )

        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return render(
                request,
                "home.html",
                context={
                    "title": title,
                    "error": "Account does not exist",
                },
            )
    else:
        return render(
            request,
            "home.html",
            context={
                "title": title,
            },
        )


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
