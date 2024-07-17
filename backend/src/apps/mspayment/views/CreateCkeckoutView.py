from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from msproduct.models import Item, Product, Price, Bill
from django.conf import settings
import stripe


def product_dict(product_name, product_price, product_amount):
    return {
        "price_data": {
            "currency": "pen",
            "product_data": {
                "name": product_name,
            },
            "unit_amount": product_price,
        },
        "quantity": product_amount,
    }


class CreateCkeckoutView(APIView):

    def post(self, request, pk):
        item_list = Item.objects.filter(bill=pk)
        my_line_items = []
        # for item in item_list:
        #     product = Product.objects.get(id=item.product.id)
        #     price = Price.objects.get(id=product.price.id)
        #     my_line_items.append(
        #         product_dict(
        #             product_name=product.title,
        #             product_price=price.originalPrice,
        #             product_amount=item.quantity,
        #         )
        #     )
        # try:
        #     checkout_sesion = stripe.checkout.Session.create(
        #         line_items=my_line_items,
        #         mode="payment",
        #     )
        #     new_bill = Bill.objects.get(id=pk)
        #     new_bill.total = checkout_sesion.amount_total
        #     new_bill.save()
        #     return Response(checkout_sesion, status=status.HTTP_200_OK)
        # except Exception as e:
        #     return e


class CreateCheckoutSimpleView(APIView):

    def post(self, request, pk):
        item_list = Item.objects.filter(bill=pk)

        if len(item_list) == 0:
            return Response(
                {"message": "No tiene productos en su carrito de compras"},
                status=status.HTTP_403_FORBIDDEN,
            )

        current_bill = Bill.objects.get(id=pk)
        total_amount = sum([i.price.discountPrice * i.quantity for i in item_list])
        current_bill.total = total_amount
        current_bill.save()
        return Response({"message": "Successful payment"}, status=status.HTTP_200_OK)
