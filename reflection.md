# Reflection — Lab 5: Static Code Analysis

### 1️⃣ Easiest vs Hardest Fixes
- **Easiest:** Replacing `eval()` and changing `logs=[]` to `logs=None`.
- **Hardest:** Adding input validation and exception handling without breaking existing logic.

### 2️⃣ False Positives
- Pylint reported missing docstrings; these are acceptable for a small lab file.
- No major false positives from Bandit or Flake8.

### 3️⃣ Integration into Workflow
- These tools can be integrated into **CI/CD** using GitHub Actions.
- Developers can also add **pre-commit hooks** to run `flake8` and `bandit` locally before pushing code.

### 4️⃣ Tangible Improvements
- Code readability improved with f-strings and logging.
- Safer file handling using `with` statements.
- Reduced runtime errors by adding input validation.
- Removed security risks (`eval`) and bad patterns (`bare except`).
