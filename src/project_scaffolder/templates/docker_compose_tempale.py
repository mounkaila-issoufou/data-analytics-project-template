def build_project_docker_compose(project_name: str, package_name: str) -> str:
    return rf"""version: '3.8'
services:
  {package_name}: 
    build: .
    command: {package_name} run
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - PYTHONPATH=/app/src/{package_name}
    depends_on: []
    restart: unless-stopped
    postgres:
    image: postgres:15
    environment:
        POSTGRES_USER: postgres
        POSTGRES_PASSWORD: password
        POSTGRES_DB: {package_name}_db
    ports:
        - "5432:5432"
    volumes:
        - postgres_data:/var/lib/postgresql/data
volumes:
  postgres_data:
"""