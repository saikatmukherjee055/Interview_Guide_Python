# Unix Practice Lab: `grep`, `awk`, `find`, and Unix Utilities

This lab contains a realistic directory tree and **120 tested exercises with solutions**:

- Problems 1–30: `grep`
- Problems 31–60: `awk`
- Problems 61–90: `find`
- Problems 91–120: Unix text/file utilities, including `sort`, `uniq`, `cut`, `tr`, `paste`, `join`, `comm`, `sed`, `tee`, `xargs`, `nl`, `tac`, `rev`, `cksum`, `cmp`, `diff`, and `du`

## Environment

The commands were validated with Bash and GNU utilities on Linux. BSD/macOS versions of `grep`, `find`, `sed`, and other commands can have option differences, especially GNU `find -printf` and `find -xtype`.

## Start the lab

```bash
cd unix_practice_lab
./reset_metadata.sh
```

Run all commands from the `unix_practice_lab` directory unless a problem says otherwise.

## Safety

The exercises are non-destructive. Commands that create output write only inside `workspace/`. The supplied sample credentials and keys are fictional.

## Important files

| Path | Format | Purpose |
|---|---|---|
| `data/employees.csv` | CSV | Employee filtering, grouping, salary calculations |
| `data/sales.csv` | CSV | Revenue, region, product, and transaction analysis |
| `data/students.csv` | CSV | Averages, pass/fail, ranking, grouping |
| `data/inventory.tsv` | TSV | Tab-separated inventory analysis |
| `data/users.txt` | Colon-separated | Passwd-style field processing |
| `data/web_access.log` | Log | IP, HTTP method, status, and byte analysis |
| `data/app.log` | Log | Log-level searching and counting |
| `data/auth.log` | Log | Authentication and failed-login analysis |
| `projects/` | Mixed source tree | Recursive search and filesystem exercises |
| `logs/` | Dated logs | `find`, `grep`, timestamps, and `-exec` |
| `backups/` | Various sizes | Size-based `find` exercises |
| `permissions/` | Varied modes | Permission searches |
| `mixed/` | Unusual names | Spaces, uppercase extension, leading dash, broken link |
| `temp/` | Empty/duplicate/cache files | Empty-file, checksum, and permission practice |

## Directory map

```text
unix_practice_lab/
├── data/
│   ├── employees.csv
│   ├── sales.csv
│   ├── students.csv
│   ├── inventory.tsv
│   ├── users.txt
│   ├── web_access.log
│   ├── app.log
│   ├── auth.log
│   └── supporting word/list files
├── logs/
│   ├── 2025/december/
│   └── 2026/{january,february}/
├── projects/
│   ├── alpha/{src,tests,docs}/
│   ├── beta/{src,config}/
│   ├── gamma/docs/
│   └── archive/
├── backups/{daily,weekly}/
├── permissions/{scripts,private}/
├── mixed/
├── temp/{cache,empty}/
├── reports/
├── workspace/
├── FILE_INDEX.txt
└── reset_metadata.sh
```

---


# Grep Practice

## 1. Find all ERROR lines

**Problem:** Display every line containing `ERROR` in the application log.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep 'ERROR' data/app.log
```

**How it works:** `grep` prints lines containing the given pattern. Matching is case-sensitive by default.

**Expected output:**

```text
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
```

</details>

## 2. Case-insensitive INFO search

**Problem:** Display lines containing `info`, regardless of letter case.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -i 'info' data/app.log
```

**How it works:** `-i` makes the match case-insensitive, so `INFO`, `Info`, and `info` are treated alike.

**Expected output:**

```text
2026-01-10 09:00:01 INFO  app started version=2.4.1
2026-01-10 09:06:19 INFO  user login user=alice
2026-01-10 09:09:40 INFO  order completed order=ORD-1008
2026-01-10 09:12:02 INFO  graceful shutdown initiated
```

</details>

## 3. Show line numbers

**Problem:** Find `WARN` lines and include their line numbers.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -n 'WARN' data/app.log
```

**How it works:** `-n` prefixes every matching line with its input line number.

**Expected output:**

```text
3:2026-01-10 09:03:44 WARN  cache miss rate high value=0.73
7:2026-01-10 09:08:11 WARN  retrying request attempt=2
```

</details>

## 4. Match several log levels

**Problem:** Display lines containing either `ERROR` or `FATAL`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -E 'ERROR|FATAL' data/app.log
```

**How it works:** `-E` enables extended regular expressions, where `|` means OR.

**Expected output:**

```text
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
2026-01-10 09:11:22 FATAL disk unavailable mount=/data
```

</details>

## 5. Count failed logins

**Problem:** Count lines containing `Failed password` in the authentication log.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -c 'Failed password' data/auth.log
```

**How it works:** `-c` prints the number of matching lines instead of the lines themselves.

**Expected output:**

```text
3
```

</details>

## 6. Exclude INFO lines

**Problem:** Display application-log lines that do not contain `INFO`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -v 'INFO' data/app.log
```

**How it works:** `-v` inverts the match and prints nonmatching lines.

**Expected output:**

```text
2026-01-10 09:01:13 DEBUG database connection pool initialized size=10
2026-01-10 09:03:44 WARN  cache miss rate high value=0.73
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
2026-01-10 09:08:11 WARN  retrying request attempt=2
2026-01-10 09:11:22 FATAL disk unavailable mount=/data
```

</details>

## 7. Match a whole word

**Problem:** Find occurrences of the whole word `root` in the authentication log.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -w 'root' data/auth.log
```

**How it works:** `-w` requires word boundaries, avoiding matches where the pattern is only part of a longer word.

**Expected output:**

```text
Jan 10 08:04:44 server sudo: alice : TTY=pts/0 ; PWD=/home/alice ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx
Jan 10 08:09:33 server sshd[144]: Failed password for root from 203.0.113.7 port 60213 ssh2
Jan 10 08:12:21 server sshd[155]: Connection closed by authenticating user root 203.0.113.7 port 60213
```

</details>

## 8. Match a line prefix

**Problem:** Display access-log requests coming from IP address `192.168.1.10`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep '^192\.168\.1\.10 ' data/web_access.log
```

**How it works:** `^` anchors the pattern to the beginning of a line. Dots are escaped so they mean literal dots.

**Expected output:**

```text
192.168.1.10 - - [10/Jan/2026:09:15:21 +0530] "GET /index.html HTTP/1.1" 200 1024
192.168.1.10 - - [10/Jan/2026:09:18:11 +0530] "GET /images/logo.png HTTP/1.1" 304 0
192.168.1.10 - - [10/Jan/2026:09:35:18 +0530] "GET /download/report.pdf HTTP/1.1" 200 8192
```

</details>

## 9. Find HTTP 4xx responses

**Problem:** Display access-log lines whose response status is in the 400–499 range.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -E '" 4[0-9]{2} ' data/web_access.log
```

**How it works:** `4[0-9]{2}` matches a 4 followed by exactly two digits.

**Expected output:**

```text
192.168.1.11 - - [10/Jan/2026:09:16:03 +0530] "POST /login HTTP/1.1" 401 512
10.0.0.8 - - [10/Jan/2026:09:19:07 +0530] "GET /admin HTTP/1.1" 403 256
192.168.1.13 - - [10/Jan/2026:09:26:39 +0530] "GET /contact HTTP/1.1" 404 333
10.0.0.8 - - [10/Jan/2026:09:31:10 +0530] "DELETE /api/users/7 HTTP/1.1" 403 210
```

</details>

## 10. Find GET or POST requests

**Problem:** Display requests whose HTTP method is either GET or POST.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -E '"(GET|POST) ' data/web_access.log
```

**How it works:** Parentheses group alternatives, and `|` selects GET or POST.

**Expected output:**

