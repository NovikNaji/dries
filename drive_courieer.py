from math import radians, sin, cos, sqrt, atan2

# Функция для вычисления расстояния
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # радиус Земли
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# Заказы
def read_orders(filename):
    orders = []
    with open(filename, 'r') as file:
        for line in file:
            order_info = line.split()
            order = {
                "from": (float(order_info[0]), float(order_info[1])),
                "to": (float(order_info[2]), float(order_info[3])),
                "cost": float(order_info[4]),
                "address": str(order_info[5])
            }
            orders.append(order)
    return orders

# Курьеры
def read_couriers(filename):
    couriers = []
    with open(filename, 'r') as file:
        for line in file:
            courier_info = line.split()
            courier = {
                "location": (float(courier_info[0]), float(courier_info[1])),
                "speed": float(courier_info[2]),
                "name": str(courier_info[3]),
                "address": str(courier_info[4])
            }
            couriers.append(courier)
    return couriers

# Функция для расчета времени доставки
def calculate_delivery_time(order, courier):
    distance = calculate_distance(*order["from"], *courier["location"])
    time = distance / courier["speed"]  # время в часах
    return time

# Заказы и курьеры
orders = read_orders("orders.txt")
couriers = read_couriers("couriers.txt")

# Распределение заказов
for order in orders:
    min_time = float('inf')
    fastest_courier = None
    for courier in couriers:
        delivery_time = calculate_delivery_time(order, courier)
        if delivery_time < min_time:
            min_time = delivery_time
            fastest_courier = courier
    print(f"Order: {order['address']}, Assigned courier: {fastest_courier['name']}, {fastest_courier['address']}")

