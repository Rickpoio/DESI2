# DESI2

## Instalación

### Requisitos previos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y abierto.
- Git.

### Pasos

1. **Clonar el repositorio**

   ```bash
   git clone <url-del-repositorio>
   cd DESI2/Ejercicio/Ejercicio
   ```

2. **Crear el archivo `.env`**

   Copia el archivo de ejemplo:

   ```bash
   cp .env.example .env
   ```

   Abre `.env` y completa `MYSQL_ROOT_PASSWORD` con la contraseña real del proyecto (**no uses el valor de ejemplo**).

3. **Levantar los contenedores**

   ```bash
   docker compose up -d
   ```

   Esto descarga las imágenes, crea la base de datos MySQL con los datos ya cargados, y levanta Metabase con los dashboards ya armados.

4. **Esperar a que ambos servicios arranquen**

   La primera vez Metabase tarda un poco en iniciar. Puedes revisar el progreso con:

   ```bash
   docker compose logs -f metabase
   ```

5. **Abrir Metabase**

   Entra a [http://localhost:3000](http://localhost:3000) e inicia sesión con las credenciales. Ahí veras los dashboards ya creados, con los datos de la base cargados automáticamente.

### Apagar el proyecto

```bash
docker compose down
```

(Esto no borra los datos ni los dashboards; solo detiene los contenedores.)
