# 数据库与迁移（概念）

迁移工具
- 常见工具：Alembic（SQLAlchemy）、Django migrations 等。流程：修改模型 -> 生成迁移 -> 应用迁移（alembic revision --autogenerate -> alembic upgrade head）。

测试数据库
- 在 CI/测试中使用临时数据库（或 sqlite）以免影响开发 DB。可以在测试 job 中启动 postgres service 并把 DATABASE_URL 指向它。
