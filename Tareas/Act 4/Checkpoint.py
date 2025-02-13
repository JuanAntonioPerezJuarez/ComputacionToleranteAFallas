import pickle
import os

# Archivo donde se guardará el estado
STATE_FILE = 'program_state.pkl'

# Estado inicial del programa
state = {
    'counter': 0,
    'progress': []
}

def save_state(state):
    with open(STATE_FILE, 'wb') as f:
        pickle.dump(state, f)
    print(f"Estado guardado: {state}")

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'rb') as f:
            state = pickle.load(f)
        print(f"Estado restaurado: {state}")
        return state
    else:
        return None

def main():
    global state

    # Intentar restaurar el estado anterior
    previous_state = load_state()
    if previous_state:
        state = previous_state

    # Simulación de ejecución del programa
    for i in range(state['counter'], 10):
        state['counter'] = i
        state['progress'].append(f"Step {i}")
        print(f"Ejecutando paso {i}")
        save_state(state)
        if i == 5:  # Simulamos un punto de restauración en el paso 5
            print("Simulando interrupcion...")
            break

if __name__ == "__main__":
    main()
