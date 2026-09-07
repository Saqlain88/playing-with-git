from fastapi import FastAPI

app = FastAPI(title="GitHub Actions Demo API")


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/tasks")
def get_tasks():
    return [
        {
            "id": 1,
            "title": "Learn GitHub Actions",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Build a CI pipeline",
            "completed": False,
        },
    ]