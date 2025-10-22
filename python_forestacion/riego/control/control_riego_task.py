import threading
import time
from typing import Optional
from datetime import date
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Controlador que observa sensores y riega automáticamente."""

    def __init__(self, sensor_temperatura, sensor_humedad, plantacion, plantacion_service):
        threading.Thread.__init__(self)
        Observer.__init__(self)

        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service

        self._detenido = threading.Event()
        self.daemon = True  # Thread daemon

        # Estado actual
        self._ultima_temperatura: Optional[float] = None
        self._ultima_humedad: Optional[float] = None
        self._riegos_realizados: int = 0

        # Registrar este controlador como observador de los sensores
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)

    def run(self) -> None:
        """Bucle principal del controlador de riego."""
        print("[ControlRiego] 🚀 Iniciando controlador de riego automático...")
        while not self._detenido.is_set():
            try:
                self._evaluar_condiciones_riego()
                self._detenido.wait(INTERVALO_CONTROL_RIEGO)  # Permite interrupción inmediata
            except Exception as e:
                print(f"[ControlRiego] ❌ Error en bucle de control: {e}")

    def actualizar(self, evento: float, sensor=None) -> None:
        """
        Método llamado por los sensores.
        Se pasa el sensor que envía el dato para distinguirlo.
        """
        if sensor == self._sensor_temperatura:
            self._ultima_temperatura = evento
            print(f"[ControlRiego] 🌡 Temperatura actualizada: {evento}°C")
        elif sensor == self._sensor_humedad:
            self._ultima_humedad = evento
            print(f"[ControlRiego] 💧 Humedad actualizada: {evento}%")
        else:
            print(f"[ControlRiego] ⚠️ Evento de sensor desconocido: {evento}")

    def _evaluar_condiciones_riego(self) -> None:
        """Evalúa las condiciones ambientales y decide si regar."""
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            print("[ControlRiego] ⏳ Esperando datos de sensores...")
            return

        temp_ok = TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO
        humedad_ok = self._ultima_humedad < HUMEDAD_MAX_RIEGO

        if temp_ok and humedad_ok:
            print(f"[ControlRiego] ✅ Condiciones óptimas (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)")
            self._realizar_riego_automatico()
        else:
            if not temp_ok:
                print(f"[ControlRiego] ❌ Temperatura fuera de rango (T:{self._ultima_temperatura}°C)")
            if not humedad_ok:
                print(f"[ControlRiego] ❌ Humedad muy alta (H:{self._ultima_humedad}%)")

    def _realizar_riego_automatico(self) -> None:
        """Realiza el riego automático de la plantación."""
        try:
            resumen = self._plantacion_service.regar(self._plantacion)
            self._riegos_realizados += 1

            print(f"[ControlRiego] 💦 Riego #{self._riegos_realizados} completado")
            print(f"[ControlRiego]   Agua consumida: {resumen['agua_consumida']}L")
            print(f"[ControlRiego]   Cultivos regados: {resumen['cultivos_regados']}")
            print(f"[ControlRiego]   Agua absorbida total: {resumen['agua_absorbida_total']}L")

            for tipo, datos in resumen["detalle_por_tipo"].items():
                print(f"[ControlRiego]   - {tipo}: {datos['cantidad']} cultivos, {datos['agua_absorbida']}L absorbida")
        except Exception as e:
            print(f"[ControlRiego] ❌ Error en riego automático: {e}")

    def detener(self) -> None:
        """Solicita la detención del hilo y desregistra los observadores."""
        self._detenido.set()
        print("[ControlRiego] 🛑 Deteniendo controlador de riego...")

        if hasattr(self._sensor_temperatura, "eliminar_observador"):
            self._sensor_temperatura.eliminar_observador(self)
        if hasattr(self._sensor_humedad, "eliminar_observador"):
            self._sensor_humedad.eliminar_observador(self)

    def get_estadisticas(self) -> dict:
        """Obtiene estadísticas del controlador."""
        return {
            "riegos_realizados": self._riegos_realizados,
            "ultima_temperatura": self._ultima_temperatura,
            "ultima_humedad": self._ultima_humedad,
            "condiciones_actuales": self._obtener_condiciones_actuales(),
            "observando_sensores": {
                "temperatura": id(self._sensor_temperatura),
                "humedad": id(self._sensor_humedad)
            }
        }

    def _obtener_condiciones_actuales(self) -> str:
        """Obtiene descripción de las condiciones actuales."""
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            return "Esperando datos de sensores..."

        temp_ok = TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO
        humedad_ok = self._ultima_humedad < HUMEDAD_MAX_RIEGO

        if temp_ok and humedad_ok:
            return f"Óptimas para riego (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)"
        elif not temp_ok:
            return f"Temperatura fuera de rango (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)"
        else:
            return f"Humedad muy alta (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)"

    def __str__(self) -> str:
        stats = self.get_estadisticas()
        return f"ControlRiegoTask(riegos={stats['riegos_realizados']}, estado={stats['condiciones_actuales']})"
