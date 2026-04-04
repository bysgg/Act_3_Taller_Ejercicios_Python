from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Producto:
    def __init__(self, codigo: str, descripcion: str, precio: float, cantidad: int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"[{self.codigo}] {self.descripcion} - ${self.precio} (Stock: {self.cantidad})"

class MetodoPago(ABC):
    @abstractmethod
    def procesar(self, monto: float) -> bool: # Agregamos -> bool para que coincida
        pass

class TarjetaCredito(MetodoPago):
    def procesar(self, monto: float) -> bool: # Ahora Pylance está feliz
        print(f"[Pago] Procesando ${monto} con Tarjeta de Crédito... ¡Exitoso!")
        return True

class OrdenCompra:
    def __init__(self, cliente: str):
        self.cliente = cliente
        # Especificamos que el Dict tiene llaves String y valores de cualquier tipo (Any)
        self.items: List[Dict[str, Any]] = [] 
        self.estado = "PENDIENTE" 

    def agregar_producto(self, producto: Producto, cantidad: int):
        if producto.cantidad >= cantidad:
            self.items.append({"prod": producto, "cant": cantidad})
            producto.cantidad -= cantidad
            print(f"[Orden] Agregado: {producto.descripcion} x{cantidad}")
        else:
            print(f"[Error] Stock insuficiente para {producto.descripcion}")

    def cancelar(self):
        for item in self.items:
            # Ahora Pylance sabe que 'item' es un Dict y puede acceder a sus llaves
            item["prod"].cantidad += item["cant"]
        self.estado = "CANCELADA"
        print(f"[Orden] Orden de {self.cliente} cancelada. Stock devuelto.")

class AgenteDeposito:
    def armar_pedido(self, orden: OrdenCompra):
        if orden.estado == "PENDIENTE":
            print(f"[Depósito] Armando y empaquetando pedido para {orden.cliente}...")
            orden.estado = "ARMADA"

class Logistica:
    @staticmethod
    def despachar(orden: OrdenCompra, empresa_transporte: str):
        if orden.estado == "ARMADA":
            print(f"[Logística] Pedido enviado vía {empresa_transporte}.")
            orden.estado = "ENVIADA"

class Queja:
    def __init__(self, cliente: str, motivo: str):
        self.cliente = cliente
        self.motivo = motivo

    def remitir_a_gerencia(self):
        print(f"[GERENCIA] Reclamo recibido de {self.cliente}: {self.motivo}")