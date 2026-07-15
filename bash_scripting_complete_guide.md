# Complete Bash Scripting Syllabus

Bash stands for **Bourne Again Shell**. It is both:

1. A command-line shell used to interact with Linux and Unix systems.
2. A scripting language used to automate commands, file operations, server administration, deployments, backups, monitoring, and many other tasks.

---

# 1. Shell and Terminal Fundamentals

## 1.1 Terminal, shell, and Bash

These terms are related but different:

- **Terminal**: The graphical or text interface where you type commands.
- **Shell**: A program that interprets those commands.
- **Bash**: One particular shell.
- **Shell script**: A file containing shell commands.

Check your current shell:

```bash
echo "$SHELL"
```

Check the Bash version:

```bash
bash --version
```

Find Bash:

```bash
which bash
```

Common shells include:

```text
sh
bash
zsh
fish
ksh
dash
```

---

# 2. Basic Linux Commands Required for Bash

Before scripting, you should understand common terminal commands.

## Navigation

```bash
pwd
ls
cd /home/user
cd ..
cd ~
```

## File operations

```bash
touch file.txt
mkdir project
cp source.txt destination.txt
mv old.txt new.txt
rm file.txt
rm -r directory
```

## Reading files

```bash
cat file.txt
less file.txt
head file.txt
tail file.txt
```

## Searching

```bash
find . -name "*.txt"
grep "error" log.txt
```

## System information

```bash
whoami
hostname
date
uptime
df -h
free -h
```

Bash scripts usually combine commands like these into automated workflows.

---

# 3. Creating Your First Bash Script

Create a file:

```bash
nano hello.sh
```

Write:

```bash
#!/usr/bin/env bash

echo "Hello, Bash!"
```

The first line is called the **shebang**.

```bash
#!/usr/bin/env bash
```

It tells the operating system to execute the file using Bash.

Make the file executable:

```bash
chmod +x hello.sh
```

Run it:

```bash
./hello.sh
```

You may also run it without executable permission:

```bash
bash hello.sh
```

## Difference

```bash
./hello.sh
```

uses the interpreter specified in the shebang.

```bash
bash hello.sh
```

explicitly runs the file with Bash.

---

# 4. Comments

A comment begins with `#`.

```bash
# This is a comment
echo "Hello"
```

Inline comment:

```bash
name="Arko"  # Store the user's name
```

The shebang is technically a special interpreter directive:

```bash
#!/usr/bin/env bash
```

---

# 5. Commands and Exit Status

Every command returns an **exit status**.

- `0` means success.
- A non-zero value means failure.

Example:

```bash
mkdir test_directory
echo "$?"
```

Check a failed command:

```bash
ls nonexistent_file
echo "$?"
```

You can use exit statuses in conditions.

```bash
if mkdir project; then
    echo "Directory created"
else
    echo "Could not create directory"
fi
```

Terminate a script manually:

```bash
exit 0
```

Failure:

```bash
exit 1
```

---

# 6. Variables

## 6.1 Creating variables

Do not put spaces around `=`.

```bash
name="Arko"
age=25
```

Incorrect:

```bash
name = "Arko"
```

Bash interprets `name` as a command in the incorrect example.

## 6.2 Reading variables

```bash
echo "$name"
echo "$age"
```

Prefer braces when combining variables with text:

```bash
file="report"
echo "${file}.txt"
```

Without braces:

```bash
echo "$file.txt"
```

Bash may interpret `file.txt` incorrectly as part of the variable name.

## 6.3 Read-only variables

```bash
readonly country="India"
```

Trying to modify it causes an error:

```bash
country="Japan"
```

## 6.4 Removing variables

```bash
unset name
```

---

# 7. Environment Variables

Environment variables are available to programs started by the shell.

Common environment variables:

```bash
echo "$HOME"
echo "$USER"
echo "$PATH"
echo "$PWD"
echo "$SHELL"
echo "$LANG"
```

Create a shell variable:

```bash
name="Arko"
```

Export it to child processes:

```bash
export name
```

Or create and export it together:

```bash
export APP_ENV="production"
```

Run a command with a temporary environment variable:

```bash
APP_ENV="testing" ./app.sh
```

Display environment variables:

```bash
env
```

or:

```bash
printenv
```

---

# 8. Quoting

Quoting is one of the most important Bash topics.

## 8.1 Double quotes

Variables and command substitutions are expanded.

```bash
name="Arko"
echo "Hello, $name"
```

Output:

```text
Hello, Arko
```

## 8.2 Single quotes

Everything is treated literally.

```bash
echo 'Hello, $name'
```

Output:

```text
Hello, $name
```

## 8.3 No quotes

Unquoted variables undergo word splitting and filename expansion.

```bash
message="Hello world"
echo $message
```

This may work, but it becomes dangerous with filenames and special characters.

Prefer:

```bash
echo "$message"
```

## 8.4 Escape character

```bash
echo "He said, \"Hello\""
```

New line:

```bash
printf "First line\nSecond line\n"
```

Tab:

```bash
printf "Name\tAge\n"
```

---

# 9. Reading User Input

Basic input:

```bash
read name
echo "Hello, $name"
```

Display a prompt:

```bash
read -p "Enter your name: " name
echo "Hello, $name"
```

Silent input, useful for passwords:

```bash
read -s -p "Enter password: " password
echo
```

Read multiple values:

```bash
read -p "Enter first and last name: " first_name last_name
```

Read with a timeout:

```bash
read -t 10 -p "Enter your name within 10 seconds: " name
```

Preserve backslashes:

```bash
IFS= read -r line
```

This is the recommended form when reading arbitrary text.

---

# 10. Command-Line Arguments

Suppose a script is run like this:

```bash
./user.sh Arko 25 India
```

Inside the script:

```bash
echo "$0"
echo "$1"
echo "$2"
echo "$3"
```

Special positional parameters:

| Parameter | Meaning |
|---|---|
| `$0` | Script name |
| `$1` | First argument |
| `$2` | Second argument |
| `$#` | Number of arguments |
| `$@` | All arguments, individually preserved |
| `$*` | All arguments combined |
| `$$` | Current process ID |
| `$?` | Previous command's exit status |
| `$!` | Process ID of the latest background process |

