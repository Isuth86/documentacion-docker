# Instrucciones de Entrega y Despliegue

¡El proyecto ha sido creado localmente! Ahora debes seguir estos pasos para publicarlo en GitHub y obtener los enlaces para la entrega.

## 1. Crear Repositorio en GitHub

1.  Inicia sesión en [GitHub](https://github.com).
2.  Crea un **nuevo repositorio** (botón "New").
3.  Nombre del repositorio (ejemplo): `documentacion-docker`.
4.  Público.
5.  **NO** añadas README, .gitignore ni licencia (ya los tienes localmente).
6.  Haz clic en **Create repository**.

## 2. Subir el código

Abre una terminal en la carpeta de tu proyecto (`trabajo proyecto`) y ejecuta los comandos que te muestra GitHub (sustituyendo `TU_USUARIO` por tu nombre de usuario real):

```bash
git remote add origin https://github.com/TU_USUARIO/documentacion-docker.git
git branch -M main
git push -u origin main
```

## 3. Desplegar en GitHub Pages

Una vez subido el código, usa `mkdocs` para desplegar el sitio:

1.  En la misma terminal, ejecuta:
    ```bash
    mkdocs gh-deploy
    ```
    *(Asegúrate de tener MkDocs instalado con `pip install mkdocs-material` si no lo tienes).*

2.  Este comando creará una rama `gh-pages` en tu repositorio.

## 4. Obtener Enlaces para la Entrega

*   **Enlace al Repositorio**: `https://github.com/TU_USUARIO/documentacion-docker`
*   **Enlace al Sitio Web**: Ve a la pestaña **Settings** > **Pages** de tu repositorio. Ahí verás la URL publicada (normalmente `https://TU_USUARIO.github.io/documentacion-docker/`).

## Resumen de lo realizado

*   [x] Configuración de MkDocs con tema Material.
*   [x] Extracción de contenido de los PDFs proporcionados.
*   [x] Creación de 5 páginas de contenido (Inicio, Intro, Instalación, Uso, Conclusiones).
*   [x] Implementación de bloques de código y admonitions (advertencias).
*   [x] Inicialización de Git local.