```text
192.168.1.10 - - [10/Jan/2026:09:15:21 +0530] "GET /index.html HTTP/1.1" 200 1024
192.168.1.11 - - [10/Jan/2026:09:16:03 +0530] "POST /login HTTP/1.1" 401 512
10.0.0.5 - - [10/Jan/2026:09:17:44 +0530] "GET /products HTTP/1.1" 200 4096
192.168.1.10 - - [10/Jan/2026:09:18:11 +0530] "GET /images/logo.png HTTP/1.1" 304 0
10.0.0.8 - - [10/Jan/2026:09:19:07 +0530] "GET /admin HTTP/1.1" 403 256
172.16.0.3 - - [10/Jan/2026:09:20:33 +0530] "GET /api/users HTTP/1.1" 500 128
192.168.1.12 - - [10/Jan/2026:09:22:01 +0530] "GET /index.html HTTP/1.1" 200 1024
10.0.0.5 - - [10/Jan/2026:09:23:45 +0530] "POST /cart HTTP/1.1" 201 768
172.16.0.3 - - [10/Jan/2026:09:25:14 +0530] "GET /api/orders HTTP/1.1" 502 140
192.168.1.13 - - [10/Jan/2026:09:26:39 +0530] "GET /contact HTTP/1.1" 404 333
10.0.0.9 - - [10/Jan/2026:09:28:02 +0530] "GET /products/42 HTTP/1.1" 200 2048
192.168.1.11 - - [10/Jan/2026:09:30:27 +0530] "POST /login HTTP/1.1" 200 600
... (output truncated in workbook)
```

</details>

## 11. Search recursively for TODO or FIXME

**Problem:** Search the entire `projects` tree for unfinished-work markers.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -RInE 'TODO|FIXME' projects
```

**How it works:** `-R` searches recursively, `-I` skips binary data, `-n` shows line numbers, and `-E` supports alternation.

**Expected output:**

```text
projects/alpha/docs/README.md:3:TODO: add installation instructions.
projects/gamma/docs/guide.md:3:FIXME: document backup process.
projects/latest/docs/README.md:3:TODO: add installation instructions.
```

</details>

## 12. List files containing ERROR

**Problem:** Print only the names of log files that contain `ERROR`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -rl 'ERROR' logs
```

**How it works:** `-r` searches recursively and `-l` prints each matching filename once.

**Expected output:**

```text
logs/2026/january/server1.log
logs/2026/january/server2.log
logs/2026/february/server1.log
logs/2025/december/old.log
```

</details>

## 13. List files without ERROR

**Problem:** Print names of log files that contain no `ERROR` line.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -rL 'ERROR' logs
```

**How it works:** `-L` is the opposite of `-l`: it lists files with no match.

**Expected output:**

```text
logs/2026/february/debug.log
```

</details>

## 14. Match an entire line

**Problem:** Find lines in `words.txt` that are exactly lowercase `apple`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -x 'apple' data/words.txt
```

**How it works:** `-x` requires the entire line to match the pattern.

**Expected output:**

```text
apple
apple
```

</details>

## 15. Count apple ignoring case

**Problem:** Count lines equal to or containing `apple` regardless of case.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -ic 'apple' data/words.txt
```

**How it works:** Combining `-i` and `-c` performs case-insensitive matching and returns a count.

**Expected output:**

```text
3
```

</details>

## 16. Names starting with A or R

**Problem:** Display names beginning with uppercase A or R.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -E '^[AR]' data/names.txt
```

**How it works:** `^[AR]` means the first character must be either A or R.

**Expected output:**

```text
Aarav
Ananya
Arjun
Riya
Rohan
```

</details>

## 17. Engineering employees

**Problem:** Display employee records belonging to Engineering.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep ',Engineering,' data/employees.csv
```

**How it works:** Including commas around the value targets the complete CSV field more precisely.

**Expected output:**

```text
101,Aarav Sharma,Engineering,Senior Developer,95000,Delhi,2020-03-15,active
104,Meera Iyer,Engineering,Data Engineer,88000,Bengaluru,2021-06-21,active
107,Vikram Rao,Engineering,DevOps Engineer,92000,Hyderabad,2020-09-18,active
111,Neel Joshi,Engineering,Junior Developer,52000,Pune,2024-01-08,active
115,Aditya Kulkarni,Engineering,QA Engineer,69000,Pune,2021-03-03,active
118,Riya Chatterjee,Engineering,Data Scientist,105000,Kolkata,2020-02-20,active
```

</details>

## 18. Inactive employees

**Problem:** Display employee records whose final CSV field is `inactive`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep ',inactive$' data/employees.csv
```

**How it works:** `$` anchors the match to the end of the line.

**Expected output:**

```text
105,Kabir Khan,Finance,Accountant,65000,Delhi,2018-11-30,inactive
114,Tania Roy,HR,Recruiter,56000,Kolkata,2022-05-16,inactive
```

</details>

## 19. Show context around FATAL

**Problem:** Display the FATAL line together with one line before and one line after it.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -B 1 -A 1 'FATAL' data/app.log
```

**How it works:** `-B 1` adds one line before each match and `-A 1` adds one line after.

**Expected output:**

```text
2026-01-10 09:09:40 INFO  order completed order=ORD-1008
2026-01-10 09:11:22 FATAL disk unavailable mount=/data
2026-01-10 09:12:02 INFO  graceful shutdown initiated
```

</details>

## 20. Extract only IP addresses

**Problem:** Extract every IPv4-like address from the access log.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' data/web_access.log
```

**How it works:** `-o` prints only the matched text. The expression matches four dot-separated numeric groups.

**Expected output:**

```text
192.168.1.10
192.168.1.11
10.0.0.5
192.168.1.10
10.0.0.8
172.16.0.3
192.168.1.12
10.0.0.5
172.16.0.3
192.168.1.13
10.0.0.9
192.168.1.11
... (output truncated in workbook)
```

</details>

## 21. Count requests per IP

**Problem:** Create a frequency table showing how many requests each IP sent.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -oE '^([0-9]{1,3}\.){3}[0-9]{1,3}' data/web_access.log | sort | uniq -c | sort -nr
```

**How it works:** The first command extracts IPs; sorting groups equal values; `uniq -c` counts them; the final sort ranks them.

**Expected output:**

```text
      3 192.168.1.10
      2 192.168.1.11
      2 172.16.0.3
      2 10.0.0.8
      2 10.0.0.5
      1 192.168.1.13
      1 192.168.1.12
      1 172.16.0.4
      1 10.0.0.9
```

</details>

## 22. Extract key=value pairs

**Problem:** Extract all `name=value` fragments from the application log.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -oE '[A-Za-z_]+=[^ ]+' data/app.log
```

**How it works:** This pattern matches a key made of letters or underscores, `=`, and a non-space value.

**Expected output:**

```text
version=2.4.1
size=10
value=0.73
order=ORD-1008
user=alice
transaction=TX-77
attempt=2
order=ORD-1008
mount=/data
```

</details>

## 23. Locate blank lines

**Problem:** Show the line numbers of blank lines in `multiline.txt`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -n '^$' mixed/multiline.txt
```

**How it works:** `^$` matches a line with nothing between its beginning and end.

**Expected output:**

```text
2:
4:
```

</details>

## 24. Remove blank lines

**Problem:** Display only nonblank lines from `multiline.txt`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -v '^$' mixed/multiline.txt
```

**How it works:** Inverting the blank-line pattern removes empty lines from the displayed output.

**Expected output:**

```text
first line
third line
fifth line
```

</details>

## 25. Search selected file extensions

**Problem:** Search only Markdown files for TODO or FIXME markers.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -RInE --include='*.md' 'TODO|FIXME' projects
```

**How it works:** `--include` limits recursive searching to names matching `*.md`.

**Expected output:**

```text
projects/alpha/docs/README.md:3:TODO: add installation instructions.
projects/gamma/docs/guide.md:3:FIXME: document backup process.
projects/latest/docs/README.md:3:TODO: add installation instructions.
```

</details>

## 26. Exclude an archive directory

**Problem:** Search Python files for `print` but skip `projects/archive`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -RIn --include='*.py' --exclude-dir='archive' 'print' projects
```

