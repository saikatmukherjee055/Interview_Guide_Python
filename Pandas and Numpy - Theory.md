# Pandas and Numpy - Theory

# 1. Difference Between merge(), join(), and concat()

---

## merge()

Used like SQL JOIN.

### DataFrame 1

```python
import pandas as pd

employees=pd.DataFrame({
"emp_id":[1,2,3],
"name":["John","Alice","Bob"]
})

employees
```

Output

```
   emp_id   name
0       1   John
1       2  Alice
2       3    Bob
```

### DataFrame 2

```python
salary=pd.DataFrame({
"emp_id":[1,2,3],
"salary":[50000,70000,60000]
})
```

### Merge

```python
result=pd.merge(
employees,
salary,
on="emp_id",
how="inner"
)

print(result)
```

Output

```
   emp_id   name  salary
0       1   John   50000
1       2  Alice   70000
2       3    Bob   60000
```

### SQL Equivalent

```sql
SELECT*
FROM employees
INNERJOIN salary
ON employees.emp_id= salary.emp_id;
```

### Industry Use

```
Orders Table
+
Customer Table

Join customer details into order data
```

---

## join()

Works primarily on index.

```python
employees=employees.set_index("emp_id")
salary=salary.set_index("emp_id")

employees.join(salary)
```

Output

```
        name salary
emp_id
1       John 50000
2      Alice 70000
3        Bob 60000
```

### When Used

```
Same index
Need fast index-based join
```

---

## concat()

Stack data.

### Vertical

```python
jan=pd.DataFrame({
"sales":[100,200]
})

feb=pd.DataFrame({
"sales":[300,400]
})

pd.concat([jan,feb])
```

Output

```
sales
100
200
300
400
```

### Horizontal

```python
pd.concat(
    [employees,salary],
axis=1
)
```

---

## Interview Summary

| Function | Purpose |
| --- | --- |
| merge() | SQL Join |
| join() | Index Join |
| concat() | Stack Data |

---

# 2. How Would You Optimize a Pandas Job Running for 30 Minutes?

Interviewers love this.

Suppose:

```python
for i,row in df.iterrows():
df.loc[i,"bonus"]=row["salary"]*0.1
```

This is extremely slow.

---

## Step 1 Replace Loops

Bad

```python
for i,row in df.iterrows():
```

Good

```
df["bonus"]=df["salary"]*0.1
```

### Why?

Vectorized operations use C-level implementation.

Can be 100x–1000x faster.

---

## Step 2 Use Categories

Bad

```
df["state"]
```

Memory:

```
object datatype
```

Convert:

```
df["state"]=df["state"].astype("category")
```

Memory can reduce 90%.

---

## Step 3 Read Only Required Columns

Bad

```
pd.read_csv("sales.csv")
```

Good

```
pd.read_csv(
"sales.csv",
usecols=["sales","date"]
)
```

---

## Step 4 Chunk Processing

```
forchunkinpd.read_csv(
"sales.csv",
chunksize=100000
):
process(chunk)
```

---

## Step 5 Profile

```
%timeit
```

or

```
importcProfile
```

---

# 3. Pandas vs PySpark

---

## Pandas

Best when data fits in memory.

```
5 GB RAM
2 GB Data
```

Good.

---

## PySpark

Distributed.

```
500 GB Data
```

Split across machines.

---

## Example

Pandas

```
df.groupby("city")["sales"].sum()
```

PySpark

```
df.groupBy("city").sum("sales")
```

---

## Interview Answer

| Feature | Pandas | PySpark |
| --- | --- | --- |
| Single Machine | Yes | No |
| Distributed | No | Yes |
| Easy Debugging | Yes | Harder |
| Small Data | Excellent | Overkill |
| Big Data | Bad | Excellent |

---

## Rule

```
< 10 GB → Pandas

10-50 GB → Dask

50+ GB → Spark
```

---

# 4. How Do You Process 100 Million Rows?

---

Suppose:

```
100 Million Rows
20 Columns
```

Cannot load directly.

---

## Option 1

Chunk Processing

```python
for chunk in pd.read_csv(
"sales.csv",
chunksize=500000
):
process(chunk)
```

---

## Option 2

Database Pushdown

Bad

```
SELECT*
FROMsales
```

Good

```
SELECT
customer_id,
SUM(amount)
FROM sales
GROUPBY customer_id
```

Let database do aggregation.

---

## Option 3

PySpark

```
spark.read.csv(...)
```

Distributed processing.

---

## Interview Answer

