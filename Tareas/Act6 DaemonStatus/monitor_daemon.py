import os
import time
import psutil
import curses

DAEMON_NAME = "ascii_daemon.py"

def is_process_running(process_name):
    """Verifica si el proceso está en ejecución."""
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if process_name in " ".join(proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def monitor_daemon(stdscr):
    """Monitorea el demonio y muestra su estado con colores en curses."""
    curses.curs_set(0)  # Ocultar cursor
    stdscr.nodelay(True)
    stdscr.timeout(1000)  # Refrescar cada segundo

    # Inicializar colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Verde
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Rojo

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()  # Obtener tamaño de pantalla
        msg = "Presiona 'q' para salir"

        if is_process_running(DAEMON_NAME):
            status = "🟢 Demonio en ejecución"
            color = curses.color_pair(1)
        else:
            status = "🔴 Demonio detenido"
            color = curses.color_pair(2)

        # Centrar texto en pantalla
        stdscr.addstr(h // 2, (w - len(status)) // 2, status, color)
        stdscr.addstr(h - 2, (w - len(msg)) // 2, msg, curses.A_DIM)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):  # Salir con 'q'
            break

if __name__ == "__main__":
    curses.wrapper(monitor_daemon)