**How it works:** `--exclude-dir` prevents descent into matching directories.

**Expected output:**

```text
projects/alpha/src/main.py:8:    print(greet(sys.argv[1] if len(sys.argv) > 1 else "World"))
projects/latest/src/main.py:8:    print(greet(sys.argv[1] if len(sys.argv) > 1 else "World"))
```

</details>

## 27. Use a fixed-string search

**Problem:** Search literally for `division by zero` in the project tree.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -RFn 'division by zero' projects
```

**How it works:** `-F` treats the pattern as plain text rather than a regular expression.

**Expected output:**

```text
projects/alpha/src/utils.py:6:        raise ValueError("division by zero")
projects/latest/src/utils.py:6:        raise ValueError("division by zero")
```

</details>

## 28. Match an exact configuration line

**Problem:** Find a line that is exactly `DEBUG=false`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -x 'DEBUG=false' projects/beta/config/app.conf
```

**How it works:** `-x` prevents partial-line matches and is useful for exact configuration values.

**Expected output:**

```text
DEBUG=false
```

</details>

## 29. Find server-error requests

**Problem:** Display web requests that returned an HTTP 5xx status.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -E '" 5[0-9]{2} ' data/web_access.log
```

**How it works:** The expression targets status codes from 500 through 599.

**Expected output:**

```text
172.16.0.3 - - [10/Jan/2026:09:20:33 +0530] "GET /api/users HTTP/1.1" 500 128
172.16.0.3 - - [10/Jan/2026:09:25:14 +0530] "GET /api/orders HTTP/1.1" 502 140
```

</details>

## 30. Extract error and fatal messages

**Problem:** Print only the message text after `ERROR` or `FATAL` in `app.log`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -E ' (ERROR|FATAL) ' data/app.log | sed -E 's/^.* (ERROR|FATAL) +//'
```

**How it works:** `grep` selects severe log entries; `sed` removes the timestamp and level prefix, leaving the message.

**Expected output:**

```text
payment service timeout order=ORD-1008
database deadlock transaction=TX-77
disk unavailable mount=/data
```

</details>


# Awk Practice

## 31. Print selected CSV fields

**Problem:** Print each employee name followed by the department.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {print $2, $3}' data/employees.csv
```

**How it works:** `-F,` sets comma as the field separator. `NR>1` skips the header; `$2` and `$3` select fields.

**Expected output:**

```text
Aarav Sharma Engineering
Ishita Sen HR
Rohan Mehta Sales
Meera Iyer Engineering
Kabir Khan Finance
Ananya Das Marketing
Vikram Rao Engineering
Nisha Patel Sales
Arjun Nair Support
Priya Bose Finance
Neel Joshi Engineering
Sana Ali Marketing
... (output truncated in workbook)
```

</details>

## 32. Use a custom output separator

**Problem:** Print employee name, role, and city separated by ` | `.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'BEGIN{OFS=" | "} NR>1 {print $2,$4,$6}' data/employees.csv
```

**How it works:** `OFS` controls the separator inserted by `print` between multiple expressions.

**Expected output:**

```text
Aarav Sharma | Senior Developer | Delhi
Ishita Sen | HR Manager | Kolkata
Rohan Mehta | Sales Executive | Mumbai
Meera Iyer | Data Engineer | Bengaluru
Kabir Khan | Accountant | Delhi
Ananya Das | SEO Specialist | Kolkata
Vikram Rao | DevOps Engineer | Hyderabad
Nisha Patel | Sales Manager | Ahmedabad
Arjun Nair | Support Engineer | Kochi
Priya Bose | Financial Analyst | Kolkata
Neel Joshi | Junior Developer | Pune
Sana Ali | Content Writer | Delhi
... (output truncated in workbook)
```

</details>

## 33. Filter high salaries

**Problem:** Print names and salaries of employees earning more than 80,000.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 && $5>80000 {print $2, $5}' data/employees.csv
```

**How it works:** Numeric comparison on field 5 filters records before printing.

**Expected output:**

```text
Aarav Sharma 95000
Meera Iyer 88000
Vikram Rao 92000
Nisha Patel 83000
Riya Chatterjee 105000
Sneha Pillai 82000
```

</details>

## 34. Combine multiple conditions

**Problem:** Find active Engineering employees located in Kolkata.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 && $3=="Engineering" && $6=="Kolkata" && $8=="active" {print $2,$4}' data/employees.csv
```

**How it works:** `&&` requires every condition to be true for the record.

**Expected output:**

```text
Riya Chatterjee Data Scientist
```

</details>

## 35. Count employees by status

**Problem:** Count active and inactive employees.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {count[$8]++} END{for (s in count) print s, count[s]}' data/employees.csv | sort
```

**How it works:** An associative array uses status text as a key and increments the count for each row.

**Expected output:**

```text
active 18
inactive 2
```

</details>

## 36. Calculate total payroll

**Problem:** Calculate the sum of all employee salaries.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {sum+=$5} END{print sum}' data/employees.csv
```

**How it works:** The running variable `sum` accumulates field 5; the END block prints it once.

**Expected output:**

```text
1427000
```

</details>

## 37. Calculate average salary

**Problem:** Calculate the average employee salary.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {sum+=$5; n++} END{printf "%.2f\n", sum/n}' data/employees.csv
```

**How it works:** The program tracks both the sum and record count, then formats the result to two decimal places.

**Expected output:**

```text
71350.00
```

</details>

## 38. Find the minimum salary

**Problem:** Print the employee with the lowest salary.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR==2 {min=$5; name=$2} NR>2 && $5<min {min=$5; name=$2} END{print name,min}' data/employees.csv
```

**How it works:** The first data row initializes the minimum; later rows replace it when a smaller value appears.

**Expected output:**

```text
Sana Ali 50000
```

</details>

## 39. Find the maximum salary

**Problem:** Print the employee with the highest salary.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR==2 {max=$5; name=$2} NR>2 && $5>max {max=$5; name=$2} END{print name,max}' data/employees.csv
```

**How it works:** This is the maximum-value version of the running comparison pattern.

**Expected output:**

```text
Riya Chatterjee 105000
```

</details>

## 40. Count employees per department

**Problem:** Print a department-wise employee count.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {count[$3]++} END{for (d in count) print d,count[d]}' data/employees.csv | sort
```

**How it works:** The department field becomes an associative-array key.

**Expected output:**

```text
Engineering 6
Finance 3
HR 2
Marketing 2
Operations 2
Sales 3
Support 2
```

</details>

## 41. Average salary per department

**Problem:** Calculate average salary for each department.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {sum[$3]+=$5; count[$3]++} END{for (d in sum) printf "%s %.2f\n",d,sum[d]/count[d]}' data/employees.csv | sort
```

**How it works:** Parallel arrays store each department’s salary sum and row count.

**Expected output:**

```text
Engineering 83500.00
Finance 75000.00
HR 64000.00
Marketing 55500.00
Operations 66500.00
Sales 67000.00
Support 64000.00
```

</details>

## 42. Payroll by city

**Problem:** Calculate total salary paid in each city.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {pay[$6]+=$5} END{for (c in pay) print c,pay[c]}' data/employees.csv | sort
```

**How it works:** The city is the array key and salaries are added to the corresponding total.

**Expected output:**

```text
Ahmedabad 83000
Bengaluru 88000
Chandigarh 57000
Delhi 270000
Hyderabad 166000
Jaipur 76000
Kochi 136000
Kolkata 372000
Mumbai 58000
Pune 121000
```

</details>

## 43. Calculate each sale amount

