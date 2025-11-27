# 应用代码（FastAPI）基础

路由与视图
- 使用 @app.get/post/... 装饰器定义端点。I/O 密集任务优先使用 async def。

项目结构建议
- 按功能拆分模块：app/main.py、app/config.py、app/api、app/services、app/models 等。

健康检查
- 实现 `/health` 或 `/healthz` 端点用于负载均衡器与容器就绪检测，并编写对应单元测试。
