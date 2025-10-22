import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Sensor de temperatura que notifica lecturas periódicas a sus observadores."""

    def __init__(self):
        threading.Thread.__init__(self)
        Observable.__init__(self)

        self._detenido = threading.Event()
        self.daemon = True  # Hilo daemon
        self._ultima_temperatura: float = None
        self._lecturas_realizadas: int = 0

        # Identificador único para este sensor
        self._sensor_id = f"TEMP_{id(self)}"

    def run(self) -> None:
        """Bucle principal del sensor de temperatura."""
        print(f"[{self._sensor_id}] 🌡 Iniciando sensor de temperatura...")
        while not self._detenido.is_set():
            try:
                temperatura = self._leer_temperatura()
                self._ultima_temperatura = temperatura
                self._lecturas_realizadas += 1

                print(f"[{self._sensor_id}] 📊 Lectura #{self._lecturas_realizadas}: {temperatura}°C")
                self.notificar_observadores(temperatura, sensor=self)

                # Espera interruptible
                self._detenido.wait(INTERVALO_SENSOR_TEMPERATURA)

            except Exception as e:
                print(f"[{self._sensor_id}] ❌ Error: {e}")

    def _leer_temperatura(self) -> float:
        """Simula la lectura de temperatura del sensor."""
        temperatura = random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)
        return round(temperatura, 1)

    def detener(self) -> None:
        """Detiene el sensor de temperatura."""
        self._detenido.set()
        print(f"[{self._sensor_id}] 🛑 Deteniendo sensor de temperatura...")

    def get_ultima_temperatura(self) -> float:
        """Devuelve la última temperatura leída."""
        return self._ultima_temperatura

    def get_estadisticas(self) -> dict:
        """Obtiene estadísticas del sensor."""
        return {
            "sensor_id": self._sensor_id,
            "lecturas_realizadas": self._lecturas_realizadas,
            "ultima_temperatura": self._ultima_temperatura,
            "observadores": self.get_cantidad_observadores()
        }

    def __str__(self) -> str:
        return f"TemperaturaReaderTask(id={self._sensor_id}, observadores={self.get_cantidad_observadores()})"
