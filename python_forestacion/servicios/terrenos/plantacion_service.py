from typing import List, Dict
from datetime import date
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import AGUA_MINIMA

class PlantacionService:
    
    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> List:
        """
        Planta múltiples cultivos de una especie en la plantación.
        
        Args:
            plantacion: La plantación donde plantar
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria")
            cantidad: Número de cultivos a plantar
            
        Returns:
            Lista de cultivos plantados
            
        Raises:
            SuperficieInsuficienteException: Si no hay suficiente superficie
        """
        # Calcular superficie requerida
        cultivo_ejemplo = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_ejemplo.get_superficie() * cantidad
        
        # Verificar superficie disponible
        superficie_disponible = self._calcular_superficie_disponible(plantacion)
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                f"No hay suficiente superficie para plantar {cantidad} {especie}(s)",
                f"Superficie requerida: {superficie_requerida}, disponible: {superficie_disponible}",
                superficie_requerida,
                superficie_disponible
            )
        
        # Crear y agregar cultivos
        cultivos_creados = []
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)
            cultivos_creados.append(cultivo)
        
        return cultivos_creados
    
    def _calcular_superficie_disponible(self, plantacion: Plantacion) -> float:
        """Calcula la superficie disponible en la plantación."""
        superficie_ocupada = sum(
            cultivo.get_superficie() for cultivo in plantacion.get_cultivos()
        )
        return plantacion.get_superficie() - superficie_ocupada
    
    def regar(self, plantacion: Plantacion) -> Dict:
        """
        Riega todos los cultivos de la plantación.
        
        Returns:
            Dict con resumen del riego:
            {
                'agua_consumida': int,
                'cultivos_regados': int,
                'agua_absorbida_total': int,
                'detalle_por_tipo': dict,
                'agua_restante': float
            }
        """
        # Verificar agua disponible
        agua_disponible = plantacion.get_agua()
        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(
                "No hay suficiente agua para regar la plantación",
                f"Agua disponible: {agua_disponible}, mínima requerida: {AGUA_MINIMA}",
                agua_disponible,
                AGUA_MINIMA
            )
        
        # Obtener registry
        registry = CultivoServiceRegistry.get_instance()
        
        # Variables para el resumen
        agua_consumida_total = 0
        cultivos_regados = 0
        agua_absorbida_total = 0
        detalle_por_tipo = {}
        
        # Obtener condiciones ambientales (simuladas)
        fecha_actual = date.today()
        temperatura = 20.0  # °C simulada
        humedad = 60.0      # % simulada
        
        # Regar cada cultivo
        for cultivo in plantacion.get_cultivos():
            try:
                # Usar registry para absorber agua
                agua_absorbida = registry.absorber_agua(cultivo, fecha_actual, temperatura, humedad)
                
                # Actualizar estadísticas
                agua_absorbida_total += agua_absorbida
                cultivos_regados += 1
                
                # Actualizar detalle por tipo
                tipo_cultivo = type(cultivo).__name__
                if tipo_cultivo not in detalle_por_tipo:
                    detalle_por_tipo[tipo_cultivo] = {
                        'cantidad': 0,
                        'agua_absorbida': 0
                    }
                detalle_por_tipo[tipo_cultivo]['cantidad'] += 1
                detalle_por_tipo[tipo_cultivo]['agua_absorbida'] += agua_absorbida
                
                # Hacer crecer los árboles (solo pinos y olivos)
                registry.hacer_crecer(cultivo)
                
            except Exception as e:
                print(f"Error regando cultivo {cultivo.get_id()}: {e}")
                continue
        
        # Consumir agua de la plantación
        agua_consumida_total = agua_absorbida_total
        plantacion.descontar_agua(agua_consumida_total)
        
        # Retornar resumen
        return {
            'agua_consumida': agua_consumida_total,
            'cultivos_regados': cultivos_regados,
            'agua_absorbida_total': agua_absorbida_total,
            'detalle_por_tipo': detalle_por_tipo,
            'agua_restante': plantacion.get_agua()
        }
    
    def get_estado_plantacion(self, plantacion: Plantacion) -> dict:
        """Obtiene el estado actual de la plantación."""
        cultivos = plantacion.get_cultivos()
        superficie_ocupada = sum(cultivo.get_superficie() for cultivo in cultivos)
        superficie_disponible = plantacion.get_superficie() - superficie_ocupada
        
        return {
            'cantidad_cultivos': len(cultivos),
            'superficie_ocupada': superficie_ocupada,
            'superficie_disponible': superficie_disponible,
            'agua_disponible': plantacion.get_agua()
        }