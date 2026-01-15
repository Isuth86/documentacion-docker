# Conclusiones y Mejoras Futuras

## Conclusiones

La realización de este proyecto práctico ha permitido consolidar conocimientos fundamentales en la administración de sistemas modernos:

*   **Flexibilidad de Docker**: Hemos comprobado cómo Docker facilita levantar servicios complejos (como un stack LAMP completo) en cuestión de minutos, sin "ensuciar" el sistema operativo anfitrión.
*   **Gestión Visual**: Portainer demuestra ser una herramienta indispensable para quienes prefieren una gestión visual sobre la línea de comandos pura, facilitando la monitorización del estado de los contenedores.
*   **Automatización**: Configuración de scripts de inicio (`.bashrc`) para automatizar el arranque de servicios dentro del contenedor.

## Mejoras Futuras

Para evolucionar este proyecto, se proponen las siguientes mejoras:

1.  **Docker Compose**: Migrar la creación manual del contenedor LAMP (`docker run`) a un archivo `docker-compose.yml`. Esto permitiría definir toda la infraestructura como código, facilitando el despliegue con un solo comando.
2.  **HTTPS Real**: Configurar certificados SSL válidos (por ejemplo, con Let's Encrypt) para el acceso seguro, en lugar de usar HTTP simple o certificados autofirmados.
3.  **Persistencia de datos en LAMP**: Sacar la base de datos y los archivos web a volúmenes Docker, para que la información no se pierda si se elimina el contenedor LAMP.
