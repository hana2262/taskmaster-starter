# 版本控制（Git）与协作流程

提交与分支
- 提交粒度小且单一责任。使用语义前缀（feat/fix/chore/docs/test）。  
- 分支策略：main 保持稳定，feature branch 做开发，PR 用于代码审查。

Pr 实践
- PR 描述包含“为什么”与“做了什么”，尽量关联对应 issue。PR 合并前确保 CI 通过。
