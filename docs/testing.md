# 测试（pytest）与测试实践

测试优先级
- 单元测试为主，集成测试次之。使用 pytest 执行： pytest -q。

在容器中运行测试
- docker compose run --rm -e PYTHONPATH=/code web pytest -q

测试建议
- 为关键路由和基础能力（如健康检查）写测试。  
- 在 CI 上确保所有 PR 都运行测试，避免回归。

调试测试失败
- 比较本地与 CI 的环境差异（环境变量、DB、依赖版本）。使用 `pytest -k <name>` 定位问题。
