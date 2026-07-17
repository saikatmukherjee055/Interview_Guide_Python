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


# Grep Problems

## 1. Find all ERROR lines

Display every line containing `ERROR` in the application log.

## 2. Case-insensitive INFO search

Display lines containing `info`, regardless of letter case.

## 3. Show line numbers

Find `WARN` lines and include their line numbers.

## 4. Match several log levels

Display lines containing either `ERROR` or `FATAL`.

## 5. Count failed logins

Count lines containing `Failed password` in the authentication log.

## 6. Exclude INFO lines

Display application-log lines that do not contain `INFO`.

## 7. Match a whole word

Find occurrences of the whole word `root` in the authentication log.

## 8. Match a line prefix

Display access-log requests coming from IP address `192.168.1.10`.

## 9. Find HTTP 4xx responses

Display access-log lines whose response status is in the 400–499 range.

## 10. Find GET or POST requests

Display requests whose HTTP method is either GET or POST.

## 11. Search recursively for TODO or FIXME

Search the entire `projects` tree for unfinished-work markers.

## 12. List files containing ERROR

Print only the names of log files that contain `ERROR`.

## 13. List files without ERROR

Print names of log files that contain no `ERROR` line.

## 14. Match an entire line

Find lines in `words.txt` that are exactly lowercase `apple`.

## 15. Count apple ignoring case

Count lines equal to or containing `apple` regardless of case.

## 16. Names starting with A or R

Display names beginning with uppercase A or R.

## 17. Engineering employees

Display employee records belonging to Engineering.

## 18. Inactive employees

Display employee records whose final CSV field is `inactive`.

## 19. Show context around FATAL

Display the FATAL line together with one line before and one line after it.

## 20. Extract only IP addresses

Extract every IPv4-like address from the access log.

## 21. Count requests per IP

Create a frequency table showing how many requests each IP sent.

## 22. Extract key=value pairs

Extract all `name=value` fragments from the application log.

## 23. Locate blank lines

Show the line numbers of blank lines in `multiline.txt`.

## 24. Remove blank lines

Display only nonblank lines from `multiline.txt`.

## 25. Search selected file extensions

Search only Markdown files for TODO or FIXME markers.

## 26. Exclude an archive directory

Search Python files for `print` but skip `projects/archive`.

## 27. Use a fixed-string search

Search literally for `division by zero` in the project tree.

## 28. Match an exact configuration line

Find a line that is exactly `DEBUG=false`.

## 29. Find server-error requests

Display web requests that returned an HTTP 5xx status.

## 30. Extract error and fatal messages

Print only the message text after `ERROR` or `FATAL` in `app.log`.


# Awk Problems

## 31. Print selected CSV fields

Print each employee name followed by the department.

## 32. Use a custom output separator

Print employee name, role, and city separated by ` | `.

## 33. Filter high salaries

Print names and salaries of employees earning more than 80,000.

## 34. Combine multiple conditions

Find active Engineering employees located in Kolkata.

## 35. Count employees by status

Count active and inactive employees.

## 36. Calculate total payroll

Calculate the sum of all employee salaries.

## 37. Calculate average salary

Calculate the average employee salary.

## 38. Find the minimum salary

Print the employee with the lowest salary.

## 39. Find the maximum salary

Print the employee with the highest salary.

## 40. Count employees per department

Print a department-wise employee count.

## 41. Average salary per department

Calculate average salary for each department.

## 42. Payroll by city

Calculate total salary paid in each city.

## 43. Calculate each sale amount

Print sale ID, product, and `quantity × unit_price`.

## 44. Calculate total sales revenue

Calculate revenue across every sales record.

## 45. Revenue by region

Calculate total sales revenue for each region.

## 46. Highest-value sale

Print the sale ID and value of the largest single sales transaction.

## 47. Quantity sold by product

Calculate the total quantity sold for every product.

## 48. Student average marks

Print each student and the average of math, science, and English.

## 49. Assign pass or fail

Mark a student PASS when the three-subject average is at least 60.

## 50. Find the top student

Print the student with the highest three-subject average.

## 51. Count students by major

Print how many students belong to each major.

## 52. Find out-of-stock items

Print inventory items whose stock is zero.

## 53. Inventory value per item

Print each item and its stock value (`stock × price`).

## 54. Inventory value by category

Calculate total inventory value for each category.

## 55. Users with Bash shells

Print usernames whose login shell is `/bin/bash`.

## 56. Format username and home directory

Print `username -> home_directory` for every user.

## 57. Count HTTP status codes

Create a count of each response status in the access log.

## 58. Sum bytes by HTTP status

Calculate total response bytes sent for every HTTP status.

## 59. Find the most active IP

