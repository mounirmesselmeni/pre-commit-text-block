# pre-commit-textfind

For pre-commit: see https://github.com/pre-commit/pre-commit

Using pre-commit-textfind with pre-commit
Add this to your .pre-commit-config.yaml 🚀🚀

```yaml
- repo: https://github.com/mounirmesselmeni/pre-commit-textfind
  rev: "0.1.0"
  hooks:
    - id: textfind
      args: ["--text", "unwanted-text1", "--text", "unwanted-text2"]
```
