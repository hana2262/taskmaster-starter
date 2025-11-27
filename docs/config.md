# 配置与环境变量（.env、Pydantic）

## 为什么用 .env

把部署相关的配置（数据库 URL、secret keys）和代码分离，便于不同环境（dev/test/prod）使用不同配置。

## Pydantic 的 BaseSettings

用于从环境变量或 .env 文件加载配置。注意 pydantic v1 与 v2 的差异：

- **v1** 使用 `class Config` 与 `Field(..., env="...")`。
- **v2** 将 `BaseSettings` 移到 `pydantic-settings`，并引入 `model_config`，且 `Field(..., env="...")` 在 v2 被标记为弃用（仍可用但未来会移除）。

## 实践建议

在代码里适配 pydantic v1/v2（本项目示例已实现），并把敏感值放在 `.env` 或在生产中使用更安全的 secrets 管理器。

---

日期：2025-11-23  
作者：指导者（持续更新）