**Problem:** Print sale ID, product, and `quantity × unit_price`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'BEGIN{OFS=","} NR>1 {print $1,$5,$6*$7}' data/sales.csv
```

**How it works:** AWK automatically performs numeric multiplication on fields 6 and 7.

**Expected output:**

```text
S001,Laptop,130000
S002,Monitor,60000
S003,Keyboard,18000
S004,Laptop,72000
S005,Mouse,13500
S006,Server,180000
S007,Monitor,45000
S008,Router,26000
S009,Laptop,136000
S010,Keyboard,17600
S011,Mouse,15000
S012,Printer,48000
... (output truncated in workbook)
```

</details>

## 44. Calculate total sales revenue

**Problem:** Calculate revenue across every sales record.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {total+=$6*$7} END{print total}' data/sales.csv
```

**How it works:** Each row contributes quantity multiplied by unit price to the running total.

**Expected output:**

```text
2212050
```

</details>

## 45. Revenue by region

**Problem:** Calculate total sales revenue for each region.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {rev[$3]+=$6*$7} END{for (r in rev) print r,rev[r]}' data/sales.csv | sort
```

**How it works:** An associative array groups calculated revenue by region.

**Expected output:**

```text
East 812500
North 589750
South 464900
West 344900
```

</details>

## 46. Highest-value sale

**Problem:** Print the sale ID and value of the largest single sales transaction.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {v=$6*$7; if(v>max){max=v; id=$1; product=$5}} END{print id,product,max}' data/sales.csv
```

**How it works:** Each transaction value is compared with the current maximum.

**Expected output:**

```text
S017 Laptop 225000
```

</details>

## 47. Quantity sold by product

**Problem:** Calculate the total quantity sold for every product.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {qty[$5]+=$6} END{for (p in qty) print p,qty[p]}' data/sales.csv | sort
```

**How it works:** Product names are used as keys, and quantities are accumulated.

**Expected output:**

```text
Keyboard 39
Laptop 12
Monitor 25
Mouse 78
Printer 6
Router 23
Server 3
```

</details>

## 48. Student average marks

**Problem:** Print each student and the average of math, science, and English.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {printf "%-10s %.2f\n",$2,($4+$5+$6)/3}' data/students.csv
```

**How it works:** The three marks are added and divided by 3; `printf` aligns names and formats averages.

**Expected output:**

```text
Aditi      87.67
Bimal      71.67
Charu      92.33
Deepak     65.33
Esha       97.67
Farhan     59.00
Gita       83.33
Harsh      78.67
Indira     87.67
Jay        69.67
Kavya      92.00
Lalit      52.00
... (output truncated in workbook)
```

</details>

## 49. Assign pass or fail

**Problem:** Mark a student PASS when the three-subject average is at least 60.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {avg=($4+$5+$6)/3; print $2,(avg>=60?"PASS":"FAIL")}' data/students.csv
```

**How it works:** The ternary operator chooses PASS or FAIL based on the calculated average.

**Expected output:**

```text
Aditi PASS
Bimal PASS
Charu PASS
Deepak PASS
Esha PASS
Farhan FAIL
Gita PASS
Harsh PASS
Indira PASS
Jay PASS
Kavya PASS
Lalit FAIL
... (output truncated in workbook)
```

</details>

## 50. Find the top student

**Problem:** Print the student with the highest three-subject average.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {avg=($4+$5+$6)/3; if(avg>max){max=avg; name=$2}} END{printf "%s %.2f\n",name,max}' data/students.csv
```

**How it works:** The program maintains the highest average and corresponding name.

**Expected output:**

```text
Esha 97.67
```

</details>

## 51. Count students by major

**Problem:** Print how many students belong to each major.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F, 'NR>1 {count[$3]++} END{for (m in count) print m,count[m]}' data/students.csv | sort
```

**How it works:** The major field groups rows in an associative array.

**Expected output:**

```text
Chemistry 4
Computer Science 3
Mathematics 4
Physics 4
```

</details>

## 52. Find out-of-stock items

**Problem:** Print inventory items whose stock is zero.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F '\t' 'NR>1 && $4==0 {print $1,$2}' data/inventory.tsv
```

**How it works:** The TSV file requires a tab field separator; field 4 contains stock.

**Expected output:**

```text
P009 Webcam
```

</details>

## 53. Inventory value per item

**Problem:** Print each item and its stock value (`stock × price`).

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F '\t' 'BEGIN{OFS=" | "} NR>1 {print $2,$4*$5}' data/inventory.tsv
```

**How it works:** Multiplying stock by unit price gives the inventory value of each item.

**Expected output:**

```text
Laptop | 1625000
Mouse | 135000
Keyboard | 153000
Monitor | 480000
Router | 117000
Server | 720000
Printer | 288000
USB Cable | 105000
Webcam | 0
Switch | 135000
```

</details>

## 54. Inventory value by category

**Problem:** Calculate total inventory value for each category.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F '\t' 'NR>1 {value[$3]+=$4*$5} END{for (c in value) print c,value[c]}' data/inventory.tsv | sort
```

**How it works:** Values are grouped and accumulated using category names as keys.

**Expected output:**

```text
Accessories 393000
Electronics 2393000
Networking 972000
```

</details>

## 55. Users with Bash shells

**Problem:** Print usernames whose login shell is `/bin/bash`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F: '$7=="/bin/bash" {print $1}' data/users.txt
```

**How it works:** Colon separates passwd-style fields, and field 7 is the login shell.

**Expected output:**

```text
root
alice
carol
eve
```

</details>

## 56. Format username and home directory

**Problem:** Print `username -> home_directory` for every user.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk -F: '{print $1 " -> " $6}' data/users.txt
```

**How it works:** String concatenation combines literal text with selected fields.

**Expected output:**

```text
root -> /root
alice -> /home/alice
bob -> /home/bob
carol -> /home/carol
dave -> /home/dave
eve -> /home/eve
frank -> /home/frank
guest -> /nonexistent
```

</details>

## 57. Count HTTP status codes

**Problem:** Create a count of each response status in the access log.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk '{count[$9]++} END{for (s in count) print s,count[s]}' data/web_access.log | sort -n
```

**How it works:** In this log format, field 9 is the status code. The associative array counts each value.

**Expected output:**

```text
200 7
201 1
304 1
401 1
403 2
404 1
500 1
502 1
```

</details>

## 58. Sum bytes by HTTP status

**Problem:** Calculate total response bytes sent for every HTTP status.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk '{bytes[$9]+=$10} END{for (s in bytes) print s,bytes[s]}' data/web_access.log | sort -n
```

**How it works:** Field 10 stores response size, which is accumulated for each status code.

**Expected output:**

```text
200 17048
201 768
304 0
401 512
403 466
404 333
500 128
502 140
```

</details>

## 59. Find the most active IP

**Problem:** Print the IP address that made the most requests.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk '{count[$1]++} END{for (ip in count) if(count[ip]>max){max=count[ip]; top=ip} print top,max}' data/web_access.log
```

**How it works:** The program counts by IP and then scans the associative array for the largest count.

**Expected output:**

```text
192.168.1.10 3
```

</details>

## 60. Count application log levels

**Problem:** Count INFO, DEBUG, WARN, ERROR, and FATAL entries.

<details>
<summary><strong>Show solution</strong></summary>

```bash
awk '{count[$3]++} END{for (level in count) print level,count[level]}' data/app.log | sort
```

**How it works:** The third whitespace-separated field contains the log level.

**Expected output:**

```text
DEBUG 1
ERROR 2
FATAL 1
INFO 4
WARN 2
```

</details>


# Find Practice

## 61. List every regular file

**Problem:** List all regular files under the lab directory.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f | sort
```

**How it works:** `-type f` restricts results to regular files. Sorting makes the output predictable.

**Expected output:**

```text
backups/daily/db_2026-01-10.sql
backups/daily/db_2026-01-11.sql
backups/daily/db_2026-01-12.sql.gz
backups/weekly/full_2026-W01.tar
backups/weekly/full_2026-W02.tar.gz
data/app.log
data/auth.log
data/departments.txt
data/dept_codes.csv
data/employees.csv
data/inventory.tsv
data/names.txt
... (output truncated in workbook)
```

