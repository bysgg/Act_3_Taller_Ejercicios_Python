# 🛒 Sistema TeleVentas La Salle

## Descripción del Proyecto
Este módulo automatiza el ciclo de compra a distancia, integrando la gestión de inventario, pasarela de pagos, logística de distribución y soporte al cliente.

## Conceptos de POO Aplicados
* **Abstracción:** Implementación de la clase base `MetodoPago` para desacoplar la lógica de cobro del flujo de la orden.
* **Encapsulamiento:** Gestión de estados de la orden (`PENDIENTE`, `PAGADA`, `ARMADA`, `ENVIADA`) para asegurar la integridad del proceso.
* **Relación de Composición:** La `OrdenCompra` gestiona una colección de objetos `Producto`.
* **Responsabilidad Única (SRP):** Clases separadas para `Logistica`, `AgenteDeposito` y `Queja`.

## Estructura de Clases
* `Producto`: Entidad básica con atributos de stock y precio.
* `OrdenCompra`: Cerebro del proceso que valida existencias y estados.
* `Logistica`: Clase estática encargada de la delegación a empresas de transporte.
* `Queja`: Sistema de remisión inmediata a la Gerencia de Relaciones.

## Instrucciones de Ejecución
Ejecutar el archivo principal:
```bash
python main.py