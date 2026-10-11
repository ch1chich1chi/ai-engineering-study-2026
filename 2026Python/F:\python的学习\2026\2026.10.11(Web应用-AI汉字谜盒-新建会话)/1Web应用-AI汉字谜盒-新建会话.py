from fastapi import FastAPI
from starlette import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from datetime import datetime
import json
from typing import Any
from pydantic import BaseModel

# 创建FastAPI实例
app = FastAPI(title="汉字谜盒")

# 挂载静态文件的存放目录
app.mount("/static",StaticFiles(directory="static"),name="static")

# 创建会话存放的目录 sessions
if not os.path.exists("sessions"):
    os.mkdir("sessions")

# 生成会话标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 数据模型
class ApiResponse(BaseModel):
    Code : int
    message : str
    data : Any # 任意类型的数据

# 定义操作路径函数
@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")

# 新建会话
@app.post("/api/sessions")
def create_session():
    print("创建会话")
    # 1.生成会话标识(名字)
    session_id = generate_session_id()

    # 2.组装会话信息,保存到文件
    session_data = {
        "current_session":session_id,
        "message":[]
    }
    with open(f"sessions/{session_id}.json","w",encoding="utf-8") as f:
        json.dump(session_data,f,ensure_ascii=False,indent=2)

    # 3.返回数据
    # return {"code":200,"message":"创建会话成功","data": session_id}
    return ApiResponse(code=200,message="创建会话成功",data=session_id)

if __name__ == "__main__":
    import unicorn
    unicorn.run(app,host="0.0.0.0",pot="8000")