</details>

## 62. List every directory

**Problem:** List all directories under `projects`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects -type d | sort
```

**How it works:** `-type d` selects directories, including the starting directory.

**Expected output:**

```text
projects
projects/alpha
projects/alpha/docs
projects/alpha/src
projects/alpha/tests
projects/archive
projects/beta
projects/beta/config
projects/beta/src
projects/gamma
projects/gamma/docs
```

</details>

## 63. Find lowercase .log files

**Problem:** Find files whose names end in lowercase `.log`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -name '*.log' | sort
```

**How it works:** `-name` performs case-sensitive shell-pattern matching on the basename.

**Expected output:**

```text
data/app.log
data/auth.log
data/web_access.log
logs/2025/december/old.log
logs/2026/february/debug.log
logs/2026/february/server1.log
logs/2026/january/server1.log
logs/2026/january/server2.log
temp/empty/empty_1.log
temp/empty/empty_2.log
temp/empty/empty_3.log
temp/empty/empty_4.log
```

</details>

## 64. Case-insensitive text files

**Problem:** Find `.txt` files regardless of extension case.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -iname '*.txt' | sort
```

**How it works:** `-iname` is the case-insensitive form of `-name`, so it includes `Report.TXT`.

**Expected output:**

```text
data/departments.txt
data/names.txt
data/paragraphs.txt
data/users.txt
data/words.txt
mixed/-strange-name.txt
mixed/Report.TXT
mixed/empty.txt
mixed/multiline.txt
mixed/notes final.txt
permissions/private/notes.txt
permissions/private/passwords.txt
... (output truncated in workbook)
```

</details>

## 65. Find names containing spaces

**Problem:** Find filesystem entries whose names contain a space.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -name '* *' | sort
```

**How it works:** The quoted wildcard pattern matches any basename containing a literal space.

**Expected output:**

```text
mixed/notes final.txt
mixed/sub dir
mixed/sub dir/data file.csv
```

</details>

## 66. Find empty files

**Problem:** List all zero-byte regular files.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -empty | sort
```

**How it works:** For regular files, `-empty` means size zero.

**Expected output:**

```text
mixed/empty.txt
temp/empty/empty_1.log
temp/empty/empty_2.log
temp/empty/empty_3.log
temp/empty/empty_4.log
```

</details>

## 67. Find empty directories

**Problem:** List directories containing no entries.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type d -empty | sort
```

**How it works:** For directories, `-empty` means no child entries.

**Expected output:**

```text
(no output)
```

</details>

## 68. Find files larger than 5 KiB

**Problem:** List regular files larger than 5 KiB.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -size +5k | sort
```

**How it works:** The plus sign means strictly greater than five 1-KiB blocks.

**Expected output:**

```text
backups/weekly/full_2026-W01.tar
backups/weekly/full_2026-W02.tar.gz
```

</details>

## 69. Find files from 1 to 5 KiB

**Problem:** List files at least roughly 1 KiB but no larger than 5 KiB.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -size +1k -size -5k | sort
```

**How it works:** Multiple tests are implicitly joined with AND. `+1k` is greater than 1 KiB and `-5k` is less than 5 KiB.

**Expected output:**

```text
backups/daily/db_2026-01-10.sql
backups/daily/db_2026-01-11.sql
backups/daily/db_2026-01-12.sql.gz
data/employees.csv
data/sales.csv
data/web_access.log
```

</details>

## 70. Find executable files

**Problem:** List regular files executable by at least one user class.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects permissions -type f -executable | sort
```

**How it works:** `-executable` tests whether the current user can execute the file.

**Expected output:**

```text
permissions/scripts/report.py
permissions/scripts/run.sh
projects/alpha/src/main.py
projects/beta/src/cleanup.sh
projects/beta/src/deploy.sh
```

</details>

## 71. Find files with exact mode 600

**Problem:** Find regular files whose permission bits are exactly `600`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -perm 600 | sort
```

**How it works:** Without a prefix, `-perm 600` requires an exact permission-bit match.

**Expected output:**

```text
permissions/private/passwords.txt
```

</details>

## 72. Find files older than one year

**Problem:** Find archived files modified more than 365 days ago.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects/archive -type f -mtime +365 -print | sort
```

**How it works:** `-mtime +365` selects files whose age in whole 24-hour periods exceeds 365 days.

**Expected output:**

```text
projects/archive/legacy.py
projects/archive/old_report.txt
```

</details>

## 73. Find files newer than a reference

**Problem:** Find files in the January log directory newer than `server1.log`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find logs/2026/january -type f -newer logs/2026/january/server1.log -print | sort
```

**How it works:** `-newer reference` compares modification timestamps.

**Expected output:**

```text
logs/2026/january/server2.log
```

</details>

## 74. Find files older than a reference

**Problem:** Find log files older than January’s `server1.log`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find logs -type f ! -newer logs/2026/january/server1.log -print | sort
```

**How it works:** Negating `-newer` selects files not newer than the reference; this includes equal or older timestamps.

**Expected output:**

```text
logs/2025/december/old.log
logs/2026/january/server1.log
```

</details>

## 75. Limit search depth

**Problem:** List regular files no deeper than two levels below the current directory.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find . -maxdepth 2 -type f | sort
```

**How it works:** `-maxdepth 2` prevents descent beyond two path levels from the starting point.

**Expected output:**

```text
./.hidden_dir/secret.txt
./FILE_INDEX.txt
./data/app.log
./data/auth.log
./data/departments.txt
./data/dept_codes.csv
./data/employees.csv
./data/inventory.tsv
./data/names.txt
./data/paragraphs.txt
./data/sales.csv
./data/students.csv
... (output truncated in workbook)
```

</details>

## 76. Require a minimum depth

**Problem:** List project files located at depth 3 or deeper.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects -mindepth 3 -type f | sort
```

**How it works:** `-mindepth 3` suppresses results from shallower levels while still traversing them.

**Expected output:**

```text
projects/alpha/docs/README.md
projects/alpha/src/main.py
projects/alpha/src/utils.py
projects/alpha/tests/test_utils.py
projects/beta/config/app.conf
projects/beta/src/cleanup.sh
projects/beta/src/deploy.sh
projects/gamma/docs/guide.md
```

</details>

## 77. Prune an archive directory

**Problem:** Find Python files under `projects` without descending into `projects/archive`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects -path 'projects/archive' -prune -o -type f -name '*.py' -print | sort
```

**How it works:** When the archive path matches, `-prune` stops descent; otherwise the right side finds Python files.

**Expected output:**

```text
projects/alpha/src/main.py
projects/alpha/src/utils.py
projects/alpha/tests/test_utils.py
```

</details>

## 78. Match multiple extensions

**Problem:** Find regular files ending in `.py` or `.sh`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects permissions -type f \( -name '*.py' -o -name '*.sh' \) | sort
```

**How it works:** Escaped parentheses group the OR expression so `-type f` applies to both filename patterns.

**Expected output:**

```text
permissions/scripts/report.py
permissions/scripts/run.sh
projects/alpha/src/main.py
projects/alpha/src/utils.py
projects/alpha/tests/test_utils.py
projects/archive/legacy.py
projects/beta/src/cleanup.sh
projects/beta/src/deploy.sh
```

</details>

## 79. Find files owned by the current user

**Problem:** List regular files owned by your current username.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -user "$(id -un)" | sort
```

**How it works:** Command substitution obtains the current username, and `-user` matches ownership.

**Expected output:**

```text
backups/daily/db_2026-01-10.sql
backups/daily/db_2026-01-11.sql
backups/daily/db_2026-01-12.sql.gz
backups/weekly/full_2026-W01.tar
backups/weekly/full_2026-W02.tar.gz
data/app.log
data/auth.log
data/departments.txt
data/dept_codes.csv
data/employees.csv
data/inventory.tsv
data/names.txt
... (output truncated in workbook)
```