```
100 million rows should not be processed entirely in Pandas.

Use:
- Chunking
- SQL pushdown
- PySpark
- Partitioning
```

---

# 5. How Do You Debug Memory Leaks in Pandas?

---

Check memory.

```
df.info(memory_usage="deep")
```

Output

```
500 MB
```

---

## Find Heavy Columns

```python
df.memory_usage(deep=True)
```

Output

```
name     300 MB
city     200 MB
```

---

## Convert Types

Bad

```
int64
```

Good

```
int32
```

```
df["age"]=df["age"].astype("int32")
```

---

## Delete Unused Objects

```
deltemp_df
```

```
importgc

gc.collect()
```

---

## Common Leak

```python
dfs=[]

for file in files:
dfs.append(pd.read_csv(file))
```

Every dataframe stays in memory.

---

# 6. Explain Vectorization

---

## Non-Vectorized

```python
bonus=[]

for salary in df["salary"]:
bonus.append(
salary*0.1
    )
```

Python executes row by row.

---

## Vectorized

```python
df["bonus"]=df["salary"]*0.1
```

Internally:

```
NumPy
↓
C Language
↓
CPU Optimization
```

Much faster.

---

## Benchmark

Loop

```
10 seconds
```

Vectorized

```
0.1 second
```

---

## Why Faster?

```
No Python loop
No Python object creation
Uses contiguous memory
Uses CPU cache efficiently
```

---

# 7. Data Quality Framework Using Pandas

Production Example.

---

## Rule 1

Salary cannot be negative.

```python
negative_salary= (
df["salary"]<0
).sum()
```

---

## Rule 2

Customer ID required.

```python
missing_id= (
df["customer_id"]
.isna()
.sum()
)
```

---

## Rule 3

Email Format

```python
invalid_email= (
~df["email"]
.str.contains("@")
)
```

---

## Framework

```
report= {
"negative_salary":
negative_salary,

"missing_id":
missing_id,

"invalid_email":
invalid_email.sum()
}
```

Output

```
{
'negative_salary':12,
'missing_id':5,
'invalid_email':3
}
```

---

# 8. ETL Pipeline Using Pandas

---

## Extract

```
df=pd.read_csv(
"sales.csv"
)
```

---

## Transform

```
df["sales"]= (
df["sales"]
.fillna(0)
)

df["bonus"]= (
df["sales"]*0.1
)
```

---

## Load

```
fromsqlalchemyimportcreate_engine

engine=create_engine(
connection_string
)

df.to_sql(
"sales_table",
engine,
if_exists="append"
)
```

---

## Production Flow

```
CSV
↓
Extract
↓
Validate
↓
Transform
↓
Load Database
↓
Logging
↓
Alerting
```

---

# 9. Schema Drift in CSV Files

---

Yesterday

```
id,name,salary
```

Today

```
id,name,salary,department
```

Pipeline breaks.

---

## Detect

```
expected= {
"id",
"name",
"salary"
}

actual=set(df.columns)

extra=actual-expected
missing=expected-actual
```

---

Output

```
extra={'department'}
missing=set()
```

---

## Production Solution

```
forcolinexpected:
ifcolnotindf:
df[col]=None
```

---

Log differences.

```
logger.info(extra)
```

---

# 10. Incremental Loading Efficiently

Most common real-world ETL question.

---

## Full Load

Bad

```
readallrows
loadallrows
```

Every day.

---

## Incremental Load

Database Table

```
id created_date
```

Keep last processed timestamp.

```
last_load="2026-06-14"
```

---

Read only new data.

```
new_data=df[
df["created_date"]
>last_load
]
```

---

Load only new rows.

```
new_data.to_sql(
"sales",
engine,
if_exists="append"
)
```

---

## Numpy:

These three topics are among the most frequently asked NumPy interview questions.

# 1. Broadcasting Rules

### What is Broadcasting?

Broadcasting allows NumPy to perform arithmetic operations on arrays of different shapes without explicitly copying data.

Example:

```
importnumpyasnp

a=np.array([1,2,3])
b=10

print(a+b)
```

Output:

```
[111213]
```

NumPy automatically "broadcasts" `10` across all elements.

---

### Broadcasting Rules

NumPy compares shapes from **right to left**.

Two dimensions are compatible if:

1. They are equal
2. One of them is 1

---

### Example 1: Valid Broadcasting

```
A.shape= (3,4)
B.shape= (1,4)
```

Comparison:

```
(3,4)
(1,4)
```

- 4 == 4 ✓
- 1 can expand to 3 ✓

Result shape:

```
(3,4)
```

---

### Example 2: Valid Broadcasting

