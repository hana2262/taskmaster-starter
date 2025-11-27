# 本地开发与 Docker

为什么用 Docker
- 统一环境、便于 CI 重现、隔离依赖（数据库、缓存）。

常见操作
- 启动：docker compose up -d --build
- 日志：docker compose logs --tail=200 web
- 运行命令：docker compose exec web sh
- 在容器里运行测试：docker compose run --rm -e PYTHONPATH=/code web pytest -q

开发提示
- 若要即时生效代码改动，可在 compose 添加 volume（如 ./:/code），但注意依赖与权限。  
- 推荐在 docker-compose.yml 中为 web 服务设置 PYTHONPATH=/code，避免每次运行都传 env。