</details>

## 80. Find symbolic links

**Problem:** List all symbolic links, whether valid or broken.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type l | sort
```

**How it works:** `-type l` selects symbolic links themselves rather than their targets.

**Expected output:**

```text
data/current_app.log
mixed/broken_link
projects/latest
```

</details>

## 81. Find broken symbolic links

**Problem:** List symbolic links whose targets do not exist.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -xtype l | sort
```

**How it works:** On GNU find, `-xtype l` selects links that ultimately resolve as broken.

**Expected output:**

```text
mixed/broken_link
```

</details>

## 82. Run wc on found files

**Problem:** Count lines in every `.log` file under `logs`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find logs -type f -name '*.log' -exec wc -l {} +
```

**How it works:** `-exec ... {} +` passes many found paths to each `wc` invocation efficiently.

**Expected output:**

```text
  3 logs/2026/january/server1.log
  3 logs/2026/january/server2.log
  2 logs/2026/february/server1.log
  2 logs/2026/february/debug.log
  2 logs/2025/december/old.log
 12 total
```

</details>

## 83. Run grep on found files

**Problem:** Find TODO or FIXME markers in project Markdown files.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects -type f -name '*.md' -exec grep -HnE 'TODO|FIXME' {} +
```

**How it works:** `{}` is replaced by found paths; `-Hn` prints filenames and line numbers.

**Expected output:**

```text
projects/alpha/docs/README.md:3:TODO: add installation instructions.
projects/gamma/docs/guide.md:3:FIXME: document backup process.
```

</details>

## 84. Print size and path

**Problem:** Print each backup file’s byte size followed by its path.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find backups -type f -printf '%s %p\n' | sort -n
```

**How it works:** GNU find’s `%s` prints size in bytes and `%p` prints the full found path.

**Expected output:**

```text
1800 backups/daily/db_2026-01-12.sql.gz
2080 backups/daily/db_2026-01-10.sql
3120 backups/daily/db_2026-01-11.sql
5600 backups/weekly/full_2026-W01.tar
6000 backups/weekly/full_2026-W02.tar.gz
```

</details>

## 85. Rank files by size

**Problem:** Display the five largest regular files in the lab.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -printf '%s %p\n' | sort -nr | head -n 5
```

**How it works:** The pipeline emits byte sizes, sorts numerically in reverse, and keeps the first five rows.

**Expected output:**

```text
6000 backups/weekly/full_2026-W02.tar.gz
5600 backups/weekly/full_2026-W01.tar
3120 backups/daily/db_2026-01-11.sql
2080 backups/daily/db_2026-01-10.sql
1800 backups/daily/db_2026-01-12.sql.gz
```

</details>

## 86. Find the newest file

**Problem:** Print the most recently modified regular file.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find logs -type f -printf '%T@ %p\n' | sort -nr | head -n 1
```

**How it works:** `%T@` prints a sortable modification timestamp. Reverse numeric sorting puts the newest first.

**Expected output:**

```text
1770724800.0000000000 logs/2026/february/debug.log
```

</details>

## 87. Print only basenames

**Problem:** Print only the basenames of Python files.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects -type f -name '*.py' -exec basename {} \; | sort
```

**How it works:** Each found path is passed to `basename`, which removes directory components.

**Expected output:**

```text
legacy.py
main.py
test_utils.py
utils.py
```

</details>

## 88. Safely find leading-dash names

**Problem:** Find files whose basename begins with `-`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find mixed -type f -name '-*' -print
```

**How it works:** The pattern is passed as a `find` argument, so the matching filename is not misread as an option.

**Expected output:**

```text
mixed/-strange-name.txt
```

</details>

## 89. Find files not ending in .log

**Problem:** List regular files under `logs` whose names do not end in `.log`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find logs -type f ! -name '*.log' | sort
```

**How it works:** `!` negates the following name test.

**Expected output:**

```text
(no output)
```

</details>

## 90. Find world-writable files

**Problem:** List regular files writable by “others.”

<details>
<summary><strong>Show solution</strong></summary>

```bash
find data logs projects backups temp permissions mixed reports -type f -perm -002 -print | sort
```

**How it works:** The `-` prefix means all bits in `002` must be present, identifying world-writable files.

**Expected output:**

```text
temp/public.tmp
```

</details>


# Unix Utilities Practice

## 91. Count lines, words, and bytes

**Problem:** Show line, word, and byte counts for `employees.csv`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
wc data/employees.csv
```

**How it works:** `wc` reports lines, words, and bytes when no specific count option is supplied.

**Expected output:**

```text
  21   59 1494 data/employees.csv
```

</details>

## 92. Preview the beginning of a file

**Problem:** Display the header and first three employee records.

<details>
<summary><strong>Show solution</strong></summary>

```bash
head -n 4 data/employees.csv
```

**How it works:** `head -n 4` prints the first four lines: one header plus three data rows.

**Expected output:**

```text
id,name,department,role,salary,city,join_date,status
101,Aarav Sharma,Engineering,Senior Developer,95000,Delhi,2020-03-15,active
102,Ishita Sen,HR,HR Manager,72000,Kolkata,2019-07-01,active
103,Rohan Mehta,Sales,Sales Executive,58000,Mumbai,2022-01-10,active
```

</details>

## 93. Preview the end of a file

**Problem:** Display the final five sales records.

<details>
<summary><strong>Show solution</strong></summary>

```bash
tail -n 5 data/sales.csv
```

**How it works:** `tail` reads from the end of a file.

**Expected output:**

```text
S026,2026-02-11,North,Nisha,Monitor,7,13500
S027,2026-02-12,West,Arjun,Keyboard,9,2100
S028,2026-02-13,South,Priya,Printer,3,23000
S029,2026-02-14,East,Neel,Laptop,1,66000
S030,2026-02-15,North,Sana,Router,8,6800
```

</details>

## 94. Extract CSV columns with cut

**Problem:** Print employee name and department columns.

<details>
<summary><strong>Show solution</strong></summary>

```bash
cut -d, -f2,3 data/employees.csv
```

**How it works:** `-d,` sets comma as delimiter, and `-f2,3` selects fields 2 and 3.

**Expected output:**

```text
name,department
Aarav Sharma,Engineering
Ishita Sen,HR
Rohan Mehta,Sales
Meera Iyer,Engineering
Kabir Khan,Finance
Ananya Das,Marketing
Vikram Rao,Engineering
Nisha Patel,Sales
Arjun Nair,Support
Priya Bose,Finance
Neel Joshi,Engineering
... (output truncated in workbook)
```

</details>

## 95. Extract passwd-style fields

**Problem:** Print username and shell from `users.txt`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
cut -d: -f1,7 data/users.txt
```

**How it works:** Colon is the delimiter; the username and shell are fields 1 and 7.

**Expected output:**

```text
root:/bin/bash
alice:/bin/bash
bob:/bin/zsh
carol:/bin/bash
dave:/usr/sbin/nologin
eve:/bin/bash
frank:/bin/fish
guest:/usr/sbin/nologin
```

</details>

## 96. Sort words alphabetically

**Problem:** Sort `words.txt` using bytewise ordering.

<details>
<summary><strong>Show solution</strong></summary>

```bash
LC_ALL=C sort data/words.txt
```

**How it works:** `sort` orders lines; `LC_ALL=C` makes ordering deterministic and case-sensitive by byte value.

**Expected output:**

```text
Apple
Cherry
apple
apple
apricot
banana
banana
cherry
date
fig
grape
kiwi
... (output truncated in workbook)
```

</details>

## 97. Create a case-insensitive unique list

**Problem:** Print unique words while treating uppercase and lowercase forms as equal.

<details>
<summary><strong>Show solution</strong></summary>

```bash
sort -f data/words.txt | uniq -i
```

**How it works:** `sort -f` groups case variants together; `uniq -i` suppresses case-insensitive duplicates.

