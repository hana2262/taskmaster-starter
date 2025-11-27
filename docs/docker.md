# 本地开发与 Docker

## 为什么用 Docker

- 统一运行环境（依赖一致）
- 方便在 CI/其他机器重现
- 隔离服务（数据库、缓存）

## Docker Compose

用于定义多个服务（web/db/redis）。

### 常见操作

- **启动**：`docker compose up -d --build`
- **查看日志**：`docker compose logs --tail=200 web`
- **运行命令**：`docker compose exec web sh`

## 开发提示

- 如果你想"代码修改立即生效"，可以在 compose 中添加 volume 把当前目录挂载进容器（例：`./:/code`），但需要注意容器内依赖已安装与权限问题。
- 永久把 PYTHONPATH 设置到容器里可以避免运行测试时反复传环境变量。

## 追加记录：在 docker-compose.yml 中设置 PYTHONPATH（2025-11-23）

我们在 docker-compose.yml 的 web 服务下添加了 `environment: - PYTHONPATH=/code`，使容器内的 Python 解释器在运行时能够默认把 `/code`（项目根）加入模块搜索路径。

### 目的

- 避免每次在容器中运行测试或脚本时都要手动传递 PYTHONPATH 环境变量（例如 `docker compose run --rm -e PYTHONPATH=/code ...`）。
- 保证容器运行环境与 CI 中的一致性，减少因导入路径导致的问题。

### 注意事项

- 这个改动只会设置环境变量，不会影响镜像内已安装包或 bind-mount 的行为。
- 若启用 volumes 挂载（把宿主目录挂入容器），需要注意宿主与容器的文件覆盖和权限问题（这在本次改动中未启用）。
- 在后续任务中我们可能会把 volumes 加入以实现即时重载（dev 模式），但那需要额外调整 Dockerfile 与权限策略。

### 相关命令

- 备份：`cp docker-compose.yml docker-compose.yml.bak`
- 校验：`docker compose config`
- 重启：`docker compose up -d --build`

---

日期：2025-11-23  
作者：指导者（持续更新）
