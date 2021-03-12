from django.shortcuts import render


def home_page(request):
    return render(request, 'main/home.html')


def contact_page(request):
    return render(request, 'main/contact.html')


def about_page(request):
    return render(request, 'main/about.html')


def reports(request):
    return render(request, 'main/reports.html')


def rules(request):
    return render(request, 'main/rules.html')


def rules2(request):
    return render(request, 'main/rules2.html')


def cart2(request):
    return render(request, 'main/cart2.html')

