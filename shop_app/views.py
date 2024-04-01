from django.shortcuts import render
from django.views import View


class ProductDetailView(View):
    def get(self, request):
        return render(request, 'shop_app/detail.html')
