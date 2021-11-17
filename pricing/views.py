from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def pricing_view(request):
    return render(request, 'pricing/main.html')


@login_required
def get_payment_methods_view(request):
    if request.htmx:
        return render(request, 'pricing/partials/payment-methods.html')
    else:
        return redirect('pricing')


def proceed_with_payment_view(request):
    payment_method = request.POST.get("payment_method")
    if payment_method == "card":
        return HttpResponse("this will return a stripe page")
    elif payment_method == "paypal":
        return HttpResponse("this will return a paypal page")
    elif payment_method == "coinbase":
        return HttpResponse("this will return a coinbase page")
    return HttpResponse("somethin wrong happend :(")