**Expected output:**

```text
Apple
apricot
banana
Cherry
date
fig
grape
kiwi
lemon
lime
mango
nectarine
... (output truncated in workbook)
```

</details>

## 98. Count word frequencies

**Problem:** Count each word ignoring case and rank by frequency.

<details>
<summary><strong>Show solution</strong></summary>

```bash
tr '[:upper:]' '[:lower:]' < data/words.txt | sort | uniq -c | sort -nr
```

**How it works:** `tr` normalizes case, `sort` groups equal words, and `uniq -c` counts each group.

**Expected output:**

```text
      3 apple
      2 cherry
      2 banana
      1 plum
      1 pear
      1 papaya
      1 orange
      1 nectarine
      1 mango
      1 lime
      1 lemon
      1 kiwi
... (output truncated in workbook)
```

</details>

## 99. Numerically sort salaries

**Problem:** Display the five highest-paid employee records.

<details>
<summary><strong>Show solution</strong></summary>

```bash
{ head -n 1 data/employees.csv; tail -n +2 data/employees.csv | sort -t, -k5,5nr | head -n 5; }
```

**How it works:** The header is preserved separately; data rows are sorted numerically and descending by field 5.

**Expected output:**

```text
id,name,department,role,salary,city,join_date,status
118,Riya Chatterjee,Engineering,Data Scientist,105000,Kolkata,2020-02-20,active
101,Aarav Sharma,Engineering,Senior Developer,95000,Delhi,2020-03-15,active
107,Vikram Rao,Engineering,DevOps Engineer,92000,Hyderabad,2020-09-18,active
104,Meera Iyer,Engineering,Data Engineer,88000,Bengaluru,2021-06-21,active
108,Nisha Patel,Sales,Sales Manager,83000,Ahmedabad,2017-04-09,active
```

</details>

## 100. Sort by two keys

**Problem:** Sort employees by department, then by descending salary.

<details>
<summary><strong>Show solution</strong></summary>

```bash
{ head -n 1 data/employees.csv; tail -n +2 data/employees.csv | sort -t, -k3,3 -k5,5nr; }
```

**How it works:** The first key is department text; the second is numeric salary in reverse order.

**Expected output:**

```text
id,name,department,role,salary,city,join_date,status
118,Riya Chatterjee,Engineering,Data Scientist,105000,Kolkata,2020-02-20,active
101,Aarav Sharma,Engineering,Senior Developer,95000,Delhi,2020-03-15,active
107,Vikram Rao,Engineering,DevOps Engineer,92000,Hyderabad,2020-09-18,active
104,Meera Iyer,Engineering,Data Engineer,88000,Bengaluru,2021-06-21,active
115,Aditya Kulkarni,Engineering,QA Engineer,69000,Pune,2021-03-03,active
111,Neel Joshi,Engineering,Junior Developer,52000,Pune,2024-01-08,active
120,Sneha Pillai,Finance,Senior Accountant,82000,Kochi,2016-09-13,active
110,Priya Bose,Finance,Financial Analyst,78000,Kolkata,2021-12-05,active
105,Kabir Khan,Finance,Accountant,65000,Delhi,2018-11-30,inactive
102,Ishita Sen,HR,HR Manager,72000,Kolkata,2019-07-01,active
114,Tania Roy,HR,Recruiter,56000,Kolkata,2022-05-16,inactive
... (output truncated in workbook)
```

</details>

## 101. Convert text to uppercase

**Problem:** Convert every name to uppercase.

<details>
<summary><strong>Show solution</strong></summary>

```bash
tr '[:lower:]' '[:upper:]' < data/names.txt
```

**How it works:** `tr` maps every lowercase character to its uppercase equivalent.

**Expected output:**

```text
AARAV
ANANYA
ARJUN
ISHITA
KABIR
MEERA
NEEL
NISHA
PRIYA
RIYA
ROHAN
SANA
... (output truncated in workbook)
```

</details>

## 102. Squeeze repeated spaces

**Problem:** Collapse repeated spaces in the application log to one space.

<details>
<summary><strong>Show solution</strong></summary>

```bash
tr -s ' ' < data/app.log
```

**How it works:** `-s` squeezes consecutive occurrences of the selected character into one.

**Expected output:**

```text
2026-01-10 09:00:01 INFO app started version=2.4.1
2026-01-10 09:01:13 DEBUG database connection pool initialized size=10
2026-01-10 09:03:44 WARN cache miss rate high value=0.73
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:06:19 INFO user login user=alice
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
2026-01-10 09:08:11 WARN retrying request attempt=2
2026-01-10 09:09:40 INFO order completed order=ORD-1008
2026-01-10 09:11:22 FATAL disk unavailable mount=/data
2026-01-10 09:12:02 INFO graceful shutdown initiated
```

</details>

## 103. Combine files side by side

**Problem:** Pair each name with a department using a tab separator.

<details>
<summary><strong>Show solution</strong></summary>

```bash
paste data/names.txt data/departments.txt
```

**How it works:** `paste` merges corresponding lines. Because the files have different lengths, later rows have an empty second field.

**Expected output:**

```text
Aarav	Engineering
Ananya	Finance
Arjun	HR
Ishita	Marketing
Kabir	Operations
Meera	Sales
Neel	Support
Nisha	
Priya	
Riya	
Rohan	
Sana	
... (output truncated in workbook)
```

</details>

## 104. Join related tables

**Problem:** Attach department codes to employee rows.

<details>
<summary><strong>Show solution</strong></summary>

```bash
join -t, -1 3 -2 1 <(tail -n +2 data/employees.csv | sort -t, -k3,3) <(tail -n +2 data/dept_codes.csv | sort -t, -k1,1) | head
```

**How it works:** `join` matches employee field 3 with code-table field 1. Both inputs must be sorted by their join keys.

**Expected output:**

```text
Engineering,101,Aarav Sharma,Senior Developer,95000,Delhi,2020-03-15,active,ENG
Engineering,104,Meera Iyer,Data Engineer,88000,Bengaluru,2021-06-21,active,ENG
Engineering,107,Vikram Rao,DevOps Engineer,92000,Hyderabad,2020-09-18,active,ENG
Engineering,111,Neel Joshi,Junior Developer,52000,Pune,2024-01-08,active,ENG
Engineering,115,Aditya Kulkarni,QA Engineer,69000,Pune,2021-03-03,active,ENG
Engineering,118,Riya Chatterjee,Data Scientist,105000,Kolkata,2020-02-20,active,ENG
Finance,105,Kabir Khan,Accountant,65000,Delhi,2018-11-30,inactive,FIN
Finance,110,Priya Bose,Financial Analyst,78000,Kolkata,2021-12-05,active,FIN
Finance,120,Sneha Pillai,Senior Accountant,82000,Kochi,2016-09-13,active,FIN
HR,102,Ishita Sen,HR Manager,72000,Kolkata,2019-07-01,active,HUM
```

</details>

## 105. Compare two sorted sets

**Problem:** Show names that are employees but never appear as salespeople.

<details>
<summary><strong>Show solution</strong></summary>

```bash
comm -23 <(tail -n +2 data/employees.csv | cut -d, -f2 | sort -u) <(tail -n +2 data/sales.csv | cut -d, -f4 | sort -u)
```

**How it works:** `comm -23` suppresses columns 2 and 3, leaving values unique to the first sorted input.

**Expected output:**

```text
Aarav Sharma
Aditya Kulkarni
Ananya Das
Arjun Nair
Ishita Sen
Kabir Khan
Karan Malhotra
Manish Verma
Meera Iyer
Neel Joshi
Nisha Patel
Pooja Reddy
... (output truncated in workbook)
```

</details>

## 106. Replace text with sed

