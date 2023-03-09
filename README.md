# pre-commit-text-find

For pre-commit: see https://github.com/pre-commit/pre-commit

Using pre-commit-text-find with pre-commit
Add this to your .pre-commit-config.yaml 🚀🚀

```yaml
- repo: https://github.com/mounirmesselmeni/pre-commit-text-find
  rev: "" # Use the sha / tag you want to point at
  hooks:
    - id: text-find
      args: ["--text", "unwanted-text1", "--text", "unwanted-text2"]
```
