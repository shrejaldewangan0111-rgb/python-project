# Student Record Management System

**PS No. 14** | Rungta International Skills University
School of Computer Science and Engineering | B.Tech Computer Science and Engineering

**Student:** `<Your Name>`  |  **Roll No / Enrollment No:** `<Your Roll No>`  |  **Section:** `<Section>`

---

## 1. Problem Statement

Develop a console-based system to maintain student records (roll number, name, course, marks) with the ability to **add, view, search, update and delete** records.

**Rules**
- Roll numbers must be unique.
- Marks must be between 0 and 100.
- Test cases run in order on the same records.

**Language:** Python 3
**Concepts used:** Lists, Tuples, Dictionaries, CRUD

---

## 2. Features

| Operation | Function | Description |
|---|---|---|
| Create | `add_record()` | Adds a new student after validating roll number and marks |
| Read (all) | `view_records()` | Prints all records in a neat table, sorted by roll number |
| Read (one) | `search_record()` | Finds a student by roll number |
| Update | `update_record()` | Changes the marks of an existing student |
| Delete | `delete_record()` | Removes a student by roll number |

Extra: input helpers (`read_int`, `read_text`) keep the program from crashing on wrong input, and menu option 6 runs all four test cases automatically.

---

## 3. Data Structures Used

- **Dictionary**: `records = {roll_number: record}` gives fast lookup, and the roll number acts as a unique key.
- **Tuple**: each record is stored as `(roll, name, course, marks)`. Tuples are immutable, so an update creates a new tuple and replaces the old one.
- **List**: records are collected into a list and sorted before being shown in the table.

---

## 4. How to Run

Requirement: Python 3.x (no external libraries needed).

```bash
python one.py
```

Menu:

```
===== Student Record Management System =====
1. Add record
2. View all records
3. Search record
4. Update marks
5. Delete record
6. Run the 4 test cases
7. Exit
```

---

## 5. Test Cases and Results

The four test cases from the problem sheet, run in order on the same records:

| # | Scenario | Input | Expected / Actual Output |
|---|---|---|---|
| 1 | Normal input | Add: 101, Aman, BTech, 78 | `Record added: 101 \| Aman \| BTech \| 78` |
| 2 | Boundary input | Add: 102, Riya, BTech, 100 | `Record added: 102 \| Riya \| BTech \| 100` |
| 3a | Invalid (duplicate) | Add: 101, Neha, BTech, 70 | `Roll number 101 already exists.` |
| 3b | Invalid (marks) | Add: 103, Ravi, BTech, 150 | `Marks must be between 0 and 100.` |
| 4a | Search | Search: 101 | `101 \| Aman \| BTech \| 78` |
| 4b | Update | Update marks of 101 to 85 | `Marks updated: 85` |
| 4c | Delete (missing) | Delete: 999 | `Roll number 999 not found.` |

All outputs match the expected results.

### Sample table output (option 2)

```
+----------+--------------------+------------+--------+
| Roll No  | Name               | Course     | Marks  |
+----------+--------------------+------------+--------+
| 101      | Aman               | BTech      | 85     |
| 102      | Riya               | BTech      | 100    |
+----------+--------------------+------------+--------+
```

---

## 6. Project Structure

```
student-record-management-system/
├── one.py   # complete source code (single file)
└── README.md            # project documentation
```

---

## 7. Possible Improvements

- Save records to a JSON or CSV file so data persists between runs
- Sort or filter by marks
- Show class average, topper and fail count

---

## 8. Conclusion

The project implements all CRUD operations using lists, tuples and dictionaries, enforces unique roll numbers and valid marks, and passes all four given test cases.