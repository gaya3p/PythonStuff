# Todo

## Functions (6/10)
1. feet to inch ✅
2. factorial ✅
3. Prime numbers ✅
<!-- 4. Tic tac toe😋 -->
4. palindrome ✅
5. guessing game ✅
6. roman ✅

## Libraries (2/3)
1. Create a module 'mensuration.py' area and perimeter of following figures:
    (a)Circle, (b)Square, (c)Rectangle, (d)Equilateral Triangle, (e)Parallelogram.
    Insert help() function, which should give proper information about module. ✅
<!-- 2. Matrix operations (inverse, determinant, transpose) -->
3. Calculator ✅

## Stacks (3/4)
1. Write a program to implement a stack in python using lists. ✅
2. Write a program that implements a stack where the elements are shifted towards right so that the top always remains at 0th index. ✅
<!-- 3. comfest pulley thing -->
4. Write the game 2048 using stacks. 
Input: A list of integers.
Output: If two adjacent numbers are equal, the will be merged into one number with double the value. The task is to find the final set of numbers so that they cannot be merged further.
Eg: The input [2, 2, 4, 8, 8] will give [8, 16] ✅

## File Handling (9/12)
1. Write a program to read and display file content line by line with each word separated by '#' ✅
2. Write a program to read the content of file and display the total number of consonants, uppercase, vowels and lower case characters. ✅
3. Write a program to find the frequency of a given word in the file.✅
4. Write a program to read the content of file line by line and write it to another file except for the lines contains 'a' letter in it.✅
5. Write a program to take 10 sample phishing emails, and find the most common word occurring. ✅

6. Write a program to write student roll no, name and marks to a binary file. ✅
7. Write a program to update student marks in a binary file and show error if roll no is not found. ✅
8. Write a program to read, write and search students records to a binary file according to the user choice. ✅
9. Write a program to read marks of students from a binary file and show frequency of marks in every range (0 - 10, 10 - 20 etc. till 100). ✅
6. hangman 😁
7. csv file search

## pysql (5)
1. Write Python application that fetches all records from employee table of ecorp database ✅
1. Write Python application that insert records in employee table of ecorp database. Take the record as input from user, as many as desired.✅
2. Write a python program that can update a record in employee table of ecorp database based on value of primary key given by the user.✅
3. Write Python application that provides the user the choice, either to add a column or modify an exisiting column emp table of ecorp database. Take the required input from user.✅
4. Write a python application that fetches the population of every continent from the country table in world databse and lists them in decreasing order. Use SQL group statements to do the same.✅

## SQL (6)

#### Table 1
1. SELECT, GROUP, ORDER stuff
- a) List all names of those students who are in class 12 sorted by Stipend.
- b) List the Name and Stream of the students whose Grade is A.
- c) List the maximum and minimum mark in each stream

2. UPDATE, DELETE stuff
- a) Increase the stipend of medical students by 100
- b) Delete student records where grade is 'C' or 'B'
- c) insert shit

3. ALTER TABLE, MODIFY DATA, DROP ATTRIBUTE stuff
- a) Make the name attribute not null
- b) Delete the grade attribute from the table
- c) Rename AvgMark attribute to Mark

#### Table 2
4. SELECT, GROUP, ORDER stuff
- a) Display only the jobs with maximum salary greater than 70000
SELECT job FROM emp GROUP BY job HAVING MAX(salary) > 70000;
- b) Show the average salary of all departments with more than 2 employees for a job.
SELECT deptno, job, avg(salary) FROM emp GROUP BY deptno, job HAVING count(job) < 3 ORDER BY deptno, job;
- c) List the numbers of employees having 'Manager' as the job in every department. 
SELECT count(*) 'No. of Managers' FROM emp WHERE job = 'manager';

5. Join shit
- A) Identify the foreign key in table employee
- a) List employee name and their corresponding department name sorted by department name and then employee name.
SELECT name, dept_name FROM emp, depts WHERE emp.deptno = depts.deptno ORDER BY dept_name, name;
- b) List the name of the employee with maximum sales in each department along with the department name and sales
SELECT emp.deptno, dept_name, name 'Employee with max sales', sales FROM emp, depts WHERE sales = (SELECT MAX(sales) FROM emp WHERE emp.deptno = depts.deptno) GROUP BY emp.deptno;
- c) List the number of unique jobs in each department.
SELECT dept_name, count(DISTINCT job) 'No. of unique jobs' FROM emp, depts GROUP BY emp.deptno;

6. ALTER TABLE, MODIFY DATA, DROP ATTRIBUTE stuff
- a) Add attribute branch to the job table with default value of 'Corporate'.
- b) Chnage the name of the table to employee_new 
ALTER TABLE t RENAME TO employees;