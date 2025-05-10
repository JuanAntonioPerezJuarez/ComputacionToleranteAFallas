from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import random
import time

# Argumentos por defecto para el DAG
default_args = {
    'owner': 'tu_nombre',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 8),
    'email': ['tu_correo@ejemplo.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Crear el DAG
dag = DAG(
    'analisis_datos_ejemplo',
    default_args=default_args,
    description='Un DAG de ejemplo para análisis de datos',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['ejemplo', 'tutorial']
)

# Función para simular extracción de datos
def extraer_datos(**context):
    time.sleep(5)  # Simular proceso
    return {'datos_extraidos': random.randint(100, 1000)}

# Función para simular procesamiento
def procesar_datos(**context):
    ti = context['task_instance']
    datos_extraidos = ti.xcom_pull(task_ids='extraccion_datos')['datos_extraidos']
    time.sleep(3)  # Simular proceso
    return {'datos_procesados': datos_extraidos * 2}

# Función para simular análisis
def analizar_datos(**context):
    ti = context['task_instance']
    datos_procesados = ti.xcom_pull(task_ids='procesamiento_datos')['datos_procesados']
    time.sleep(4)  # Simular proceso
    return {'resultado_analisis': f'Análisis completado con valor: {datos_procesados}'}

# Función para generar reporte
def generar_reporte(**context):
    ti = context['task_instance']
    analisis = ti.xcom_pull(task_ids='analisis_datos')['resultado_analisis']
    time.sleep(3)  # Simular proceso
    return {'reporte': f'Reporte generado basado en: {analisis}'}

# Tareas
inicio = BashOperator(
    task_id='inicio',
    bash_command='echo "Iniciando pipeline de análisis: $(date)"',
    dag=dag
)

extraccion = PythonOperator(
    task_id='extraccion_datos',
    python_callable=extraer_datos,
    dag=dag
)

procesamiento = PythonOperator(
    task_id='procesamiento_datos',
    python_callable=procesar_datos,
    dag=dag
)

analisis = PythonOperator(
    task_id='analisis_datos',
    python_callable=analizar_datos,
    dag=dag
)

reporte = PythonOperator(
    task_id='generar_reporte',
    python_callable=generar_reporte,
    dag=dag
)

fin = BashOperator(
    task_id='fin',
    bash_command='echo "Pipeline completado exitosamente: $(date)"',
    dag=dag
)

# Definir el orden de las tareas
inicio >> extraccion >> procesamiento >> analisis >> reporte >> fin
