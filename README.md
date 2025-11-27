# Taskmaster Starter

一个用于学习和练手的 FastAPI 后端模板，包含常用后端开发要素：配置管理（Pydantic）、测试（pytest）、容器化（Docker / docker-compose）、CI（GitHub Actions）、以及示例健康检查端点。

## 快速开始

先确保你已安装：Docker Desktop（含 WSL2 支持）或本地 Python 3.11 + virtualenv。

1. 克隆仓库
   git clone git@github.com:hana2262/taskmaster-starter.git
   cd taskmaster-starter

2. 使用 Docker（推荐）
   docker compose up -d --build
   # 启动后查看 web 日志
   docker compose logs --tail=200 -f web

3. 直接在本地运行（若不使用容器）
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   export PYTHONPATH=$(pwd)
   uvicorn app.main:app --reload --port 8000

4. 健康检查
   curl -sS http://localhost:8000/health | jq .

## 配置
- 使用 `.env`（已在 `.gitignore` 中排除）与 `app/config.py` 中的 `Settings`。项目已提供 `app/config.py`，在模块末尾实例化了 `settings = Settings()`，方便全局 import：
  from app.config import settings

## 运行测试
- 在容器里运行：
  docker compose run --rm -e PYTHONPATH=/code web pytest -q
- 或在本地 venv 中：
  pytest -q

## 开发工作流（建议）
- 小步提交、小 PR（feat/fix/chore 前缀）
- PR 必须通过 CI（测试通过）与至少一次自我审查
- 用 issues 与 Project board 管理短期目标（Week1 / Week2）

## 常用命令速查
- 启动： docker compose up -d --build
- 查看日志： docker compose logs --tail=200 web
- 运行测试： docker compose run --rm -e PYTHONPATH=/code web pytest -q
- 提交： git add . && git commit -m "msg" && git push

## 贡献
- 请 fork -> branch -> PR。每个 PR 描述“为什么改”和“改了什么”，关联对应 issue（如适用）。

## 文档
- docs/backend_guide.md & docs/* — 后端工程师核心素养指南（持续更新）

---
作者/维护：你与协助者（持续更新）
