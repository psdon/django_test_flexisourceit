import random

import factory
from rest_framework.authtoken.models import Token

from app.users.models import User
from ..models import Stock, StockOwned


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stock

    name = factory.Faker('name')
    price = factory.LazyAttribute(random.randrange(2, 10))


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)


class StockOwnedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockOwned

    user = factory.SubFactory(UserFactory)
    stock = factory.SubFactory(StockFactory)
    quantity = factory.LazyAttribute(random.randrange(2, 10))
