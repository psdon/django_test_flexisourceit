from django.urls import reverse
from faker import Faker
from nose.tools import eq_
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import StockFactory, TokenFactory
from ..models import StockOwned

fake = Faker()


class TestBuyStockTestCase(APITestCase):
    """Buy Stocks."""

    def setUp(self):
        self.url = reverse('buy-list')
        self.token = TokenFactory()
        self.data = StockFactory(name="JFC", price="10.2")

    def test_post_request_with_no_data_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "stock_symbol": self.data.name,
            "quantity": 1
        }
        response = self.client.post(self.url, data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        obj = StockOwned.objects.filter(stock__name=response.data.get('stock_symbol')).first()
        eq_(obj.quantity, 1)


class TestSellStockTestCase(APITestCase):
    """Buy Stocks."""

    def setUp(self):
        self.url = reverse('sell-list')
        self.token = TokenFactory()
        self.stock = StockFactory(name="JFC", price="10.2")

    def test_post_request_with_no_data_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        test_data = {
            "stock_symbol": self.stock.name,
            "quantity": 2
        }
        response = self.client.post(reverse('buy-list'), test_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        obj = StockOwned.objects.filter(stock__name=response.data.get('stock_symbol')).first()
        eq_(obj.quantity, 2)

        # Test Sell
        test_data = {
            "stock_symbol": self.stock.name,
            "quantity": 1
        }

        response = self.client.post(self.url, test_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        obj = StockOwned.objects.filter(stock__name=response.data.get('stock_symbol')).first()
        eq_(obj.quantity, 1)


class TestStockOwnTestCase(APITestCase):
    """Buy Stocks."""

    def setUp(self):
        self.url = reverse('stocks-list')
        self.token = TokenFactory()
        self.stock = StockFactory(name="JFC", price="10.2")

    def test_get_request_with_valid_data_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        test_data = {
            "stock_symbol": self.stock.name,
            "quantity": 2
        }

        response = self.client.post(reverse('buy-list'), test_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        obj = StockOwned.objects.filter(stock__name=response.data.get('stock_symbol')).first()
        eq_(obj.quantity, 2)

        # Test Detail
        url = reverse('stocks-detail', kwargs={'pk': self.stock.name})
        response = self.client.get(url)

        eq_(response.status_code, status.HTTP_200_OK)

        eq_(response.data.get('total_value'), 20.4)


