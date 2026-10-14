# 日志记录
# 为了能够灵活的控制项目中日志的输出,我们可以通过官方提供的logging模块来输出日志.具体做法如下:
from fastapi import FastAPI
import logging
from fastapi.responses import FileResponse

logging.baseConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
)
# %(asctime)s:时间;%(levelname)s:日志级别;%(filename)s:文件名;%(lineno)d:行数;%(message)s:日志信息
# 在uvicorn.run()里,可以添加access_log=False,这是关闭日志

# 创建FastAPI实例
app = FastAPI()

# 定义路径操作函数
@app.get("/")
def root():
    logging.info("访问首页~")
    return FileResponse("static/index.html")
# 日志级别:日志级别就是给日志信息贴上的"重要性标签",常见的级别有:DEBUG INFO WARNING ERROR FATAL(日志级别依次升高)