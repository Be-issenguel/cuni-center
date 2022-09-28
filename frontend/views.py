from django.shortcuts import render


# Create your views here.
def main(request):
    context = {}
    return render(request, 'frontend/store/main.html', context=context)


def store(request):
    context = {}
    return render(request, 'frontend/store/store.html', context=context)


def checkout(request):
    context = {}
    return render(request, 'frontend/store/checkout.html', context=context)


def cart(request):
    context = {}
    return render(request, 'frontend/store/cart.html', context=context)
