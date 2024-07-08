from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def read_csv():
    data = []
    with open('./data-398-2018-08-30.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] != 'Name' or row[4] != 'Street' or row[6] != 'District': 
                data.append({
                    'Name': row[1],
                    'Street': row[4],
                    'District': row[6]
                })

    return data


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    data = read_csv()

    paginator = Paginator(data, 10)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
