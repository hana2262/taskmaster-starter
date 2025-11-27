# 配置与环境变量（.env、Pydantic）

目标
- 把运行时配置与代码分离，支持不同环境（dev/test/prod）。

Pydantic 与配置
- v1: 使用 BaseSettings 与 class Config。  
- v2: 使用 pydantic-settings 与 model_config。两者在项目中都可兼容，代码中应有适配逻辑（本仓库示例已实现）。  
- 推荐在模块末尾提供 `settings = Settings()`，方便 `from app.config import settings` 全局使用。

实践建议
- 将敏感值放在 .env 或 production secrets 管理器，不要直接写在 repo 中。  
- 在 CI 中使用 GitHub Secrets 提供所需敏感配置（不要硬编码在 workflow 中）。
