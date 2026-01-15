# Uso y Funcionamiento

Una vez completada la instalación, podemos acceder y utilizar los servicios.

## Acceso a WordPress

Para acceder a nuestro sitio WordPress configurado en el contenedor LAMP:

1.  Abre tu navegador web.
2.  Navega a la URL: `http://localhost:8080/blog` (o la ruta que hayas configurado).
3.  Si la configuración es correcta, verás el instalador de WordPress o la página de inicio.

??? info "Solución de Problemas"
    Si ves un error, verifica que el archivo `/etc/wordpress/config-localhost.php` esté correctamente configurado con las credenciales de la base de datos que creaste.

## Gestión con Portainer

Para gestionar tus contenedores de forma gráfica:

1.  Abre el navegador y ve a `https://localhost:9443`.
2.  Acepta el certificado de seguridad (autofirmado por defecto).
3.  Crea el usuario administrador inicial.
    *   **Usuario**: `admin`
    *   **Contraseña**: (mínimo 12 caracteres, ej: `cefireadmindocker`)

### Panel de Control

Una vez dentro, verás el "Environment" local. Al hacer clic, accederás al dashboard (tablero) donde puedes ver:

*   **Containers**: Lista de contenedores activos/inactivos. Puedes iniciar (`start`), detener (`stop`) o eliminar (`remove`) contenedores (incluyendo el de LAMP).
*   **Images**: Imágenes Docker descargadas en tu sistema.
*   **Volumes**: Volúmenes de datos persistentes.

![Placeholder para imagen de dashboard Portainer](assets/placeholder_portainer.png)
*Imagen representativa del dashboard de Portainer.*
