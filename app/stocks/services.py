"""Business Logic."""
from .models import Stock, StockOwned


def buy_stock(request, name, quantity):
    """
    Buy Stock Service.
    :param request: Request Object
    :param name: String stock name
    :param quantity: Integer
    :return: Dict(stock_symbol, quantity)
    """
    stock_obj = Stock.objects.filter(name=name).first()

    if not stock_obj:
        return {
            "status": "error",
            "message": "Stock name does not exists."
        }

    # If user does not own any stocks
    if not request.user.stocks_owned.filter(stock__name=name).first():
        obj = StockOwned(user=request.user, stock=stock_obj, quantity=quantity)
        obj.save()

        return {
            "status": "success"
        }

    stock_owned_obj = StockOwned.objects.filter(user=request.user, stock=stock_obj).first()

    stock_owned_obj.quantity += quantity
    stock_owned_obj.save()

    return {
        "status": "success"
    }


def sell_stock(request, name, quantity):
    """
       Sell Stock Service.
       :param request: Request Object
       :param name: String stock name
       :param quantity: Integer
       :return: Dict(stock_symbol, quantity)
       """
    stock_obj = Stock.objects.filter(name=name).first()

    if not stock_obj:
        return {
            "status": "error",
            "message": "Stock name does not exists."
        }

    stock_owned_obj = StockOwned.objects.filter(user=request.user, stock=stock_obj).first()

    if not stock_owned_obj:
        return {
            "status": "error",
            "message": "The user does not own this stock."
        }

    new_quantity = int(stock_owned_obj.quantity) - int(quantity)
    if new_quantity == 0:
        stock_owned_obj.delete()
        return {
            "status": "success"
        }
    elif new_quantity <= 0:
        return {
            "status": "error",
            "message": "Quantity must not be greater than user owned stocks."
        }

    stock_owned_obj.quantity = new_quantity
    stock_owned_obj.save()

    return {
        "status": "success"
    }
