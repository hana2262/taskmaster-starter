# 持续集成（GitHub Actions）

## CI 作用

自动化运行测试、静态检查（lint）、构建镜像。

## 简单 workflow 流程

1. checkout
2. setup python
3. pip install
4. pytest

## 注意事项

在 CI 中注意：不要在 workflow 中硬编码秘密，使用 GitHub Secrets。

---

## 追加记录：持续集成（GitHub Actions）说明（2025-11-23）

### 场景

我们为仓库添加了一个基本的 GitHub Actions workflow，用于在每次 push 或 pull request 到 main 分支时自动运行测试（pytest）。

### 为什么要做

CI 可以在每次提交/PR 时自动验证代码不会回归，保证主分支稳定，方便多人协作并且提前发现环境/依赖问题。

### workflow 做了什么

- checkout 源码
- 设置 Python 3.11
- 安装 requirements.txt 中列出的依赖
- 运行 pytest（简洁模式 -q）

### 注意事项与常见问题

- 如果 workflow 在"Install dependencies"时报错，常见原因是 requirements.txt 中引用了私有包或临时网络问题。可以在 workflow 中添加依赖缓存或使用镜像源（中国大陆用户可考虑添加 pip 镜像）。
- 如果测试在 Actions 中失败，但本地通过：
  - 检查是否把 .env（或 secrets）依赖写入 workflow（不要把敏感值直接放在 workflow）。
  - 在 Actions 中使用 GitHub Secrets 配置必要的环境变量（Settings → Secrets）。
  - 在 workflow 增加更多调试输出（例如 `pytest -q -k health` 或 run tests with `-v`），或把失败时的 pytest 输出打印出来。

### 如何查看结果

- 在仓库页面点击 Actions 标签页，打开最近一次 workflow 运行并查看日志。
- 可用 gh CLI 查看：`gh run list` / `gh run view <run-id> --log`

### 后续提升建议

- 为依赖安装添加缓存（actions/cache）以加速构建。
- 在 workflow 中增加 lint（flake8/ruff）和类型检查（mypy）。
- 如果需要集成 DB/Redis 在 CI 做集成测试，扩展 jobs 使用 services（postgres、redis）并配置数据库 URL 供测试使用。

---

日期：2025-11-23  
作者：指导者（持续更新）
