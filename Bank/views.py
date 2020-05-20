from django.shortcuts import render
# from Bank.models import bank_s
from Bank.models import bank_b
from Bank.models import banks


def index(request):
    return render(request, 'data/main.html')


def search_bank(request):
    try:
        bank_name = banks.objects.get(name=request.GET['bank_name'])
    except:
        return render(request, 'data/bank_not_found.html', {'test': request.GET['bank_name']})
    if (request.method == "GET") and ('bank_name' in request.GET) and (request.GET['bank_name'] == bank_name.title):
        return render(request, 'data/bank_found.html', {'test': request.GET['bank_name']})


# def search_month(request):
#     try:
#         month_name = banks.objects.get(month=request.GET['month_name'])
#     except:
#         return render(request, 'data/month_not_found.html', {'test': request.GET['month_name']})
#     if (request.method == "GET") and ('month_name' in request.GET) and (request.GET['month_name'] == month_name.month):
#         return render(request, 'data/month_found.html', {'test': request.GET['month_name']})
#

def choice(request):
    results = request.GET["choices"]
    return render(request, 'data/secondmain.html', {'choices': results})
