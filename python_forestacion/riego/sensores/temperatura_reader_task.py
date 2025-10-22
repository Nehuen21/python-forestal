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
    """Sensor de temperatura que notifica lecturas periódicamente."""
    
    def __init__(self):
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._contador_lecturas = 0
        self.daemon = True
        self.name = "TEMP_" + str(id(self))

    def run(self) -> None:
        """Bucle principal del sensor de temperatura."""
        print(f"[{self.name}] 🔥 Sensor de temperatura iniciado")
        
        while not self._detenido.is_set():
            try:
                # Simular lectura de temperatura
                temperatura = random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)
                self._contador_lecturas += 1
                
                # Notificar a observadores
                self.notificar_observadores(temperatura)
                
                # Debug
                if self._contador_lecturas % 100 == 0:
                    print(f"[{self.name}] 📊 Lectura #{self._contador_lecturas}: {temperatura:.1f}°C")
                
                time.sleep(INTERVALO_SENSOR_TEMPERATURA)
                
            except Exception as e:
                print(f"[{self.name}] ❌ Error: {e}")
                time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def detener(self) -> None:
        """Detiene el sensor de forma segura."""
        self._detenido.set()
        print(f"[{self.name}] 🛑 Sensor de temperatura detenido")

    def get_contador_lecturas(self) -> int:
        """Retorna el número total de lecturas realizadas."""
        return self._contador_lecturas