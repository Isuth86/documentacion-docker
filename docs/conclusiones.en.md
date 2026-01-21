# Conclusions & Future Improvements

## Conclusions

Completing this practical project has allowed us to consolidate fundamental knowledge in modern systems administration:

*   **Docker Flexibility**: We have seen how Docker makes it easy to spin up complex services (like a full LAMP stack) in a matter of minutes, without "cluttering" the host operating system.
*   **Visual Management**: Portainer proves to be an indispensable tool for those who prefer visual management over pure command line, facilitating container status monitoring.
*   **Automation**: Configuring startup scripts (`.bashrc`) to automate service startup within the container.

## Future Improvements

To evolve this project, the following improvements are proposed:

1.  **Docker Compose**: Migrate manual LAMP container creation (`docker run`) to a `docker-compose.yml` file. This would allow defining the entire infrastructure as code, facilitating deployment with a single command.
2.  **Real HTTPS**: Configure valid SSL certificates (e.g., with Let's Encrypt) for secure access, instead of using simple HTTP or self-signed certificates.
3.  **Data Persistence in LAMP**: Move database and web files to Docker volumes, so information is not lost if the LAMP container is deleted.