**Problem:** Display `app.log` with `INFO` changed to `INFORMATION`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
sed 's/INFO/INFORMATION/g' data/app.log
```

**How it works:** The substitute command replaces every occurrence on each line because of the `g` flag.

**Expected output:**

```text
2026-01-10 09:00:01 INFORMATION  app started version=2.4.1
2026-01-10 09:01:13 DEBUG database connection pool initialized size=10
2026-01-10 09:03:44 WARN  cache miss rate high value=0.73
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:06:19 INFORMATION  user login user=alice
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
2026-01-10 09:08:11 WARN  retrying request attempt=2
2026-01-10 09:09:40 INFORMATION  order completed order=ORD-1008
2026-01-10 09:11:22 FATAL disk unavailable mount=/data
2026-01-10 09:12:02 INFORMATION  graceful shutdown initiated
```

</details>

## 107. Delete blank lines with sed

**Problem:** Display `multiline.txt` without blank lines.

<details>
<summary><strong>Show solution</strong></summary>

```bash
sed '/^$/d' mixed/multiline.txt
```

**How it works:** The address `/^$/` selects blank lines and `d` deletes them from output.

**Expected output:**

```text
first line
third line
fifth line
```

</details>

## 108. Print a line range with sed

**Problem:** Display lines 3 through 6 from `app.log`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
sed -n '3,6p' data/app.log
```

**How it works:** `-n` disables automatic printing; `3,6p` explicitly prints the selected range.

**Expected output:**

```text
2026-01-10 09:03:44 WARN  cache miss rate high value=0.73
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:06:19 INFO  user login user=alice
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
```

</details>

## 109. Extract a configuration value

**Problem:** Print only the value assigned to `PORT`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
sed -n 's/^PORT=//p' projects/beta/config/app.conf
```

**How it works:** The substitution removes the `PORT=` prefix, and `p` prints only matching lines.

**Expected output:**

```text
8080
```

</details>

## 110. Save and display output with tee

**Problem:** Display severe log entries and save them to `workspace/severe.log`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
grep -E 'ERROR|FATAL' data/app.log | tee workspace/severe.log
```

**How it works:** `tee` copies standard input both to the terminal and to a file.

**Expected output:**

```text
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
2026-01-10 09:11:22 FATAL disk unavailable mount=/data
```

</details>

## 111. Use xargs to count lines

**Problem:** Count lines in every project Markdown file.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find projects -type f -name '*.md' -print0 | xargs -0 wc -l
```

**How it works:** Null delimiters keep filenames safe, and `xargs -0` builds a `wc -l` command from the found paths.

**Expected output:**

```text
  3 projects/alpha/docs/README.md
  3 projects/gamma/docs/guide.md
  6 total
```

</details>

## 112. Use xargs with grep safely

**Problem:** Search every log file for ERROR using null-delimited paths.

<details>
<summary><strong>Show solution</strong></summary>

```bash
find logs -type f -name '*.log' -print0 | xargs -0 grep -H 'ERROR'
```

**How it works:** The null-delimited pipeline works even when filenames contain whitespace or unusual characters.

**Expected output:**

```text
logs/2026/january/server1.log:ERROR disk full
logs/2026/january/server2.log:ERROR timeout
logs/2026/february/server1.log:ERROR network unreachable
logs/2025/december/old.log:ERROR deprecated config
```

</details>

## 113. Number every line

**Problem:** Display `paragraphs.txt` with line numbers.

<details>
<summary><strong>Show solution</strong></summary>

```bash
nl -ba data/paragraphs.txt
```

**How it works:** `-ba` numbers all lines, including blank ones.

**Expected output:**

```text
     1	Unix tools are powerful because each command performs one focused task.
     2	Pipelines combine small commands into larger workflows.
     3	Grep searches text, awk processes fields, and find locates filesystem objects.
     4	A careful administrator tests commands before using destructive options.
     5	Error messages should be redirected only when you understand the consequences.
     6	Regular expressions are shared by many Unix text-processing tools.
```

</details>

## 114. Reverse line order

**Problem:** Display the application log from last line to first.

<details>
<summary><strong>Show solution</strong></summary>

```bash
tac data/app.log
```

**How it works:** `tac` is the line-order reverse of `cat`.

**Expected output:**

```text
2026-01-10 09:12:02 INFO  graceful shutdown initiated
2026-01-10 09:11:22 FATAL disk unavailable mount=/data
2026-01-10 09:09:40 INFO  order completed order=ORD-1008
2026-01-10 09:08:11 WARN  retrying request attempt=2
2026-01-10 09:07:55 ERROR database deadlock transaction=TX-77
2026-01-10 09:06:19 INFO  user login user=alice
2026-01-10 09:05:02 ERROR payment service timeout order=ORD-1008
2026-01-10 09:03:44 WARN  cache miss rate high value=0.73
2026-01-10 09:01:13 DEBUG database connection pool initialized size=10
2026-01-10 09:00:01 INFO  app started version=2.4.1
```

</details>

## 115. Reverse characters

**Problem:** Reverse the characters of each line in `names.txt`.

<details>
<summary><strong>Show solution</strong></summary>

```bash
rev data/names.txt
```

**How it works:** `rev` reverses characters independently on every input line.

**Expected output:**

```text
varaA
aynanA
nujrA
atihsI
ribaK
areeM
leeN
ahsiN
ayirP
ayiR
nahoR
anaS
... (output truncated in workbook)
```

</details>

## 116. Verify duplicate contents

**Problem:** Calculate checksums for the suspected duplicate files.

<details>
<summary><strong>Show solution</strong></summary>

```bash
cksum temp/duplicate_a.txt temp/duplicate_b.txt temp/unique.txt
```

**How it works:** Identical checksum and byte-count pairs strongly indicate identical content; `cmp` can verify exactly.

**Expected output:**

```text
4081661171 13 temp/duplicate_a.txt
4081661171 13 temp/duplicate_b.txt
2846108029 18 temp/unique.txt
```

</details>

## 117. Compare files byte by byte

**Problem:** Verify whether the two duplicate files are identical.

<details>
<summary><strong>Show solution</strong></summary>

```bash
cmp -s temp/duplicate_a.txt temp/duplicate_b.txt && echo 'identical' || echo 'different'
```

**How it works:** `cmp -s` produces no normal output and uses its exit status to indicate equality.

**Expected output:**

```text
identical
```

</details>

## 118. Show differences between reports

**Problem:** Compare January and February reports in unified format.

<details>
<summary><strong>Show solution</strong></summary>

```bash
diff -u reports/report_jan.txt reports/report_feb.txt || true
```

**How it works:** `diff -u` shows contextual changes. `|| true` prevents the expected “files differ” status from stopping scripts.

**Expected output:**

```text
--- reports/report_jan.txt	2026-07-17 07:26:40.481647538 +0000
+++ reports/report_feb.txt	2026-07-17 07:26:40.481714335 +0000
@@ -1,2 +1,2 @@
-January revenue: 125000
-January expenses: 82000
+February revenue: 148000
+February expenses: 91000
```

</details>

## 119. Inspect disk usage

**Problem:** Display the total apparent disk space used by each top-level practice directory.

<details>
<summary><strong>Show solution</strong></summary>

```bash
du -sh data logs projects backups temp permissions mixed reports 2>/dev/null | sort -h
```

**How it works:** `du -sh` summarizes each argument in human-readable units; `sort -h` sorts those units numerically.

**Expected output:**

```text
1.5K	reports
2.0K	permissions
2.5K	logs
2.5K	mixed
5.5K	projects
5.5K	temp
11K	data
20K	backups
```

</details>

## 120. Build a top-IP pipeline

**Problem:** Print the three most active IP addresses and request counts.

<details>
<summary><strong>Show solution</strong></summary>

```bash
cut -d' ' -f1 data/web_access.log | sort | uniq -c | sort -nr | head -n 3
```

**How it works:** This pipeline extracts IPs, groups and counts them, ranks counts descending, and keeps the top three.

**Expected output:**

```text
      3 192.168.1.10
      2 192.168.1.11
      2 172.16.0.3
```

</details>