Example:

```bash
#!/usr/bin/env bash

echo "Script: $0"
echo "First argument: $1"
echo "Number of arguments: $#"
```

Loop through all arguments:

```bash
for argument in "$@"; do
    echo "$argument"
done
```

Use `"$@"` instead of `$@` in most situations because it preserves each argument correctly.

---

# 11. The `shift` Command

`shift` removes the first positional argument.

```bash
echo "$1"
shift
echo "$1"
```

Example:

```bash
while [[ $# -gt 0 ]]; do
    echo "Processing: $1"
    shift
done
```

This is useful for processing command-line options.

---

# 12. Output with `echo` and `printf`

## `echo`

```bash
echo "Hello"
```

Suppress the final newline:

```bash
echo -n "Loading..."
```

However, `echo` behavior can vary between systems.

## `printf`

`printf` is more reliable.

```bash
printf "Hello, %s\n" "$name"
```

Formatting numbers:

```bash
price=12
printf "Price: ₹%d\n" "$price"
```

Floating-point format:

```bash
printf "%.2f\n" 12.3456
```

Formatted columns:

```bash
printf "%-15s %5s\n" "Name" "Age"
printf "%-15s %5d\n" "Arko" 25
```

---

# 13. Arithmetic Operations

## 13.1 Arithmetic expansion

```bash
a=10
b=5

result=$((a + b))
echo "$result"
```

Operations:

```bash
echo $((a + b))
echo $((a - b))
echo $((a * b))
echo $((a / b))
echo $((a % b))
echo $((a ** b))
```

Bash performs integer arithmetic by default.

```bash
echo $((5 / 2))
```

Output:

```text
2
```

## 13.2 Increment and decrement

```bash
((count++))
((count--))
((count += 5))
```

Be careful with `set -e` and post-increment because `((count++))` returns failure when the original value is zero.

A safer form is:

```bash
((++count))
```

## 13.3 `let`

```bash
let "result = a + b"
```

Arithmetic expansion is generally preferred:

```bash
result=$((a + b))
```

## 13.4 Decimal calculations

Use `bc`:

```bash
result=$(echo "scale=2; 5 / 2" | bc)
echo "$result"
```

---

# 14. Command Substitution

Command substitution stores command output.

Modern syntax:

```bash
current_date=$(date)
echo "$current_date"
```

Store the number of files:

```bash
file_count=$(find . -maxdepth 1 -type f | wc -l)
```

Old syntax:

```bash
current_date=`date`
```

Prefer `$(...)` because it is easier to read and nest.

Nested substitution:

```bash
echo "$(basename "$(pwd)")"
```

---

# 15. Conditional Statements

## 15.1 Basic `if`

```bash
age=20

if [[ $age -ge 18 ]]; then
    echo "Adult"
fi
```

## 15.2 `if-else`

```bash
if [[ $age -ge 18 ]]; then
    echo "Adult"
else
    echo "Minor"
fi
```

## 15.3 `if-elif-else`

```bash
marks=75

if [[ $marks -ge 90 ]]; then
    echo "Grade A"
elif [[ $marks -ge 70 ]]; then
    echo "Grade B"
elif [[ $marks -ge 50 ]]; then
    echo "Grade C"
else
    echo "Fail"
fi
```

---

# 16. Test Commands

Bash provides three major condition styles.

## 16.1 Single brackets

```bash
if [ "$age" -ge 18 ]; then
    echo "Adult"
fi
```

Spaces are mandatory:

```bash
[ "$age" -ge 18 ]
```

This is incorrect:

```bash
["$age" -ge 18]
```

## 16.2 Double brackets

```bash
if [[ $age -ge 18 ]]; then
    echo "Adult"
fi
```

`[[ ... ]]` is safer and more powerful in Bash.

It supports:

- Pattern matching
- Regular expressions
- Safer variable handling
- Logical operators

## 16.3 Arithmetic condition

```bash
if (( age >= 18 )); then
    echo "Adult"
fi
```

This is best for integer arithmetic.

---

# 17. Comparison Operators

## Numeric operators

| Operator | Meaning |
|---|---|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-gt` | Greater than |
| `-ge` | Greater than or equal |
| `-lt` | Less than |
| `-le` | Less than or equal |

Example:

```bash
if [[ $a -gt $b ]]; then
    echo "a is greater"
fi
```

With arithmetic syntax:

```bash
if (( a > b )); then
    echo "a is greater"
fi
```

## String operators

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `<` | Alphabetically smaller |
| `>` | Alphabetically greater |
| `-z` | Empty string |
| `-n` | Non-empty string |

Examples:

```bash
if [[ $name == "Arko" ]]; then
    echo "Name matched"
fi
```

```bash
if [[ -z $name ]]; then
    echo "Name is empty"
fi
```

```bash
if [[ -n $name ]]; then
    echo "Name is not empty"
fi
```

---

# 18. Logical Operators

## AND

```bash
if [[ $age -ge 18 && $country == "India" ]]; then
    echo "Condition matched"
fi
```

Command-level AND:

```bash
mkdir project && cd project
```

The second command runs only when the first succeeds.

## OR

```bash
if [[ $role == "admin" || $role == "manager" ]]; then
    echo "Access allowed"
fi
```

Command-level OR:

```bash
mkdir project || echo "Could not create directory"
```

## NOT

```bash
if [[ ! -f config.txt ]]; then
    echo "Configuration file is missing"
fi
```

---

# 19. File Test Operators

| Test | Meaning |
|---|---|
| `-e file` | Path exists |
| `-f file` | Regular file |
| `-d file` | Directory |
| `-r file` | Readable |
| `-w file` | Writable |
| `-x file` | Executable |
| `-s file` | File exists and is not empty |
| `-L file` | Symbolic link |
| `file1 -nt file2` | File 1 is newer |
| `file1 -ot file2` | File 1 is older |

Example:

```bash
file="data.txt"

if [[ -f $file ]]; then
    echo "Regular file exists"
else
    echo "File does not exist"
fi
```

Directory check:

```bash
if [[ -d /var/log ]]; then
    echo "Log directory exists"
