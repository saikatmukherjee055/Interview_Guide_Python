# Bash Scripting: Complete Detailed Guide

> A practical, beginner-to-advanced Bash scripting course with line-by-line explanations, expected output, common mistakes, best practices, and real-world projects.

---

## Table of Contents

1. [What Bash Is](#1-what-bash-is)
2. [Terminal, Shell, and Bash](#2-terminal-shell-and-bash)
3. [Creating and Running Scripts](#3-creating-and-running-scripts)
4. [Comments and Script Documentation](#4-comments-and-script-documentation)
5. [Commands and Exit Status](#5-commands-and-exit-status)
6. [Variables](#6-variables)
7. [Quoting Rules](#7-quoting-rules)
8. [Reading User Input](#8-reading-user-input)
9. [Command-Line Arguments](#9-command-line-arguments)
10. [Arithmetic](#10-arithmetic)
11. [Command Substitution](#11-command-substitution)
12. [Conditional Statements](#12-conditional-statements)
13. [Test Operators](#13-test-operators)
14. [Case Statements](#14-case-statements)
15. [Loops](#15-loops)
16. [Functions](#16-functions)
17. [Arrays](#17-arrays)
18. [String Manipulation](#18-string-manipulation)
19. [Parameter Expansion](#19-parameter-expansion)
20. [Globbing and Wildcards](#20-globbing-and-wildcards)
21. [Regular Expressions](#21-regular-expressions)
22. [Redirection and File Descriptors](#22-redirection-and-file-descriptors)
23. [Pipelines](#23-pipelines)
24. [Here Documents and Here Strings](#24-here-documents-and-here-strings)
25. [Subshells and Command Groups](#25-subshells-and-command-groups)
26. [Processes and Background Jobs](#26-processes-and-background-jobs)
27. [Signals and Traps](#27-signals-and-traps)
28. [Error Handling and Strict Mode](#28-error-handling-and-strict-mode)
29. [Debugging](#29-debugging)
30. [Command-Line Options with getopts](#30-command-line-options-with-getopts)
31. [Temporary Files and Directories](#31-temporary-files-and-directories)
32. [Reading Files Safely](#32-reading-files-safely)
33. [Text Processing](#33-text-processing)
34. [Find Command](#34-find-command)
35. [Permissions and Ownership](#35-permissions-and-ownership)
36. [Networking](#36-networking)
37. [JSON Processing](#37-json-processing)
38. [Date and Time](#38-date-and-time)
39. [Logging](#39-logging)
40. [Configuration Files](#40-configuration-files)
41. [Cron and Scheduling](#41-cron-and-scheduling)
42. [Locking](#42-locking)
43. [Security](#43-security)
44. [Portability](#44-portability)
45. [Performance](#45-performance)
46. [Professional Script Structure](#46-professional-script-structure)
47. [Common Mistakes](#47-common-mistakes)
48. [Testing](#48-testing)
49. [Complete Backup Project](#49-complete-backup-project)
50. [Learning Roadmap](#50-learning-roadmap)

---

# 1. What Bash Is

Bash means **Bourne Again Shell**.

It can be used in two ways:

1. As an interactive command interpreter.
2. As a scripting language.

When you type this command:

```bash
ls -l
```

Bash reads the command, understands its syntax, finds the `ls` program, starts it, and displays its output.

When several commands are written in a file, that file becomes a Bash script.

Example:

```bash
#!/usr/bin/env bash

echo "Starting backup"
cp important.txt backup.txt
echo "Backup complete"
```

### Line-by-line explanation

```bash
#!/usr/bin/env bash
```

- This is called the **shebang**.
- It tells the operating system to find Bash through the `env` command.
- It makes the script less dependent on Bash being installed in one exact location.

```bash
echo "Starting backup"
```

- `echo` prints text.
- This tells the user that the backup process is starting.

```bash
cp important.txt backup.txt
```

- `cp` copies a file.
- `important.txt` is the source file.
- `backup.txt` is the destination file.

```bash
echo "Backup complete"
```

- This prints a completion message.
- Notice that this message will still run even if `cp` fails.
- Later, you will learn how to stop the script when a command fails.

---

# 2. Terminal, Shell, and Bash

These concepts are often confused.

## Terminal

The terminal is the interface where you type commands.

Examples:

- GNOME Terminal
- Konsole
- Windows Terminal
- macOS Terminal

## Shell

The shell is the program that interprets commands.

Examples:

- Bash
- Zsh
- Fish
- Dash
- KornShell

## Bash

Bash is one particular shell.

Check your login shell:

```bash
echo "$SHELL"
```

### Explanation

```bash
echo
```

- Prints text to the terminal.

```bash
"$SHELL"
```

- `$SHELL` expands to the value of the `SHELL` environment variable.
- Double quotes preserve the value as one argument.

Possible output:

```text
/bin/bash
```

Check the current Bash version:

```bash
bash --version
```

### Explanation

```bash
bash
```

- Starts or queries the Bash executable.

```bash
--version
```

- Asks Bash to print version information instead of opening a new shell.

Find where Bash is installed:

```bash
command -v bash
```

### Explanation

- `command -v` checks how the shell resolves a command.
- It is generally more portable than `which`.

Possible output:

```text
/usr/bin/bash
```

---

# 3. Creating and Running Scripts

Create a file named `hello.sh`:

```bash
nano hello.sh
```

Add this code:

```bash
#!/usr/bin/env bash

echo "Hello, Bash!"
```

Save the file.

Make it executable:

```bash
chmod +x hello.sh
```

### Explanation

```bash
chmod
```

- Changes file permissions.

```bash
+x
```

- Adds executable permission.

```bash
hello.sh
```

- The file whose permissions are being changed.

Run the script:

```bash
./hello.sh
```

### Why `./` is required

By default, the current directory is usually not searched for commands.

```bash
./hello.sh
```

means:

- `.` means the current directory.
- `/` separates the directory from the filename.
- `hello.sh` is the script.

You can also run it like this:

```bash
bash hello.sh
```

### Difference

```bash
./hello.sh
```

- Uses the interpreter mentioned in the shebang.
- Requires executable permission.

```bash
bash hello.sh
```

- Explicitly uses Bash.
- Does not require executable permission.
- Ignores the shebang for interpreter selection.

---

# 4. Comments and Script Documentation

A comment begins with `#`.

```bash
# Display a welcome message
echo "Welcome"
```

### Explanation

```bash
# Display a welcome message
```

- Bash ignores this line.
- It exists only to help humans understand the code.

```bash
echo "Welcome"
```

- This command is executed.

Inline comments:

```bash
name="Arko"  # Store the user's name
```

The inline comment must be separated from the command.

A useful script header:

```bash
#!/usr/bin/env bash

# Script: backup.sh
# Purpose: Create a compressed backup
# Author: Your Name
# Usage: ./backup.sh SOURCE DESTINATION
```

Good comments explain **why**, not only **what**.

Weak comment:

```bash
# Add 1 to count
((++count))
```

Better comment:

```bash
# Move to the next processed record
((++count))
```

---

# 5. Commands and Exit Status

Every command returns an integer called an **exit status**.

- `0` means success.
- Any non-zero value means failure.

Example:

```bash
mkdir test_directory
echo "$?"
```

### Explanation

```bash
mkdir test_directory
```

- Attempts to create a directory.

```bash
echo "$?"
```

- `$?` contains the exit status of the previous command.
- If the directory was created, the output is usually `0`.
- If creation failed, the output is non-zero.

Example of direct testing:

```bash
if mkdir project; then
    echo "Directory created successfully"
else
    echo "Could not create directory" >&2
fi
```

### Line-by-line explanation

```bash
if mkdir project; then
```

- Bash runs `mkdir project`.
- The `if` condition is true when `mkdir` returns `0`.

```bash
echo "Directory created successfully"
```

- Runs only when directory creation succeeds.

```bash
else
```

- Begins the failure branch.

```bash
echo "Could not create directory" >&2
```

- Prints the error message to standard error.
- `>&2` redirects output to file descriptor `2`.

```bash
fi
```

- Ends the `if` statement.

Manual exit:

```bash
exit 0
```

- Stops the script.
- Returns success to the caller.

```bash
exit 1
```

- Stops the script.
- Returns failure to the caller.

---

# 6. Variables

Create variables without spaces around `=`:

```bash
name="Arko"
age=25
```

### Explanation

```bash
name="Arko"
```

- Creates a variable called `name`.
- Stores the string `Arko`.

```bash
age=25
```

- Creates a variable called `age`.
- Bash stores it as text, although arithmetic contexts can treat it as an integer.

Incorrect:

```bash
name = "Arko"
```

Why it fails:

- Bash treats `name` as a command.
- `=` becomes an argument.
- `"Arko"` becomes another argument.

Read variables:

```bash
echo "$name"
echo "$age"
```

Use braces when joining text:

```bash
file="report"
echo "${file}.txt"
```

### Explanation

```bash
${file}
```

- Explicitly marks the variable name.

```bash
.txt
```

- Literal text added after the variable.

Output:

```text
report.txt
```

Readonly variable:

```bash
readonly country="India"
```

- Creates `country`.
- Prevents later modification.

Remove a variable:

```bash
unset name
```

- Deletes the variable from the current shell.

Environment variable:

```bash
export APP_ENV="production"
```

### Explanation

```bash
export
```

- Makes the variable available to child processes.

```bash
APP_ENV="production"
```

- Creates the variable and assigns its value.

---

# 7. Quoting Rules

Quoting is one of the most important Bash topics.

## Double quotes

```bash
name="Arko"
echo "Hello, $name"
```

Output:

```text
Hello, Arko
```

Double quotes allow:

- Variable expansion
- Command substitution
- Arithmetic expansion

They prevent:

- Word splitting
- Filename expansion

## Single quotes

```bash
echo 'Hello, $name'
```

Output:

```text
Hello, $name
```

Single quotes treat everything literally.

## Unquoted variables

```bash
message="Hello     world"
printf '<%s>\n' $message
```

Possible output:

```text
<Hello>
<world>
```

Why?

- The unquoted variable is split into words.
- Multiple spaces are treated as separators.

Quoted version:

```bash
printf '<%s>\n' "$message"
```

Output:

```text
<Hello     world>
```

## Escape character

```bash
echo "He said, \"Hello\""
```

Explanation:

- `\"` means a literal double quote inside double quotes.

Use `printf` for predictable escape sequences:

```bash
printf "First line\nSecond line\n"
```

- `\n` creates a newline.

```bash
printf "Name\tAge\n"
```

- `\t` creates a tab.

---

# 8. Reading User Input

Basic input:

```bash
read name
echo "Hello, $name"
```

### Explanation

```bash
read name
```

- Waits for the user to enter text.
- Stores the text in `name`.

```bash
echo "Hello, $name"
```

- Prints the entered value.

Prompt on the same line:

```bash
read -p "Enter your name: " name
```

### Explanation

- `-p` displays a prompt.
- The final argument is the destination variable.

Silent input:

```bash
read -s -p "Enter password: " password
echo
```

### Explanation

```bash
-s
```

- Hides typed characters.

```bash
-p
```

- Displays the prompt.

```bash
echo
```

- Moves to a new line after hidden input.

Safe line reading:

```bash
IFS= read -r line
```

### Explanation

```bash
IFS=
```

- Temporarily clears the input field separator.
- Prevents trimming leading or trailing whitespace.

```bash
read -r
```

- Prevents backslash interpretation.

```bash
line
```

- Variable receiving the input.

---

# 9. Command-Line Arguments

Run:

```bash
./user.sh Arko 25 India
```

Inside `user.sh`:

```bash
#!/usr/bin/env bash

echo "Script name: $0"
echo "Name: $1"
echo "Age: $2"
echo "Country: $3"
echo "Argument count: $#"
```

### Explanation

```bash
$0
```

- Script name.

```bash
$1
```

- First argument.

```bash
$2
```

- Second argument.

```bash
$3
```

- Third argument.

```bash
$#
```

- Number of arguments.

Loop through all arguments:

```bash
for argument in "$@"; do
    printf 'Argument: %s\n' "$argument"
done
```

### Explanation

```bash
"$@"
```

- Expands to all arguments.
- Preserves each argument separately.
- Correctly handles spaces.

Example:

```bash
./script.sh "John Doe" London
```

The loop receives two arguments:

1. `John Doe`
2. `London`

Using unquoted `$@` could incorrectly split `John Doe`.

## `shift`

```bash
while (( $# > 0 )); do
    printf 'Processing: %s\n' "$1"
    shift
done
```

### Explanation

```bash
while (( $# > 0 )); do
```

- Continue while at least one argument remains.

```bash
"$1"
```

- Current first argument.

```bash
shift
```

- Removes the current first argument.
- Former `$2` becomes `$1`.

---

# 10. Arithmetic

Arithmetic expansion:

```bash
a=10
b=5
result=$((a + b))
echo "$result"
```

### Explanation

```bash
$((a + b))
```

- Opens an arithmetic context.
- Reads `a` and `b` as integers.
- Calculates their sum.

Supported operators:

```bash
echo $((a + b))
echo $((a - b))
echo $((a * b))
echo $((a / b))
echo $((a % b))
echo $((a ** b))
```

Meaning:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` integer division
- `%` remainder
- `**` exponentiation

Integer division:

```bash
echo $((5 / 2))
```

Output:

```text
2
```

Bash does not perform floating-point arithmetic directly.

Increment:

```bash
count=0
((++count))
echo "$count"
```

### Explanation

```bash
((++count))
```

- Increases `count` before evaluating it.
- Returns success because the resulting value is non-zero.

Avoid this with strict mode when `count` starts at zero:

```bash
((count++))
```

Why?

- It evaluates the old value first.
- Old value `0` produces exit status `1`.
- With `set -e`, that may stop the script.

Decimal calculation using `bc`:

```bash
result=$(printf 'scale=2; 5 / 2\n' | bc)
echo "$result"
```

Output:

```text
2.50
```

---

# 11. Command Substitution

Command substitution stores command output.

```bash
current_date=$(date '+%Y-%m-%d')
echo "$current_date"
```

### Explanation

```bash
$(date '+%Y-%m-%d')
```

- Runs the `date` command.
- Captures its standard output.
- Removes trailing newline characters.

```bash
current_date=...
```

- Stores the captured output.

Nested substitution:

```bash
directory_name=$(basename "$(pwd)")
echo "$directory_name"
```

### Explanation

```bash
$(pwd)
```

- Gets the current directory path.

```bash
basename ...
```

- Removes the parent path.
- Keeps only the final directory name.

```bash
$(basename "$(pwd)")
```

- Captures the final name.

Prefer `$(...)` over backticks:

```bash
current_date=`date`
```

Backticks are harder to read and nest.

---

# 12. Conditional Statements

Basic condition:

```bash
age=20

if (( age >= 18 )); then
    echo "Adult"
fi
```

### Explanation

```bash
if
```

- Starts a conditional statement.

```bash
(( age >= 18 ))
```

- Performs an integer comparison.

```bash
then
```

- Begins commands for the true case.

```bash
fi
```

- Ends the condition.

With `else`:

```bash
if (( age >= 18 )); then
    echo "Adult"
else
    echo "Minor"
fi
```

Multiple branches:

```bash
marks=75

if (( marks >= 90 )); then
    echo "Grade A"
elif (( marks >= 70 )); then
    echo "Grade B"
elif (( marks >= 50 )); then
    echo "Grade C"
else
    echo "Fail"
fi
```

Important behavior:

- Bash checks conditions from top to bottom.
- The first true branch runs.
- Remaining branches are skipped.

---

# 13. Test Operators

## String tests

```bash
name="Arko"

if [[ $name == "Arko" ]]; then
    echo "Name matched"
fi
```

Operators:

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `-z` | Empty |
| `-n` | Non-empty |

Example:

```bash
if [[ -z $name ]]; then
    echo "Name is empty"
fi
```

## Numeric tests

```bash
if [[ $age -ge 18 ]]; then
    echo "Adult"
fi
```

Operators:

| Operator | Meaning |
|---|---|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-gt` | Greater than |
| `-ge` | Greater than or equal |
| `-lt` | Less than |
| `-le` | Less than or equal |

For arithmetic, this style is often clearer:

```bash
if (( age >= 18 )); then
    echo "Adult"
fi
```

## File tests

```bash
file="data.txt"

if [[ -f $file ]]; then
    echo "Regular file exists"
fi
```

Common operators:

| Operator | Meaning |
|---|---|
| `-e` | Path exists |
| `-f` | Regular file |
| `-d` | Directory |
| `-r` | Readable |
| `-w` | Writable |
| `-x` | Executable |
| `-s` | Exists and is non-empty |
| `-L` | Symbolic link |

Combined condition:

```bash
if [[ -f $file && -r $file ]]; then
    echo "File exists and is readable"
fi
```

### Explanation

```bash
&&
```

- Logical AND.
- Both conditions must be true.

Logical OR:

```bash
if [[ $role == "admin" || $role == "manager" ]]; then
    echo "Access granted"
fi
```

Logical NOT:

```bash
if [[ ! -f config.txt ]]; then
    echo "Configuration file is missing"
fi
```

---

# 14. Case Statements

Use `case` when one value may match many patterns.

```bash
read -p "Enter command: " command_name

case $command_name in
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
        echo "Unknown command"
        ;;
esac
```

### Explanation

```bash
case $command_name in
```

- Starts pattern matching for `command_name`.

```bash
start)
```

- Matches the exact word `start`.

```bash
;;
```

- Ends that branch.

```bash
*)
```

- Default branch.
- `*` matches anything.

```bash
esac
```

- Ends the case statement.
- `esac` is `case` written backward.

Multiple accepted values:

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

The `|` separates alternative patterns.

---

# 15. Loops

## For loop

```bash
for number in 1 2 3 4 5; do
    echo "$number"
done
```

### Explanation

```bash
for number in 1 2 3 4 5
```

- Assigns each value to `number`.

```bash
do
```

- Starts the loop body.

```bash
done
```

- Ends the loop.

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

### Explanation

```bash
i = 1
```

- Initial value.

```bash
i <= 5
```

- Condition checked before every iteration.

```bash
i++
```

- Increment after every iteration.

## While loop

```bash
count=1

while (( count <= 5 )); do
    echo "$count"
    ((++count))
done
```

The loop continues while the condition is true.

## Until loop

```bash
count=1

until (( count > 5 )); do
    echo "$count"
    ((++count))
done
```

The loop continues until the condition becomes true.

## Break

```bash
for number in {1..10}; do
    if (( number == 5 )); then
        break
    fi

    echo "$number"
done
```

- `break` immediately stops the loop.

## Continue

```bash
for number in {1..5}; do
    if (( number == 3 )); then
        continue
    fi

    echo "$number"
done
```

- `continue` skips only the current iteration.

---

# 16. Functions

Basic function:

```bash
greet() {
    echo "Hello"
}

greet
```

### Explanation

```bash
greet()
```

- Declares a function called `greet`.

```bash
{
```

- Starts the function body.

```bash
}
```

- Ends the function body.

```bash
greet
```

- Calls the function.

Function arguments:

```bash
greet() {
    local name=$1
    echo "Hello, $name"
}

greet "Arko"
```

### Explanation

```bash
local name=$1
```

- Creates a function-local variable.
- `$1` is the first function argument.

```bash
greet "Arko"
```

- Calls the function with one argument.

Return status:

```bash
is_adult() {
    local age=$1

    if (( age >= 18 )); then
        return 0
    fi

    return 1
}
```

Use it:

```bash
if is_adult 20; then
    echo "Adult"
else
    echo "Minor"
fi
```

Important:

- `return` is for exit statuses.
- It is not for returning text or large numbers.

Return data through output:

```bash
add() {
    local a=$1
    local b=$2
    printf '%d\n' "$((a + b))"
}

result=$(add 10 20)
echo "$result"
```

The function prints the result, and command substitution captures it.

---

# 17. Arrays

## Indexed arrays

```bash
fruits=("apple" "banana" "mango")
```

Access one element:

```bash
echo "${fruits[0]}"
```

All values:

```bash
printf '%s\n' "${fruits[@]}"
```

Array length:

```bash
echo "${#fruits[@]}"
```

Append:

```bash
fruits+=("orange")
```

Loop:

```bash
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done
```

### Explanation

```bash
"${fruits[@]}"
```

- Expands each array element as a separate argument.
- Preserves spaces inside elements.

Indexes:

```bash
for index in "${!fruits[@]}"; do
    printf '%s: %s\n' "$index" "${fruits[$index]}"
done
```

## Associative arrays

```bash
declare -A user

user[name]="Arko"
user[age]="25"
user[country]="India"
```

### Explanation

```bash
declare -A user
```

- Creates an associative array.
- Associative arrays use string keys.

Read a value:

```bash
echo "${user[name]}"
```

Loop:

```bash
for key in "${!user[@]}"; do
    printf '%s = %s\n' "$key" "${user[$key]}"
done
```

---

# 18. String Manipulation

```bash
text="Hello Bash World"
```

Length:

```bash
echo "${#text}"
```

Output:

```text
16
```

Substring:

```bash
echo "${text:0:5}"
```

Output:

```text
Hello
```

Replace first match:

```bash
echo "${text/Bash/Linux}"
```

Output:

```text
Hello Linux World
```

Replace all matches:

```bash
value="one one one"
echo "${value//one/two}"
```

Output:

```text
two two two
```

Remove shortest matching prefix:

```bash
filename="report.final.txt"
echo "${filename#*.}"
```

Output:

```text
final.txt
```

Remove longest matching prefix:

```bash
echo "${filename##*.}"
```

Output:

```text
txt
```

Remove shortest suffix:

```bash
echo "${filename%.*}"
```

Output:

```text
report.final
```

Uppercase:

```bash
name="arko"
echo "${name^^}"
```

Lowercase:

```bash
name="ARKO"
echo "${name,,}"
```

---

# 19. Parameter Expansion

Default value:

```bash
echo "${name:-Guest}"
```

Meaning:

- Use `$name` when it is non-empty.
- Otherwise use `Guest`.
- Does not permanently assign the default.

Assign a default:

```bash
name="${name:=Guest}"
```

Meaning:

- Use `Guest` when `name` is unset or empty.
- Store `Guest` in `name`.

Required value:

```bash
database_url="${DATABASE_URL:?DATABASE_URL is required}"
```

Meaning:

- If `DATABASE_URL` is unset or empty, print the message.
- Exit the script with failure.

Alternative value:

```bash
echo "${name:+Name was provided}"
```

Meaning:

- If `name` is set and non-empty, use `Name was provided`.
- Otherwise produce an empty value.

Difference between `-` and `:-`:

```bash
${value-default}
```

- Uses the default only when `value` is unset.

```bash
${value:-default}
```

- Uses the default when `value` is unset or empty.

---

# 20. Globbing and Wildcards

Match all `.txt` files:

```bash
printf '%s\n' *.txt
```

`*` matches zero or more characters.

Match exactly one character:

```bash
printf '%s\n' file?.txt
```

Character range:

```bash
printf '%s\n' file[0-9].txt
```

Matches:

- `file0.txt`
- `file1.txt`
- `file9.txt`

Safe loop:

```bash
shopt -s nullglob

for file in *.txt; do
    printf 'Processing: %s\n' "$file"
done
```

### Explanation

```bash
shopt -s nullglob
```

- When no files match, the pattern expands to nothing.
- Without it, the literal string `*.txt` may remain.

Recursive globbing:

```bash
shopt -s globstar nullglob

for file in **/*.txt; do
    echo "$file"
done
```

- `globstar` makes `**` search recursively.

---

# 21. Regular Expressions

Bash regular expressions are used with `=~`.

```bash
value="12345"

if [[ $value =~ ^[0-9]+$ ]]; then
    echo "Only digits"
fi
```

### Explanation

```text
^
```

- Beginning of string.

```text
[0-9]
```

- One digit.

```text
+
```

- One or more occurrences.

```text
$
```

- End of string.

Capture groups:

```bash
date_value="2026-07-15"

if [[ $date_value =~ ^([0-9]{4})-([0-9]{2})-([0-9]{2})$ ]]; then
    echo "Year: ${BASH_REMATCH[1]}"
    echo "Month: ${BASH_REMATCH[2]}"
    echo "Day: ${BASH_REMATCH[3]}"
fi
```

### Explanation

```bash
BASH_REMATCH[0]
```

- Entire match.

```bash
BASH_REMATCH[1]
```

- First captured group.

```bash
BASH_REMATCH[2]
```

- Second captured group.

```bash
BASH_REMATCH[3]
```

- Third captured group.

---

# 22. Redirection and File Descriptors

Standard streams:

| Descriptor | Stream |
|---|---|
| `0` | Standard input |
| `1` | Standard output |
| `2` | Standard error |

Overwrite a file:

```bash
echo "Hello" > output.txt
```

Append:

```bash
echo "Another line" >> output.txt
```

Redirect errors:

```bash
ls missing.txt 2> error.log
```

Redirect both output and errors:

```bash
command > output.log 2>&1
```

### Explanation

```bash
> output.log
```

- Redirects standard output to the file.

```bash
2>&1
```

- Redirects standard error to the same destination as standard output.

Modern Bash shorthand:

```bash
command &> output.log
```

Discard output:

```bash
command > /dev/null 2>&1
```

`/dev/null` discards anything written to it.

Extra file descriptor:

```bash
exec 3>> application.log
echo "Application started" >&3
exec 3>&-
```

### Explanation

```bash
exec 3>> application.log
```

- Opens descriptor `3` for appending.

```bash
>&3
```

- Writes to descriptor `3`.

```bash
exec 3>&-
```

- Closes descriptor `3`.

---

# 23. Pipelines

A pipeline connects commands.

```bash
grep "ERROR" application.log | sort | uniq -c
```

### Step-by-step

1. `grep` selects lines containing `ERROR`.
2. `sort` groups identical lines together.
3. `uniq -c` counts adjacent duplicate lines.

Enable pipeline failure detection:

```bash
set -o pipefail
```

Without `pipefail`, this pipeline may appear successful because `sort` succeeds:

```bash
cat missing.txt | sort
```

With `pipefail`, the pipeline returns failure because `cat` fails.

Avoid unnecessary `cat`:

```bash
grep "ERROR" application.log
```

Better than:

```bash
cat application.log | grep "ERROR"
```

---

# 24. Here Documents and Here Strings

Here document:

```bash
cat <<EOF
Hello
Current user: $USER
EOF
```

### Explanation

```bash
<<EOF
```

- Starts multiline input.
- Input ends when a line contains only `EOF`.

Variables expand because `EOF` is unquoted.

Literal here document:

```bash
cat <<'EOF'
The literal text is $USER
EOF
```

Because `'EOF'` is quoted, `$USER` is not expanded.

Write a file:

```bash
cat > config.ini <<EOF
host=localhost
port=8080
EOF
```

Here string:

```bash
grep "Bash" <<< "Hello Bash World"
```

- `<<<` sends one string to standard input.

---

# 25. Subshells and Command Groups

Subshell:

```bash
(
    cd /tmp
    echo "Inside: $PWD"
)

echo "Outside: $PWD"
```

### Explanation

- Parentheses create a child shell.
- Directory changes inside do not affect the parent shell.

Current-shell group:

```bash
{
    cd /tmp
    echo "Inside: $PWD"
}
```

- Braces run commands in the current shell.
- The directory change remains after the group.

Important syntax:

```bash
{ echo "Hello"; }
```

A semicolon or newline is required before `}`.

---

# 26. Processes and Background Jobs

Run in background:

```bash
sleep 10 &
```

Get process ID:

```bash
pid=$!
echo "$pid"
```

### Explanation

```bash
$!
```

- PID of the most recent background process.

Wait:

```bash
wait "$pid"
```

- Pauses until the process finishes.
- Returns the process exit status.

Parallel example:

```bash
task_one &
pid1=$!

task_two &
pid2=$!

wait "$pid1"
wait "$pid2"
```

Kill normally:

```bash
kill "$pid"
```

This sends `SIGTERM`.

Force kill:

```bash
kill -9 "$pid"
```

This sends `SIGKILL`.

Use `SIGKILL` only when graceful termination fails.

---

# 27. Signals and Traps

Cleanup example:

```bash
temporary_file=$(mktemp)

cleanup() {
    rm -f -- "$temporary_file"
}

trap cleanup EXIT
```

### Explanation

```bash
temporary_file=$(mktemp)
```

- Creates a secure temporary file.

```bash
cleanup()
```

- Defines cleanup logic.

```bash
trap cleanup EXIT
```

- Runs `cleanup` whenever the script exits.

Handle interruption:

```bash
handle_interrupt() {
    echo
    echo "Interrupted" >&2
    exit 130
}

trap handle_interrupt INT
```

`INT` is usually generated by `Ctrl+C`.

Common signals:

| Signal | Meaning |
|---|---|
| `INT` | Keyboard interruption |
| `TERM` | Graceful termination request |
| `HUP` | Terminal closed or reload request |
| `KILL` | Forced termination; cannot be trapped |
| `EXIT` | Bash pseudo-signal on script exit |

---

# 28. Error Handling and Strict Mode

Common strict mode:

```bash
set -Eeuo pipefail
```

### Explanation

```bash
-e
```

- Exits on many unhandled command failures.

```bash
-E
```

- Makes `ERR` traps inherited in more contexts.

```bash
-u
```

- Treats unset variables as errors.

```bash
-o pipefail
```

- Makes pipelines fail when any command fails.

Error trap:

```bash
trap 'printf "Error on line %d\n" "$LINENO" >&2' ERR
```

### Explanation

```bash
$LINENO
```

- Current script line number.

Explicit error handling:

```bash
if ! cp -- "$source" "$destination"; then
    echo "Copy failed" >&2
    exit 1
fi
```

Why this is useful:

- Gives a specific error message.
- Avoids depending only on `set -e`.
- Makes failure behavior obvious.

---

# 29. Debugging

Syntax check:

```bash
bash -n script.sh
```

- Parses the script.
- Does not execute normal commands.

Execution trace:

```bash
bash -x script.sh
```

Inside the script:

```bash
set -x
```

Disable:

```bash
set +x
```

Custom trace prompt:

```bash
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
set -x
```

### Explanation

```bash
BASH_SOURCE
```

- Current source file.

```bash
LINENO
```

- Current line number.

```bash
FUNCNAME[0]
```

- Current function name.

Debug print:

```bash
printf 'DEBUG: value=%q\n' "$value" >&2
```

`%q` displays a shell-escaped representation.

Static analysis:

```bash
shellcheck script.sh
```

ShellCheck can detect:

- Unquoted variables
- Broken loops
- Unsafe command substitution
- Portability issues
- Incorrect tests

---

# 30. Command-Line Options with getopts

Example script:

```bash
#!/usr/bin/env bash

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
            echo "Option -$OPTARG requires a value" >&2
            exit 1
            ;;
        \?)
            echo "Unknown option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

shift $((OPTIND - 1))
```

### Explanation

```bash
getopts ":s:d:vh" option
```

Options:

- `s:` means `-s` requires a value.
- `d:` means `-d` requires a value.
- `v` is a flag.
- `h` is a flag.
- Leading `:` enables custom missing-value handling.

```bash
OPTARG
```

- Value supplied to the current option.

```bash
OPTIND
```

- Index of the next argument to process.

```bash
shift $((OPTIND - 1))
```

- Removes processed options.
- Leaves remaining positional arguments.

Usage:

```bash
./backup.sh -s documents -d backups -v
```

---

# 31. Temporary Files and Directories

Secure file:

```bash
temporary_file=$(mktemp)
```

Secure directory:

```bash
temporary_directory=$(mktemp -d)
```

Cleanup:

```bash
cleanup() {
    if [[ -n ${temporary_directory:-} && -d $temporary_directory ]]; then
        rm -rf -- "$temporary_directory"
    fi
}

trap cleanup EXIT
```

### Explanation

```bash
${temporary_directory:-}
```

- Prevents an unset-variable error under `set -u`.

```bash
-d
```

- Confirms that the path is a directory.

```bash
rm -rf -- "$temporary_directory"
```

- Recursively removes it.
- `--` prevents option interpretation.

Never use predictable names like:

```bash
temporary_file="/tmp/myfile"
```

Another process could create or replace that path.

---

# 32. Reading Files Safely

Recommended loop:

```bash
while IFS= read -r line; do
    printf '%s\n' "$line"
done < file.txt
```

### Explanation

```bash
IFS=
```

- Preserves leading and trailing whitespace.

```bash
read -r
```

- Preserves backslashes.

```bash
done < file.txt
```

- Redirects the file into the loop.
- Avoids a pipeline subshell.

Handle a final line without newline:

```bash
while IFS= read -r line || [[ -n $line ]]; do
    printf '%s\n' "$line"
done < file.txt
```

Read comma-separated fields:

```bash
while IFS=',' read -r name age city; do
    printf 'Name=%s Age=%s City=%s\n' "$name" "$age" "$city"
done < users.csv
```

This is suitable only for simple CSV data without quoted commas.

Read into an array:

```bash
mapfile -t lines < file.txt
```

- `mapfile` reads lines into an indexed array.
- `-t` removes newline characters.

---

# 33. Text Processing

Bash is commonly combined with specialized text-processing tools. The three most important are:

- `grep` for searching text
- `sed` for editing and transforming text streams
- `awk` for field-based processing, filtering, calculations, and reports

---

## 33.1 `grep`

Search for lines containing a word:

```bash
grep "error" application.log
```

### Explanation

```bash
grep
```

- Searches input text line by line.

```bash
"error"
```

- The pattern to search for.

```bash
application.log
```

- The input file.

Case-insensitive search:

```bash
grep -i "error" application.log
```

- `-i` ignores uppercase and lowercase differences.

Show line numbers:

```bash
grep -n "error" application.log
```

- `-n` prints the matching line number.

Search recursively:

```bash
grep -R "TODO" .
```

- `-R` searches directories recursively.
- `.` means the current directory.

Search whole words only:

```bash
grep -w "cat" words.txt
```

This matches:

```text
cat
the cat is sleeping
```

It does not match:

```text
catalog
educate
```

Invert the match:

```bash
grep -v "DEBUG" application.log
```

- `-v` prints lines that do not match.

Count matching lines:

```bash
grep -c "ERROR" application.log
```

Show surrounding context:

```bash
grep -C 2 "ERROR" application.log
```

- `-C 2` shows two lines before and after each match.

---

## 33.2 `sed`: Stream Editor

`sed` means **stream editor**.

It reads text one line at a time, applies editing instructions, and prints the result.

By default, `sed` does not modify the original file.

---

### Example 1: Replace the first occurrence on each line

Input file:

```text
apple apple banana
apple mango apple
```

Command:

```bash
sed 's/apple/orange/' fruits.txt
```

Output:

```text
orange apple banana
orange mango apple
```

### Explanation

```bash
s/apple/orange/
```

The `s` command means substitute.

Its structure is:

```text
s/search/replacement/
```

Only the first match on each line is replaced.

---

### Example 2: Replace every occurrence on each line

```bash
sed 's/apple/orange/g' fruits.txt
```

Output:

```text
orange orange banana
orange mango orange
```

### Explanation

```bash
g
```

- Means global.
- Replaces all matches on each line.

---

### Example 3: Replace text only on a specific line

```bash
sed '2s/apple/orange/g' fruits.txt
```

### Explanation

```bash
2
```

- Applies the substitution only to line 2.

```bash
s/apple/orange/g
```

- Replaces all occurrences on that line.

---

### Example 4: Replace text within a line range

```bash
sed '2,5s/error/warning/g' application.log
```

### Explanation

```bash
2,5
```

- Limits the command to lines 2 through 5.

```bash
s/error/warning/g
```

- Replaces every `error` with `warning` in those lines.

---

### Example 5: Replace only lines matching a pattern

```bash
sed '/ERROR/s/failed/unsuccessful/g' application.log
```

### Explanation

```bash
/ERROR/
```

- Selects only lines containing `ERROR`.

```bash
s/failed/unsuccessful/g
```

- Replaces `failed` only in selected lines.

---

### Example 6: Delete empty lines

```bash
sed '/^$/d' file.txt
```

### Explanation

```text
^
```

- Beginning of line.

```text
$
```

- End of line.

```text
^$
```

- A line containing nothing.

```bash
d
```

- Deletes the selected line.

To delete lines containing only spaces or tabs:

```bash
sed '/^[[:space:]]*$/d' file.txt
```

### Explanation

```text
[[:space:]]
```

- Matches whitespace characters.

```text
*
```

- Matches zero or more occurrences.

---

### Example 7: Delete lines containing a word

```bash
sed '/DEBUG/d' application.log
```

- Deletes every line containing `DEBUG`.

Case-insensitive GNU `sed` version:

```bash
sed '/debug/Id' application.log
```

- `I` makes the pattern case-insensitive on GNU `sed`.

For portability, use:

```bash
grep -vi "debug" application.log
```

---

### Example 8: Print only selected lines

```bash
sed -n '5,10p' file.txt
```

### Explanation

```bash
-n
```

- Disables automatic printing.

```bash
5,10
```

- Selects lines 5 through 10.

```bash
p
```

- Explicitly prints selected lines.

Without `-n`, selected lines would be printed twice.

---

### Example 9: Print lines matching a pattern

```bash
sed -n '/ERROR/p' application.log
```

This behaves similarly to:

```bash
grep "ERROR" application.log
```

### Explanation

```bash
-n
```

- Suppresses normal output.

```bash
/ERROR/
```

- Selects matching lines.

```bash
p
```

- Prints those lines.

---

### Example 10: Insert text before a line

```bash
sed '/database_url/i\
# Database configuration
' config.txt
```

### Explanation

```bash
/database_url/
```

- Finds lines containing `database_url`.

```bash
i\
```

- Inserts text before the matching line.

---

### Example 11: Append text after a line

```bash
sed '/server_name/a\
server_port=8080
' config.txt
```

### Explanation

```bash
a\
```

- Appends text after the matching line.

---

### Example 12: Change an entire line

```bash
sed '/^environment=/c\
environment=production
' config.env
```

### Explanation

```bash
/^environment=/
```

- Matches a line beginning with `environment=`.

```bash
c\
```

- Replaces the entire matching line.

---

### Example 13: Remove leading whitespace

```bash
sed 's/^[[:space:]]*//' file.txt
```

### Explanation

```text
^
```

- Beginning of line.

```text
[[:space:]]*
```

- Zero or more whitespace characters.

The replacement is empty, so the whitespace is removed.

---

### Example 14: Remove trailing whitespace

```bash
sed 's/[[:space:]]*$//' file.txt
```

### Explanation

```text
[[:space:]]*
```

- Matches whitespace.

```text
$
```

- Ensures that whitespace is at the end of the line.

---

### Example 15: Remove both leading and trailing whitespace

```bash
sed \
    -e 's/^[[:space:]]*//' \
    -e 's/[[:space:]]*$//' \
    file.txt
```

### Explanation

```bash
-e
```

- Adds a separate `sed` expression.

The first expression removes leading whitespace.

The second removes trailing whitespace.

---

### Example 16: Use capture groups

Input:

```text
Arko Mukherjee
John Smith
```

Command:

```bash
sed -E 's/^([^ ]+) ([^ ]+)$/Last: \2, First: \1/' names.txt
```

Output:

```text
Last: Mukherjee, First: Arko
Last: Smith, First: John
```

### Explanation

```bash
-E
```

- Enables extended regular expressions.

```text
([^ ]+)
```

- Captures one or more non-space characters.

```text
\1
```

- First captured group.

```text
\2
```

- Second captured group.

---

### Example 17: Change delimiters

Suppose a file path contains `/`.

```bash
path="/home/arko/documents"
```

This is harder to read:

```bash
sed 's/\/home\/arko/\/data\/user/'
```

Use another delimiter:

```bash
sed 's|/home/arko|/data/user|' file.txt
```

### Explanation

`sed` does not require `/` as the delimiter.

These are valid:

```bash
s|old|new|
s#old#new#
s@old@new@
```

Choose a delimiter that makes the command readable.

---

### Example 18: Edit a file in place

GNU/Linux:

```bash
sed -i 's/development/production/g' config.txt
```

### Explanation

```bash
-i
```

- Modifies the original file directly.

Create a backup first:

```bash
sed -i.bak 's/development/production/g' config.txt
```

This creates:

```text
config.txt
config.txt.bak
```

On macOS, in-place syntax often requires:

```bash
sed -i '' 's/development/production/g' config.txt
```

---

### Example 19: Replace only the second occurrence

Input:

```text
apple apple apple
```

Command:

```bash
sed 's/apple/orange/2' file.txt
```

Output:

```text
apple orange apple
```

The final `2` means replace only the second match on each line.

---

### Example 20: Add line numbers

```bash
sed = file.txt | sed 'N;s/\n/ /'
```

### Step-by-step explanation

First command:

```bash
sed = file.txt
```

Produces:

```text
1
first line
2
second line
```

Second command:

```bash
sed 'N;s/\n/ /'
```

- `N` reads the next line into pattern space.
- `s/\n/ /` replaces the newline with a space.

Final result:

```text
1 first line
2 second line
```

A simpler tool for line numbers is:

```bash
nl -ba file.txt
```

---

### Practical `sed` example: Update a configuration value

Input:

```text
host=localhost
port=3000
environment=development
```

Command:

```bash
sed -E 's/^(port=).*/\18080/' config.env
```

Output:

```text
host=localhost
port=8080
environment=development
```

### Explanation

```text
^(port=)
```

- Matches `port=` at the beginning.
- Captures it as group 1.

```text
.*
```

- Matches the current value.

```text
\18080
```

- Reuses `port=`.
- Adds the new value `8080`.

A clearer version avoids ambiguity:

```bash
sed -E 's/^(port=).*/\1'"8080"'/' config.env
```

---

### Common `sed` mistakes

#### Mistake 1: Forgetting that `sed` prints every line by default

This command:

```bash
sed '/ERROR/p' file.txt
```

prints matching lines twice.

Correct:

```bash
sed -n '/ERROR/p' file.txt
```

#### Mistake 2: Using `-i` without a backup

Risky:

```bash
sed -i 's/old/new/g' important.txt
```

Safer:

```bash
sed -i.bak 's/old/new/g' important.txt
```

#### Mistake 3: Forgetting regular-expression characters

This pattern:

```bash
sed 's/file.txt/report.txt/' file.txt
```

The dot means any character.

Literal dot:

```bash
sed 's/file\.txt/report.txt/' file.txt
```

---

## 33.3 `awk`: Field and Record Processing

`awk` is a programming language designed for processing structured text.

The basic structure is:

```bash
awk 'condition { action }' file
```

An input file is read as records.

By default:

- One line is one record.
- Whitespace separates fields.
- `$0` is the entire line.
- `$1` is the first field.
- `$2` is the second field.
- `NF` is the number of fields.
- `NR` is the current record number.

---

### Example 1: Print the first field

Input:

```text
Arko 25 Kolkata
Mira 30 Delhi
John 28 London
```

Command:

```bash
awk '{print $1}' users.txt
```

Output:

```text
Arko
Mira
John
```

### Explanation

```bash
$1
```

- The first field of the current record.

```bash
print
```

- Prints a value.

---

### Example 2: Print selected fields

```bash
awk '{print $1, $3}' users.txt
```

Output:

```text
Arko Kolkata
Mira Delhi
John London
```

A comma in `print` inserts the output field separator.

---

### Example 3: Print the entire line

```bash
awk '{print $0}' users.txt
```

- `$0` means the complete input record.

---

### Example 4: Show line number and content

```bash
awk '{print NR, $0}' users.txt
```

Output:

```text
1 Arko 25 Kolkata
2 Mira 30 Delhi
3 John 28 London
```

### Explanation

```bash
NR
```

- Number of records processed so far.

---

### Example 5: Print the last field

```bash
awk '{print $NF}' users.txt
```

### Explanation

```bash
NF
```

- Number of fields in the current line.

```bash
$NF
```

- The last field.

Second-last field:

```bash
awk '{print $(NF-1)}' users.txt
```

---

### Example 6: Use a custom input separator

CSV input:

```text
Arko,25,Kolkata
Mira,30,Delhi
John,28,London
```

Command:

```bash
awk -F',' '{print $1, $3}' users.csv
```

### Explanation

```bash
-F','
```

- Sets comma as the input field separator.

---

### Example 7: Set a custom output separator

```bash
awk -F',' 'BEGIN {OFS=" | "} {print $1, $2, $3}' users.csv
```

Output:

```text
Arko | 25 | Kolkata
Mira | 30 | Delhi
John | 28 | London
```

### Explanation

```bash
BEGIN
```

- Runs before input is processed.

```bash
OFS=" | "
```

- Sets the output field separator.

---

### Example 8: Filter numeric values

Input:

```text
Arko 85
Mira 72
John 45
```

Command:

```bash
awk '$2 >= 70 {print $1, $2}' marks.txt
```

Output:

```text
Arko 85
Mira 72
```

### Explanation

```bash
$2 >= 70
```

- Condition.
- Only records where the second field is at least 70 are selected.

```bash
{print $1, $2}
```

- Action performed for selected records.

---

### Example 9: Filter text values

```bash
awk '$3 == "Kolkata" {print $1}' users.txt
```

- Prints names of users whose third field is `Kolkata`.

Not equal:

```bash
awk '$3 != "Kolkata" {print $1}' users.txt
```

---

### Example 10: Match a regular expression

```bash
awk '/ERROR/ {print NR, $0}' application.log
```

### Explanation

```bash
/ERROR/
```

- Matches lines containing `ERROR`.

```bash
{print NR, $0}
```

- Prints line number and complete line.

Case-insensitive matching:

```bash
awk 'tolower($0) ~ /error/ {print NR, $0}' application.log
```

### Explanation

```bash
tolower($0)
```

- Converts the entire line to lowercase.

```bash
~
```

- Regular-expression match operator.

---

### Example 11: Match one field

```bash
awk '$1 ~ /^A/ {print $0}' users.txt
```

- Selects lines whose first field begins with `A`.

Does not match:

```bash
awk '$1 !~ /^A/ {print $0}' users.txt
```

- `!~` means does not match.

---

### Example 12: Sum a column

Input:

```text
Laptop 50000
Phone 30000
Monitor 15000
```

Command:

```bash
awk '{sum += $2} END {print sum}' prices.txt
```

Output:

```text
95000
```

### Explanation

```bash
sum += $2
```

- Adds the second field to `sum`.

```bash
END
```

- Runs after all records are processed.

```bash
print sum
```

- Prints the final total.

---

### Example 13: Calculate an average

```bash
awk '{sum += $2} END {if (NR > 0) print sum / NR}' marks.txt
```

### Explanation

```bash
NR > 0
```

- Prevents division by zero for an empty file.

```bash
sum / NR
```

- Calculates the average.

Formatted output:

```bash
awk '{sum += $2} END {if (NR > 0) printf "Average: %.2f\n", sum / NR}' marks.txt
```

---

### Example 14: Find maximum value

```bash
awk 'NR == 1 || $2 > max {max = $2; name = $1} END {print name, max}' marks.txt
```

### Explanation

```bash
NR == 1
```

- Initializes values from the first record.

```bash
$2 > max
```

- Checks for a larger score.

```bash
max = $2
```

- Stores the new maximum.

```bash
name = $1
```

- Stores the corresponding name.

---

### Example 15: Find minimum value

```bash
awk 'NR == 1 || $2 < min {min = $2; name = $1} END {print name, min}' marks.txt
```

The logic is the same as the maximum example, but uses `<`.

---

### Example 16: Count matching records

```bash
awk '$2 >= 70 {count++} END {print count}' marks.txt
```

### Explanation

```bash
count++
```

- Increases the counter for each matching record.

---

### Example 17: Count values by category

Input:

```text
Arko Engineering
Mira Design
John Engineering
Sara Design
Ali Engineering
```

Command:

```bash
awk '{count[$2]++} END {for (category in count) print category, count[category]}' employees.txt
```

Possible output:

```text
Engineering 3
Design 2
```

### Explanation

```bash
count[$2]++
```

- Uses the second field as an associative-array key.

```bash
for (category in count)
```

- Loops over all category keys.

---

### Example 18: Print a formatted table

```bash
awk 'BEGIN {
    printf "%-15s %10s\n", "Name", "Score"
    printf "%-15s %10s\n", "---------------", "----------"
}
{
    printf "%-15s %10d\n", $1, $2
}' marks.txt
```

### Explanation

```bash
%-15s
```

- Left-aligns a string in 15 characters.

```bash
%10d
```

- Right-aligns an integer in 10 characters.

---

### Example 19: Skip the header row

CSV:

```text
name,age,city
Arko,25,Kolkata
Mira,30,Delhi
```

Command:

```bash
awk -F',' 'NR > 1 {print $1, $3}' users.csv
```

### Explanation

```bash
NR > 1
```

- Skips the first record.

Alternative:

```bash
awk -F',' 'NR == 1 {next} {print $1, $3}' users.csv
```

```bash
next
```

- Stops processing the current record.
- Moves to the next record.

---

### Example 20: Use shell variables inside `awk`

```bash
minimum_score=70

awk -v min="$minimum_score" '$2 >= min {print $1, $2}' marks.txt
```

### Explanation

```bash
-v min="$minimum_score"
```

- Passes a Bash variable into `awk`.
- Creates an `awk` variable called `min`.

Do not inject values directly into the program text.

Unsafe and difficult to quote:

```bash
awk '$2 >= '"$minimum_score"' {print $1}' marks.txt
```

Preferred:

```bash
awk -v min="$minimum_score" '$2 >= min {print $1}' marks.txt
```

---

### Example 21: Multiple conditions

```bash
awk '$2 >= 70 && $3 == "Kolkata" {print $1}' users.txt
```

- Both conditions must be true.

Logical OR:

```bash
awk '$3 == "Kolkata" || $3 == "Delhi" {print $1, $3}' users.txt
```

---

### Example 22: Conditional output

```bash
awk '{
    if ($2 >= 80)
        grade = "A"
    else if ($2 >= 60)
        grade = "B"
    else
        grade = "C"

    print $1, $2, grade
}' marks.txt
```

### Explanation

The grade variable is assigned based on the second field.

Each record is then printed with its calculated grade.

---

### Example 23: Calculate a total price

Input:

```text
Laptop 2 50000
Mouse 5 500
Keyboard 3 1500
```

Command:

```bash
awk '{
    total = $2 * $3
    print $1, total
}' orders.txt
```

Output:

```text
Laptop 100000
Mouse 2500
Keyboard 4500
```

Grand total:

```bash
awk '{
    line_total = $2 * $3
    grand_total += line_total
    print $1, line_total
}
END {
    print "Grand Total:", grand_total
}' orders.txt
```

---

### Example 24: Process colon-separated `/etc/passwd`

```bash
awk -F':' '{print "User:", $1, "Home:", $6, "Shell:", $7}' /etc/passwd
```

### Field meanings

- `$1`: username
- `$6`: home directory
- `$7`: login shell

Find Bash users:

```bash
awk -F':' '$7 ~ /bash$/ {print $1}' /etc/passwd
```

---

### Example 25: Replace a field

Input:

```text
Arko 25 Kolkata
Mira 30 Delhi
```

Command:

```bash
awk '{$2 = $2 + 1; print}' users.txt
```

Output:

```text
Arko 26 Kolkata
Mira 31 Delhi
```

### Explanation

```bash
$2 = $2 + 1
```

- Updates the second field.

```bash
print
```

- Without arguments, prints `$0`.
- After a field is changed, `awk` reconstructs the record.

---

### Example 26: Change the output delimiter

```bash
awk 'BEGIN {OFS=","} {$2 = $2 + 1; print $1, $2, $3}' users.txt
```

Output:

```text
Arko,26,Kolkata
Mira,31,Delhi
```

---

### Example 27: Extract unique values

```bash
awk '!seen[$1]++ {print $1}' users.txt
```

### Explanation

```bash
seen[$1]
```

- Tracks whether the first field has appeared before.

```bash
!seen[$1]++
```

- True only the first time each value appears.

---

### Example 28: Print duplicate values

```bash
awk 'seen[$1]++ == 1 {print $1}' users.txt
```

This prints a value when it appears for the second time.

To count all duplicates:

```bash
awk '{count[$1]++} END {for (value in count) if (count[value] > 1) print value, count[value]}' users.txt
```

---

### Example 29: Process multiple files

```bash
awk '{print FILENAME, FNR, $0}' file1.txt file2.txt
```

### Explanation

```bash
FILENAME
```

- Current input filename.

```bash
FNR
```

- Record number within the current file.

```bash
NR
```

- Record number across all files.

---

### Example 30: Use `BEGIN` and `END`

```bash
awk '
BEGIN {
    print "Report started"
}
{
    count++
}
END {
    print "Total records:", count
}
' users.txt
```

### Execution order

1. `BEGIN` runs once before input.
2. Main block runs for each line.
3. `END` runs once after input.

---

### Practical `awk` example: Generate a score report

Input:

```text
Arko 85
Mira 72
John 45
Sara 91
```

Command:

```bash
awk '
BEGIN {
    printf "%-12s %-8s %-6s\n", "Name", "Score", "Grade"
    printf "%-12s %-8s %-6s\n", "------------", "--------", "------"
}
{
    score = $2

    if (score >= 90)
        grade = "A"
    else if (score >= 75)
        grade = "B"
    else if (score >= 60)
        grade = "C"
    else
        grade = "F"

    total += score
    count++

    printf "%-12s %-8d %-6s\n", $1, score, grade
}
END {
    if (count > 0)
        printf "\nAverage score: %.2f\n", total / count
}
' marks.txt
```

This demonstrates:

- Headers
- Conditions
- Variables
- Formatting
- Totals
- Average calculation

---

### Common `awk` mistakes

#### Mistake 1: Using double quotes around the whole program

Problem:

```bash
awk "{print $1}" file.txt
```

Bash expands `$1` before `awk` sees it.

Correct:

```bash
awk '{print $1}' file.txt
```

#### Mistake 2: Forgetting the input delimiter

For CSV:

```bash
awk '{print $1}' users.csv
```

This may print the entire line because whitespace is the default separator.

Correct:

```bash
awk -F',' '{print $1}' users.csv
```

#### Mistake 3: Dividing by zero

Unsafe:

```bash
awk '{sum += $2} END {print sum / NR}' empty.txt
```

Safer:

```bash
awk '{sum += $2} END {if (NR > 0) print sum / NR}' empty.txt
```

#### Mistake 4: Assuming associative-array output order

```bash
for (key in count)
```

does not guarantee sorted order.

Sort afterward:

```bash
awk '{count[$1]++} END {for (key in count) print key, count[key]}' file.txt |
sort
```

---

# 34. The `find` Command

`find` searches directory trees using conditions and actions.

General structure:

```bash
find STARTING_PATH CONDITIONS ACTIONS
```

Example:

```bash
find . -type f -name "*.txt"
```

### Explanation

```bash
find
```

- Starts a filesystem search.

```bash
.
```

- Begin in the current directory.

```bash
-type f
```

- Match regular files.

```bash
-name "*.txt"
```

- Match filenames ending in `.txt`.

The pattern is quoted so Bash does not expand it before `find` receives it.

---

## 34.1 Search by name

Case-sensitive:

```bash
find . -name "*.jpg"
```

Case-insensitive:

```bash
find . -iname "*.jpg"
```

Find one exact filename:

```bash
find /home -name "config.yaml"
```

Find several extensions:

```bash
find . -type f \( -name "*.jpg" -o -name "*.png" \)
```

### Explanation

```bash
\(
```

- Starts a grouped expression.

```bash
-o
```

- Logical OR.

```bash
\)
```

- Ends the group.

Parentheses are escaped so the shell does not interpret them.

---

## 34.2 Search by type

Regular files:

```bash
find . -type f
```

Directories:

```bash
find . -type d
```

Symbolic links:

```bash
find . -type l
```

Empty files:

```bash
find . -type f -empty
```

Empty directories:

```bash
find . -type d -empty
```

---

## 34.3 Limit search depth

Only current directory:

```bash
find . -maxdepth 1 -type f
```

### Explanation

```bash
-maxdepth 1
```

- Search only the starting directory.
- Do not descend further.

Skip the starting directory itself:

```bash
find . -mindepth 1 -maxdepth 1
```

Search exactly two levels below:

```bash
find . -mindepth 2 -maxdepth 2
```

---

## 34.4 Search by size

Files larger than 100 MB:

```bash
find . -type f -size +100M
```

Files smaller than 1 KB:

```bash
find . -type f -size -1k
```

Files exactly around 10 MB units:

```bash
find . -type f -size 10M
```

Units include:

- `c`: bytes
- `k`: kibibytes
- `M`: mebibytes
- `G`: gibibytes

Largest files:

```bash
find . -type f -printf '%s %p\n' | sort -nr | head
```

### Step-by-step

```bash
-printf '%s %p\n'
```

- `%s` prints size in bytes.
- `%p` prints the path.

```bash
sort -nr
```

- Numeric reverse sort.

```bash
head
```

- Shows the first ten results.

Note: `-printf` is available in GNU `find`, not all BSD/macOS versions.

Portable alternative:

```bash
find . -type f -exec du -h {} + | sort -hr | head
```

---

## 34.5 Search by modification time

Modified in the last seven days:

```bash
find . -type f -mtime -7
```

Modified more than 30 days ago:

```bash
find . -type f -mtime +30
```

Modified exactly around seven 24-hour periods ago:

```bash
find . -type f -mtime 7
```

### Meaning

- `-7`: less than seven days
- `+30`: more than thirty days
- `7`: approximately seven days

Modified in the last 60 minutes:

```bash
find . -type f -mmin -60
```

Modified more than 120 minutes ago:

```bash
find . -type f -mmin +120
```

---

## 34.6 Search by access and change time

Accessed recently:

```bash
find . -type f -atime -7
```

Metadata changed recently:

```bash
find . -type f -ctime -7
```

Important:

- `mtime`: file content modification time
- `ctime`: metadata change time, not creation time
- `atime`: last access time

Linux does not always store creation time in a portable way.

---

## 34.7 Search relative to another file

Files newer than `reference.txt`:

```bash
find . -type f -newer reference.txt
```

Practical use:

```bash
touch -d '2026-07-01' reference.txt
find . -type f -newer reference.txt
```

On systems without GNU `touch -d`, date syntax differs.

---

## 34.8 Search by permissions

Files with exact permission `644`:

```bash
find . -type f -perm 0644
```

Files where all specified bits are set:

```bash
find . -type f -perm -0644
```

World-writable files:

```bash
find . -type f -perm -0002
```

Executable files:

```bash
find . -type f -executable
```

Readable files:

```bash
find . -type f -readable
```

Writable files:

```bash
find . -type f -writable
```

GNU-specific tests such as `-executable` may differ across platforms.

---

## 34.9 Search by owner or group

Files owned by a user:

```bash
find /home -user arko
```

Files owned by a group:

```bash
find /shared -group developers
```

Files with no valid owner:

```bash
find / -nouser 2>/dev/null
```

Files with no valid group:

```bash
find / -nogroup 2>/dev/null
```

`2>/dev/null` hides permission-denied errors.

Use it carefully because it can also hide other errors.

---

## 34.10 Exclude directories

Ignore `.git`:

```bash
find . -path './.git' -prune -o -type f -print
```

### Explanation

```bash
-path './.git'
```

- Matches the `.git` directory.

```bash
-prune
```

- Prevents descending into it.

```bash
-o
```

- Otherwise evaluate the next expression.

```bash
-type f -print
```

- Prints normal files outside `.git`.

Ignore multiple directories:

```bash
find . \
    \( -path './.git' -o -path './node_modules' \) -prune \
    -o -type f -print
```

---

## 34.11 Run commands on found files

Run `ls -l` once per file:

```bash
find . -type f -name "*.txt" -exec ls -l -- {} \;
```

### Explanation

```bash
-exec
```

- Runs a command.

```bash
{}
```

- Placeholder for the current matched path.

```bash
\;
```

- Ends the command.
- Executes once per match.

Run with multiple files per command:

```bash
find . -type f -name "*.txt" -exec ls -l -- {} +
```

### Difference

```bash
\;
```

- One command per match.

```bash
+
```

- Groups many paths into fewer commands.
- Usually faster.

---

## 34.12 Delete files

Preview first:

```bash
find /tmp -type f -name "*.tmp"
```

Then delete:

```bash
find /tmp -type f -name "*.tmp" -delete
```

Delete old logs:

```bash
find /var/log/myapp -type f -name "*.log" -mtime +30 -delete
```

### Safety rule

Always run the command without `-delete` first.

Also note that expression order matters.

Risky:

```bash
find . -delete -name "*.tmp"
```

Safer:

```bash
find . -type f -name "*.tmp" -delete
```

---

## 34.13 Confirm before running an action

```bash
find . -type f -name "*.bak" -ok rm -- {} \;
```

### Explanation

```bash
-ok
```

- Like `-exec`, but asks for confirmation.

---

## 34.14 Find and compress files

```bash
find . -type f -name "*.log" -mtime +7 -exec gzip -- {} +
```

### Explanation

- Finds log files older than seven days.
- Passes them to `gzip`.
- Uses `+` to process many paths efficiently.

---

## 34.15 Find and copy files

```bash
destination="/backup/text-files"

mkdir -p -- "$destination"

find . -type f -name "*.txt" -exec cp --parents -- {} "$destination" \;
```

GNU `cp --parents` preserves directory structure.

Portable alternative:

```bash
find . -type f -name "*.txt" -exec cp -- {} "$destination" \;
```

This may overwrite files with identical names from different directories.

---

## 34.16 Find files containing text

```bash
find . -type f -name "*.sh" -exec grep -l "TODO" -- {} +
```

### Explanation

```bash
grep -l
```

- Prints filenames containing the pattern.

A simpler recursive grep may be better:

```bash
grep -R -l --include='*.sh' "TODO" .
```

---

## 34.17 Null-delimited output

Filenames can contain spaces, tabs, and newlines.

Safe pattern:

```bash
find . -type f -print0 |
while IFS= read -r -d '' file; do
    printf 'File: %s\n' "$file"
done
```

### Explanation

```bash
-print0
```

- Separates paths with a null byte.

```bash
read -d ''
```

- Reads until the null byte.

This is safer than line-based parsing.

---

## 34.18 Use `xargs` safely

```bash
find . -type f -name "*.tmp" -print0 |
xargs -0 rm -f --
```

### Explanation

```bash
-print0
```

- Null-delimited paths.

```bash
xargs -0
```

- Reads null-delimited input.

```bash
--
```

- Ends options for `rm`.

Often this is simpler:

```bash
find . -type f -name "*.tmp" -exec rm -f -- {} +
```

---

## 34.19 Search with logical AND, OR, and NOT

AND is implicit:

```bash
find . -type f -name "*.txt"
```

Both conditions must match.

OR:

```bash
find . -type f \( -name "*.jpg" -o -name "*.png" \)
```

NOT:

```bash
find . -type f ! -name "*.bak"
```

Exclude hidden files:

```bash
find . -type f ! -path '*/.*'
```

---

## 34.20 Search for broken symbolic links

```bash
find . -xtype l
```

On GNU `find`, `-xtype l` finds broken symbolic links.

Another method:

```bash
find -L . -type l
```

Behavior differs by implementation, so test on your platform.

---

## 34.21 Find duplicate names

```bash
find . -type f -printf '%f\n' |
sort |
uniq -d
```

### Explanation

```bash
%f
```

- Prints only the filename, not the complete path.

```bash
uniq -d
```

- Prints values appearing more than once.

GNU-specific because of `-printf`.

---

## 34.22 Find recently changed shell scripts

```bash
find . \
    -type f \
    -name "*.sh" \
    -mtime -7 \
    -print
```

This finds:

- Regular files
- Ending in `.sh`
- Modified within seven days

---

## 34.23 Find large log files and display human-readable sizes

```bash
find /var/log \
    -type f \
    -name "*.log" \
    -size +50M \
    -exec du -h -- {} +
```

This is useful for investigating disk-space problems.

---

## 34.24 Find and rename files

Suppose you want to change `.jpeg` to `.jpg`.

```bash
find . -type f -name "*.jpeg" -print0 |
while IFS= read -r -d '' file; do
    new_name=${file%.jpeg}.jpg
    mv -- "$file" "$new_name"
done
```

### Line-by-line explanation

```bash
find . -type f -name "*.jpeg" -print0
```

- Finds `.jpeg` files safely.

```bash
while IFS= read -r -d '' file
```

- Reads each null-delimited path.

```bash
new_name=${file%.jpeg}.jpg
```

- Removes the shortest `.jpeg` suffix.
- Adds `.jpg`.

```bash
mv -- "$file" "$new_name"
```

- Renames the file safely.

Preview before renaming:

```bash
printf 'Would rename: %s -> %s\n' "$file" "$new_name"
```

---

## 34.25 Practical cleanup script

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

log_directory=${1:-/var/log/myapp}
days=${2:-30}

if [[ ! -d $log_directory ]]; then
    printf 'Directory not found: %s\n' "$log_directory" >&2
    exit 1
fi

if [[ ! $days =~ ^[0-9]+$ ]]; then
    printf 'Days must be a non-negative integer\n' >&2
    exit 1
fi

printf 'Files selected for deletion:\n'

find "$log_directory" \
    -type f \
    -name "*.log" \
    -mtime "+$days" \
    -print

find "$log_directory" \
    -type f \
    -name "*.log" \
    -mtime "+$days" \
    -delete
```

### Explanation

```bash
log_directory=${1:-/var/log/myapp}
```

- Uses the first argument.
- Defaults to `/var/log/myapp`.

```bash
days=${2:-30}
```

- Uses the second argument.
- Defaults to 30 days.

```bash
[[ ! $days =~ ^[0-9]+$ ]]
```

- Rejects non-numeric input.

The first `find` previews selected files.

The second deletes them.

For production use, consider a confirmation flag rather than deleting automatically.

---

## Common `find` mistakes

### Mistake 1: Not quoting the pattern

Wrong:

```bash
find . -name *.txt
```

The shell may expand `*.txt` before `find` runs.

Correct:

```bash
find . -name "*.txt"
```

### Mistake 2: Deleting without previewing

Risky:

```bash
find . -name "*.tmp" -delete
```

Preview first:

```bash
find . -name "*.tmp"
```

### Mistake 3: Incorrect OR grouping

Wrong:

```bash
find . -type f -name "*.jpg" -o -name "*.png"
```

The second branch may match directories named `.png`.

Correct:

```bash
find . -type f \( -name "*.jpg" -o -name "*.png" \)
```

### Mistake 4: Parsing paths line by line

Unsafe:

```bash
for file in $(find . -type f); do
    echo "$file"
done
```

Correct:

```bash
find . -type f -print0 |
while IFS= read -r -d '' file; do
    echo "$file"
done
```

### Mistake 5: Confusing `ctime` with creation time

`ctime` is metadata change time.

It is not portable file creation time.

---


# 35. Permissions and Ownership

Display permissions:

```bash
ls -l
```

Example:

```text
-rwxr-xr-- 1 user group 1200 Jul 15 script.sh
```

Permission groups:

1. Owner
2. Group
3. Others

Values:

| Number | Permission |
|---|---|
| `4` | Read |
| `2` | Write |
| `1` | Execute |

Examples:

```bash
chmod 755 script.sh
```

Means:

- Owner: `7 = 4 + 2 + 1 = rwx`
- Group: `5 = 4 + 1 = r-x`
- Others: `5 = 4 + 1 = r-x`

Configuration file:

```bash
chmod 600 secret.conf
```

- Owner can read and write.
- Nobody else has permission.

Change ownership:

```bash
sudo chown user:group file.txt
```

Root check:

```bash
if (( EUID != 0 )); then
    echo "Run this script as root" >&2
    exit 1
fi
```

---

# 36. Networking

Ping:

```bash
ping -c 4 example.com
```

- `-c 4` sends four packets.

Reliable HTTP request:

```bash
curl --fail --silent --show-error https://example.com
```

### Explanation

```bash
--fail
```

- Returns failure for HTTP error responses.

```bash
--silent
```

- Hides progress output.

```bash
--show-error
```

- Still displays error messages.

Save a file:

```bash
curl --fail --location --output file.zip https://example.com/file.zip
```

- `--location` follows redirects.
- `--output` chooses a filename.

Check a port:

```bash
nc -zv localhost 8080
```

- `-z` scans without sending normal data.
- `-v` prints detailed output.

Listening sockets:

```bash
ss -tuln
```

- `-t` TCP
- `-u` UDP
- `-l` listening
- `-n` numeric addresses

---

# 37. JSON Processing

Read a field:

```bash
jq -r '.name' user.json
```

### Explanation

```bash
.name
```

- Selects the `name` property.

```bash
-r
```

- Prints raw text without JSON quotes.

Loop through array items:

```bash
jq -r '.users[].name' users.json
```

Create JSON safely:

```bash
jq -n \
    --arg name "$name" \
    --arg city "$city" \
    '{name: $name, city: $city}'
```

### Explanation

```bash
-n
```

- Starts without reading input.

```bash
--arg name "$name"
```

- Passes a Bash value safely as a JSON string.

```bash
'{name: $name, city: $city}'
```

- Constructs a JSON object.

API example:

```bash
response=$(curl --fail --silent --show-error https://api.example.com/user)
name=$(jq -r '.name' <<< "$response")
```

---

# 38. Date and Time

Current formatted date:

```bash
date '+%Y-%m-%d'
```

Format elements:

| Code | Meaning |
|---|---|
| `%Y` | Four-digit year |
| `%m` | Month |
| `%d` | Day |
| `%H` | Hour |
| `%M` | Minute |
| `%S` | Second |

Timestamped filename:

```bash
timestamp=$(date '+%Y%m%d_%H%M%S')
backup_file="backup_${timestamp}.tar.gz"
```

Measure duration:

```bash
start_time=$(date +%s)

sleep 2

end_time=$(date +%s)
duration=$((end_time - start_time))

printf 'Duration: %d seconds\n' "$duration"
```

### Explanation

```bash
date +%s
```

- Returns Unix time in seconds.

```bash
end_time - start_time
```

- Calculates elapsed seconds.

---

# 39. Logging

Reusable log functions:

```bash
log_info() {
    printf '[%s] [INFO] %s\n' \
        "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
}

log_error() {
    printf '[%s] [ERROR] %s\n' \
        "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >&2
}
```

### Explanation

```bash
"$*"
```

- Combines all function arguments into one message.

```bash
>&2
```

- Sends errors to standard error.

Usage:

```bash
log_info "Backup started"

if ! cp -- "$source" "$destination"; then
    log_error "Backup failed"
    exit 1
fi
```

Log terminal output and file output:

```bash
exec > >(tee -a application.log) 2>&1
```

- Sends later output through `tee`.
- `tee -a` displays and appends to the log.

---

# 40. Configuration Files

Trusted Bash-style configuration:

```bash
APP_PORT=8080
APP_ENV=production
```

Load:

```bash
source config.env
```

Warning:

- `source` executes the file as Bash code.
- Use it only with trusted files.

Simple safer parser:

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

### Explanation

```bash
IFS='='
```

- Splits each line at `=`.

```bash
[[ -z $key || $key == \#* ]] && continue
```

- Skips empty lines.
- Skips comments beginning with `#`.

```bash
case
```

- Allows only recognized configuration keys.

---

# 41. Cron and Scheduling

Open crontab:

```bash
crontab -e
```

Run every day at 2:30 AM:

```cron
30 2 * * * /home/user/backup.sh >> /home/user/backup.log 2>&1
```

Fields:

```text
minute hour day-of-month month day-of-week command
```

Example:

```cron
0 9 * * 1-5 /home/user/report.sh
```

Meaning:

- Minute: `0`
- Hour: `9`
- Any day of month
- Any month
- Monday through Friday
- Run the script

Cron has a limited environment.

Use absolute paths:

```cron
PATH=/usr/local/bin:/usr/bin:/bin
0 9 * * 1-5 /home/user/report.sh
```

---

# 42. Locking

Prevent duplicate execution with `flock`:

```bash
exec 9>/tmp/backup.lock

if ! flock -n 9; then
    echo "Another instance is already running" >&2
    exit 1
fi
```

### Explanation

```bash
exec 9>/tmp/backup.lock
```

- Opens the lock file on descriptor `9`.

```bash
flock -n 9
```

- Tries to lock descriptor `9`.
- `-n` means do not wait.

If locking fails, another process probably holds the lock.

Command-line form:

```bash
flock -n /tmp/backup.lock ./backup.sh
```

---

# 43. Security

Always quote variables:

```bash
rm -- "$file"
```

Why:

- Protects spaces.
- Protects wildcard characters.
- `--` prevents filenames beginning with `-` from becoming options.

Avoid `eval`:

```bash
eval "$user_input"
```

This can execute arbitrary commands.

Use arrays for commands:

```bash
command=(grep -- "$pattern" "$file")
"${command[@]}"
```

### Explanation

- Each argument is stored separately.
- Spaces are preserved.
- No extra shell parsing occurs.

Validate input:

```bash
if [[ ! $port =~ ^[0-9]+$ ]] || (( port < 1 || port > 65535 )); then
    echo "Invalid port" >&2
    exit 1
fi
```

Protect new files:

```bash
umask 077
```

- New files become owner-only by default.

Avoid exposing secrets in tracing:

```bash
set +x
token=$(get_secret)
set -x
```

---

# 44. Portability

Bash script:

```bash
#!/usr/bin/env bash
```

POSIX shell script:

```bash
#!/bin/sh
```

Bash-specific features include:

- `[[ ... ]]`
- Arrays
- Associative arrays
- Process substitution
- `mapfile`
- `shopt`
- `=~`

Do not use a `#!/bin/sh` shebang with Bash-only syntax.

Check syntax:

```bash
bash -n script.sh
```

Check POSIX portability:

```bash
shellcheck -s sh script.sh
```

---

# 45. Performance

Bash is good for:

- Running programs
- Connecting commands
- File automation
- System administration
- Deployment helpers

Bash is weak for:

- Heavy numerical computation
- Complex data structures
- Large-scale application logic
- High-performance processing

Inefficient loop:

```bash
while IFS= read -r line; do
    uppercase=$(printf '%s\n' "$line" | tr '[:lower:]' '[:upper:]')
    echo "$uppercase"
done < file.txt
```

Why slower:

- Starts external commands repeatedly.

Better:

```bash
awk '{print toupper($0)}' file.txt
```

One `awk` process handles the complete file.

---

# 46. Professional Script Structure

Template:

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_NAME=${0##*/}

usage() {
    cat <<EOF
Usage: $SCRIPT_NAME INPUT OUTPUT
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
}

trap cleanup EXIT
main "$@"
```

### Structural explanation

```bash
readonly SCRIPT_NAME=${0##*/}
```

- Gets only the script filename.
- Makes it immutable.

```bash
usage()
```

- Centralizes help text.

```bash
log_error()
```

- Centralizes error formatting.

```bash
cleanup()
```

- Centralizes resource cleanup.

```bash
main()
```

- Keeps executable logic organized.
- Makes testing easier.

```bash
main "$@"
```

- Passes all script arguments to `main`.

---

# 47. Common Mistakes

## Spaces around assignment

Wrong:

```bash
name = "Arko"
```

Correct:

```bash
name="Arko"
```

## Unquoted variables

Wrong:

```bash
cp $source $destination
```

Correct:

```bash
cp -- "$source" "$destination"
```

## Parsing `ls`

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

## Reading file lines with `for`

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

## Checking `$?` unnecessarily

Less clear:

```bash
grep -q "error" file.txt
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

## Pipeline subshell problem

Problem:

```bash
count=0

printf '%s\n' a b c |
while IFS= read -r line; do
    ((++count))
done

echo "$count"
```

The loop may run in a subshell, so `count` remains unchanged.

Better:

```bash
count=0

while IFS= read -r line; do
    ((++count))
done < <(printf '%s\n' a b c)

echo "$count"
```

---

# 48. Testing

Simple test:

```bash
add() {
    printf '%d\n' "$(($1 + $2))"
}

actual=$(add 2 3)
expected=5

if [[ $actual == "$expected" ]]; then
    echo "PASS"
else
    echo "FAIL: expected $expected, got $actual" >&2
    exit 1
fi
```

### Explanation

```bash
actual=$(add 2 3)
```

- Runs the function.
- Captures its output.

```bash
expected=5
```

- Defines expected result.

```bash
[[ $actual == "$expected" ]]
```

- Compares actual and expected strings.

Test edge cases:

- Empty values
- Missing files
- Filenames containing spaces
- Filenames beginning with `-`
- Permission failures
- Interrupted execution
- Invalid numbers
- Missing arguments
- Very large input
- Unexpected command failure

Temporary test environment:

```bash
test_directory=$(mktemp -d)
trap 'rm -rf -- "$test_directory"' EXIT
```

This prevents tests from modifying real data.

---

# 49. Complete Backup Project

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_NAME=${0##*/}
readonly TIMESTAMP=$(date '+%Y%m%d_%H%M%S')

source_directory=""
destination_directory=""
verbose=false
temporary_file=""

usage() {
    cat <<EOF
Usage:
  $SCRIPT_NAME -s SOURCE -d DESTINATION [-v]

Options:
  -s SOURCE       Directory to back up
  -d DESTINATION  Backup destination
  -v              Enable verbose output
  -h              Show help
EOF
}

log() {
    if [[ $verbose == true ]]; then
        printf '[%s] %s\n' \
            "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
    fi
}

fail() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 1
}

cleanup() {
    if [[ -n $temporary_file && -f $temporary_file ]]; then
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
            fail "Option -$OPTARG requires a value"
            ;;
        \?)
            fail "Unknown option: -$OPTARG"
            ;;
    esac
done

[[ -n $source_directory ]] ||
    fail "Source directory is required"

[[ -n $destination_directory ]] ||
    fail "Destination directory is required"

[[ -d $source_directory ]] ||
    fail "Source directory does not exist: $source_directory"

mkdir -p -- "$destination_directory"

backup_name="$(basename "$source_directory")_${TIMESTAMP}.tar.gz"
backup_path="${destination_directory}/${backup_name}"

temporary_file=$(mktemp)

log "Creating backup"
log "Source: $source_directory"
log "Destination: $backup_path"

tar -czf "$temporary_file" \
    -C "$(dirname "$source_directory")" \
    "$(basename "$source_directory")"

mv -- "$temporary_file" "$backup_path"
temporary_file=""

printf 'Backup created: %s\n' "$backup_path"
```

## Detailed explanation

```bash
set -Eeuo pipefail
```

- Enables stricter failure behavior.

```bash
readonly SCRIPT_NAME=${0##*/}
```

- Removes the path from `$0`.
- Stores only the script filename.

```bash
readonly TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
```

- Creates a timestamp once.
- Prevents accidental modification.

```bash
source_directory=""
destination_directory=""
verbose=false
temporary_file=""
```

- Defines variables before strict unset-variable checking can affect them.

```bash
usage()
```

- Prints command syntax and option descriptions.

```bash
log()
```

- Prints messages only when verbose mode is enabled.

```bash
fail()
```

- Prints an error to standard error.
- Exits with status `1`.

```bash
cleanup()
```

- Removes the temporary archive if the script exits before completion.

```bash
trap cleanup EXIT
```

- Guarantees cleanup on normal exit and many failures.

```bash
trap 'fail "Unexpected error on line $LINENO"' ERR
```

- Reports unexpected command failures.

```bash
while getopts ...
```

- Parses short command-line options.

```bash
[[ -n $source_directory ]]
```

- Confirms the source was provided.

```bash
[[ -d $source_directory ]]
```

- Confirms that the source exists and is a directory.

```bash
mkdir -p -- "$destination_directory"
```

- Creates the destination if needed.
- Does not fail when it already exists.

```bash
backup_name="$(basename "$source_directory")_${TIMESTAMP}.tar.gz"
```

- Uses the source directory name.
- Adds a timestamp.
- Adds `.tar.gz`.

```bash
temporary_file=$(mktemp)
```

- Creates a secure temporary output path.

```bash
tar -czf "$temporary_file"
```

Options:

- `-c`: create archive
- `-z`: compress with gzip
- `-f`: next argument is archive filename

```bash
-C "$(dirname "$source_directory")"
```

- Changes directory before archiving.
- Avoids storing long absolute paths.

```bash
"$(basename "$source_directory")"
```

- Archives the source directory by its short name.

```bash
mv -- "$temporary_file" "$backup_path"
```

- Moves the completed archive into the final destination.
- This reduces the chance of leaving an incomplete final backup.

```bash
temporary_file=""
```

- Prevents cleanup from deleting the completed archive.

Usage:

```bash
chmod +x backup.sh
./backup.sh -s /home/user/documents -d /home/user/backups -v
```

---

# 50. Learning Roadmap

## Stage 1: Fundamentals

Learn:

- Terminal navigation
- Basic Linux commands
- Script creation
- Variables
- Quoting
- Input and output

Practice:

- Greeting script
- Calculator
- File checker

## Stage 2: Control Flow

Learn:

- Conditions
- Test operators
- Case statements
- Loops
- Functions

Practice:

- Menu system
- Number guessing game
- File organizer

## Stage 3: Data and Text

Learn:

- Arrays
- Strings
- File reading
- `grep`
- `sed`
- `awk`
- `find`

Practice:

- Log analyzer
- CSV report generator
- Batch renamer

## Stage 4: System Automation

Learn:

- Processes
- Signals
- Traps
- Permissions
- Networking
- Cron
- Locking

Practice:

- Disk monitor
- Service checker
- Website health monitor
- Automated backup

## Stage 5: Professional Bash

Learn:

- Strict mode
- Error handling
- Debugging
- Security
- Testing
- Portability
- Performance

Practice:

- Production backup tool
- Deployment helper
- Server bootstrap script
- Multi-server automation

---

# Final Best-Practice Checklist

```bash
#!/usr/bin/env bash
```

Use the correct interpreter.

```bash
set -Eeuo pipefail
```

Use stricter failure behavior when appropriate.

```bash
command -- "$variable"
```

Quote variables and use `--`.

```bash
while IFS= read -r line; do
    ...
done < file
```

Read files safely.

```bash
for argument in "$@"; do
    ...
done
```

Preserve script arguments correctly.

```bash
if command; then
    ...
else
    ...
fi
```

Test commands directly.

```bash
trap cleanup EXIT
```

Clean up temporary resources.

```bash
bash -n script.sh
shellcheck script.sh
```

Check syntax and common problems.

---

This guide covers the full Bash learning path from beginner syntax to secure, production-style automation.
