# 应用代码（FastAPI）基础

## 路由与视图

用装饰器 `@app.get/post/...` 定义端点；异步函数（`async def`）适合 I/O 密集的请求。

## 结构化建议

把业务代码按功能拆成模块：
- `app/main.py`
- `app/config.py`
- `app/services`
- `app/api`
- `app/models`

## 健康检查

实现 `/healthz` 用于容器/负载均衡器检测服务就绪情况。

---

日期：2025-11-23  
作者：指导者（持续更新）
