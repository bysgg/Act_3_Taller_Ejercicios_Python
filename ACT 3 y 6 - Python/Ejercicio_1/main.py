from modelos import Producto, OrdenCompra, TarjetaCredito, AgenteDeposito, Logistica, Queja

def simulacion_televentas():
    print("=== SISTEMA TELEVENTAS LA SALLE ===\n")
    
    # 1. Catálogo e Inventario
    p1 = Producto("TV01", "Smart TV 50", 1800000, 10)
    
    # 2. El cliente crea orden y paga
    mi_orden = OrdenCompra("Sebastian Gutierrez")
    mi_orden.agregar_item(p1, 1)
    
    pago = TarjetaCredito()
    if pago.procesar_pago(1800000):
        mi_orden.estado = "PAGADA"

    # 3. Agente de Depósito (Consultando órdenes pagadas)
    agente = AgenteDeposito()
    agente.armar_pedido(mi_orden)

    # 4. Logística (Selección de transporte)
    Logistica.asignar_transporte(mi_orden, "Servientrega")

    # 5. Soporte (Simulación de queja)
    reclamo = Queja("Sebastian G.", "Caja del TV un poco golpeada")
    reclamo.remitir()

if __name__ == "__main__":
    simulacion_televentas()