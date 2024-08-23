from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket

from Backend.authentication.AuthRouter import authrouter
from Backend.configs.Database import engine, Base
from Backend.Router import router
from Backend.controller.CompanyController import company_router
from Backend.controller.QRCodeController import qr_router
from Backend.controller.ShopController import shop_router
from Backend.controller.TokenController import token_router

app = FastAPI()

# origins = [
#     "http://localhost:5174",
#     "http://127.0.0.1:5174",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

app.include_router(authrouter, prefix="/auth", tags=["Auth"])
app.include_router(company_router, prefix="/com")
app.include_router(shop_router, prefix="/sh")

app.include_router(qr_router, prefix="/qr")

app.include_router(token_router, prefix="/token")

app.mount("/static", StaticFiles(directory="Backend/staticfiles"), name="static")


@app.get("/")
async def root():
    return {"Connected With NextQueue Server"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
