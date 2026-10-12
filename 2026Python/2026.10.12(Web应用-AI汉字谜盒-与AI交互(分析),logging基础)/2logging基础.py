import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

logger = logging.getLogger(__name__)

logging.debug("正在检查请求数据")
logging.info("请求正常完成")
logging.warning("响应速度有点慢")
logging.error("请求 DeepSeek 失败")

"""
debug()：调试细节
info()：程序正常运行
warning()：出现了异常迹象,但还能继续
error()：本次操作失败了

%(... )s 是 logging 规定的占位符

第一条 DEBUG 不显示,因为：
level=logging.INFO
相当于设置了门槛:只显示 INFO 以及比 INFO 更严重的日志.
"""
