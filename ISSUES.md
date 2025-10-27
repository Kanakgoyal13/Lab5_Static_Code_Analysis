# Lab 5 — Static Code Analysis  
### Identified and Fixed Issues

| Tool    | Severity | Line(s) | Issue ID / Description | Fix Implemented | Status |
|----------|-----------|---------|------------------------|------------------|--------|
| **Pylint** | High | 8 | `W0102`: Mutable default argument `logs=[]` | Changed to `logs=None` and initialized inside function | ✅ Fixed |
| **Bandit** | High | 63 | `B307`: Insecure use of `eval()` | Removed `eval()` and replaced with safe print message | ✅ Fixed |
| **Flake8 / Pylint** | Medium | 21–24 | `E722` / `W0702`: Bare except | Added specific exceptions `(KeyError, TypeError, ValueError)` and logging | ✅ Fixed |
| **Pylint** | Medium | 30–37 | `R1732`: File not closed | Used `with open(...) as f:` context manager | ✅ Fixed |
| **Pylint** | Medium | 26 | KeyError risk in `getQty` | Used `stock_data.get(item, 0)` instead of direct indexing | ✅ Fixed |
| **Pylint** | Low | 63 | Missing main guard | Added `if __name__ == "__main__": main()` | ✅ Fixed |
