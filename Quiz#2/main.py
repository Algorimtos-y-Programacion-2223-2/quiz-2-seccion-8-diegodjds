# Pregunta#2

from gaming import Gaming
from ropa import Ropa
from hogar import Hogar


products = [
    {"id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800},
    {"id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600},
    {"id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25},
    {"id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5},
    {"id": 5, "name": "Laptop Gamer",
     "type": "Gaming", "stock": 11, "price": 2500},
    {"id": 6, "name": "Nintendo Switch OLED",
     "type": "Gaming", "stock": 25, "price": 400},
]


def main():
    print('**** Bienvenido ****')
    new_dt_obj = dt_obj()
    while True:
        menu = ["Agregar productos", "Ver productos",
                "Salir"]
        for index, item in enumerate(menu):
            print(f"{index+1}. {item}")
        select_option = int(input("Seleccione una opción del menu: "))

        if select_option == 1:
            Agregar_productos(new_dt_base)
        elif select_option == 2:
            Ver_productos(new_dt_base)
        elif select_option == 4:
            print('**** Hasta Luego ****')
            break


def Agregar_productos(new_dt_obj):
    for products in new_dt_obj['products']:
        print(f"""
                id: {products.id}
                name: {products.name}
                type: {products.type}
                stock: {products.stock}
                price: {products.price}
                """)


def Ver_productos(new_dt_obj):
    print(f"\n**** Productos ****")

    for products in new_dt_obj['products']:
        products.mostrar()


def dt_obj():
    new_dt_obj = {
        "products": [],
    }

    for category in products:
        for item in products[category]:
            if category == "products":
                new_products = products(item.get('id'), item.get('name'), item.get(
                    'type'), item.get('stock'), item.get('price'))
                new_dt_obj[category].append(new_products)


main()
