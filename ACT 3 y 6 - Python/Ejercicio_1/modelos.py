from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Producto:
    def __init__(self, codigo: str, descripcion: str, precio: float, cantidad: int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad # Cantidad disponible en stock

    def __str__(self) -> str:
        return f"Producto: {self.descripcion} | Precio: ${self.precio} | Stock: {self.cantidad}"

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        pass

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"Pago exitoso de ${monto} procesado con Tarjeta de Crédito.")

class Queja:
    def __init__(self, cliente: str, motivo: str):
        self.cliente = cliente
        self.motivo = motivo

    def remitir_a_gerencia(self):
        # Las quejas se remiten inmediatamente al gerente [cite: 30]
        print(f"ALERTA GERENCIA: Queja recibida de {self.cliente} por: {self.motivo}")

class OrdenCompra:
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.items: List[Dict[str, Any]] = []
        self.confirmada = False

    def agregar_item(self, producto: Producto, cantidad: int):
        if producto.cantidad >= cantidad:
            self.items.append({"producto": producto, "cantidad": cantidad})
            producto.cantidad -= cantidad # Actualiza disponibilidad según el taller [cite: 29]
            print(f"Agregado: {cantidad} unidades de {producto.descripcion}")
        else:
            print(f"Error: No hay stock suficiente de {producto.descripcion}")