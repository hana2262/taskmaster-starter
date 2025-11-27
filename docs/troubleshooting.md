# 常见问题与调试步骤

服务启动但无法访问
- 检查 docker compose ps、docker compose logs --tail=200 web、端口映射与网络。  
- ModuleNotFoundError：确认 PYTHONPATH 是否包含项目根或包已正确安装。  
- Pydantic 配置错误：确认是否混用 class Config 与 model_config，根据 pydantic 版本调整。

网络与 WSL 问题
- 若在 WSL 内遇到网络问题，尝试 `wsl --shutdown`、重启 Docker Desktop，或在 Windows 侧检查网络适配器与 VPN。
