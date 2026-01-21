# Installation & Requirements

Below are the detailed steps for installing both environments.

## Part 1: Creating Docker LAMP + WordPress

### 1.1 Create the Base Container
First, we create a container based on Ubuntu 22.04, exposing port 80 of the container to 8080 on the host.

```bash
docker run –it –p 8080:80 –name LAMP Ubuntu:22.04 /bin/bash
```

![LAMP Container Creation](assets/docker compose.png){: style="width: 100%; max-width: 600px;"}
![Process Verification](assets/docker compose1.png){: style="width: 100%; max-width: 600px;"}

### 1.2 Package Installation
Inside the container, we update and install the necessary services (Apache, MariaDB, PHP, WordPress).

```bash
apt update
apt install wordpress php libapache2-mod-php mariadb-server php-mysql
```

We can start Apache with:
```bash
service apache2 start
```

![Package Installation](assets/docker compose2.png){: style="width: 100%; max-width: 600px;"}

### 1.3 Apache Configuration
We need to configure Apache to serve WordPress. We install a text editor:
```bash
apt install nano
```
We create the file `/etc/apache2/sites-available/wordpress.conf` and configure `URL rewriting`:
```bash
a2ensite wordpress
a2enmode rewrite
service apache2 restart
```

### 1.4 Database Configuration
We start MariaDB and secure the installation:
```bash
service mariadb start
mysql_secure_installation
```
Then we access MySQL to create the database and user:
```sql
CREATE DATABASE wordpress;
CREATE USER 'wordpress'@'%' IDENTIFIED BY 'MyPass-2023';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'%' WITH GRANT OPTION;
```

![MySQL Configuration](assets/docker compose3.png){: style="width: 100%; max-width: 600px;"}
![Final Configuration](assets/docker compose4.png){: style="width: 100%; max-width: 600px;"}

---

## Part 2: Portainer CE Installation

### 2.1 Create Volume
We create a volume to persist Portainer data:
```bash
docker volume create portainer_data
```

![Portainer Volume Creation](assets/docker portainer.png){: style="width: 100%; max-width: 600px;"}

### 2.2 Run the Container
We launch Portainer mapping ports 8000 and 9443:

```bash
docker run -d -p 8000:8000 -p 9443:9443 --name portainer \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer-ce:latest
```

![Running Portainer](assets/docker portainer1.png){: style="width: 100%; max-width: 600px;"}
