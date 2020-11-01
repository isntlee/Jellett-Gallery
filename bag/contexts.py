from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    delivery = 0
    product_count = 0
    delivery_total = 0
    delivery_percentage = 10
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.offer
            product_count += item_data
            delivery = (total/delivery_percentage)
            delivery_total = delivery + total
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'delivery_total': delivery_total,
    }

    return context
