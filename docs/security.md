# 安全性基础

## 秘密管理

不要把秘密推到仓库（`.env` 应在 `.gitignore`），生产环境使用 secrets 管理器。

## 依赖安全

定期审查依赖并升级：
- `pip-audit`
- Dependabot

## 密钥管理

为 GitHub 使用 fine-grained PAT 或 SSH，并妥善保管私钥。

---

日期：2025-11-23  
作者：指导者（持续更新）
