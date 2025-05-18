# Tutorial de Docker

Este tutorial te guiará a través de los conceptos básicos de Docker, desde la ejecución de contenedores simples hasta la creación de tu propia aplicación Node.js en contenedores.

## Índice
1. [Comandos básicos de Docker](#comandos-básicos-de-docker)
2. [Trabajando con imágenes Alpine](#trabajando-con-imágenes-alpine)
3. [Trabajando con Nginx](#trabajando-con-nginx)
4. [Gestión de contenedores](#gestión-de-contenedores)
5. [Exponiendo puertos](#exponiendo-puertos)
6. [Creando una aplicación Node.js](#creando-una-aplicación-nodejs)
7. [Creando un Dockerfile](#creando-un-dockerfile)
8. [Construyendo y ejecutando tu propia imagen](#construyendo-y-ejecutando-tu-propia-imagen)
9. [Actualizando tu aplicación](#actualizando-tu-aplicación)

## Comandos básicos de Docker

Estos comandos te permiten ver las imágenes y contenedores en tu sistema:

```bash
# Ver todas las imágenes de Docker descargadas en tu sistema
docker images

# Ver todos los contenedores en ejecución
docker ps
```

## Trabajando con imágenes Alpine

Alpine es una distribución de Linux ligera, perfecta para contenedores:

```bash
# Descargar la imagen Alpine versión 3.18.4
docker pull alpine:3.18.4

# Iniciar un contenedor Alpine interactivo con shell
docker run -it alpine:3.18.4 sh
```

Una vez dentro del contenedor Alpine, puedes ejecutar comandos como:

```bash
# Actualizar la lista de paquetes
apk update

# Actualizar todos los paquetes instalados
apk upgrade 

# Instalar la herramienta curl
apk add curl

# Verificar la conectividad haciendo una petición a Google
curl www.google.com

# Salir del contenedor
exit 
```

## Trabajando con Nginx

Nginx es un servidor web popular, frecuentemente usado en contenedores:

```bash
# Descargar la imagen Nginx versión 1.23
docker pull nginx:1.23

# Descargar la última versión de Nginx
docker pull nginx

# Ejecutar Nginx en primer plano (verás los logs en la terminal)
docker run nginx:1.23
```

## Gestión de contenedores

```bash
# En otra terminal, ver los contenedores en ejecución
docker ps

# Ejecutar Nginx en modo detached (en segundo plano)
docker run -d nginx:1.23

# Ver los logs de un contenedor específico (reemplaza el ID con el de tu contenedor)
docker logs [ID_CONTENEDOR]
# Ejemplo: docker logs 7250a9f1d7b9

# Detener un contenedor en ejecución
docker stop [ID_CONTENEDOR]
# Ejemplo: docker stop 7250a9f1d7b9
```

## Exponiendo puertos

Para acceder a servicios dentro del contenedor desde tu máquina local:

```bash
# Ejecutar Nginx exponiendo el puerto 80 del contenedor al puerto 9090 de tu máquina
docker run -d -p 9090:80 nginx:1.23
```

Ahora puedes abrir tu navegador y visitar `localhost:9090` para ver la página de bienvenida de Nginx.

```bash
# Ver todos los contenedores (incluso los detenidos)
docker ps -a

# Iniciar un contenedor existente en modo interactivo
docker start -i [ID_CONTENEDOR]
# Ejemplo: docker start -i 1d057b59b0a5
```

## Asignando nombres a los contenedores

En lugar de usar IDs aleatorios, puedes asignar nombres descriptivos:

```bash
# Ejecutar un contenedor con un nombre personalizado
docker run --name mi-web-app -d -p 9090:80 nginx:1.23
```

Resultado:
```
CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS         PORTS                  NAMES
48ae1dbc21e7   nginx:1.23   "/docker-entrypoint.…"   4 seconds ago   Up 2 seconds   0.0.0.0:9090->80/tcp   mi-web-app
```

## Creando una aplicación Node.js

Para crear una aplicación simple de Node.js, sigue estos pasos:

1. Crea un archivo `src/server.js`:

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send("Welcome to my awesome app!");
});

app.listen(3000, function() {
    console.log("app listening on port 3000");
});
```

2. Crea un archivo `package.json`:

```json
{
    "name": "my-app",
    "version": "1.0",
    "dependencies": {
        "express": "4.18.2"
    }
}
```

3. Ejecuta la aplicación localmente:

```bash
node src/server.js
```

Deberías ver el mensaje: `app listening on port 3000`

## Creando un Dockerfile

Para containerizar tu aplicación Node.js, crea un archivo `Dockerfile`:

```dockerfile
FROM node:19-alpine
COPY package.json /app/
COPY src /app/
WORKDIR /app
RUN npm install
CMD ["node", "server.js"]
```

Este Dockerfile:
- Usa Node.js 19 en Alpine como base
- Copia los archivos necesarios
- Establece el directorio de trabajo
- Instala las dependencias
- Define el comando para iniciar la aplicación

## Construyendo y ejecutando tu propia imagen

```bash
# Construir la imagen con la etiqueta "node-app:1.0"
docker build -t node-app:1.0 .

# Ver la imagen recién creada
docker images

# Ejecutar un contenedor de tu aplicación
docker run -d -p 3000:3000 node-app:1.0
```

Ahora puedes acceder a tu aplicación en `localhost:3000`.

## Actualizando tu aplicación

1. Modifica `server.js` para cambiar el mensaje:

```javascript
app.get('/', (req, res) => {
    res.send("Welcome to my awesome app v2!");
});
```

2. Reconstruye y ejecuta la nueva versión:

```bash
# Detener el contenedor actual
docker stop [ID_CONTENEDOR]
# Ejemplo: docker stop c6a9b5578e98

# Reconstruir la imagen
docker build -t node-app:1.0 .

# Ejecutar la nueva versión
docker run -d -p 3000:3000 node-app:1.0
```

Ahora puedes visitar `localhost:3000` para ver tu mensaje actualizado.

---

Este tutorial cubre los conceptos básicos de Docker para principiantes, incluyendo la gestión de contenedores, la exposición de puertos y la creación de tus propias imágenes. ¡Feliz aprendizaje!