fi
```

---

# 20. `case` Statements

`case` is useful when comparing one value against many patterns.

```bash
read -p "Enter an option: " option

case $option in
    start)
        echo "Starting service"
        ;;
    stop)
        echo "Stopping service"
        ;;
    restart)
        echo "Restarting service"
        ;;
    *)
        echo "Unknown option"
        ;;
esac
```

Multiple patterns:

```bash
case $answer in
    yes|y|Y)
        echo "Confirmed"
        ;;
    no|n|N)
        echo "Cancelled"
        ;;
    *)
        echo "Invalid answer"
        ;;
esac
```

---

# 21. Loops

## 21.1 `for` loop

```bash
for number in 1 2 3 4 5; do
    echo "$number"
done
```

Range:

```bash
for number in {1..5}; do
    echo "$number"
done
```

C-style loop:

```bash
for ((i = 1; i <= 5; i++)); do
    echo "$i"
done
```

Loop through files:

```bash
for file in *.txt; do
    echo "Processing: $file"
done
```

Safer version when no file matches:

```bash
shopt -s nullglob

for file in *.txt; do
    echo "Processing: $file"
done
```

## 21.2 `while` loop

```bash
count=1

while (( count <= 5 )); do
    echo "$count"
    ((++count))
done
```

## 21.3 `until` loop

Runs until the condition becomes true.

```bash
count=1

until (( count > 5 )); do
    echo "$count"
    ((++count))
done
```

## 21.4 Infinite loop

```bash
while true; do
    echo "Running..."
    sleep 1
done
```

Stop it with `Ctrl+C`.

---

# 22. `break` and `continue`

## `break`

Stops the loop.

```bash
for number in {1..10}; do
    if (( number == 5 )); then
        break
    fi

    echo "$number"
done
```

## `continue`

Skips the current iteration.

```bash
for number in {1..5}; do
    if (( number == 3 )); then
        continue
    fi

    echo "$number"
done
```

---

# 23. Reading Files Line by Line

Recommended pattern:

```bash
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

Why use this?

- `IFS=` prevents trimming whitespace.
- `-r` prevents backslash interpretation.
- Redirection avoids unnecessary processes.

Read a file whose final line may not end with a newline:

```bash
while IFS= read -r line || [[ -n $line ]]; do
    echo "$line"
done < file.txt
```

Read comma-separated data:

```bash
while IFS=',' read -r name age city; do
    printf "Name: %s, Age: %s, City: %s\n" "$name" "$age" "$city"
done < users.csv
```

For complicated CSV files containing quoted commas, use a proper CSV parser rather than plain `IFS`.

---

# 24. Functions

Basic function:

```bash
greet() {
    echo "Hello"
}

greet
```

Alternative syntax:

```bash
function greet {
    echo "Hello"
}
```

The first style is more portable:

```bash
greet() {
    echo "Hello"
}
```

## Function arguments

```bash
greet() {
    local name=$1
    echo "Hello, $name"
}

greet "Arko"
```

Inside a function:

- `$1` is the first function argument.
- `$#` is the number of function arguments.
- `"$@"` represents all function arguments.

## Local variables

```bash
calculate() {
    local result
    result=$((10 + 20))
    echo "$result"
}
```

Without `local`, variables are global by default.

## Returning values

Bash functions return an exit status, not arbitrary text.

```bash
is_adult() {
    local age=$1

    if (( age >= 18 )); then
        return 0
    else
        return 1
    fi
}
```

Use it:

```bash
if is_adult 20; then
    echo "Adult"
fi
```

To return data, print it:

```bash
add() {
    local a=$1
    local b=$2

    echo $((a + b))
}

result=$(add 10 20)
echo "$result"
```

---

# 25. Indexed Arrays

Create an array:

```bash
fruits=("apple" "banana" "mango")
```

Access an element:

```bash
echo "${fruits[0]}"
echo "${fruits[1]}"
```

All elements:

```bash
printf '%s\n' "${fruits[@]}"
```

Number of elements:

```bash
echo "${#fruits[@]}"
```

Add an element:

```bash
fruits+=("orange")
```

Change an element:

```bash
fruits[1]="grape"
```

Remove an element:

```bash
unset 'fruits[1]'
```

Loop through array values:

```bash
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done
```

Loop through indexes:

```bash
for index in "${!fruits[@]}"; do
    echo "$index: ${fruits[$index]}"
done
```

Array slicing:

```bash
echo "${fruits[@]:1:2}"
```

---

# 26. Associative Arrays

Associative arrays use named keys.

They require modern Bash.

```bash
declare -A user

user[name]="Arko"
user[age]="25"
user[country]="India"
```

Access values:

```bash
echo "${user[name]}"
```

Loop through keys:

```bash
for key in "${!user[@]}"; do
    echo "$key = ${user[$key]}"
done
```

Check whether a key exists:

```bash
if [[ -v 'user[name]' ]]; then
    echo "Name exists"
fi
```

---

# 27. String Manipulation

```bash
text="Hello Bash World"
```

## String length

```bash
echo "${#text}"
```

## Substring

```bash
echo "${text:0:5}"
```

Output:

```text
Hello
```

## Replace first match

```bash
echo "${text/Bash/Linux}"
```

## Replace all matches

```bash
value="one one one"
echo "${value//one/two}"
```

## Remove prefix

```bash
filename="report.final.txt"
echo "${filename#*.}"
```

Output:

```text
final.txt
```

Remove the longest matching prefix:

```bash
echo "${filename##*.}"
```

Output:

```text
txt
```

## Remove suffix

```bash
echo "${filename%.*}"
```

Output:

```text
report.final
```

Remove the longest matching suffix:

```bash
path="/home/user/report.txt"
echo "${path%%/*}"
```

Pattern behavior depends on the supplied pattern.

## Uppercase and lowercase

```bash
name="arko"

echo "${name^^}"
echo "${name^}"
```

```bash
name="ARKO"

echo "${name,,}"
echo "${name,}"
```

---

# 28. Parameter Expansion

Parameter expansion provides defaults and validation.

## Default value

```bash
echo "${name:-Guest}"
```

