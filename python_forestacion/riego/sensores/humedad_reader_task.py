import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)

class HumedadReaderTask(threading.Thread, Observable[float]):
    """Sensor de humedad que notifica lecturas periódicas a sus observadores."""

    def __init__(self):
        threading.Thread.__init__(self)
        Observable.__init__(self)

        self._detenido = threading.Event()
        self.daemon = True  # Hilo daemon
        self._ultima_humedad: float = None
        self._lecturas_realizadas: int = 0

        # Identificador único para este sensor
        self._sensor_id = f"HUM_{id(self)}"

    def run(self) -> None:
        """Bucle principal del sensor de humedad."""
        print(f"[{self._sensor_id}] 🌡 Iniciando sensor de humedad...")
        while not self._detenido.is_set():
            try:
                humedad = self._leer_humedad()
                self._ultima_humedad = humedad
                self._lecturas_realizadas += 1

                print(f"[{self._sensor_id}] 💧 Lectura #{self._lecturas_realizadas}: {humedad}%")
                self.notificar_observadores(humedad, sensor=self)

                # Espera interruptible
                self._detenido.wait(INTERVALO_SENSOR_HUMEDAD)

            except Exception as e:
                print(f"[{self._sensor_id}] ❌ Error: {e}")

    def _leer_humedad(self) -> float:
        """Simula la lectura de humedad del sensor."""
        humedad = random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)
        return round(humedad, 1)

    def detener(self) -> None:
        """Detiene el sensor de humedad."""
        self._detenido.set()
        print(f"[{self._sensor_id}] 🛑 Deteniendo sensor de humedad...")

    def get_ultima_humedad(self) -> float:
        """Devuelve la última humedad leída."""
        return self._ultima_humedad

    def get_estadisticas(self) -> dict:
        """Obtiene estadísticas del sensor."""
        return {
            "sensor_id": self._sensor_id,
            "lecturas_realizadas": self._lecturas_realizadas,
            "ultima_humedad": self._ultima_humedad,
            "observadores": self.get_cantidad_observadores()
        }

    def __str__(self) -> str:
        return f"HumedadReaderTask(id={self._sensor_id}, observadores={self.get_cantidad_observadores()})"
