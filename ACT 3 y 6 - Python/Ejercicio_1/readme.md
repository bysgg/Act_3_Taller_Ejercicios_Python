# 🛒 Manual de Programación: Sistema TeleVentas La Salle

## 1. Descripción General
Este software es una solución integral para la gestión de ventas a distancia. El sistema permite automatizar el flujo completo desde la consulta de productos en un catálogo hasta la entrega logística, pasando por pasarelas de pago y soporte post-venta.

---

## 2. Arquitectura del Sistema
El proyecto se divide en dos módulos principales para separar la lógica de negocio de la ejecución, siguiendo buenas prácticas de desarrollo:

* **`modelos.py`**: Define la estructura de datos, las reglas de negocio y las abstracciones del sistema.
* **`main.py`**: Orquestador que ejecuta la simulación y valida la interacción entre objetos.

---

## 3. Implementación de Conceptos POO

### A. Abstracción y Herencia
Se implementó una **Clase Abstracta** para la gestión de pagos, cumpliendo con el principio de **Inversión de Dependencia**:
* **Clase `MetodoPago`**: Define el contrato `procesar_pago(monto)`.
* **Clase `TarjetaCredito`**: Implementación concreta que hereda de la base abstracta. Esto permite que el sistema sea escalable a otros métodos (Efectivo, PSE, Bitcoin) sin modificar la lógica interna de la orden de compra.

### B. Encapsulamiento y Máquina de Estados
La clase `OrdenCompra` utiliza un sistema de estados para proteger la integridad del proceso comercial:
1.  **`PENDIENTE`**: Estado inicial. Solo aquí se permite agregar productos.
2.  **`PAGADA`**: Estado alcanzado tras validar el método de pago. Habilita al Agente de Depósito.
3.  **`ARMADA`**: El pedido ha sido físicamente procesado y empaquetado.
4.  **`ENVIADA`**: Estado final tras la asignación de transporte logístico.
5.  **`CANCELADA`**: Estado de reversión que devuelve automáticamente el stock al inventario.

### C. Métodos Estáticos y Composición
* **`Logistica.asignar_transporte`**: Definido como `@staticmethod`. Actúa como un servicio de utilidad que no requiere persistencia de estado propia, delegando la entrega a empresas externas (ej. Servientrega).
* **Composición**: La `OrdenCompra` mantiene una lista de diccionarios que vinculan objetos de la clase `Producto` con cantidades específicas.

---

## 4. Manual de Pruebas Funcionales (Escenarios)

| Funcionalidad | Método / Clase | Resultado Validado |
| :--- | :--- | :--- |
| **Control de Inventario** | `agregar_item()` | Se descuenta el stock en tiempo real al añadir a la orden. |
| **Validación de Pago** | `TarjetaCredito` | Simulación de transacción exitosa que actualiza el estado a `PAGADA`. |
| **Gestión de Depósito** | `AgenteDeposito` | Bloquea el empaque si la orden no registra pago previo. |
| **Soporte al Cliente** | `Queja.remitir()` | Envío inmediato de incidencias a la Gerencia de Relaciones. |

---

## 5. Instrucciones de Uso
Para ejecutar la simulación y verificar los logs de trazabilidad en la terminal:

```bash
python main.py