Use `Guest` when `name` is unset or empty.

## Assign default value

```bash
name="${name:=Guest}"
```

## Alternative value

```bash
echo "${name:+Name was provided}"
```

## Required variable

```bash
database_url="${DATABASE_URL:?DATABASE_URL is required}"
```

The script exits with an error when the variable is unset or empty.

## Difference between `-` and `:-`

```bash
${variable-default}
```

Uses the default only when the variable is unset.

```bash
${variable:-default}
```

Uses the default when the variable is unset or empty.

---

# 29. Shell Expansion Order

Bash processes command text through several expansions.

Important expansion types include:

1. Brace expansion
2. Tilde expansion
3. Parameter expansion
4. Arithmetic expansion
5. Command substitution
6. Word splitting
7. Filename expansion
8. Quote removal

Example:

```bash
echo file{1..3}.txt
```

Brace expansion creates:

```text
file1.txt file2.txt file3.txt
```

Example of word splitting:

```bash
value="one two three"
printf '<%s>\n' $value
```

This becomes three arguments.

Quoted:

```bash
printf '<%s>\n' "$value"
```

This remains one argument.

Understanding expansion explains many Bash errors.

---

# 30. Wildcards and Globbing

## `*`

Matches any number of characters.

```bash
ls *.txt
```

## `?`

Matches exactly one character.

```bash
ls file?.txt
```

## Character class

```bash
ls file[0-9].txt
```

## Negated character class

```bash
ls file[!0-9].txt
```

## Extended globbing

Enable it:

```bash
shopt -s extglob
```

Examples:

```bash
ls +(file).txt
ls @(one|two).txt
ls !(temporary).txt
```

Extended patterns include:

| Pattern | Meaning |
|---|---|
| `?(pattern)` | Zero or one |
| `*(pattern)` | Zero or more |
| `+(pattern)` | One or more |
| `@(pattern)` | Exactly one |
| `!(pattern)` | Anything except pattern |

---

# 31. Regular Expressions

Bash supports regular expressions inside `[[ ... =~ ... ]]`.

```bash
email="user@example.com"

if [[ $email =~ ^[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}$ ]]; then
    echo "Valid format"
else
    echo "Invalid format"
fi
```

Captured groups are stored in `BASH_REMATCH`.

```bash
date_value="2026-07-15"

if [[ $date_value =~ ^([0-9]{4})-([0-9]{2})-([0-9]{2})$ ]]; then
    echo "Year: ${BASH_REMATCH[1]}"
    echo "Month: ${BASH_REMATCH[2]}"
    echo "Day: ${BASH_REMATCH[3]}"
fi
```

Do not quote the regular expression variable incorrectly when using `=~`, because quoting changes matching behavior.

---

# 32. Input and Output Streams

Every command normally has three standard streams.

| Number | Stream |
|---|---|
| `0` | Standard input |
| `1` | Standard output |
| `2` | Standard error |

## Redirect output

```bash
echo "Hello" > output.txt
```

This overwrites the file.

Append:

```bash
echo "Hello" >> output.txt
```

## Redirect errors

```bash
ls missing.txt 2> error.log
```

Append errors:

```bash
ls missing.txt 2>> error.log
```

## Redirect output and errors

```bash
command > output.log 2>&1
```

Modern Bash:

```bash
command &> output.log
```

Append both:

```bash
command &>> output.log
```

## Discard output

```bash
command > /dev/null
```

Discard output and errors:

```bash
command > /dev/null 2>&1
```

---

# 33. Pipelines

A pipe sends one command's output to another command's input.

```bash
cat access.log | grep "ERROR"
```

A better form:

```bash
grep "ERROR" access.log
```

Multiple commands:

```bash
grep "ERROR" application.log | sort | uniq -c
```

Count running Bash processes:

```bash
ps aux | grep '[b]ash' | wc -l
```

By default, a pipeline's status is usually the status of its final command.

Enable `pipefail`:

```bash
set -o pipefail
```

Now the pipeline fails when an earlier pipeline command fails.

---

# 34. Here Documents

A here document provides multiline input.

```bash
cat <<EOF
Hello
This is a multiline message.
Current user: $USER
EOF
```

Variables expand because `EOF` is unquoted.

Prevent expansion:

```bash
cat <<'EOF'
The literal variable is $USER.
EOF
```

Write a configuration file:

```bash
cat > config.ini <<EOF
host=localhost
port=8080
environment=production
EOF
```

Indented here document with tabs:

```bash
cat <<-EOF
	This indentation may use tabs.
	EOF
```

---

# 35. Here Strings

A here string sends a string to a command's standard input.

```bash
grep "Bash" <<< "Hello Bash World"
```

Read words:

```bash
read -r first second <<< "Hello World"
```

---

# 36. Process Substitution

Process substitution treats command output like a temporary file.

```bash
diff <(sort file1.txt) <(sort file2.txt)
```

Input process substitution:

```bash
while IFS= read -r line; do
    echo "$line"
done < <(find . -type f)
```

Output process substitution:

```bash
command > >(tee output.log)
```

Process substitution is a Bash feature and may not work in basic `sh`.

---

# 37. Subshells and Command Groups

## Subshell

Commands inside parentheses run in a child shell.

```bash
(
    cd /tmp
    echo "Inside: $PWD"
)

echo "Outside: $PWD"
```

The directory change does not affect the parent shell.

## Current-shell group

```bash
{
    cd /tmp
    echo "Inside: $PWD"
}
```

This affects the current shell.

A semicolon or newline is required before `}`:

```bash
{ echo "Hello"; }
```

---

# 38. Processes and Background Jobs

Run a command in the background:

```bash
sleep 10 &
```

Get its process ID:

```bash
pid=$!
echo "$pid"
```

Wait for it:

```bash
wait "$pid"
```

Run multiple background tasks:

```bash
task_one &
pid1=$!

task_two &
pid2=$!

wait "$pid1"
wait "$pid2"
```

View jobs:

```bash
jobs
```

Bring a background job to the foreground:

```bash
fg %1
```

Resume a stopped job in the background:

```bash
bg %1
```

Terminate a process:

```bash
kill "$pid"
```

Force termination:

