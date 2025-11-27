# 持续集成（GitHub Actions）

角色
- 自动在 PR 或 push 时运行测试、静态检查与构建镜像，确保主分支稳定。

简单 workflow 示例
- checkout -> setup python -> pip install -> pytest

注意
- 在 workflow 中使用 GitHub Secrets 管理敏感信息。  
- 可加入缓存（actions/cache）加速依赖安装；加入 lint（ruff/flake8）与类型检查（mypy）提高代码质量。

扩展
- 若需在 CI 做集成测试，可使用 services: postgres/redis 并在 job 中设置对应的数据库 URL。
