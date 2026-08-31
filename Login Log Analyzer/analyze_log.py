INPUT_FILE = "sample_auth.log"
OUTPUT_FILE = "report.txt"
SUSPICIOUS_THRESHOLD = 3

# TODO 1: Create counters for total, successful, and failed login attempts.
total_logins = 0
successful_logins = 0
failed_logins = 0
# TODO 2: Create an empty dictionary for failed-login counts by IP address.
failed_counts_by_ip = {}
# TODO 3: Open INPUT_FILE for reading and process it one line at a time.
# Each line can be separated into pieces with line.strip().split().
try:
    with open(INPUT_FILE, 'r', encoding="utf-8") as file:
        for line in file:
            line_parts = line.strip().split()
# TODO 4: Update the correct counters for SUCCESS and FAILED lines.
            total_logins += 1
            status_parts = line_parts[2].split()
            if "SUCCESS" in line_parts:
                successful_logins += 1
            elif "FAILED" in line_parts:
                failed_logins += 1
# TODO 5: For each FAILED line, extract the IP address and update its value in
# the dictionary. A useful counting pattern is:
# counts[key] = counts.get(key, 0) + 1
            raw_ip_part = next((p for p in line_parts if p.startswith("ip=")), None)
            if raw_ip_part:
                try:
                    clean_ip_value = raw_ip_part.replace('"', '').split('=')[1].strip()
                    failed_counts_by_ip[clean_ip_value] = failed_counts_by_ip.get(clean_ip_value, 0) + 1
                except IndexError:
                    print(f"Warning: Line format incorrect, failed to parse IP key/value: {raw_ip_part}")
            else:
                pass
except FileNotFoundError:
    print(f"Warning: File not found: {INPUT_FILE}")
    import sys
    sys.exit(1)
except Exception as e:
    print(f"Warning: {e}")
    import sys
    sys.exit(1)
# TODO 6: Open OUTPUT_FILE for writing and include the totals, failed attempts
# by IP, and suspicious IPs. Use sorted(...) when looping through IP addresses.
print("----Generating Report...----")
try:
    with open(OUTPUT_FILE, 'w', encoding="utf-8") as report_file:
        report_file.write(f"Total logins: {total_logins}\n")
        report_file.write(f"Successful logins: {successful_logins}\n")
        report_file.write(f"Failed logins: {failed_logins}\n\n")
        report_file.write("---Failed Attempts by IP address (Sorted)---\n")
        sorted_ips = sorted(failed_counts_by_ip.keys())
        for ip in sorted_ips:
            count = failed_counts_by_ip[ip]
            report_file.write(f"{ip}: {count} failed attempt(s)\n")
        report_file.write("\n")
# TODO 7: Include only IP addresses whose failed count is greater than or equal
# to SUSPICIOUS_THRESHOLD in the suspicious section.
        report_file.write(f"---Suspicious Activity (Failure Count >= {SUSPICIOUS_THRESHOLD})---\n")
        suspicious_found = False
        for ip in sorted_ips:
            count = failed_counts_by_ip[ip]
            if count>= SUSPICIOUS_THRESHOLD:
                suspicious_found = True
                report_file.write(f"SUSPICIOUS: {ip}: {count} failed attempt(s)\n")
        if not suspicious_found:
            report_file.write("No suspicious IP address found\n")
    print(f"Report successfully written to {OUTPUT_FILE}")
except Exception as e:
    print(f"Warning: {e}")
print("----Finished----")