```bash
kill -9 "$pid"
```

Use force only when normal termination does not work.

---

# 39. Signals and `trap`

Signals notify processes about events.

Common signals:

| Signal | Meaning |
|---|---|
| `SIGINT` | Interrupt, usually `Ctrl+C` |
| `SIGTERM` | Request process termination |
| `SIGHUP` | Terminal disconnected or reload request |
| `SIGKILL` | Immediate termination; cannot be trapped |
| `EXIT` | Bash pseudo-signal when the script exits |

Cleanup example:

```bash
#!/usr/bin/env bash

temporary_file=$(mktemp)

cleanup() {
    rm -f "$temporary_file"
}

trap cleanup EXIT

echo "Temporary data" > "$temporary_file"
```

Handle interruption:

```bash
handle_interrupt() {
    echo
    echo "Script interrupted"
    exit 130
}

trap handle_interrupt INT
```

Handle several signals:

```bash
trap cleanup EXIT INT TERM
```

---

# 40. Error Handling

A professional Bash script should handle errors intentionally.

## Strict mode

```bash
set -Eeuo pipefail
```

Meaning:

- `-e`: Exit when an unhandled command fails.
- `-E`: Allow `ERR` traps to work in functions and subshell-related contexts.
- `-u`: Treat unset variables as errors.
- `pipefail`: Fail a pipeline when any command fails.

Example:

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

trap 'printf "Error on line %d\n" "$LINENO" >&2' ERR

input_file=${1:?Usage: script.sh INPUT_FILE}

if [[ ! -f $input_file ]]; then
    printf "File not found: %s\n" "$input_file" >&2
    exit 1
fi
```

## Important warning about `set -e`

`set -e` has many exceptions and should not replace proper error handling.

Use explicit checks when failure requires a particular response:

```bash
if ! cp "$source" "$destination"; then
    echo "Copy failed" >&2
    exit 1
fi
```

---

# 41. Debugging Bash Scripts

## Syntax check

```bash
bash -n script.sh
```

This checks syntax without executing commands.

## Trace execution

```bash
bash -x script.sh
```

Inside the script:

```bash
set -x
```

Disable tracing:

```bash
set +x
```

## Verbose mode

```bash
bash -v script.sh
```

## Custom trace format

```bash
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
set -x
```

## Print debugging

```bash
printf 'DEBUG: value=%q\n' "$value" >&2
```

`%q` displays a shell-safe representation.

## Static analysis

A widely used Bash analysis tool is ShellCheck.

Typical command:

```bash
shellcheck script.sh
```

It identifies quoting problems, unsafe patterns, unused variables, and portability issues.

---

# 42. `getopts` for Command-Line Options

Suppose a script accepts:

```bash
./backup.sh -s source -d destination -v
```

Implementation:

```bash
#!/usr/bin/env bash

set -u

source_directory=""
destination_directory=""
verbose=false

usage() {
    echo "Usage: $0 -s SOURCE -d DESTINATION [-v]"
}

while getopts ":s:d:vh" option; do
    case $option in
        s)
            source_directory=$OPTARG
            ;;
        d)
            destination_directory=$OPTARG
            ;;
        v)
            verbose=true
            ;;
        h)
            usage
            exit 0
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

shift $((OPTIND - 1))

if [[ -z $source_directory || -z $destination_directory ]]; then
    usage >&2
    exit 1
fi

if [[ $verbose == true ]]; then
    echo "Source: $source_directory"
    echo "Destination: $destination_directory"
fi
```

A colon after an option means that option requires a value:

```bash
"s:d:vh"
```

Here, `s` and `d` require values; `v` and `h` do not.

---

# 43. Temporary Files and Directories

Do not create predictable temporary filenames like this:

```bash
temporary_file="/tmp/my-script.tmp"
```

Another process may interfere with it.

Use `mktemp`:

```bash
temporary_file=$(mktemp)
```

Temporary directory:

```bash
temporary_directory=$(mktemp -d)
```

Cleanup:

```bash
cleanup() {
    rm -rf -- "$temporary_directory"
}

trap cleanup EXIT
```

Be extremely careful with `rm -rf`.

Validate the path first:

```bash
if [[ -n $temporary_directory && -d $temporary_directory ]]; then
    rm -rf -- "$temporary_directory"
fi
```

---

# 44. File Descriptors

Bash can open additional file descriptors.

Open a file for reading:

```bash
exec 3< input.txt
```

Read from descriptor 3:

```bash
while IFS= read -r line <&3; do
    echo "$line"
