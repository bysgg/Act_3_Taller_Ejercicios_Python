# 🏛️ Sistema de Gestión de Obras de Arte - Museo La Salle

## Descripción del Proyecto
Software diseñado para la automatización del catálogo, restauración y cesión internacional de obras de arte, con módulos de seguridad y reportes gerenciales.

## Conceptos de POO Aplicados
* **Herencia:** Jerarquía clara entre `ObraDeArte` (Padre), `Cuadro` y `Escultura` (Hijos).
* **Polimorfismo:** Uso de métodos abstractos (`mostrar_detalle`) que se comportan diferente según el tipo de obra.
* **Lógica de Negocio Compleja:** Algoritmo de detección automática de mantenimiento basado en el tiempo (`timedelta`).
* **Seguridad:** Sistema de autenticación de usuarios basado en roles (Director, Restaurador, Encargado).

## Reglas de Negocio Implementadas
1.  **Mantenimiento Quinquenal:** El sistema identifica diariamente obras con más de 5 años desde su última restauración.
2.  **Lista de Espera:** Si una obra está en restauración o cedida, las nuevas solicitudes de museos quedan en cola.
3.  **Valoración Patrimonial:** El Director puede obtener el valor total de la colección en tiempo real.

## Instrucciones de Ejecución
Ejecutar el flujo integral:
```bash
python main_museo.py