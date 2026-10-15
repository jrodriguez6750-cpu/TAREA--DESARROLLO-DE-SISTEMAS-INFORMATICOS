# =====================================================
# ACTIVIDAD 1: SISTEMA DE RESCATE Y ADOPCIÓN ANIMAL
# Patrones aplicados: Fábrica, Observador, Composite
# =====================================================

from abc import ABC, abstractmethod

# =====================================================
# PATRÓN 1: FÁBRICA (Creacional)
# =====================================================
class Animal:
    def __init__(self, nombre, especie, edad, ubicacion, estado="Rescatado"):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.ubicacion = ubicacion
        self.estado = estado

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.estado}"

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"✅ {self.nombre} cambió a: {nuevo_estado}")


class FabricaAnimales:
    @staticmethod
    def crear_animal(tipo, nombre, edad, ubicacion):
        tipo = tipo.lower()
        if tipo == "perro":
            return Animal(nombre, "Perro", edad, ubicacion)
        elif tipo == "gato":
            return Animal(nombre, "Gato", edad, ubicacion)
        else:
            return Animal(nombre, tipo.capitalize(), edad, ubicacion)


# =====================================================
# PATRÓN 2: OBSERVADOR (Comportamiento)
# =====================================================
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass


class SujetoNotificaciones:
    def __init__(self):
        self._suscriptores = []

    def suscribir(self, observador):
        self._suscriptores.append(observador)
        print("➕ Nuevo suscriptor agregado")

    def desuscribir(self, observador):
        self._suscriptores.remove(observador)

    def notificar_cambio(self, mensaje):
        print(f"\n📢 Enviando notificación: {mensaje}")
        for suscriptor in self._suscriptores:
            suscriptor.actualizar(mensaje)


class AdoptanteSuscriptor(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"💌 {self.nombre} recibió: {mensaje}")


# =====================================================
# PATRÓN 3: COMPOSITE (Estructural)
# =====================================================
class ElementoExpediente:
    def mostrar(self):
        pass


class RegistroMedico(ElementoExpediente):
    def __init__(self, fecha, contenido):
        self.fecha = fecha
        self.contenido = contenido

    def mostrar(self):
        return f"📄 [{self.fecha}] {self.contenido}"


class CarpetaExpediente(ElementoExpediente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def mostrar(self):
        salida = f"📂 Carpeta: {self.nombre}\n"
        for elemento in self.elementos:
            salida += f"   {elemento.mostrar()}\n"
        return salida


# =====================================================
# EJECUCIÓN Y PRUEBA
# =====================================================
if __name__ == "__main__":
    print("=" * 50)
    print("   SISTEMA DE RESCATE Y ADOPCIÓN - PRUEBA")
    print("=" * 50)

    # --- Fábrica ---
    print("\n--- 1. Creación de animales ---")
    fabrica = FabricaAnimales()
    perro = fabrica.crear_animal("perro", "Firulais", 3, "Riobamba")
    gato = fabrica.crear_animal("gato", "Mishi", 2, "Ambato")
    print(perro)
    print(gato)

    # --- Observador ---
    print("\n--- 2. Notificaciones ---")
    notificador = SujetoNotificaciones()
    adoptante1 = AdoptanteSuscriptor("María López")
    adoptante2 = AdoptanteSuscriptor("Juan Pérez")
    notificador.suscribir(adoptante1)
    notificador.suscribir(adoptante2)
    mensaje_disponible = f"¡{perro.nombre} está disponible para adopción!"
    notificador.notificar_cambio(mensaje_disponible)
    perro.actualizar_estado("En proceso de adopción")
    mensaje_adoptado = f"{perro.nombre} ya fue adoptado 🎉"
    notificador.notificar_cambio(mensaje_adoptado)

    # --- Composite ---
    print("\n--- 3. Expediente médico ---")
    expediente = CarpetaExpediente("Expediente de Firulais")
    expediente.agregar(RegistroMedico("2026-10-01", "Chequeo general - Saludable"))
    expediente.agregar(RegistroMedico("2026-10-05", "Vacunación completa"))
    subcarpeta = CarpetaExpediente("Exámenes complementarios")
    subcarpeta.agregar(RegistroMedico("2026-10-10", "Análisis sanguíneo - Normal"))
    expediente.agregar(subcarpeta)
    print(expediente.mostrar())

    print("\n✅ Todas las pruebas finalizadas")
