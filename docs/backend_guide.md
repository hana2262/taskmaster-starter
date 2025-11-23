# 后端工程师核心素养指南（Taskmaster Starter）

说明
- 这是你作为后端初学者的单一持续更新文档。每次我们在项目中做新操作（如添加 CI、修改 Docker 配置、迁移数据库等），我会把要点追加到这里，保证所有知识都集中在一个地方，便于学习和复习。
- 文档面向初学者，尽量以实际操作结合概念解释，举例说明为什么以及常见坑。

目录（快速导航）
- 项目与工具概览
- 本地开发与 Docker
- 配置与环境变量（.env、Pydantic）
- 应用代码（FastAPI）基础
- 测试（pytest）与测试实践
- 持续集成（GitHub Actions）
- 日志与监控基础
- 数据库与迁移（概念与常用工具）
- 版本控制（Git）与协作流程
- 安全性基础（密钥、敏感信息、依赖）
- 常见问题与调试步骤
- 如何扩展本指南（添加条目）

一、项目与工具概览
- 这个仓库是一个 FastAPI + PostgreSQL + Redis 的后端模板，使用 Docker Compose 管理依赖（db/redis/web）。
- 关键工具：Python 3.11、FastAPI（web 框架）、Pydantic（配置与数据校验）、Uvicorn（ASGI 服务器）、pytest（测试）、docker / docker compose（容器化）、git / GitHub（版本控制与远程托管）。

二、本地开发与 Docker（为什么用容器）
- 为什么用 Docker：统一运行环境（依赖一致）、方便在 CI/其他机器重现、隔离服务（数据库、缓存）。
- Docker Compose：用于定义多个服务（web/db/redis）。常见操作：
  - 启动：docker compose up -d --build
  - 查看日志：docker compose logs --tail=200 web
  - 运行命令：docker compose exec web sh
- 开发提示：
  - 如果你想“代码修改立即生效”，可以在 compose 中添加 volume 把当前目录挂载进容器（例：./:/code），但需要注意容器内依赖已安装与权限问题。
  - 永久把 PYTHONPATH 设置到容器里可以避免运行测试时反复传环境变量。

三、配置与环境变量（.env、Pydantic）
- 为什么用 .env：把部署相关的配置（数据库 URL、secret keys）和代码分离，便于不同环境（dev/test/prod）使用不同配置。
- Pydantic 的 BaseSettings：用于从环境变量或 .env 文件加载配置。注意 pydantic v1 与 v2 的差异：
  - v1 使用 class Config 与 Field(..., env="...")。
  - v2 将 BaseSettings 移到 pydantic-settings，并引入 model_config，且 Field(..., env="...") 在 v2 被标记为弃用（仍可用但未来会移除）。
- 实践建议：在代码里适配 pydantic v1/v2（本项目示例已实现），并把敏感值放在 .env 或在生产中使用更安全的 secrets 管理器。

四、应用代码（FastAPI）基础
- 路由与视图：用装饰器 @app.get/post/... 定义端点；异步函数（async def）适合 I/O 密集的请求。
- 结构化建议：把业务代码按功能拆成模块（app/main.py、app/config.py、app/services、app/api、app/models）。
- 健康检查：实现 /healthz 用于容器/负载均衡器检测服务就绪情况。

五、测试（pytest）与测试实践
- 单元测试优先，集成测试次之。用 pytest 执行：pytest -q。
- 在容器中运行测试时，确保 PYTHONPATH 包含项目根（例如 PYTHONPATH=/code）。
- 把基础健康检查写成测试（tests/test_health.py），便能保证服务基础可用。
- CI 会在每次 push/PR 时运行测试，保证改动不破坏现有行为。

六、持续集成（GitHub Actions）
- CI 作用：自动化运行测试、静态检查（lint）、构建镜像。
- 简单 workflow 流程：checkout -> setup python -> pip install -> pytest。
- 在 CI 中注意：不要在 workflow 中硬编码秘密，使用 GitHub Secrets。

七、日志与监控基础
- 应用日志：在后端中用结构化日志（JSON 或包含时间戳、级别、请求 id）提高可读性与可关联性。
- 本地查看：docker compose logs -f web。
- 生产监控：接入 Prometheus / Grafana 或基于云的监控方案；设置健康检查与告警策略。

