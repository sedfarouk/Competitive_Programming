from collections import OrderedDict

def calculate_net_price(items):
    net_price_dict = OrderedDict()
    for item in items:
        item_name, price = item
        if item_name not in net_price_dict:
            net_price_dict[item_name] = price
        else:
            net_price_dict[item_name] += price
    return net_price_dict

num_items = int(input())
items = []
for _ in range(num_items):
    item = input().split()
    item_name = " ".join(item[:-1])
    price = int(item[-1])
    items.append((item_name, price))

net_price_dict = calculate_net_price(items)

for item_name, net_price in net_price_dict.items():
    print(item_name, net_price)
