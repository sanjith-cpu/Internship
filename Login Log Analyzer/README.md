# Login Log Analyzer

Build a Python program that reads a server login log and creates a short
security report. Aim to complete it in **60 to 90 minutes**.

Each log line looks like this:

```text
2026-08-28 09:10:15 FAILED user=admin ip=203.0.113.10
```

## Your task

Complete `analyze_log.py` so it:

1. Reads `sample_auth.log` one line at a time.
2. Counts total, successful, and failed login attempts.
3. Counts failed attempts for each IP address.
4. Flags an IP as suspicious when it has 3 or more failures.
5. Lists IP addresses in ascending order.
6. Writes the results to `report.txt`.

Do not hard-code totals or IP addresses. Calculate everything from the input
file.

Run the program from this folder:

```bash
python3 analyze_log.py
```

The report should show the three totals, failed attempts for each IP address,
and which IP addresses are suspicious. Check your answers against the log
yourself before submitting.

If you get stuck, look up:

- `for line in file`
- `line.strip().split()`
- `dictionary.get(key, 0)`
- `sorted(dictionary)`

Complete the work on a branch named `login-log-analyzer`. Commit it, push it,
open a pull request, address the review feedback, and merge it after approval.
