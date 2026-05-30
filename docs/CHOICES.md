# Technology Choices and Rationale

## YOLOv8

### Why YOLOv8 was selected

YOLOv8 was chosen because:

- Fast inference speed
- High accuracy for person detection
- Easy integration with Python
- Lightweight models available
- Strong community support

### Benefits

- Real-time processing capability
- Suitable for CCTV analytics
- Easy deployment in Docker environments

---

## FastAPI

### Why FastAPI was selected

FastAPI was chosen because:

- High performance
- Automatic Swagger documentation
- Native request validation using Pydantic
- Simple REST API development
- Excellent developer productivity

### Benefits

- Reduced development time
- Built-in OpenAPI support
- Strong typing support
- Easy API testing through Swagger UI

---

## SQLite

### Why SQLite was selected

SQLite was chosen because:

- Zero configuration database
- Lightweight deployment
- Ideal for prototype and challenge environments
- No separate database server required

### Benefits

- Easy setup
- Portable database file
- Fast local development
- Minimal resource usage

---

## Docker

### Why Docker was selected

Docker was chosen because:

- Consistent deployment environment
- Easy setup for reviewers
- Dependency isolation
- Reproducible builds

### Benefits

- Single-command deployment
- Platform independence
- Simplified environment management
- Easy scalability in the future

---

## Event-Driven Architecture

### Why Event-Based Processing

Event-driven processing was selected because:

- Decouples detection and analytics
- Supports future scalability
- Simplifies ingestion and reporting
- Enables batch processing

### Benefits

- Flexible architecture
- Easier maintenance
- Future integration readiness
- Better system modularity

---

## SQLAlchemy ORM

### Why SQLAlchemy was selected

SQLAlchemy was chosen because:

- Simplifies database operations
- Supports multiple database backends
- Reduces raw SQL usage
- Integrates well with FastAPI

### Benefits

- Cleaner code
- Easier maintenance
- Database portability
- Better scalability

---

## Future Improvements

- PostgreSQL for production workloads
- Redis caching layer
- Kafka event streaming
- Multi-camera visitor tracking
- Advanced anomaly detection models
- Real-time dashboard analytics
- Cloud deployment on AWS/Azure