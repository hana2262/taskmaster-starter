# Git & GitHub CLI (gh) 速查 / 使用说明

本文件面向初学者，总结了日常使用 Git 与 GitHub CLI (gh) 的常用命令、输出解析与常见问题排查。包含示例输出，便于将操作和实际终端反馈对应起来。

---

## 常用命令（逐条说明）

### git status --porcelain --branch
- 功能：简洁显示工作区状态（未跟踪、修改、已暂存等）并显示当前分支与上游分支信息。  
- 示例输出说明：
  - `## main...origin/main`：当前在 main，跟远端 main 比较。
  - 行前缀 ` M`：已跟踪文件有修改但未暂存到 index（staged）。
  - 前缀 `??`：未跟踪（untracked）文件或目录（未加入版本控制）。

### git add <file>
- 功能：把文件变更放入暂存区（staging area），准备提交。  
- 示例：
  - `git add README.md`：把 README.md 加入暂存区。

提示：想把当前目录下所有改动暂存可以用 `git add .`（谨慎使用，可能包含不想提交的改动）。

### git commit -m "msg"
- 功能：把暂存区的更改打包成一次本地提交（commit）。  
- 提示：提交信息应简洁并带语义前缀（例如 `docs:`, `feat:`, `fix:`），例如：
  - `git commit -m "docs: add README quickstart and usage (closes #1)"`  
  - 在提交信息里用 `closes #1` 会在 PR 合并时自动关闭 issue #1。

### git push -u origin <branch>
- 功能：把本地分支推送到远端仓库（origin），并用 `-u`（或 `--set-upstream`）把本地分支与远端分支关联（设置 upstream）。
- 含义拆解：
  - `origin`：远端仓库名（默认就是 GitHub 上的仓库）。
  - `<branch>`：要推送的分支名（例如 `docs/add-readme`）。
  - `-u`：建立上游关系，之后可直接用 `git push`/`git pull` 而不必每次指定远端与分支名。
- 典型 push 输出会告诉你：对象被传输、远端创建了新分支，与是否成功的提示（例如 `* [new branch] docs/add-readme -> docs/add-readme`），以及远端建议的 PR 创建 URL（git server 有时会提示）。

### gh pr create --title "..." --body "..." --base main
- 功能：使用 GitHub CLI 在远端为当前分支创建一个 Pull Request，目标分支由 `--base` 指定（一般为 main）。  
- 注意：
  - 运行前需 `gh auth login` 并确认 `gh auth status` 显示已登录。
  - `gh pr create` 会返回 PR 的 URL（例如 `https://github.com/.../pull/6`），也可能进入交互式模式让你确认或编辑正文。

---

## 示例（来自实际输出）
你运行 push 与 gh pr create 的终端输出（节选）：

```
[docs/add-readme 48c1080] docs: add README quickstart and usage (closes #1)
 1 file changed, 53 insertions(+), 11 deletions(-)

To github.com:hana2262/taskmaster-starter.git
 * [new branch]      docs/add-readme -> docs/add-readme
branch 'docs/add-readme' set up to track 'origin/docs/add-readme'.

Creating pull request for docs/add-readme into main in hana2262/taskmaster-starter

https://github.com/hana2262/taskmaster-starter/pull/6
```

---

## 常见问题与排查

1. Warning: uncommitted changes / Warning: N uncommitted changes
   - 含义：在执行 `gh pr create` 或其他操作时，检测到工作树还有未提交或未暂存的改变（包括 untracked）。
   - 解决：
     - 如果这些改动不想包含，可以 `git stash`（临时保存）或将改动移除/忽略。
     - 如果想保留但不提交，先 `git stash push -u -m "msg"` 可以同时 stash untracked 文件。之后用 `git stash pop` 恢复。

2. push 被拒绝（rejected）或需要合并冲突
   - 例因：远端分支有新提交但本地未合并。
   - 处理方式：
     - `git pull --rebase origin <branch>` 然后解决冲突，再 `git push`。
     - 或手动合并并提交后再 push。

3. 权限/认证失败（push 或 gh 报错）
   - 检查 `gh auth status` 是否已登录，或 `git remote -v` 上的 URL 使用的是你有权限的凭证（SSH/HTTPS）。
   - 若是 token 权限问题，重新生成 PAT（带 repo 权限）或用 `gh auth login` 重新登录。

4. 不想跟踪某些文件（例如 backups/）
   - 把路径加入 `.gitignore`：`echo "backups/" >> .gitignore`，然后 `git add .gitignore && git commit -m "chore: ignore backups/"`。
   - 若文件已被跟踪（已经 commit），需先 `git rm --cached <file>` 再更新 .gitignore 并提交。

---

## 好的实践建议
- 在创建 PR 之前保持工作树尽量干净（除非你确实想把当前改动都包含在一个 PR）。
- 使用小且清晰的 commit（每次改动关注一个主题），并使用语义化前缀（feat/fix/docs/chore）。
- 使用 `-u` 为新分支设置上游，之后日常推送可直接执行 `git push`。 
- 在 PR 描述中写明 “为什么” 做这件事，并可在合并信息中使用 `closes #<issue>` 来自动关联/关闭 issue。
- 学会用 `git stash` 临时保存工作进度，避免在新分支上包含不相关的改动。

---

## 练习题（建议）
1. 创建一个新分支 `feat/example`，在该分支创建一个文件 `EXAMPLE.md`，提交并把分支推到远端（包含设置上游），然后打开一个 PR。
2. 制造一个冲突：在远端修改 README，pull 时解决冲突并完成 push。
3. 使用 `gh pr create` 创建一个带有完整说明的 PR，并在 GitHub 网页端合并该 PR，观察 issue 自动关闭的行为（如果在提交或 PR body 中用了 `closes #<n>`）。

---

Author: guidance bot & user
Date: 2025-11-27
