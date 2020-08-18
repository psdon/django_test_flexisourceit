"""URLs for user"""

from rest_framework.routers import DefaultRouter

from .views import BuyStockViewSet, SellStockViewSet, StockOwnedViewSet

router = DefaultRouter()
router.register(r'stocks/buy', BuyStockViewSet, basename="buy")
router.register(r'stocks/sell', SellStockViewSet, basename="sell")
router.register(r'stocks', StockOwnedViewSet, basename='stocks')
