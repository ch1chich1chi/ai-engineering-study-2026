"""
汉字谜盒是一款基于人工智能的字谜互动游戏,专为汉字爱好者设计.
在这里,你将与AI机器人进行有趣的猜字挑战!
AI会随机出一道经典字谜(如"一箭穿心"),你需要根据谜面提示猜出对应的字,AI会根据你的回答给出相应的提示,并给出最终的答案

基础环境搭建:
    1.创建项目文件夹,将资料中的static目录拷贝到项目中
    2.编写Python程序,定义路径操作函数,访问前端HTML页面
"""

from fastapi import FastAPI
from starlette import FileResponse
from fastapi.staticfiles import StaticFiles

# 创建FastAPI实例
app = FastAPI(title="汉字谜盒")

# 挂载静态文件的存放目录
app.mount("/static",StaticFiles(directory="static"),name="static")

# 定义操作路径函数
@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port="8000")
