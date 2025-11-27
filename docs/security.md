# 安全性基础

不要把秘密推到仓库
- .env 应在 .gitignore 中；生产使用 Secrets 管理器（如 GitHub Secrets、云提供商的 Secret Manager）。

依赖安全
- 定期检查依赖（pip-audit、Dependabot）。避免在代码中硬编码凭证或密钥。

认证 & 授权 基础
- 密码哈希（bcrypt/argon2）、JWT 的使用与密钥管理、CORS 策略、输入验证。
