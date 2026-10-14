# 统一异常处理
# 项目中的功能较多,目前我们并未考虑异常处理,可以借助FastAPI中的统一异常处理方案来处理异常
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()

@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    logging.error(f"处理异常,请求路径:{request.url},异常信息:{exc}")
    return JSONResponse(content={"code": 500, "message": "服务器内部错误", "data": None})