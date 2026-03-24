from modelos import Producto
from modelos import Producto, OrdenCompra

def test_ordenes():
    print("\n--- Prueba Bloque 2: Órdenes y Stock ---")
    p1 = Producto("A01", "Laptop", 2500.0, 2)
    orden = OrdenCompra("Sebastian Gutierrez")
    
    # Intento exitoso
    orden.agregar_item(p1, 1) 
    # Intento fallido (supera el stock restante)
    orden.agregar_item(p1, 5) 

if __name__ == "__main__":
    test_ordenes()  