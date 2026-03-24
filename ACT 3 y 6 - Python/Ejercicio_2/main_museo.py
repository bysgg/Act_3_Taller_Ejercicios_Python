from modelos_museo import ObraDeArte, Cuadro, Escultura
from datetime import datetime, timedelta
from typing import List

def probar_museo() -> None:
    print("="*45)
    print("      SISTEMA DE GESTIÓN MURAL - LA SALLE")
    print("="*45)
    
    # 1. Registro de Obras
    obra1: Cuadro = Cuadro("La Noche Estrellada", "Van Gogh", "Postimpresionismo", 100000000, "1889", "Impresionista", "Óleo")
    obra2: Escultura = Escultura("El Pensador", "Rodin", "Moderna", 50000000, "1904", "Realismo", "Bronce")
    
    # 2. Definimos la lista con tipo explícito para que Pylance no se queje
    inventario: List[ObraDeArte] = [obra1, obra2]
    
    # 3. Simulación de Tiempo (Forzamos mantenimiento)
    obra2.ultima_restauracion = datetime.now() - timedelta(days=6*365)
    
    for obra in inventario:
        # Ahora Pylance sabe que 'obra' es una ObraDeArte y conoce sus métodos
        print(f"\n[*] Analizando: {obra}")
        print(f"    Detalles: {obra.mostrar_detalle()}")
        
        # Ejecutar chequeo diario automático
        obra.chequear_mantenimiento_automatico()
        
    print("\n" + "="*45)
    print("      REPORTE DE RESTAURACIONES")
    print("="*45)
    
    for obra in inventario:
        if obra.historial_restauraciones:
            print(f"Obra: {obra.titulo}")
            for res in obra.historial_restauraciones:
                print(f"  - {res}")

if __name__ == "__main__":
    probar_museo()