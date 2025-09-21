# Python Beginner Programs  

This repository contains four beginner-level Python programs. Each file demonstrates a basic programming concept such as conditions, loops, functions, and file handling.  

---

## 1. Grade Checker (`grade_checker.py`)  
This program asks the user to enter a score and then checks which grade it belongs to using `if-elif-else` conditions.  

- Score **90 or above** → Grade **A**  
- Score **80–89** → Grade **B**  
- Score **70–79** → Grade **C**  
- Score **60–69** → Grade **D**  
- Anything below 60 → Grade **F**  

It then prints the grade to the user.  

---

## 2. Student Grades (`student_grades.py`)  
This program manages a list of students and their grades using a **dictionary**.  

- **Option 1**: Add a new student and grade.  
- **Option 2**: Update an existing student's grade.  
- **Option 3**: Print all student grades using the helper function `print_grades()`.  
- **Option 4**: Exit the program.
- - A dictionary stores data in **key-value pairs**, where the student’s name is the **key** and the grade is the **value**.  
- For example:  
  ```python
  grades = {"Alice": "A", "Bob": "B"}

It uses a `while True` loop to keep showing the menu until the user chooses to exit.  

---

## 3. File Write (`file_write.py`)  
This program creates a file called **output.txt** and writes two lines of text into it using Python’s `with open(..., 'w')`.  

- `'w'` mode means **write mode** (it creates or overwrites the file).  

---

## 4. File Read (`file_read.py`)  
This program opens the **output.txt** file created earlier, reads its content using `'r'` mode, and prints it to the console.  

---

