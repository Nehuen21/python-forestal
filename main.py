"""
SISTEMA DE GESTION FORESTAL - DEMOSTRACION (refactorizado)
Este script orquesta las historias de usuario implementadas:
- Registro de tierras y plantaciones
- Creacion y manejo de cultivos (Factory + Strategy + Registry)
- Sistema de riego automatizado (Observer)
- Gestion de personal y tareas
- Operaciones de negocio (fincas, fumigacion, cosecha y empaquetado)
- Persistencia de registros
"""

import os
import time
from datetime import date

# Servicios
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService

# Registry / patrones
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

# Entidades
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.herramienta import Herramienta

# Sensores y control de riego
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Constantes
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT

def main() -> None:
    # --- Cabecera ---
    print("=" * 70)
    print("SISTEMA DE GESTION FORESTAL - DEMOSTRACION")
    print("=" * 70)

    try:
        # ---------------------------
        # Singleton: verificar registry
        # ---------------------------
        print("\n-- Verificando patron Singleton (CultivoServiceRegistry) --")
        registry_a = CultivoServiceRegistry()
        registry_b = CultivoServiceRegistry.get_instance()
        registry_c = CultivoServiceRegistry()

        if registry_a is registry_b and registry_b is registry_c:
            print("Singleton OK: unica instancia de registry encontrada.")
            print("Handlers:", registry_a.get_cantidad_handlers())
        else:
            print("Singleton NOK: instancias distintas detectadas.")
            return

        # ---------------------------
        # Crear Tierra + Plantacion
        # ---------------------------
        print("\n-- Creando Tierra y Plantacion (US-001 / US-002) --")
        tierra_service = TierraService()
        terreno = tierra_service.crear_tierra_con_plantacion(
            id_padron_catastral=1,
            superficie=10000.0,
            domicilio="Agrelo, Mendoza",
            nombre_plantacion="Finca del Madero"
        )

        print(f"Tierra creada: padron={terreno.get_id_padron_catastral()}, domicilio={terreno.get_domicilio()}")
        plantacion = terreno.get_finca()
        print(f"Plantacion asociada: {plantacion.get_nombre()}, agua={plantacion.get_agua()}L")

        # ---------------------------
        # Plantar cultivos (Factory)
        # ---------------------------
        print("\n-- Plantando cultivos via PlantacionService (Factory) --")
        plantacion_service = PlantacionService()

        pinos = plantacion_service.plantar(plantacion, "Pino", 5)
        print(f"Pinos plantados: {len(pinos)}")

        olivos = plantacion_service.plantar(plantacion, "Olivo", 3)
        print(f"Olivos plantados: {len(olivos)}")

        lechugas = plantacion_service.plantar(plantacion, "Lechuga", 10)
        print(f"Lechugas plantadas: {len(lechugas)}")

        zanahorias = plantacion_service.plantar(plantacion, "Zanahoria", 8)
        print(f"Zanahorias plantadas: {len(zanahorias)}")

        estado = plantacion_service.get_estado_plantacion(plantacion)
        print("\nEstado plantacion:")
        print(f"  cultivos totales: {estado['cantidad_cultivos']}")
        print(f"  superficie ocupada: {estado['superficie_ocupada']:.2f} m²")
        print(f"  superficie disponible: {estado['superficie_disponible']:.2f} m²")
        print(f"  agua disponible: {estado['agua_disponible']} L")

        # ---------------------------
        # Regar (Strategy + Registry)
        # ---------------------------
        print("\n-- Ejecutando riego de la plantacion (US-008) --")
        resumen = plantacion_service.regar(plantacion)
        print("Riego finalizado:")
        print(f"  agua consumida: {resumen['agua_consumida']}L")
        print(f"  cultivos regados: {resumen['cultivos_regados']}")
        print(f"  agua absorbida (total): {resumen['agua_absorbida_total']}L")
        print("  detalle por tipo:")
        for tipo, datos in resumen["detalle_por_tipo"].items():
            print(f"    - {tipo}: {datos['cantidad']} unidades, {datos['agua_absorbida']}L absorbidos")

        # ---------------------------
        # Gestion de personal y tareas
        # ---------------------------
        print("\n-- Gestion de personal (US-014 a US-016) --")
        trabajador_service = TrabajadorService()

        tareas = [
            Tarea(1, date.today(), "Desmalezar zona norte"),
            Tarea(2, date.today(), "Abonar arboles"),
            Tarea(3, date.today(), "Marcar surcos")
        ]

        trabajador = Trabajador(dni=43888734, nombre="Juan Perez", tareas=tareas)
        print(f"Trabajador: {trabajador.get_nombre()}, DNI: {trabajador.get_dni()}")

        apto = AptoMedico(apto=True, fecha_emision=date.today(), observaciones="Apto para tareas al aire libre")
        trabajador.set_apto_medico(apto)
        print("Apto medico asignado:", trabajador.get_apto_medico().esta_apto())

        # Asignar trabajador a la plantacion (US-017)
        plantacion.set_trabajadores([trabajador])
        print("Trabajador asignado a la plantacion.")

        # Ejecutar tareas (US-016)
        herramienta = Herramienta(id_herramienta=1, nombre="Pala", certificado_hys=True)
        print("Ejecutando tareas del trabajador...")
        resultado = trabajador_service.trabajar(trabajador, date.today(), herramienta)
        print("Resultado ejecucion tareas:", "Éxito" if resultado else "Fallo")

        # ---------------------------
        # Sistema de riego automatizado (Observer)
        # ---------------------------
        print("\n-- Iniciando sensores y controlador de riego (US-010 a US-013) --")
        sensor_temp = TemperaturaReaderTask()
        sensor_hum = HumedadReaderTask()
        controlador = ControlRiegoTask(
            sensor_temperatura=sensor_temp,
            sensor_humedad=sensor_hum,
            plantacion=plantacion,
            plantacion_service=plantacion_service
        )

        sensor_temp.start()
        sensor_hum.start()
        controlador.start()

        print("Sistema de riego iniciado. Funcionando por 15 segundos...")
        for remaining in range(15, 0, -1):
            time.sleep(1)
            print(f"  {remaining} segundos restantes...", end="\r")
        print()

        # Detener sistema
        sensor_temp.detener()
        sensor_hum.detener()
        controlador.detener()

        sensor_temp.join(timeout=THREAD_JOIN_TIMEOUT)
        sensor_hum.join(timeout=THREAD_JOIN_TIMEOUT)
        controlador.join(timeout=THREAD_JOIN_TIMEOUT)

        print("Sistema de riego detenido.")
        stats = controlador.get_estadisticas()
        print("Riegos realizados:", stats.get("riegos_realizados"))
        print("Condiciones finales:", stats.get("condiciones_actuales"))

        # ---------------------------
        # Operaciones de negocio (fincas, fumigacion, cosecha)
        # ---------------------------
        print("\n-- Operaciones de negocio (US-018 a US-020) --")
        registro = RegistroForestal(
            id_padron=1,
            tierra=terreno,
            plantacion=plantacion,
            propietario="Juan Perez",
            avaluo=50309233.55
        )
        fincas_service = FincasService()
        fincas_service.add_finca(registro)

        print("Fumigando plantacion...")
        fincas_service.fumigar(id_padron=1, plaguicida="insecticida organico")

        # Cosechar y empaquetar (ejemplo con Lechuga)
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        paquete_lechugas = fincas_service.cosechar_y_empaquetar(Lechuga)
        paquete_lechugas.mostrar_contenido_caja()

        # ---------------------------
        # Persistencia de registro
        # ---------------------------
        print("\n-- Persistencia (US-021 a US-023) --")
        registro_service = RegistroForestalService()
        registro_service.persistir(registro)
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        registro_service.mostrar_datos(registro_leido)

        # ---------------------------
        # Resumen final
        # ---------------------------
        print("\n" + "=" * 70)
        print("DEMONSTRACION COMPLETADA CON EXITO")
        print("Patrones utilizados: Singleton, Factory, Strategy, Observer, Registry")
        print("=" * 70)

    except Exception as exc:
        # Mostrar traza para debug si algo falla
        print("\nERROR CRITICO DURANTE LA DEMOSTRACION:", exc)
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # Asegurar existencia del directorio para persistencia
    os.makedirs("data", exist_ok=True)
    main()