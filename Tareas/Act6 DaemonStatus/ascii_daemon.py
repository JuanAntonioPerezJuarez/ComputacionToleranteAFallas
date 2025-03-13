import os
import time
import curses

def run_animation(stdscr):
    """Ejecuta la animación en pantalla."""
    curses.curs_set(0)  # Oculta el cursor
    stdscr.nodelay(True)  # Hace que getch() no bloquee
    stdscr.timeout(300)  # Controla la velocidad de la animación

    frames = [
        "   (o_o)  ",
        "   (-_-)  ",
        "   (o_o)  ",
        "   (^_^)  ",
    ]

    idx = 0
    while True:
        stdscr.clear()
        stdscr.addstr(5, 10, frames[idx])  # Muestra el frame en la posición (5,10)
        stdscr.refresh()
        idx = (idx + 1) % len(frames)  # Cambia de frame

        key = stdscr.getch()
        if key == ord('q'):  # Permite salir con 'q'
            break

if __name__ == "__main__":
    curses.wrapper(run_animation)
