from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, List, Optional, Callable

app = FastAPI()


class SuccessResponse(BaseModel):
    statusCode: int
    status: str = "success"
    message: str
    data: Optional[Any] = None


class SuccessShopResponse(BaseModel):

    ShopData: Optional[Any] = None


class ErrorResponse(BaseModel):
    statusCode: int
    status: str = "error"
    message: str
    data: Optional[Any] = None


class CustomJSONResponse(JSONResponse):
    def __init__(self, content: BaseModel, status_code: int = 200, **kwargs):
        super().__init__(content=content.dict(), status_code=status_code, **kwargs)


def success(status_code: int, message: str, data: Any = None) -> SuccessResponse:
    return SuccessResponse(statusCode=status_code, message=message, data=data)


def error(status_code: int, message: str, errors: List[str] = [], data: Any = None) -> ErrorResponse:
    return ErrorResponse(statusCode=status_code, message=message, errors=errors, data=data)


def wrap_request_handler(fn: Callable):
    async def wrapper(request: Request):
        try:
            result = await fn(request)
            if result is not None:
                return JSONResponse(content=result.dict())
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return wrapper


@app.get("/example-success")
@wrap_request_handler
async def example_success_endpoint(request: Request):
    return success(200, "This is a success message", {"key": "value"})


@app.get("/example-error")
@wrap_request_handler
async def example_error_endpoint(request: Request):
    return error(400, "This is an error message", ["error detail 1", "error detail 2"])

# Add more endpoints as needed
