## Backup script
- You'll need to install the pymongo library
```bash
pip install pymongo
```
- Now you can run the Python script with the MongoDB URI as follows
```bash
./mongodb_backup.py "mongodb://admin:password@vm-hostname1,vm-hostname2,vm-hostname3/admin?otherParams"
```

## Database design setup for microservices
1. Environment Separation:

    Create distinct Kubernetes namespaces for the test and production environments.

2. Kubernetes Deployments:

    Set up Kubernetes Deployments for each microservice.
    Define resource requirements for CPU and memory.

3. Database Isolation:

    Deploy PostgreSQL instances for each microservice as Kubernetes Deployments or StatefulSets.
    Utilize labels or namespaces to maintain database isolation.

4. Role-Based Access Control (RBAC):

    Establish Kubernetes Service Accounts for microservices in both environments.
    Use RBAC to grant read-write access in the test environment and read-only access in production.

5. Kubernetes Secrets:

    Store database credentials securely using Kubernetes Secrets.
    Manage separate secrets for each environment and service account.

6. Configuration Management:

    Store configuration settings, including database connection strings, as Kubernetes ConfigMaps.
    Reference ConfigMap values in your microservice deployments.

7. Continuous Integration/Deployment (CI/CD):

    Integrate database setup and migrations into your CI/CD pipelines.
    Implement database migration scripts using tools like Flyway or Liquibase.

8. Monitoring and Alerts:

    Implement monitoring for Kubernetes clusters and PostgreSQL instances.
    Consider using Prometheus and Grafana for monitoring and alerting.

9. Backup and Recovery:

    Implement regular database backups using Kubernetes Jobs or external backup services.
    Store backups in a separate storage solution for easy recovery.

10. High Availability:

    Consider deploying PostgreSQL in a High Availability (HA) setup.
    Explore Kubernetes StatefulSets for managing database pods.

11. Documentation:

    Create detailed documentation outlining the setup process, configuration management, and access instructions.
    Ensure developers have clear guidance on accessing databases.
