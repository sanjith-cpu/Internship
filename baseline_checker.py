from datetime import datetime
import hashlib
import os
import json

baseline_file = "baseline.json"
report_file = "report.json"
def get_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
def create_baseline():
    baseline = {}
    for file in os.listdir("."):
        if os.path.isfile(file) and file not in (baseline_file,report_file):
            baseline[file] = get_hash(file)

    with open(baseline_file, "w") as f:
        json.dump(baseline, f)

    print("Baseline file created")

def verify_integrity():
    with open(baseline_file, "r") as f:
        saved_baseline = json.load(f)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = [f"Report Check: {timestamp}"]
    any_changed = False

    for file, old_hash in saved_baseline.items():
        if not os.path.exists(file):
            report_lines.append(f"DELETED: {file}")
            any_changed = True
        elif get_hash(file) != old_hash:
            report_lines.append(f"CHANGED: {file}")
            any_changed = True

    for file in os.listdir("."):
        if (
            os.path.isfile(file)
            and file not in (baseline_file,report_file)
            and file not in saved_baseline
        ):
            report_lines.append(f"NEW: {file}")
            any_changed = True
    if not any_changed:
        report_lines.append(f"All files match previous baseline")

    report_content = "\n".join(report_lines)
    with open(report_file, "a") as f:
        f.write(report_content)
    print(report_content)

if __name__ == "__main__":
    if not os.path.exists(baseline_file):
        create_baseline()
    else:
        verify_integrity()