# 🏛️ Manual de Programación: Sistema de Gestión de Museos (MURAL)

## 1. Descripción General
El sistema **MURAL** (Management & Unified Restoration Art Ledger) es una solución diseñada para automatizar la administración de catálogos artísticos, procesos de restauración por ciclo de vida y la gestión de cesiones internacionales entre instituciones culturales.

---

## 2. Arquitectura del Proyecto
El software implementa una arquitectura modular para garantizar la escalabilidad y el mantenimiento:

* **`modelos_museo.py`**: Motor lógico que contiene la jerarquía de clases de las obras, la gestión de usuarios y el registro de restauraciones.
* **`main_museo.py`**: Punto de entrada que simula el flujo de trabajo diario de los tres roles principales (Encargado, Restaurador Jefe y Director).

---

## 3. Implementación de Conceptos POO Avanzados

### A. Herencia y Polimorfismo
Se utiliza una estructura de herencia simple para especializar los objetos del museo:
* **Clase Base `ObraDeArte`**: Clase abstracta (hereda de `ABC`) que define el contrato común. No puede ser instanciada directamente.
* **Especialización**: Las clases `Cuadro` y `Escultura` extienden la base añadiendo atributos únicos (técnica y material). 
* **Polimorfismo Dinámico**: El método `@abstractmethod def mostrar_detalle()` es implementado de forma distinta en cada subclase, permitiendo que el sistema procese cualquier obra sin conocer su tipo específico.

### B. Gestión de Tiempo y Automatización
El sistema resuelve el requisito de "proceso diario de restauración" mediante:
* **Lógica Quinquenal**: Uso de `datetime` y `timedelta` para calcular si han transcurrido más de **1,825 días (5 años)** desde la última intervención.
* **Activación por Estado**: El método `chequear_mantenimiento_automatico()` dispara el cambio de estado de forma autónoma basándose en la fecha del sistema.

### C. Manejo de Disponibilidad (Lista de Espera)
Para la gestión de cesiones, se implementó una lógica de **bloqueo de estado**:
* Una obra solo puede ser cedida si su estado es `Expuesta`.
* Si la obra está en `Restauración`, el sistema utiliza el atributo `museo_en_espera` (tipo `Optional`) para encolar la siguiente solicitud, cumpliendo con la regla de negocio de cesión diferida.

---

## 4. Seguridad y Roles
El acceso a las funciones está restringido mediante la clase `Usuario`:
* **Encargado**: Gestión de catálogo y entrada de datos.
* **Restaurador Jefe**: Supervisión de mantenimiento y consulta de historial.
* **Director**: Autorización de cesiones y consulta de valoración patrimonial ($).

---

## 5. Manual de Pruebas Funcionales

| Caso de Prueba | Funcionalidad | Resultado Validado |
| :--- | :--- | :--- |
| **Acceso Restringido** | `Usuario.autenticar()` | Impide el acceso si las credenciales no coinciden. |
| **Mantenimiento Auto** | `timedelta(days=5*365)` | Identifica obras antiguas y cambia su estado a 'Restauración'. |
| **Prioridad de Daño** | `enviar_a_restauracion()` | El envío inmediato por daño manual sobrescribe cualquier otro estado. |
| **Cálculo Patrimonial** | `sum(o.valor)` | Genera la suma total de la colección para el reporte del Director. |
| **Colas de Cesión** | `museo_en_espera` | Registra el interés de un segundo museo cuando la obra no está disponible. |

---

## 6. Ejecución del Sistema
Para iniciar la simulación integral que recorre todos los módulos de seguridad, restauración y dirección:

```bash
python main_museo.py