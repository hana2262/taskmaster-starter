# 常见问题与调试

## 服务启动但 curl 连接失败

先看 `docker compose ps`，`docker compose logs --tail=200 web`，检查端口与网络。

## ModuleNotFoundError

确认 PYTHONPATH 是否包含项目根，或确保包是可导入（目录名与 `__init__.py`）。

## Pydantic 错误

检查是否同时使用 `class Config` 与 `model_config`（两者互斥），并根据 pydantic 版本调整配置。

---

## 常用命令速查（复制粘贴）

- **启动**：`docker compose up -d --build`
- **查看日志**：`docker compose logs --tail=200 web`
- **进入容器**：`docker compose exec web sh`
- **运行测试**：`docker compose run --rm -e PYTHONPATH=/code web pytest -q`
- **提交**：`git add . && git commit -m "msg" && git push`

---

日期：2025-11-23  
作者：指导者（持续更新）