```
A.shape= (3,4)
B.shape= (3,1)
```

Comparison:

```
(3,4)
(3,1)
```

- 3 == 3 ✓
- 1 expands to 4 ✓

Result:

```
(3,4)
```

---

### Example 3: Invalid Broadcasting

```
A.shape= (3,4)
B.shape= (2,4)
```

Comparison:

```
(3,4)
(2,4)
```

- 4 == 4 ✓
- 3 ≠ 2 ✗

Error:

```
ValueError:operandscouldnotbebroadcasttogether
```

---

### Interview Answer

> Broadcasting is NumPy's mechanism for performing operations on arrays with different shapes. Starting from the trailing dimensions, dimensions must either be equal or one of them must be 1. This avoids unnecessary memory copies and improves performance.
> 

---

# 2. Memory Sharing (View vs Copy)

This is one of the most important interview topics.

## View

A view shares the same memory as the original array.

```
importnumpyasnp

a=np.array([1,2,3,4])

b=a.view()

b[0]=100

print(a)
```

Output:

```
[100234]
```

Original array changes because both arrays point to the same memory.

---

## Copy

A copy creates completely separate memory.

```
a=np.array([1,2,3,4])

b=a.copy()

b[0]=100

print(a)
```

Output:

```
[1234]
```

Original remains unchanged.

---

## Checking Memory Sharing

```
np.shares_memory(a,b)
```

Returns:

```
True
```

or

```
False
```

---

## Slicing Creates Views

```
a=np.array([1,2,3,4,5])

b=a[1:4]

b[0]=99

print(a)
```

Output:

```
[199345]
```

Many beginners expect slicing to create a copy, but NumPy slicing usually creates a view.

---

### Interview Answer

> A view shares the same underlying memory as the original array, so modifications affect both arrays. A copy allocates new memory, making changes independent. NumPy slicing typically returns views for better performance and lower memory usage.
> 

---

# 3. Time Complexity vs Python Loops

### Why is NumPy Faster?

Python loops execute element-by-element in the Python interpreter.

NumPy executes operations in optimized C code.

---

## Python Loop

```
lst=list(range(1000000))

result= []

forxinlst:
result.append(x*2)
```

Complexity:

```
O(n)
```

but with large Python overhead.

---

## NumPy Vectorized Operation

```
arr=np.arange(1000000)

result=arr*2
```

Complexity:

```
O(n)
```

also O(n), but much faster.

---

### Important Interview Point

Many candidates incorrectly say:

> "NumPy reduces time complexity."
> 

Usually **it does not change Big-O complexity**.

Example:

| Operation | Python | NumPy |
| --- | --- | --- |
| Multiply n elements | O(n) | O(n) |
| Add two arrays | O(n) | O(n) |

The improvement comes from:

- Compiled C code
- SIMD instructions
- Better cache utilization
- Contiguous memory layout
- Reduced Python interpreter overhead

---

### Typical Benchmark

```
Pythonloop:0.5seconds
NumPy:0.01seconds
```

Both are O(n), but NumPy has a much smaller constant factor.

---

# Interview Quick Revision

### Broadcasting

- Compare shapes from right to left.
- Dimensions must be equal or one must be 1.
- Avoids unnecessary copies.

### View vs Copy

- `view()` → shared memory.
- `copy()` → separate memory.
- Slicing generally returns views.

### NumPy vs Python Loops

- Both often have the same Big-O complexity.
- NumPy is faster because operations run in optimized C code.
- Vectorization removes Python loop overhead.

**Common interview question:**

> Why is `arr * 2` faster than a Python `for` loop if both are O(n)?
> 

**Answer:** Because NumPy performs the operation in compiled C code on contiguous memory with vectorized execution, reducing interpreter overhead while keeping the same asymptotic complexity.

Here are **3 advanced NumPy interview problems** that test broadcasting, indexing, vectorization, and memory-efficient thinking. I'll explain them in a simple way.

---

# Problem 1: Pairwise Euclidean Distance Matrix (No Loops)

### Question

Given:

```
X=np.array([
    [1,2],
    [3,4],
    [5,6]
])
```

Compute the distance between every pair of points without using loops.

Expected:

```
[[0.00,2.83,5.66],
 [2.83,0.00,2.83],
 [5.66,2.83,0.00]]
```

---

## Naive Solution

```
foriinrange(n):
forjinrange(n):
        ...
```

Complexity:

```
O(n²)
```

Works, but not vectorized.

---

## NumPy Solution

