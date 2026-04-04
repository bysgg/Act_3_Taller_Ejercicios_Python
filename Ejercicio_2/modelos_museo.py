from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Optional

class Restauracion:
    def __init__(self, tipo: str, fecha_inicio: datetime):
        self.tipo = tipo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin: Optional[datetime] = None

    def __str__(self) -> str:
        estado = f"Finalizada el {self.fecha_fin.date()}" if self.fecha_fin else "En curso"
        return f"[{self.fecha_inicio.date()}] Tipo: {self.tipo} - {estado}"

class ObraDeArte(ABC):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str):
        self.titulo = titulo
        self.autor = autor
        self.periodo = periodo
        self.valor = valor
        self.fecha_creacion = fecha_creacion
        self.fecha_entrada_museo = datetime.now()
        self.estado = "Expuesta"  
        self.ultima_restauracion: datetime = self.fecha_entrada_museo
        self.historial_restauraciones: List[Restauracion] = []
        self.museo_en_espera: Optional[str] = None 
        self.importe_cesion: float = 0.0
        self.museo_cesionario: Optional[str] = None

    def enviar_a_restauracion(self, tipo: str):
        if self.estado != "Restauración":
            nueva_res = Restauracion(tipo, datetime.now())
            self.historial_restauraciones.append(nueva_res)
            self.estado = "Restauración"
            print(f"[MANTENIMIENTO] {self.titulo} enviada a restauración ({tipo}).")

    # Para que Pylance no se queje de timedelta:
    def chequear_mantenimiento_automatico(self):
        cinco_anos = timedelta(days=5*365)
        if datetime.now() - self.ultima_restauracion >= cinco_anos:
            self.enviar_a_restauracion("Mantenimiento Quinquenal Automático")

    def finalizar_restauracion(self):
        if self.estado == "Restauración":
            self.historial_restauraciones[-1].fecha_fin = datetime.now()
            self.estado = "Expuesta"
            self.ultima_restauracion = datetime.now()
            print(f"[SOPORTE] Restauración de {self.titulo} finalizada.")

    def ceder_a_museo(self, nombre_museo: str, importe: float):
        if self.estado == "Expuesta":
            self.estado = "Cedida"
            self.museo_cesionario = nombre_museo
            self.importe_cesion = importe
            print(f"[DIRECTOR] Obra '{self.titulo}' cedida a {nombre_museo} por ${importe}")
        else:
            self.museo_en_espera = nombre_museo
            print(f"[DIRECTOR] {nombre_museo} en espera. '{self.titulo}' está actualmente {self.estado}")

    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.titulo} - {self.autor} (${self.valor})"

class Cuadro(ObraDeArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, tecnica: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo = estilo
        self.tecnica = tecnica

    def mostrar_detalle(self) -> str:
        return f"Estilo: {self.estilo}, Técnica: {self.tecnica}"

class Escultura(ObraDeArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, material: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo = estilo
        self.material = material

    def mostrar_detalle(self) -> str:
        return f"Estilo: {self.estilo}, Material: {self.material}"

class Usuario:
    def __init__(self, username: str, password: str, rol: str):
        self.username = username
        self.password = password
        self.rol = rol # Director, Restaurador, Encargado

    def autenticar(self, user: str, psw: str) -> bool:
        return self.username == user and self.password == psw