done
```

Close it:

```bash
exec 3<&-
```

Open a log file for writing:

```bash
exec 4>> application.log
```

Write to it:

```bash
echo "Application started" >&4
```

Close:

```bash
exec 4>&-
```

Redirect the entire script's output:

```bash
exec > script.log 2>&1
```

Everything afterward goes to `script.log`.

---

# 45. `readarray` and `mapfile`

Read file lines into an array:

```bash
mapfile -t lines < file.txt
```

or:

```bash
readarray -t lines < file.txt
```

Print them:

```bash
printf '%s\n' "${lines[@]}"
```

The `-t` option removes trailing newline characters.

Read command output safely:

```bash
mapfile -t files < <(find . -type f -name '*.txt')
```

This is safer than:

```bash
files=($(find . -type f))
```

because command substitution with unquoted array assignment breaks filenames containing spaces and newlines.

---

# 46. Important Text-Processing Commands

Bash itself is often combined with external text-processing tools.

## `grep`

Search for text:

```bash
grep "error" app.log
```

Case-insensitive:

```bash
grep -i "error" app.log
```

Recursive:

```bash
grep -R "TODO" .
```

Show line numbers:

```bash
grep -n "error" app.log
```

Extended regular expression:

```bash
grep -E "error|warning" app.log
```

## `sed`

Replace text:

```bash
sed 's/old/new/' file.txt
```

Replace all occurrences per line:

```bash
sed 's/old/new/g' file.txt
```

Modify a file:

```bash
sed -i 's/development/production/g' config.txt
```

Delete empty lines:

```bash
sed '/^$/d' file.txt
```

## `awk`

Print columns:

```bash
awk '{print $1, $3}' file.txt
```

Specify a delimiter:

```bash
awk -F',' '{print $1, $2}' users.csv
```

Filter records:

```bash
awk '$3 > 50 {print $1, $3}' marks.txt
```

Sum a column:

```bash
awk '{sum += $2} END {print sum}' data.txt
```

## `cut`

```bash
cut -d',' -f1,3 users.csv
```

## `sort`

```bash
sort names.txt
sort -n numbers.txt
sort -r names.txt
```

## `uniq`

```bash
sort names.txt | uniq
sort names.txt | uniq -c
```

## `tr`

Convert lowercase to uppercase:

```bash
tr '[:lower:]' '[:upper:]' < file.txt
```

Delete characters:

```bash
tr -d '\r' < windows_file.txt
```

## `xargs`

```bash
find . -name "*.tmp" -print0 | xargs -0 rm -f
```

For many tasks, `find -exec` is safer:

```bash
find . -name "*.tmp" -exec rm -f -- {} +
```

---

# 47. The `find` Command

Find files by name:

```bash
find . -name "*.txt"
```

Case-insensitive:

```bash
find . -iname "*.jpg"
```

Find directories:

```bash
find . -type d
```

Find files larger than 100 MB:

```bash
find . -type f -size +100M
```

Find files modified in the last seven days:

```bash
find . -type f -mtime -7
```

Execute a command:

```bash
find . -type f -name "*.log" -exec gzip -- {} +
```

Delete matching files:

```bash
find /tmp -type f -name "*.tmp" -delete
```

Always verify the matching results before using `-delete`.

---

# 48. Permissions and Ownership

Linux permissions:

```text
r = read
w = write
x = execute
```

Display permissions:

```bash
ls -l
```

Make a script executable:

```bash
chmod +x script.sh
```

Numeric permissions:

```bash
chmod 755 script.sh
chmod 644 config.txt
```

Meaning:

- `7 = rwx`
- `6 = rw-`
- `5 = r-x`
- `4 = r--`

Change owner:

```bash
sudo chown user:group file.txt
```

Check permissions in Bash:

```bash
if [[ -x script.sh ]]; then
    echo "Script is executable"
fi
```

---

# 49. User and Privilege Checks

Check whether the script is running as root:

```bash
if (( EUID != 0 )); then
    echo "This script must be run as root." >&2
    exit 1
fi
```

Current username:

```bash
whoami
```

Current user ID:

```bash
id -u
```

Group information:

```bash
id
```

Avoid running complete scripts as root when only one command requires elevated privileges.

Prefer:

```bash
sudo systemctl restart nginx
```

instead of running an entire large script under `sudo`.

---

# 50. Networking Commands

Check connectivity:

```bash
ping -c 4 example.com
```

Download a file:

```bash
curl -O https://example.com/file.txt
```

Save with another name:

```bash
curl -o output.txt https://example.com/file.txt
```

Fail on HTTP errors:

```bash
curl --fail --silent --show-error https://example.com
```

API request:

```bash
curl \
    --fail \
    --silent \
    --show-error \
    --header "Accept: application/json" \
    https://api.example.com/users
```

Check a port:

```bash
nc -zv localhost 8080
```

DNS lookup:

```bash
dig example.com
```

Display listening ports:

```bash
ss -tuln
```

---

# 51. JSON Processing with `jq`

API responses commonly use JSON.

Example JSON:

```json
{
  "name": "Arko",
  "age": 25
}
```

Extract a field:

```bash
jq -r '.name' user.json
```

From an API:

```bash
name=$(
    curl --fail --silent --show-error https://api.example.com/user |
    jq -r '.name'
)
```

Loop through an array:

```bash
jq -r '.users[].name' users.json
```

Generate JSON safely:

```bash
jq -n \
    --arg name "$name" \
    --arg city "$city" \
    '{name: $name, city: $city}'
```

Do not manually concatenate untrusted values into JSON.

---

# 52. Date and Time Operations

Current date:

```bash
date
```

Formatted date:

```bash
date '+%Y-%m-%d'
```

Formatted timestamp:

```bash
date '+%Y-%m-%d %H:%M:%S'
```

Filename timestamp:

```bash
timestamp=$(date '+%Y%m%d_%H%M%S')
backup_file="backup_${timestamp}.tar.gz"
```

Unix timestamp:

```bash
date +%s
```

Measure duration:

```bash
start_time=$(date +%s)

sleep 2

end_time=$(date +%s)
duration=$((end_time - start_time))

echo "Duration: ${duration}s"
```

Date syntax varies between GNU/Linux and BSD/macOS, so scripts using complex `date` calculations may require platform-specific handling.

---

# 53. Logging

Create reusable logging functions:

```bash
log_info() {
    printf '[%s] [INFO] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
}

log_error() {
    printf '[%s] [ERROR] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >&2
}
```

Use them:

```bash
log_info "Backup started"

if ! cp source.txt destination.txt; then
    log_error "Backup failed"
    exit 1
fi
```

Write output to the terminal and a file:

```bash
exec > >(tee -a application.log) 2>&1
```

Be aware that process substitution may make output handling asynchronous in some cases.

---

# 54. Configuration Files

Simple environment-style file:

```bash
APP_PORT=8080
APP_ENV=production
```

Load it:

```bash
source config.env
```

or:

```bash
. config.env
```

However, `source` executes the file as Bash code. Only source trusted files.

A safer simple parser:

```bash
while IFS='=' read -r key value; do
    [[ -z $key || $key == \#* ]] && continue

    case $key in
        APP_PORT)
            app_port=$value
            ;;
        APP_ENV)
            app_env=$value
            ;;
    esac