```
importnumpyasnp

X=np.array([
    [1,2],
    [3,4],
    [5,6]
])

diff=X[:,np.newaxis, :]-X[np.newaxis, :, :]

dist=np.sqrt(np.sum(diff**2,axis=2))

print(dist)
```

---

## How Broadcasting Works

Shape of X:

```
(3, 2)
```

After:

```
X[:,np.newaxis, :]
```

Shape:

```
(3, 1, 2)
```

After:

```
X[np.newaxis, :, :]
```

Shape:

```
(1, 3, 2)
```

Broadcasting:

```
(3,1,2)
(1,3,2)
---------
(3,3,2)
```

NumPy automatically creates:

```
point1 - point1
point1 - point2
point1 - point3

point2 - point1
point2 - point2
point2 - point3

point3 - point1
point3 - point2
point3 - point3
```

---

## Interview Insight

This demonstrates:

- Broadcasting
- High-dimensional thinking
- Vectorized geometry

Interviewers love this question because many candidates immediately write nested loops.

---

# Problem 2: Find All Row Duplicates in a Huge Matrix

### Question

Given:

```
A=np.array([
    [1,2,3],
    [4,5,6],
    [1,2,3],
    [7,8,9],
    [4,5,6]
])
```

Find duplicate rows.

Expected:

```
[1 2 3]
[4 5 6]
```

---

## Difficult Part

NumPy's `unique()` works on elements.

We need uniqueness across rows.

---

## Solution

```
importnumpyasnp

A=np.array([
    [1,2,3],
    [4,5,6],
    [1,2,3],
    [7,8,9],
    [4,5,6]
])

unique_rows,counts=np.unique(
A,
axis=0,
return_counts=True
)

duplicates=unique_rows[counts>1]

print(duplicates)
```

---

## Output

```
[[1 2 3]
 [4 5 6]]
```

---

## Deep Explanation

Internally:

```
np.unique(axis=0)
```

Treats each row as one unit:

```
[1,2,3]
[4,5,6]
[1,2,3]
```

instead of:

```
1,2,3,4,5,6...
```

Counts become:

```
[2,2,1]
```

Then:

```
counts>1
```

gives duplicates.

---

## Interview Follow-Up

Find first occurrence indices:

```
unique_rows,idx,counts=np.unique(
A,
axis=0,
return_index=True,
return_counts=True
)
```

Many senior-level interviews ask this extension.

---

# Problem 3: Sliding Window Moving Average Without Loops

This is considered an advanced vectorization question.

---

### Question

Given:

```
arr=np.array([1,2,3,4,5,6,7])
```

Window size:

```
3
```

Output:

```
[2.,3.,4.,5.,6.]
```

Because:

```
(1+2+3)/3 = 2
(2+3+4)/3 = 3
(3+4+5)/3 = 4
...
```

---

## Beginner Solution

```
foriinrange(len(arr)-2):
    ...
```

---

## Advanced NumPy Solution

```
importnumpyasnp

arr=np.array([1,2,3,4,5,6,7])

window=3

shape= (arr.size-window+1,window)

strides= (arr.strides[0],arr.strides[0])

view=np.lib.stride_tricks.as_strided(
arr,
shape=shape,
strides=strides
)

result=view.mean(axis=1)

print(result)
```

---

## Output

```
[2.3.4. 5.6.]
```

---

## Deep Explanation

Original memory:

```
1 2 3 4 5 6 7
```

Normal thinking:

```
[1 2 3]
[2 3 4]
[3 4 5]
[4 5 6]
[5 6 7]
```

You might think NumPy creates 5 new arrays.

It doesn't.

`as_strided()` creates a **view**.

Memory:

```
1 2 3 4 5 6 7
```

still exists only once.

The rows are just different ways of looking at the same memory.

---

## Why Interviewers Love This

Tests understanding of:

- Memory layout
- Strides
- Views
- Performance optimization

Most developers know:

```
reshape()
```

Few understand:

```
strides
```

---

# Bonus: The Senior-Level Interview Question

What is the complexity of Problem 1?

Many candidates answer:

```
O(n)
```

Wrong.

Distance matrix contains:

```
n × n
```

values.

Therefore:

```
O(n²)
```

memory and time.

Even with broadcasting, NumPy cannot escape the mathematical requirement of producing n2n^2n2 distances.

This is exactly the kind of subtle question asked in high-level interviews.

---

## What These Problems Actually Test

| Problem | Concept |
| --- | --- |
| Pairwise Distances | Broadcasting + Vectorization |
| Duplicate Rows | Axis operations + Array manipulation |
| Sliding Window | Memory sharing + Strides + Views |