Print the IP address that made the most requests.

## 60. Count application log levels

Count INFO, DEBUG, WARN, ERROR, and FATAL entries.


# Find Problems

## 61. List every regular file

List all regular files under the lab directory.

## 62. List every directory

List all directories under `projects`.

## 63. Find lowercase .log files

Find files whose names end in lowercase `.log`.

## 64. Case-insensitive text files

Find `.txt` files regardless of extension case.

## 65. Find names containing spaces

Find filesystem entries whose names contain a space.

## 66. Find empty files

List all zero-byte regular files.

## 67. Find empty directories

List directories containing no entries.

## 68. Find files larger than 5 KiB

List regular files larger than 5 KiB.

## 69. Find files from 1 to 5 KiB

List files at least roughly 1 KiB but no larger than 5 KiB.

## 70. Find executable files

List regular files executable by at least one user class.

## 71. Find files with exact mode 600

Find regular files whose permission bits are exactly `600`.

## 72. Find files older than one year

Find archived files modified more than 365 days ago.

## 73. Find files newer than a reference

Find files in the January log directory newer than `server1.log`.

## 74. Find files older than a reference

Find log files older than January’s `server1.log`.

## 75. Limit search depth

List regular files no deeper than two levels below the current directory.

## 76. Require a minimum depth

List project files located at depth 3 or deeper.

## 77. Prune an archive directory

Find Python files under `projects` without descending into `projects/archive`.

## 78. Match multiple extensions

Find regular files ending in `.py` or `.sh`.

## 79. Find files owned by the current user

List regular files owned by your current username.

## 80. Find symbolic links

List all symbolic links, whether valid or broken.

## 81. Find broken symbolic links

List symbolic links whose targets do not exist.

## 82. Run wc on found files

Count lines in every `.log` file under `logs`.

## 83. Run grep on found files

Find TODO or FIXME markers in project Markdown files.

## 84. Print size and path

Print each backup file’s byte size followed by its path.

## 85. Rank files by size

Display the five largest regular files in the lab.

## 86. Find the newest file

Print the most recently modified regular file.

## 87. Print only basenames

Print only the basenames of Python files.

## 88. Safely find leading-dash names

Find files whose basename begins with `-`.

## 89. Find files not ending in .log

List regular files under `logs` whose names do not end in `.log`.

## 90. Find world-writable files

List regular files writable by “others.”


# Unix Utilities Problems

## 91. Count lines, words, and bytes

Show line, word, and byte counts for `employees.csv`.

## 92. Preview the beginning of a file

Display the header and first three employee records.

## 93. Preview the end of a file

Display the final five sales records.

## 94. Extract CSV columns with cut

Print employee name and department columns.

## 95. Extract passwd-style fields

Print username and shell from `users.txt`.

## 96. Sort words alphabetically

Sort `words.txt` using bytewise ordering.

## 97. Create a case-insensitive unique list

Print unique words while treating uppercase and lowercase forms as equal.

## 98. Count word frequencies

Count each word ignoring case and rank by frequency.

## 99. Numerically sort salaries

Display the five highest-paid employee records.

## 100. Sort by two keys

Sort employees by department, then by descending salary.

## 101. Convert text to uppercase

Convert every name to uppercase.

## 102. Squeeze repeated spaces

Collapse repeated spaces in the application log to one space.

## 103. Combine files side by side

Pair each name with a department using a tab separator.

## 104. Join related tables

Attach department codes to employee rows.

## 105. Compare two sorted sets

Show names that are employees but never appear as salespeople.

## 106. Replace text with sed

Display `app.log` with `INFO` changed to `INFORMATION`.

## 107. Delete blank lines with sed

Display `multiline.txt` without blank lines.

## 108. Print a line range with sed

Display lines 3 through 6 from `app.log`.

## 109. Extract a configuration value

Print only the value assigned to `PORT`.

## 110. Save and display output with tee

Display severe log entries and save them to `workspace/severe.log`.

## 111. Use xargs to count lines

Count lines in every project Markdown file.

## 112. Use xargs with grep safely

Search every log file for ERROR using null-delimited paths.

## 113. Number every line

Display `paragraphs.txt` with line numbers.

## 114. Reverse line order

Display the application log from last line to first.

## 115. Reverse characters

Reverse the characters of each line in `names.txt`.

## 116. Verify duplicate contents

Calculate checksums for the suspected duplicate files.

## 117. Compare files byte by byte

Verify whether the two duplicate files are identical.

## 118. Show differences between reports

Compare January and February reports in unified format.

## 119. Inspect disk usage

Display the total apparent disk space used by each top-level practice directory.

## 120. Build a top-IP pipeline

Print the three most active IP addresses and request counts.
