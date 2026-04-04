from modelos import Producto, TarjetaCredito, OrdenCompra, AgenteDeposito, Logistica, Queja
from typing import List

def mostrar_encabezado(titulo: str):
    print("\n" + "="*50)
    print(f"       {titulo}")
    print("="*50)

def ejecutar_sistema_ventas():
    mostrar_encabezado("SISTEMA DE TELEVENTAS - COMPRAS A DISTANCIA")

    # 1. SIMULACIÓN DE INVENTARIO EXISTENTE (Requisito: El sistema posee un inventario)
    p1 = Producto("A101", "Laptop Gaming Pro", 1200.50, 10)
    p2 = Producto("B202", "Mouse Ergonómico inalámbrico", 45.00, 50)
    p3 = Producto("C303", "Teclado Mecánico RGB", 80.00, 5)
    
    inventario: List[Producto] = [p1, p2, p3]

    # --- FLUJO DE CLIENTE ---
    # 2. CONSULTA DE CATÁLOGO (Requisito: Obtener info de código, descripción, precio, stock)
    print("\n[CATÁLOGO DE PRODUCTOS]")
    for prod in inventario:
        print(prod)

    # 3. GENERAR ORDEN DE COMPRA (Requisito: Ingresar orden de compra)
    orden_sebas = OrdenCompra("Sebastian Gutierrez")
    print("\n[CLIENTE] Creando orden de compra...")
    orden_sebas.agregar_producto(p1, 1) # Compra 1 Laptop
    orden_sebas.agregar_producto(p3, 2) # Compra 2 Teclados

    # 4. PROCESAR PAGO (Requisito: Actualmente sólo tarjeta de crédito)
    pago = TarjetaCredito()
    monto_total = (1200.50 * 1) + (80.00 * 2)
    if pago.procesar(monto_total):
        orden_sebas.estado = "PAGADA"

    # --- FLUJO INTERNO EMPRESA ---
    # 5. AGENTE DE DEPÓSITO (Requisito: Armar y empaquetar órdenes confirmadas)
    deposito = AgenteDeposito()
    deposito.armar_pedido(orden_sebas)

    # 6. LOGÍSTICA (Requisito: Determinar logística y empresa de transporte)
    empresa_envio = "Servientrega"
    Logistica.despachar(orden_sebas, empresa_envio)

    # 7. GESTIÓN DE QUEJAS (Requisito: Remitir inmediatamente al gerente)
    print("\n" + "-"*30)
    reclamo = Queja("Sebastian Gutierrez", "El paquete llegó con la caja golpeada.")
    reclamo.remitir_a_gerencia()

    # --- RESUMEN FINAL ---
    mostrar_encabezado("RESUMEN DE OPERACIÓN")
    print(f"Cliente: {orden_sebas.cliente}")
    print(f"Estado Final de la Orden: {orden_sebas.estado}")
    print(f"Stock Actualizado de {p1.descripcion}: {p1.cantidad} unidades")

if __name__ == "__main__":
    ejecutar_sistema_ventas()