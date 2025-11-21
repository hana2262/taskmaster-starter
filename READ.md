```markdown
# TaskMaster (starter)

这是一个后端工程练习的最小骨架（FastAPI）。供学习后端基础设施：项目结构、配置、Docker Compose、基础测试与 CI。

## 要点
- FastAPI 应用，包含 /healthz 路由
- Docker Compose：postgres + redis + web（app）
- 配置通过环境变量（pydantic BaseSettings）
- 基本日志初始化
- pytest 单测（tests/test_health.py）
- GitHub Actions CI 示例（运行 pytest）

## 本地快速启动（开发模式）
1. 克隆仓库并进入目录
2. 复制环境文件：
   cp .env.example .env
   然后根据需要修改 .env
3. 使用 Docker Compose（推荐）：
   docker-compose up --build
   访问 http://localhost:8000/docs 或 http://localhost:8000/healthz

或者在本地（无需 docker）：
1. 建虚拟环境并激活
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   .\venv\Scripts\activate   # Windows
2. 安装依赖
   pip install -r requirements.txt
3. 启动
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## 运行测试
pytest

## CI
已包含 .github/workflows/ci.yml，会在 PR/Push 时运行 pytest。

## 接下来（Week1 目标）
- 在 GitHub 建仓并启用 Issues / Projects
- 提交这个骨架为第一版（PR）
- 本地跑通 docker-compose 与 pytest，并把执行结果贴给我（出现错误我来帮你排）
```