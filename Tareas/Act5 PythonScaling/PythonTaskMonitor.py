import threading
import multiprocessing
import time
import random
import queue
import sys
import signal
from datetime import datetime

# Clase para el sensor daemon
class SensorDaemon(threading.Thread):
    def __init__(self, name, queue, max_iterations=5, interval=1):
        super().__init__(daemon=True)
        self.name = name
        self.queue = queue
        self.interval = interval
        self.running = True
        self.iterations = 0
        self.max_iterations = max_iterations

    def run(self):
        while self.running and self.iterations < self.max_iterations:
            value = random.uniform(0, 100)
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.queue.put((self.name, value, timestamp))
            self.iterations += 1
            time.sleep(self.interval)
        
        # Indicar que el sensor ha terminado
        self.queue.put((self.name, None, None))

    def stop(self):
        self.running = False

# Función para mostrar barra de progreso
def show_progress_bar(value, width=20):
    filled = int(value * width / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f'[{bar}] {value:.1f}%'

# Proceso para analizar datos
def analyze_data(sensor_name, value):
    time.sleep(0.5)  # Simulando procesamiento
    status = "NORMAL" if value < 70 else "ALERTA"
    return f"{sensor_name}: {status}"

# Función principal de monitoreo
def monitor_system():
    # Cola para comunicación entre hilos
    sensor_queue = queue.Queue()
    
    # Crear pool de procesos para análisis
    pool = multiprocessing.Pool(processes=2)
    
    # Inicializar sensores daemon
    sensors = [
        SensorDaemon("CPU", sensor_queue, max_iterations=5, interval=1.5),
        SensorDaemon("Memoria", sensor_queue, max_iterations=5, interval=2),
        SensorDaemon("Temperatura", sensor_queue, max_iterations=5, interval=1.8)
    ]

    # Contador de sensores finalizados
    finished_sensors = 0
    total_sensors = len(sensors)

    # Iniciar sensores
    for sensor in sensors:
        sensor.start()

    try:
        print("\033[2J\033[H", end="")  # Limpiar pantalla
        print("=== Sistema de Monitoreo Iniciado ===")
        print("Se realizarán 5 lecturas por sensor\n")

        while finished_sensors < total_sensors:
            try:
                sensor_name, value, timestamp = sensor_queue.get(timeout=1)
                
                # Verificar si el sensor ha terminado
                if value is None:
                    finished_sensors += 1
                    continue

                # Limpiar línea anterior
                sys.stdout.write("\033[K")
                
                # Mostrar datos del sensor con barra de progreso
                progress_bar = show_progress_bar(value)
                print(f"\r{timestamp} | {sensor_name:12} {progress_bar}", flush=True)
                
                # Analizar datos en proceso separado
                result = pool.apply_async(analyze_data, (sensor_name, value))
                status = result.get(timeout=1)
                
                # Mostrar estado
                if "ALERTA" in status:
                    print(f"\033[91m{status}\033[0m")  # Rojo para alertas
                else:
                    print(f"\033[92m{status}\033[0m")  # Verde para normal
                
            except queue.Empty:
                continue

        print("\n\nTodos los sensores han completado sus 5 lecturas")
        print("Deteniendo sistema...")

    except KeyboardInterrupt:
        print("\n\nDeteniendo sistema prematuramente...")
    
    finally:
        # Detener sensores
        for sensor in sensors:
            sensor.stop()
        # Cerrar pool de procesos
        pool.close()
        pool.join()
        print("Sistema detenido correctamente")

if __name__ == "__main__":
    monitor_system()