# ASCII Daemon y Monitor

Este proyecto contiene dos scripts Python diseñados para funcionar en entornos Linux: un daemon que muestra una animación ASCII en la terminal y un segundo daemon que monitorea el estado del primero.

## Componentes

### 1. ascii_daemon.py

Este script muestra una sencilla animación ASCII de una cara con diferentes expresiones en la terminal.

**Características:**
- Utiliza la biblioteca `curses` para manipular la terminal
- Muestra una secuencia de frames animados: (o_o), (-_-), (o_o), (^_^)
- Control de velocidad de animación configurable
- Se puede salir de la animación presionando la tecla 'q'

**Requisitos:**
- Python 3.x
- Biblioteca curses (incluida en la mayoría de instalaciones estándar de Python)

**Uso:**
```bash
python3 ascii_daemon.py
```

### 2. monitor_daemon.py

Este script monitorea si el `ascii_daemon.py` está en ejecución y muestra su estado en la terminal con indicadores de color.

**Características:**
- Utiliza `psutil` para verificar los procesos en ejecución
- Muestra el estado del daemon con indicadores de color:
  - Verde cuando el daemon está en ejecución
  - Rojo cuando el daemon está detenido
- Actualiza el estado cada segundo
- Interface visual mediante curses
- Se puede salir del monitor presionando la tecla 'q'

**Requisitos:**
- Python 3.x
- Bibliotecas:
  - psutil
  - curses

**Instalación de dependencias:**
```bash
pip install psutil
```

**Uso:**
```bash
python3 monitor_daemon.py
```

## Instalación

1. Clona este repositorio o descarga los archivos en tu sistema Linux.
2. Instala las dependencias requeridas:
   ```bash
   pip install psutil
   ```
3. Asegúrate de que los scripts tengan permisos de ejecución:
   ```bash
   chmod +x ascii_daemon.py monitor_daemon.py
   ```

## Uso típico

1. Inicia el daemon de animación ASCII en una terminal:
   ```bash
   python3 ascii_daemon.py
   ```

2. En otra terminal, ejecuta el monitor para verificar el estado del daemon:
   ```bash
   python3 monitor_daemon.py
   ```

3. Puedes detener e iniciar el daemon ASCII y ver cómo el monitor refleja estos cambios.

## Notas

- Ambos scripts utilizan curses, que es compatible con terminales Unix/Linux.
- El monitor verifica la presencia del proceso buscando "ascii_daemon.py" en la línea de comandos.
- Se recomienda ejecutar cada script en una terminal separada para observar su funcionamiento.
