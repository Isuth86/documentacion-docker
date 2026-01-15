# Caso Práctico: WordPress + MariaDB (Contenedores Separados)

En esta práctica, desplegaremos un CMS WordPress conectando dos contenedores separados a través de una red Docker personalizada:

1.  **Contenedor MariaDB**: Servidor de base de datos.
2.  **Contenedor WordPress**: Servidor web con Apache+PHP y WordPress preinstalado.

Además, realizaremos una **migración de versión** de MariaDB conservando los datos.

## 1. Configuración de Red

Primero, creamos una red Docker para permitir la comunicación entre los contenedores.

```bash
docker network create redwp
```

![Creación de red](assets/docker wordpressmariadb.png)

Para verificar que se ha creado correctamente:
```bash
docker network ls
```

![Listado de redes](assets/docker wordpressmariadb1.png)

## 2. Despliegue de MariaDB

Creamos el contenedor de base de datos conectado a la red `redwp` y usando un volumen para persistencia.

```bash
docker run --name nuestromariadb \
  --network redwp \
  -v /home/sergi/mariadbdata:/var/lib/mysql \
  -e MARIADB_ROOT_PASSWORD=cefireroot \
  -e MARIADB_USER=cefireuser \
  -e MARIADB_PASSWORD=cefirepass \
  -e MARIADB_DATABASE=cefiredb \
  -d mariadb:10.6
```

![Ejecución MariaDB](assets/docker wordpressmariadb2.png)
![Verificación MariaDB](assets/docker wordpressmariadb3.png)

Variables de entorno utilizadas:
*   `MARIADB_ROOT_PASSWORD`: Contraseña del usuario root.
*   `MARIADB_USER`: Nuevo usuario creado.
*   `MARIADB_PASSWORD`: Contraseña del nuevo usuario.
*   `MARIADB_DATABASE`: Nombre de la base de datos inicial.

## 3. Despliegue de WordPress

Lanzamos el contenedor de WordPress, conectándolo a la misma red y exponiendo el puerto 8080.

```bash
docker run --name nuestrowp --network redwp -p 8080:80 -d wordpress
```

![Ejecución WordPress](assets/docker wordpressmariadb4.png)
![Descarga y ejecución](assets/docker wordpressmariadb5.png)

### Configuración Inicial

1.  Accede a `http://localhost:8080`.
2.  Selecciona el idioma (Español).

![Selección de idioma](assets/docker wordpressmariadb6.png)

3.  Configura la conexión a la base de datos:

![Configuración BDD](assets/docker wordpressmariadb7.png)

| Campo | Valor |
| :--- | :--- |
| **Nombre de la base de datos** | `cefiredb` |
| **Nombre de usuario** | `cefireuser` |
| **Contraseña** | `cefirepass` |
| **Servidor de la base de datos** | `nuestromariadb` (Nombre del contenedor) |

![Formulario BDD relleno](assets/docker wordpressmariadb8.png)

4.  Finaliza la instalación creando el usuario administrador de WordPress.

![Instalación exitosa](assets/docker wordpressmariadb9.png)
![Escritorio WP](assets/docker wordpressmariadb10.png)

## 4. Migración de MariaDB (Actualización)

El objetivo es actualizar la versión de MariaDB de 10.6 a 10.7 sin perder datos.

1.  **Detener y eliminar** el contenedor antiguo:
    ```bash
    docker stop nuestromariadb
    docker rm nuestromariadb
    ```
    *Nota: Los datos persisten en `/home/sergi/mariadbdata` (en el host).*

    ![Parada y borrado de contenedor](assets/docker wordpressmariadb11.png)

2.  **Crear el nuevo contenedor** (versión 10.7) mapeando el mismo volumen:
    ```bash
    docker run --name nuestromariadb \
      --network redwp \
      -v /home/sergi/mariadbdata:/var/lib/mysql \
      -e MARIADB_ROOT_PASSWORD=cefireroot \
      -e MARIADB_USER=cefireuser \
      -e MARIADB_PASSWORD=cefirepass \
      -e MARIADB_DATABASE=cefiredb \
      -d mariadb:10.7
    ```

    ![Nueva versión MariaDB](assets/docker wordpressmariadb12.png)

3.  **Verificación**:
    Al acceder de nuevo a `http://localhost:8080`, el sitio debe funcionar correctamente, indicando que la base de datos se ha conservado y migrado con éxito.

    ![Funcionamiento correcto 1](assets/docker wordpressmariadb13.png)
    ![Funcionamiento correcto 2](assets/docker wordpressmariadb14.png)
    ![Funcionamiento correcto 3](assets/docker wordpressmariadb15.png)
