from multiprocessing import Process
import time
from fastapi import FastAPI, Request
# from database import supabase
from routers.book_routers import router as book_routes
from routers.auth_routes import router as auth_routes

app = FastAPI(
    title="Supabase Demo",
    description="Supabase demo with FastAPI"
)
app.include_router(auth_routes)
app.include_router(book_routes)


@app.middleware("http")
async def request_metrics(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    print(request.method ,request.url.path,
          response.status_code, f"{process_time:.4f} ")
    return response

@app.get('/', tags=["Root"])
def home():
    return {
        "message": "Supabase API is running"
    }

