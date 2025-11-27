# 数据库与迁移

## 迁移工具

常用工具包括 Alembic（SQLAlchemy）、Django migrations 等。

## 迁移流程

1. 修改模型
2. 生成迁移：`alembic revision --autogenerate`
3. 应用迁移：`alembic upgrade head`

## 在 CI/测试中

尽量为测试数据库使用临时数据库或 sqlite，以免破坏开发 DB。

---

日期：2025-11-23  
作者：指导者（持续更新）
