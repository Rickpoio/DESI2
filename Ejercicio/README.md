# DES-Investigacion2
Proyecto enfocado a la creacion de un Dashboard para BI usando Metabase como aplicacion para generarlo

Antes de comenzar, asegúrate de tener instalado en tu oredenador los siguientes programas:
Docker Desktop 
editor de base de datos para MySQL, preferido Dbeaver

## Estructura del Proyecto

(Carpeta con nombre de tu preferencia)
├── docker-compose.yml       # Orquestación de contenedores MySQL y Metabase
├── backuppirotecnia.sql     # Respaldo completo DDL/DML para inicializar la BD
├── Graficos-Queries.sql     # Consultas SQL independientes utilizadas en Metabase
├── metabase-data/           # Volumen persistente con la configuración del Dashboard
├── seeder.py                # Script opcional en Python para generación de datos
├── .dockerignore            # Filtros de construcción para Docker
├── .gitignore               # Exclusión de archivos pesados y entornos virtuales
└── README.md                # Documentación del proyecto

Pasos para ejecutar el proyecto: 
  1. Desde la carpeta en la que se creo el repositorio debe ejecutarse el comando docker compose up -d
  2. Correr localmente el repositorio en http://localhost:3000/
  3. Si nunca se habia usado Metabase debe completarse un registro para acceder a el.
  4. Una vez dentro ir a la seccion que dice colecciones en el menu lateral izquierdo elegir la opcion nuestros analisis, 
  dentro de este menu debe elegirse el archivo indicado como pirotecnia prometeo.
  5. Se puede navegar por las diferentes pestañas del dashboard para poder entender la informacion procesada en los 
  diferentes graficos que se han indicado en el proyecto, pueden crearse mas a base de consultas eligiendo la opcion 
  nuevo y digitando la consulta con la informacion deseada.
