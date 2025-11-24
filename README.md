Taskmaster Starter
简要说明：

技术栈：FastAPI, PostgreSQL, Redis, Docker Compose, Pytest
目标：一个可以在 10 周内扩展完成的任务管理后端（见 docs/backend_guide.md）
快速启动：

复制示例环境： cp .env.example .env
启动服务： docker compose up -d --build
访问服务： http://localhost:8000/healthz
API 文档： http://localhost:8000/docs
运行测试： docker compose run --rm -e PYTHONPATH=/code web pytest -q

更多：参见 docs/backend_guide.md
