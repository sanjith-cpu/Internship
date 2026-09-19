INPUT_FILE = "sample_auth.log"
OUTPUT_FILE = "report.txt"
SUSPICIOUS_THRESHOLD = 3

# TODO 1: Create counters for total, successful, and failed login attempts.

# TODO 2: Create an empty dictionary for failed-login counts by IP address.

# TODO 3: Open INPUT_FILE for reading and process it one line at a time.
# Each line can be separated into pieces with line.strip().split().

# TODO 4: Update the correct counters for SUCCESS and FAILED lines.

# TODO 5: For each FAILED line, extract the IP address and update its value in
# the dictionary. A useful counting pattern is:
# counts[key] = counts.get(key, 0) + 1

# TODO 6: Open OUTPUT_FILE for writing and include the totals, failed attempts
# by IP, and suspicious IPs. Use sorted(...) when looping through IP addresses.

# TODO 7: Include only IP addresses whose failed count is greater than or equal
# to SUSPICIOUS_THRESHOLD in the suspicious section.