done < config.env
```

For JSON, YAML, or TOML, use appropriate parsers.

---

# 55. Scheduling Scripts

## Cron

Edit your crontab:

```bash
crontab -e
```

Run every day at 2:30 AM:

```cron
30 2 * * * /home/user/backup.sh >> /home/user/backup.log 2>&1
```

Cron format:

```text
minute hour day-of-month month day-of-week command
```

Example:

```cron
0 9 * * 1-5 /home/user/report.sh
```

This runs at 9:00 AM from Monday to Friday.

Cron has a limited environment. Use absolute paths:

```bash
/usr/bin/python3
/bin/cp
/home/user/script.sh
```

Set `PATH` explicitly when necessary.

## Systemd timers

For modern Linux servers, systemd timers provide better logging, dependency management, and service control than cron.

A service file runs the script, and a timer file defines the schedule.

---

# 56. Locking and Preventing Duplicate Execution

A scheduled script may start again before its previous execution finishes.

Use `flock`:

```bash
flock -n /tmp/backup.lock ./backup.sh
```

Inside a script:

```bash
exec 9>/tmp/backup.lock

if ! flock -n 9; then
    echo "Another instance is already running." >&2
    exit 1
fi
```

For multi-user systems, choose a secure lock-file location and permissions.

---

# 57. Security Principles

## Always quote variables

Unsafe:

```bash
rm $file
```

Safer:

```bash
rm -- "$file"
```

The `--` marks the end of command options. It protects against filenames beginning with `-`.

## Never use `eval` with untrusted data

Dangerous:

```bash
eval "$user_input"
```

The input could execute arbitrary commands.

## Avoid building commands as strings

Unsafe:

```bash
command="grep $pattern $file"
$command
```

Use an array:

```bash
command=(grep -- "$pattern" "$file")
"${command[@]}"
```

## Validate input

```bash
if [[ ! $port =~ ^[0-9]+$ ]] || (( port < 1 || port > 65535 )); then
    echo "Invalid port" >&2
    exit 1
fi
```

## Use secure temporary files

```bash
temporary_file=$(mktemp)
```

## Avoid exposing secrets

Do not print passwords or API tokens.

Do not enable tracing around secrets:

```bash
set +x
token=$(get_secret)
set -x
```

## Control permissions

```bash
umask 077
```

New files will be accessible only to the owner unless permissions are changed.

---

# 58. Portability

A Bash script may not work in `sh`, `dash`, or other shells.

Bash-specific features include:

- `[[ ... ]]`
- Arrays
- Associative arrays
- Process substitution
- `mapfile`
- `shopt`
- `=~`
- Brace ranges in some contexts

Use this for Bash scripts:

```bash
#!/usr/bin/env bash
```

Use this for portable POSIX shell scripts:

```bash
#!/bin/sh
```

Do not claim a script is POSIX-compatible while using Bash-only features.

Check portability with:

```bash
shellcheck -s sh script.sh
```

---

# 59. Performance Considerations

Bash is excellent for:

- Running commands
- Connecting programs
- File automation
- System administration
- Small and medium automation scripts

Bash is not ideal for:

- Large data structures
- Complex application logic
- Heavy numerical computation
- High-performance text processing
- Complex concurrent systems

Avoid unnecessary external processes inside large loops.

Less efficient:

```bash
while IFS= read -r line; do
    uppercase=$(echo "$line" | tr '[:lower:]' '[:upper:]')
    echo "$uppercase"
done < file.txt
```

For large files, use one `awk` process:

```bash
awk '{print toupper($0)}' file.txt
```

For large or complicated programs, Python, Go, or another language may be more appropriate.

---

# 60. Script Structure and Best Practices

A professional script often follows this structure:

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_NAME=${0##*/}

usage() {
    cat <<EOF
Usage: $SCRIPT_NAME INPUT OUTPUT

Copy INPUT to OUTPUT.
EOF
}

log_error() {
    printf 'ERROR: %s\n' "$*" >&2
}

cleanup() {
    :
}

main() {
    if (( $# != 2 )); then
        usage >&2
        return 2
    fi

    local input_file=$1
    local output_file=$2

    if [[ ! -f $input_file ]]; then
        log_error "Input file does not exist: $input_file"
        return 1
    fi

    cp -- "$input_file" "$output_file"
    printf 'Copied %s to %s\n' "$input_file" "$output_file"
}

trap cleanup EXIT
main "$@"
```

Important practices:

- Use a shebang.
- Quote variable expansions.
- Use `local` inside functions.
- Use meaningful variable names.
- Send error messages to standard error.
- Return meaningful exit statuses.
- Put main logic inside `main`.
- Validate arguments.
- Clean up temporary resources with `trap`.
- Use `shellcheck`.
- Format scripts consistently.

---

# 61. Common Bash Mistakes

## Mistake 1: Spaces around assignment

Wrong:

```bash
name = "Arko"
```

Correct:

```bash
name="Arko"
```

## Mistake 2: Unquoted variables

Unsafe:

```bash
cp $source $destination
```

Correct:

```bash
cp -- "$source" "$destination"
```

## Mistake 3: Parsing `ls`

Wrong:

```bash
for file in $(ls); do
    echo "$file"
done
```

Correct:

```bash
for file in *; do
    echo "$file"
done
```

## Mistake 4: Reading lines with `for`

Wrong:

```bash
for line in $(cat file.txt); do
    echo "$line"
done
```

Correct:

```bash
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

## Mistake 5: Testing strings with arithmetic operators

Wrong:

```bash
[[ $name -eq "Arko" ]]
```

Correct:

```bash
[[ $name == "Arko" ]]
```

## Mistake 6: Using `$?` unnecessarily

Less clear:

```bash
grep "error" file.txt
if [[ $? -eq 0 ]]; then
    echo "Found"
fi
```

Better:

```bash
if grep -q "error" file.txt; then
    echo "Found"
fi
```

## Mistake 7: Losing variable changes in a pipeline

Problem:

```bash
count=0

printf '%s\n' a b c |
while read -r line; do
    ((++count))
done

echo "$count"
```

The loop may run in a subshell, so `count` remains unchanged.

Better:

```bash
count=0

while read -r line; do
    ((++count))
done < <(printf '%s\n' a b c)

echo "$count"
```

---

# 62. Advanced Bash Topics

After mastering the fundamentals, study these advanced subjects.

## Namerefs

```bash
change_value() {
    local -n reference=$1
    reference="changed"
}

value="original"
change_value value
echo "$value"
```

`local -n` creates a reference to another variable.

## Dynamic arrays

```bash
declare -a values=()

