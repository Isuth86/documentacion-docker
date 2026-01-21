# Usage & Operation

Once the installation is complete, we can access and use the services.

## Accessing WordPress

To access our WordPress site configured in the LAMP container:

1.  Open your web browser.
2.  Navigate to the URL: `http://localhost:8080/blog` (or the path you configured).
3.  If configuration is correct, you will see the WordPress installer or the homepage.

??? info "Troubleshooting"
    If you see an error, verify that the `/etc/wordpress/config-localhost.php` file is correctly configured with the database credentials you created.

## Management with Portainer

To manage your containers graphically:

1.  Open browser and go to `https://localhost:9443`.
2.  Accept the security certificate (self-signed by default).
3.  Create the initial admin user.
    *   **Username**: `admin`
    *   **Password**: (minimum 12 characters, e.g., `cefireadmindocker`)

### Control Panel

Once inside, you will see the local "Environment". Clicking on it accesses the dashboard where you can see:

*   **Containers**: List of active/inactive containers. You can start, stop, or remove containers (including the LAMP one).
*   **Images**: Docker images downloaded on your system.
*   **Volumes**: Persistent data volumes.

![Portainer Dashboard](assets/docker portainer2.png){: style="width: 100%; max-width: 700px;"}
![Container Details](assets/docker portainer3.png){: style="width: 100%; max-width: 700px;"}
