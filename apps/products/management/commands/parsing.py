from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests

from apps.products.models import Product

class Command(BaseCommand):
    help = "Комманда для парсинга данных с Sulpak"

    def handle(self, *args, **options):
        print("Парсинг данных")
        result = []
        url = 'https://www.sulpak.kg/f/smartfoniy/osh'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        all_phones = soup.find_all('div', class_='product__item-name')
        all_prices = soup.find_all('div', class_='product__item-price')
        for phone, price in zip(all_phones, all_prices):
            print(phone.text)
            result.append({'title':phone.text, 'price':price.text.strip().replace(' ', '').replace('сом', '')})
        print(result)