八、数据库与迁移（概念）
- 迁移工具：Alembic（SQLAlchemy）、Django migrations 等。迁移流程：修改模型 -> 生成迁移 -> 应用迁移（alembic revision --autogenerate、alembic upgrade head）。
- 在 CI/测试中：尽量为测试数据库使用临时数据库或 sqlite，以免破坏开发 DB。

九、版本控制（Git）与协作流程
- 提交粒度：小而单一的提交；message 使用语义化前缀（feat/chore/fix/test）。
- 分支策略：main 保持稳定；feature branch 开发新特性；PR 用于代码审查。
- 推送认证：推荐使用 SSH key 或 PAT；已经在本项目中配置过 SSH。

十、安全性基础
- 不要把秘密推到仓库（.env 应在 .gitignore），生产环境使用 secrets 管理器。
- 依赖安全：定期审查依赖并升级（pip-audit / Dependabot）。
- 密钥管理：为 GitHub 使用 fine-grained PAT 或 SSH，并妥善保管私钥。

十一、常见问题与调试
- 服务启动但 curl 连接失败：先看 docker compose ps，docker compose logs --tail=200 web，检查端口与网络。
- ModuleNotFoundError: 确认 PYTHONPATH 是否包含项目根，或确保包是可导入（目录名与 __init__.py）。
- Pydantic 错误：检查是否同时使用 class Config 与 model_config（两者互斥），并根据 pydantic 版本调整配置。

十二、如何扩展本指南（约定）
- 我会把每次我们做的新内容（例如添加 CI、改 Dockerfile、加入迁移脚本、调优日志）追加到本文件底部，带上小节标题与日期。  
- 如果你想把某段知识扩展成更细的教程（例如一个独立的“如何写 Alembic 迁移”章节），写下“扩展: Alembic”并我会把该条目展开成子章节。

最后，常用命令速查（复制粘贴）
- 启动：docker compose up -d --build
- 查看日志：docker compose logs --tail=200 web
- 进入容器：docker compose exec web sh
- 运行测试：docker compose run --rm -e PYTHONPATH=/code web pytest -q
- 提交：git add . && git commit -m "msg" && git push

日期：2025-11-23
作者：指导者（持续更新）
### 追加记录：持续集成（GitHub Actions）说明（2025-11-23）

场景：
- 我们为仓库添加了一个基本的 GitHub Actions workflow，用于在每次 push 或 pull request 到 main 分支时自动运行测试（pytest）。

为什么要做：
- CI 可以在每次提交/PR 时自动验证代码不会回归，保证主分支稳定，方便多人协作并且提前发现环境/依赖问题。

workflow 做了什么：
- checkout 源码
- 设置 Python 3.11
- 安装 requirements.txt 中列出的依赖
- 运行 pytest（简洁模式 -q）

注意事项与常见问题：
- 如果 workflow 在“Install dependencies”时报错，常见原因是 requirements.txt 中引用了私有包或临时网络问题。可以在 workflow 中添加依赖缓存或使用镜像源（中国大陆用户可考虑添加 pip 镜像）。
- 如果测试在 Actions 中失败，但本地通过：
  - 检查是否把 .env（或 secrets）依赖写入 workflow（不要把敏感值直接放在 workflow）。
  - 在 Actions 中使用 GitHub Secrets 配置必要的环境变量（Settings → Secrets）。
  - 在 workflow 增加更多调试输出（例如 pytest -q -k health 或 run tests with -v），或把失败时的 pytest 输出打印出来。

如何查看结果：
- 在仓库页面点击 Actions 标签页，打开最近一次 workflow 运行并查看日志。
- 可用 gh CLI 查看： gh run list / gh run view <run-id> --log

后续提升建议：
- 为依赖安装添加缓存（actions/cache）以加速构建。
- 在 workflow 中增加 lint（flake8/ruff）和类型检查（mypy）。
- 如果需要集成 DB/Redis 在 CI 做集成测试，扩展 jobs 使用 services（postgres、redis）并配置数据库 URL 供测试使用。
