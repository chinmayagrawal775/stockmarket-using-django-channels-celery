from django.shortcuts import render
from yahoo_fin.stock_info import *

# Create your views here.
def home(request):
    stock_list = tickers_nifty50()
    return render(request, 'stocks/index.html', {'stock_list':stock_list})

def stocksInfo(request):
    stock_list = request.GET.getlist('stock_list')
    request.session.create()
    stock_details = {}
    for stock in stock_list:
        stock_detail = get_quote_table(stock)
        stock_details.update({stock:stock_detail})
    return render(request, 'stocks/selectedstocks.html', {'stock_details':stock_details})
