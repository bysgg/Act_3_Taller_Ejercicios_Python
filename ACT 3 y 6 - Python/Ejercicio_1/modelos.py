from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Producto:
    def __init__(self, codigo: str, descripcion: str, precio: float, cantidad: int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.descripcion} - ${self.precio} (Stock: {self.cantidad})"

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        pass

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto: float) -> bool:
        print(f"[Pago] Transacción exitosa por ${monto} con Tarjeta de Crédito.")
        return True

class OrdenCompra:
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.items: List[Dict[str, Any]] = []
        self.estado = "PENDIENTE" # PENDIENTE, PAGADA, ARMADA, CANCELADA

    def agregar_item(self, producto: Producto, cantidad: int):
        if self.estado == "PENDIENTE" and producto.cantidad >= cantidad:
            self.items.append({"producto": producto, "cantidad": cantidad})
            producto.cantidad -= cantidad 
            print(f"[Orden] Agregado: {producto.descripcion} x{cantidad}")
        else:
            print(f"[Error] No se puede agregar item. Estado: {self.estado} o sin stock.")

    def cancelar_orden(self):
        if self.estado == "PENDIENTE" or self.estado == "PAGADA":
            # Devolvemos el stock al sistema de inventario
            for item in self.items:
                item["producto"].cantidad += item["cantidad"]
            self.estado = "CANCELADA"
            print(f"[Orden] La orden de {self.cliente} ha sido cancelada.")

class AgenteDeposito:
    def armar_pedido(self, orden: OrdenCompra):
        if orden.estado == "PAGADA":
            print(f"[Depósito] Armando y empaquetando pedido de: {orden.cliente}")
            orden.estado = "ARMADA"
        else:
            print("[Depósito] La orden aún no ha sido pagada.")

class Logistica:
    @staticmethod
    def asignar_transporte(orden: OrdenCompra, empresa: str):
        if orden.estado == "ARMADA":
            print(f"[Logística] Pedido delegado a la empresa: {empresa}")
            orden.estado = "ENVIADA"
        else:
            print("[Logística] El pedido debe estar armado antes de asignar transporte.")

class Queja:
    def __init__(self, cliente: str, motivo: str):
        self.cliente = cliente
        self.motivo = motivo

    def remitir(self):
        print(f"[Gerencia] RECLAMO RECIBIDO - Cliente: {self.cliente} | Motivo: {self.motivo}")