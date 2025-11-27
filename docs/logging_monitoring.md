# 日志与监控基础

应用日志
- 使用结构化日志（时间戳、级别、request id）便于聚合与检索。  
- 在本地可用 docker compose logs 来观察输出。

监控
- 生产环境可接入 Prometheus/Grafana 或云监控方案。设置健康检查与告警策略以便及时发现问题。
