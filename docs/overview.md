# 项目与工具概览

- 本仓库是一个 FastAPI + PostgreSQL + Redis 的后端模板，使用 Docker Compose 管理依赖（db / redis / web）。  
- 关键工具：Python 3.11、FastAPI、Pydantic、Uvicorn、pytest、docker / docker-compose、git / GitHub。

用途与建议
- 用作学习与练手的项目模板，便于在短时间内建立后端常见能力（配置、测试、容器化、CI）。  
- 在每次做关键变更（如加入 CI、改 Dockerfile、添加迁移），请把要点写到相应 docs 子文件中并提交 PR。

常见命令示例
- 启动：docker compose up -d --build
- 查看日志：docker compose logs --tail=200 web
- 进入容器：docker compose exec web sh
