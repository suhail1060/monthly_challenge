from django.shortcuts import render

# importing httpresoponse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# creating first view just to check
monthly_challenges = {
    "january": "Eat",
    "february": "sleep",
    "march": "eat",
    "april": "laugh",
    "may": "eat",
    "june": "sleep",
    "july": "laugh",
    "august": "eat",
    "september": "eat and sleep",
    "october": "laugh",
    "november": "eat",
    "december": None
}


def monthly_challenge_numbers(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month number<h1>")
    redirect_month = months[month-1]
    # redirecting paths
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # the above gives like /challenge/january/
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        data = monthly_challenges[month]
        # data = render_to_string("challenges/challenge.html")
        # return HttpResponse(data)
        return render(request, "challenges/challenge.html",
                      {
                          "text": data,
                          "month": month})
    except:
        raise Http404()


def display_list(request):
    # list_items = ""
    # list_data = list(monthly_challenges.keys())
    # for s in list_data:
    #     b = s.capitalize()
    #     month_path = reverse("month-challenge", args=[s])
    #     list_items = list_items + f"<li><a href=\"{month_path}\">{b}</a></li>"
    # final_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(final_data)
    
    list_data=list(monthly_challenges.keys())
    return render(request, "challenges/index.html",
                  {
                      "months_list": list_data
                  })
