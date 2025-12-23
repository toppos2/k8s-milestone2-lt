# Kubernetes Webstack Project Instructions

## Architecture Overview
This is a simple three-tier web application deployed on Kubernetes:
- **Frontend**: Lighttpd serving static HTML that fetches data from the API
- **API**: FastAPI application providing REST endpoints
- **Database**: MongoDB for data storage

Key components are containerized and deployed as separate Kubernetes deployments in the `webstack-lt` namespace.

## Key Files and Structure
- `api/main.py`: FastAPI app with CORS middleware allowing `localhost:8080` and `localhost:8088`
- `api/Dockerfile`: Builds Python 3.11 image, exposes port 8000
- `frontend/index.html`: Simple HTML page fetching from `http://localhost:8000/name` (update to service URL in K8s)
- `frontend/Dockerfile`: Debian-based lighttpd image, exposes port 80
- `k8s/*.yaml`: Kubernetes manifests for namespace, deployments, and services

## Development Workflow
1. **Local Development**: Run containers with `docker run` or use `docker-compose` (not present, create if needed)
2. **Build Images**: Use `docker build -t api-lt:2.0 ./api` and `docker build -t frontend-lt:1.1 ./frontend`
3. **Deploy to K8s**: Apply manifests with `kubectl apply -f k8s/`
4. **Access**: Frontend service on port 80, API on 8000

## Conventions and Patterns
- **Image Naming**: Use `-lt` suffix (e.g., `api-lt`, `frontend-lt`)
- **Namespace**: Always `webstack-lt` for all resources
- **Environment Variables**: API uses `MONGO_URL` for database connection (e.g., `mongodb://mongo:27017/webstack`)
- **CORS Origins**: Include both `localhost:8080` and `localhost:8088` for development flexibility
- **Service Communication**: Use Kubernetes service names (e.g., `http://api:8000`) instead of localhost in production

## Common Tasks
- **Add API Endpoint**: Follow pattern in `api/main.py` - import FastAPI, define route with decorator
- **Update Frontend**: Modify `frontend/index.html` and rebuild image
- **Database Integration**: Connect using `MONGO_URL` env var, similar to existing setup in `k8s/api.yaml`
- **K8s Changes**: Edit YAML files in `k8s/` directory, ensure namespace is `webstack-lt`

## Future Plans
- Implement GitOps with ArgoCD
- Add HTTPS support
- Expand MongoDB usage beyond current placeholder setup</content>
<parameter name="filePath">c:\Users\topsl\k8s-milestone2\.github\copilot-instructions.md