values+=("one")
values+=("two")
```

## Coprocesses

```bash
coproc worker {
    while IFS= read -r line; do
        echo "Processed: $line"
    done
}
```

Coprocesses allow bidirectional communication with a background command, but they require careful file-descriptor handling.

## Bash built-ins

Learn:

```bash
type
command
builtin
declare
local
readonly
export
source
eval
exec
caller
help
```

Check whether something is an alias, function, built-in, or external command:

```bash
type cd
type grep
```

Find all interpretations:

```bash
type -a echo
```

## Shell options

View options:

```bash
set -o
```

Enable an option:

```bash
set -o nounset
```

Disable it:

```bash
set +o nounset
```

Bash-specific options:

```bash
shopt
```

Examples:

```bash
shopt -s nullglob
shopt -s globstar
shopt -s extglob
```

Recursive globbing:

```bash
shopt -s globstar

for file in **/*.txt; do
    echo "$file"
done
```

---

# 63. Testing Bash Scripts

## Basic function test

```bash
add() {
    echo $(($1 + $2))
}

actual=$(add 2 3)
expected=5

if [[ $actual == "$expected" ]]; then
    echo "PASS"
else
    echo "FAIL: expected $expected, got $actual"
    exit 1
fi
```

## Test temporary directories

```bash
test_directory=$(mktemp -d)
trap 'rm -rf -- "$test_directory"' EXIT
```

Run tests without affecting real files.

## Test edge cases

Test scripts with:

- Empty strings
- Spaces in filenames
- Filenames beginning with `-`
- Missing arguments
- Invalid arguments
- Missing files
- Permission errors
- Failed commands
- Interrupted execution
- Very large input
- Special characters
- Newlines in data

Popular Bash testing frameworks include Bats and ShellSpec.

---

# 64. Real-World Project Progression

## Beginner projects

1. Calculator
2. Number guessing game
3. File existence checker
4. Interactive menu
5. System-information script
6. File-renaming script
7. Directory organizer
8. Password generator
9. Word and line counter
10. Basic log searcher

## Intermediate projects

1. Automated backup script
2. Log rotation system
3. Website health checker
4. Disk-space monitor
5. User-management script
6. Batch image or file converter
7. CSV report generator
8. Service-control utility
9. Duplicate-file detector
10. Command-line task manager

## Advanced projects

1. Deployment automation system
2. Server bootstrap script
3. Multi-server SSH automation
4. Database backup and restoration tool
5. Docker management utility
6. CI/CD helper scripts
7. Application monitoring daemon
8. Secure secrets-loading utility
9. Parallel job runner
10. Complete command-line application with options, logging, locking, configuration, and tests

---

# 65. Example: Complete Backup Script

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_NAME=${0##*/}
readonly TIMESTAMP=$(date '+%Y%m%d_%H%M%S')

source_directory=""
destination_directory=""
verbose=false

usage() {
    cat <<EOF
Usage:
  $SCRIPT_NAME -s SOURCE -d DESTINATION [-v]

Options:
  -s SOURCE       Directory to back up
  -d DESTINATION  Directory where backup will be stored
  -v              Enable verbose output
  -h              Show this help message
EOF
}

log() {
    if [[ $verbose == true ]]; then
        printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
    fi
}

fail() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 1
}

cleanup() {
    if [[ -n ${temporary_file:-} && -f $temporary_file ]]; then
        rm -f -- "$temporary_file"
    fi
}

trap cleanup EXIT
trap 'fail "Unexpected error on line $LINENO"' ERR

while getopts ":s:d:vh" option; do
    case $option in
        s)
            source_directory=$OPTARG
            ;;
        d)
            destination_directory=$OPTARG
            ;;
        v)
            verbose=true
            ;;
        h)
            usage
            exit 0
            ;;
        :)
            fail "Option -$OPTARG requires an argument."
            ;;
        \?)
            fail "Unknown option: -$OPTARG"
            ;;
    esac
done

[[ -n $source_directory ]] ||
    fail "Source directory is required."

[[ -n $destination_directory ]] ||
    fail "Destination directory is required."

[[ -d $source_directory ]] ||
    fail "Source directory does not exist: $source_directory"

mkdir -p -- "$destination_directory"

backup_name="$(basename "$source_directory")_${TIMESTAMP}.tar.gz"
backup_path="${destination_directory}/${backup_name}"

temporary_file=$(mktemp)

log "Creating backup"
log "Source: $source_directory"
log "Destination: $backup_path"

tar -czf "$temporary_file" -C "$(dirname "$source_directory")" \
    "$(basename "$source_directory")"

mv -- "$temporary_file" "$backup_path"
temporary_file=""

printf 'Backup created successfully: %s\n' "$backup_path"
```

Usage:

```bash
chmod +x backup.sh
./backup.sh -s /home/user/documents -d /home/user/backups -v
```

This example combines:

- Strict mode
- Functions
- Argument parsing
- Validation
- Logging
- Temporary files
- Cleanup traps
- File paths
- Error handling
- Archive creation

---

# Recommended Learning Order

Study Bash in this sequence:

```text
1. Linux commands and terminal fundamentals
2. Script creation and execution
3. Variables and quoting
4. Input and command-line arguments
5. Arithmetic and command substitution
6. Conditions and test operators
7. Loops
8. Functions
9. Arrays and strings
10. File reading and redirection
11. Pipes and text-processing tools
12. Processes, jobs, signals, and traps
13. Command-line option parsing
14. Error handling and debugging
15. Security and portability
16. Scheduling and system administration
17. Testing and professional project structure
18. Real-world automation projects
```

The most important Bash principles are:

```bash
# Quote variables
command -- "$variable"

# Read lines safely
while IFS= read -r line; do
    printf '%s\n' "$line"
done < file.txt

# Preserve command-line arguments
for argument in "$@"; do
    printf '%s\n' "$argument"
done

# Check commands directly
if command; then
    echo "Success"
else
    echo "Failure"
fi

# Validate required variables
value=${VALUE:?VALUE is required}

# Clean up resources
trap cleanup EXIT

# Analyze scripts
bash -n script.sh
shellcheck script.sh
```

This syllabus covers the full path from basic Bash syntax to professional Linux automation.
