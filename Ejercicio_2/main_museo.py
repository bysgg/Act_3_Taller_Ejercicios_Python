from modelos_museo import ObraDeArte, Cuadro, Escultura, Usuario
from datetime import datetime, timedelta
from typing import List

def ejecutar_sistema_completo():
    # --- 1. MÓDULO DE SEGURIDAD ---
    print("="*50)
    print("      SISTEMA INTEGRADO MUSEO LA SALLE")
    print("="*50)
    
    admin = Usuario("sebas_admin", "lasalle2026", "Encargado")
    print(f"[*] Autenticando usuario: {admin.username}...")
    
    if not admin.autenticar("sebas_admin", "lasalle2026"):
        print("[ERROR] Acceso denegado.")
        return
    
    print("[OK] Acceso concedido. Cargando módulos...\n")

    # --- 2. CARGA DE CATÁLOGO (Encargado) ---
    obra1 = Cuadro("La Noche Estrellada", "Van Gogh", "Postimpresionismo", 100000000, "1889", "Impresionista", "Óleo")
    obra2 = Escultura("El Pensador", "Rodin", "Moderna", 50000000, "1904", "Realismo", "Bronce")
    
    inventario: List[ObraDeArte] = [obra1, obra2]
    print(f"[CATÁLOGO] Se han registrado {len(inventario)} obras con éxito.")

    # --- 3. PROCESO DE RESTAURACIÓN (Restaurador Jefe) ---
    print("\n" + "-"*30)
    print("EJECUTANDO CHEQUEO DE MANTENIMIENTO")
    print("-"*30)
    
    # Simulamos que 'El Pensador' no se ha tocado en 6 años
    obra2.ultima_restauracion = datetime.now() - timedelta(days=6*365)
    
    for obra in inventario:
        # Chequeo automático (Requisito: Proceso diario)
        obra.chequear_mantenimiento_automatico()
        
        # Simulación de daño accidental (Requisito: Envío inmediato)
        if "Noche Estrellada" in obra.titulo:
            print(f"[!] Alerta: Se detectó humedad en '{obra.titulo}'")
            obra.enviar_a_restauracion("Daño por Humedad")

    # --- 4. GESTIÓN DE CESIONES Y VALORACIÓN (Director) ---
    print("\n" + "-"*30)
    print("MÓDULO DE DIRECCIÓN")
    print("-"*30)
    
    # Requisito: Suma total
    total = sum(o.valor for o in inventario)
    print(f"[REPORTE] Valoración total del patrimonio: ${total}")

    # Requisito: Cesiones y lista de espera
    print("\n[GESTIÓN DE PRÉSTAMOS]")
    obra1.ceder_a_museo("Museo del Louvre", 25000000)
    obra1.ceder_a_museo("Museo del Prado", 18000000) # Debería quedar en espera

    # --- 5. REPORTE FINAL DE ESTADOS ---
    print("\n" + "="*50)
    print("      RESUMEN FINAL DE OPERACIONES")
    print("="*50)
    for obra in inventario:
        estado_espera = f" | En espera para: {obra.museo_en_espera}" if obra.museo_en_espera else ""
        print(f"Obra: {obra.titulo:20} | Estado: {obra.estado:12}{estado_espera}")

if __name__ == "__main__":
    ejecutar_sistema_completo()