---
tags:
  - course
  - computing
---

# BSCS1001 Computational Thinking

**Course Credits**: 4

**Course Type**: Foundational

**Instructors**: Madhavan Mukund, Dr. G Venkatesh

**Pre-requisites**: None

## Overview
The course introduces fundamental programming concepts through manual problem solving. It focuses on communicating procedural solutions, understanding abstractions and selecting data structures.

## Learning Objectives
- Apply a procedural approach to real-life problems
- Communicate solutions using flowcharts and pseudocode
- Understand variables, iteration, filtering and parameterised procedures
- Choose data structures like lists, trees, matrices and graphs
- Identify algorithmic techniques such as searching, sorting and matching
- Decompose problems using recursion and divide-and-conquer
- Predict and test algorithm behaviour

## Course Structure
12 weeks of coursework with weekly online assignments, two invigilated quizzes and one invigilated end term exam.

## Weekly Topics
1.  **Variables & Flowcharts**
    *   **What is Computational Thinking?**:
        *   A problem-solving approach that involves:
            *   Decomposition: Breaking down a complex problem into smaller, more manageable parts.
            *   Pattern Recognition: Identifying similarities or trends within problems or data.
            *   Abstraction: Focusing on the essential information and ignoring irrelevant details.
            *   Algorithms: Developing a step-by-step solution to the problem or parts of it.
    *   **Algorithms**:
        *   Definition: A sequence of well-defined, unambiguous instructions or steps designed to solve a specific problem or achieve a particular outcome.
        *   Analogy: A recipe for baking a cake is an algorithm – it lists ingredients (inputs) and step-by-step instructions to produce the cake (output).
    *   **Variables**:
        *   Concept: A named placeholder or container used to store a piece of information (a value) that can change or vary during the execution of an algorithm.
        *   Analogy: Think of a labeled box (the variable name) where you can store an item (the value). You can change the item in the box.
        *   Declaring Variables: Conceptually, this means giving a name to your "box" and perhaps putting an initial item (value) into it. Example: `age = 25`, `userName = "Guest"`.
        *   Data Types (Conceptual): Understanding that variables hold different kinds of information:
            *   Numbers: For quantities (e.g., `count = 10`, `price = 19.99`).
            *   Text (Strings): For textual information (e.g., `message = "Hello"`, `city = "London"`).
            *   Boolean: For true/false values (e.g., `isLoggedIn = true`, `isValid = false`).
        *   Assignment: The process of giving a value to a variable. Typically written as `variable_name = value` or `SET variable_name TO value`. The value on the right is stored in the variable on the left. Example: `score = 100`. Later, `score = score + 10`.
    *   **Tracing Simple Algorithms by Hand (Desk Checking)**:
        *   Importance: A crucial skill to understand how an algorithm executes, to verify its correctness for given inputs, and to find errors in logic.
        *   Method: Create a table where columns represent each variable in the algorithm and one column for the current step or instruction being executed. Sometimes, an additional column for "output" or "conditions" is useful. You manually go through the algorithm step-by-step, updating the variable values in your table as they change.
        *   _Example: Algorithm to Calculate Area of a Rectangle_
            *   Variables: `length`, `width`, `area`
            *   Steps (Pseudocode):
                1.  START
                2.  GET `length`
                3.  GET `width`
                4.  `area = length * width`
                5.  DISPLAY `area`
                6.  END
            *   Trace Table Example (Input: length=5, width=3):
                | Step | Instruction         | length | width | area | Output      |
                |------|---------------------|--------|-------|------|-------------|
                | 1    | START               | -      | -     | -    |             |
                | 2    | GET `length`        | 5      | -     | -    |             |
                | 3    | GET `width`         | 5      | 3     | -    |             |
                | 4    | `area = length*width`| 5      | 3     | 15   |             |
                | 5    | DISPLAY `area`      | 5      | 3     | 15   | Display: 15 |
                | 6    | END                 |        |       |      |             |
    *   **Flowcharts**:
        *   Purpose: A graphical representation of an algorithm, showing the sequence of operations, decisions, and flow of control from start to finish.
        *   Common Flowchart Symbols:
            *   **Oval (Terminator)**: Represents the Start or End point of the algorithm.
            *   **Rectangle (Process)**: Represents a calculation or an instruction (e.g., `area = length * width`, `increment counter`).
            *   **Parallelogram (Input/Output)**: Represents getting input from a user or displaying output (e.g., `GET age`, `DISPLAY result`).
            *   **Diamond (Decision)**: Represents a point where a decision is made, usually a yes/no or true/false question (e.g., `Is age > 18?`). Has one entry point and two exit points (one for true, one for false).
            *   **Circle (Connector)**: Used to connect different parts of a flowchart, especially if it spans multiple pages or is complex, to avoid crossing flow lines.
            *   **Arrows (Flow Lines)**: Indicate the direction of flow and the sequence of steps.
        *   Example: Flowchart for "Is a number even or odd?"
            1.  Oval: START
            2.  Arrow to Parallelogram: GET `number`
            3.  Arrow to Diamond: `Is number % 2 == 0?` (where % is modulo/remainder)
            4.  Arrow (labeled "Yes") from Diamond to Parallelogram: DISPLAY "`number` is Even"
            5.  Arrow (labeled "No") from Diamond to Parallelogram: DISPLAY "`number` is Odd"
            6.  Arrows from both DISPLAY Parallelograms to Oval: END
    *   **Sanity Checks for Input Data**:
        *   Concept: Initial checks performed on input data to ensure it is reasonable, valid, and in the expected format before the main algorithm processes it.
        *   Importance: Helps prevent program crashes, incorrect results, or security vulnerabilities. Embodies the "Garbage In, Garbage Out" (GIGO) principle – if input is bad, output will likely be bad.
        *   Examples of Manual Sanity Checks:
            *   Age Problem: If an algorithm calculates something based on age, a sanity check would be: "Is the entered age a positive number?" "Is the age less than a reasonable maximum (e.g., 120)?"
            *   Score Input: If inputting a test score expected to be between 0 and 100: "Is the score ≥ 0 AND score ≤ 100?"
            *   Text Input: If asking for a name: "Is the input text, not a number?" "Is the length of the name reasonable (not empty, not excessively long)?"
2.  **Iteration & Selection**
    *   **Selection (Conditional Execution)**:
        *   Concept: The ability of an algorithm to make decisions and execute different sets of instructions based on whether a certain condition is true or false.
        *   **`IF-THEN-ELSE` Structure**:
            *   Pseudocode:
                ```
                IF (condition) THEN
                    (steps to perform if condition is true)
                ELSE
                    (steps to perform if condition is false)
                ENDIF
                ```
            *   Example: Determine if a number is positive or non-positive.
                ```
                GET number
                IF (number > 0) THEN
                    DISPLAY "Number is positive"
                ELSE
                    DISPLAY "Number is zero or negative"
                ENDIF
                ```
        *   **`IF-THEN` Structure**: Used when actions are only taken if a condition is true, with no alternative actions if false.
            *   Pseudocode:
                ```
                IF (condition) THEN
                    (steps to perform if condition is true)
                ENDIF
                ```
        *   **Nested IF Statements**: An IF statement inside another IF statement, allowing for more complex decision-making.
            Example:
            ```
            IF (temperature > 30) THEN
                DISPLAY "It's hot."
                IF (humidity > 80) THEN
                    DISPLAY "It's also humid!"
                ENDIF
            ELSE
                DISPLAY "It's not hot."
            ENDIF
            ```
    *   **Logical Conditions and Operators**:
        *   Boolean Values: Represent truth values - `TRUE` or `FALSE`. Conditions in IF statements evaluate to a Boolean value.
        *   Comparison Operators: Used to compare values.
            *   `>` (greater than), `<` (less than)
            *   `>=` (greater than or equal to), `<=` (less than or equal to)
            *   `==` (equal to), `!=` (not equal to)
        *   Logical Operators: Combine or modify Boolean conditions.
            *   `AND`: `(condition1 AND condition2)` is `TRUE` only if *both* condition1 and condition2 are `TRUE`.
                | cond1 | cond2 | cond1 AND cond2 |
                |-------|-------|-----------------|
                | TRUE  | TRUE  | TRUE            |
                | TRUE  | FALSE | FALSE           |
                | FALSE | TRUE  | FALSE           |
                | FALSE | FALSE | FALSE           |
            *   `OR`: `(condition1 OR condition2)` is `TRUE` if *at least one* of condition1 or condition2 is `TRUE`.
                | cond1 | cond2 | cond1 OR cond2 |
                |-------|-------|----------------|
                | TRUE  | TRUE  | TRUE           |
                | TRUE  | FALSE | TRUE           |
                | FALSE | TRUE  | TRUE           |
                | FALSE | FALSE | FALSE          |
            *   `NOT`: `(NOT condition1)` reverses the truth value of condition1. If condition1 is `TRUE`, `NOT condition1` is `FALSE`, and vice-versa.
    *   **Iteration (Repetition/Looping)**:
        *   Concept: Repeating a block of instructions multiple times until a certain condition is met or for a predetermined number of repetitions.
        *   Types of Loops (Conceptual):
            *   **Count-Controlled Loops (`FOR` style)**: Used when you know in advance how many times you want to repeat the loop.
                *   Structure (Conceptual Pseudocode):
                    ```
                    FOR counter FROM start_value TO end_value [STEP step_increment] DO
                        (steps to perform in each iteration)
                    ENDFOR
                    ```
                *   `counter` is a variable that changes with each iteration.
                *   `step_increment` is often 1 by default.
                *   Example: Print "Hello" 5 times.
                    ```
                    FOR count FROM 1 TO 5 DO
                        DISPLAY "Hello"
                    ENDFOR
                    ```
            *   **Condition-Controlled Loops (`WHILE` style)**: Used when the repetition continues as long as a specified condition remains true. The number of iterations might not be known beforehand.
                *   Structure (Conceptual Pseudocode):
                    ```
                    WHILE (condition is TRUE) DO
                        (steps to perform in each iteration)
                        (ensure something inside the loop can change the condition to FALSE eventually)
                    ENDWHILE
                    ```
                *   Caution: If the condition never becomes false, an *infinite loop* occurs.
                *   Example: Sum numbers entered by a user until they enter 0.
                    ```
                    SET total_sum TO 0
                    GET number
                    WHILE (number != 0) DO
                        total_sum = total_sum + number
                        GET number
                    ENDWHILE
                    DISPLAY total_sum
                    ```
            *   `DO-WHILE` style (execute once, then check condition):
                ```
                DO
                    (steps to perform)
                WHILE (condition is TRUE)
                ```
    *   **Filtering Items with Conditions**:
        *   Combining iteration and selection to process a collection of items (e.g., a list of numbers, a set of student records) and perform an action only on those items that satisfy a specific condition.
        *   Example: Given a list of numbers: [10, 7, 4, 15, 3, 8]. Print only numbers greater than 5.
            *   Algorithm idea:
                1.  For each `num` in the list:
                2.  `IF (num > 5) THEN`
                3.  `  DISPLAY num`
                4.  `ENDIF`
            *   This involves iterating through the list and applying a selection (IF condition) to each item.
    *   **Basic Pseudocode Conventions**:
        *   Purpose: An intermediate step between an idea/flowchart and actual programming code. It uses plain language mixed with common programming structures to describe an algorithm's logic clearly and unambiguously, without worrying about the strict syntax of a specific programming language.
        *   Common Keywords/Structures:
            *   Input: `READ age`, `GET name`, `INPUT score`
            *   Output: `PRINT result`, `DISPLAY message`, `WRITE total`
            *   Processing/Assignment: `SET count TO 0`, `CALCULATE average = sum / count`, `variable = expression`
            *   Selection: `IF (condition) THEN ... ELSE ... ENDIF`
            *   Iteration: `FOR counter FROM start TO end DO ... ENDFOR`, `WHILE (condition) DO ... ENDWHILE`, `DO ... WHILE (condition)`
            *   Procedure/Function calls: `CALL MyProcedure(argument)`
            *   Keywords should be clear (often capitalized for distinction).
            *   Indentation is crucial to show blocks of code within loops, selections, etc., enhancing readability.
            *   Comments: Use `//` or `/* ... */` or `REM` (remark) to add explanations that are not part of the algorithm itself.
        *   Example: Pseudocode for finding the largest of two numbers.
            ```pseudocode
            // Algorithm to find the largest of two numbers
            START
                READ num1
                READ num2

                IF (num1 > num2) THEN
                    DISPLAY num1 + " is larger."
                ELSE IF (num2 > num1) THEN
                    DISPLAY num2 + " is larger."
                ELSE
                    DISPLAY "Both numbers are equal."
                ENDIF
            END
            ```
3.  **Multiple Iterations**
    *   **Recap of Boolean Logic (AND/OR/NOT)**:
        *   `AND`: True if all conditions are true. (e.g., `age >= 18 AND has_license == TRUE`)
        *   `OR`: True if at least one condition is true. (e.g., `is_weekend == TRUE OR is_holiday == TRUE`)
        *   `NOT`: Reverses the truth value. (e.g., `NOT is_member == TRUE` is same as `is_member == FALSE`)
        *   Truth Tables are useful for understanding combinations.
        *   De Morgan's Laws (Optional but powerful for simplifying complex conditions):
            *   `NOT (A AND B)` is equivalent to `(NOT A) OR (NOT B)`
            *   `NOT (A OR B)` is equivalent to `(NOT A) AND (NOT B)`
    *   **Procedures (Functions/Subroutines - Conceptual)**:
        *   Concept: A self-contained, named block of instructions designed to perform a specific, well-defined task. Procedures can be "called" (or "invoked") from other parts of an algorithm to execute their task.
        *   Benefits:
            *   Modularity: Helps break down large, complex problems into smaller, simpler, more manageable sub-problems. Each procedure handles one sub-problem.
            *   Reusability: A procedure can be written once and called multiple times with different inputs, avoiding code duplication.
            *   Readability & Maintainability: Makes algorithms easier to understand by abstracting away details. Changes to a specific task only need to be made within its procedure.
        *   Defining a Procedure (Conceptual Pseudocode):
            ```
            PROCEDURE ProcedureName (parameter1, parameter2, ...)
                (Instructions to perform the task)
                [RETURN value] // Optional: some procedures return a value
            ENDPROCEDURE
            ```
        *   Calling a Procedure (Conceptual Pseudocode):
            ```
            CALL ProcedureName (argument1, argument2, ...)
            // or if it returns a value:
            // SET result_variable TO ProcedureName (argument1, argument2, ...)
            ```
    *   **Parameters and Arguments**:
        *   Parameters: Variables declared in the procedure definition. They act as placeholders for the values that will be passed into the procedure when it is called. Example: In `PROCEDURE Add (num1, num2)`, `num1` and `num2` are parameters.
        *   Arguments: The actual values or variables that are passed to a procedure when it is called. Example: In `CALL Add (5, 7)`, `5` and `7` are arguments.
        *   Analogy: A recipe (procedure) might say "add `amount_of_sugar` (parameter)". When you bake (call), you use "1 cup of sugar" (argument).
        *   Pass-by-value (Conceptual): A copy of the argument's value is passed to the parameter. Changes to the parameter inside the procedure do not affect the original argument outside the procedure. (Common default).
        *   Pass-by-reference (Conceptual): The procedure gets direct access to the original argument (e.g., its memory location). Changes to the parameter inside the procedure *do* affect the original argument.
    *   **Side Effects of Mutation**:
        *   Mutation: The act of changing the state or value of a variable after it has been created.
        *   Side Effect: A procedure has a side effect if it modifies some state outside its local environment, other than by returning a value. This includes modifying global variables or variables passed by reference.
        *   Importance: While sometimes necessary, unintended side effects can make algorithms difficult to understand, trace, and debug because a procedure might change things in unexpected places.
        *   Example:
            ```pseudocode
            // Global variable
            SET total_items TO 0

            PROCEDURE AddItem (item_value)
                // This procedure has a side effect: it modifies global_total
                SET total_items TO total_items + item_value
            ENDPROCEDURE

            CALL AddItem(10) // total_items becomes 10
            CALL AddItem(5)  // total_items becomes 15
            ```
            It's often preferred for procedures to operate on inputs (parameters) and produce outputs (return values) without other side effects, promoting "functional purity" in some contexts.
    *   **The "Three Prizes Problem" (Illustrative Example for Logic/Iteration)**:
        *   Problem: "You have three distinct prizes (Prize1, Prize2, Prize3) to award to three distinct people (Alice, Bob, Carol). Each person can only receive one prize. List all possible ways to award the prizes."
        *   Manual Thought Process / Algorithmic Steps:
            1.  Consider Prize1: It can be given to Alice, Bob, or Carol (3 choices).
            2.  IF Prize1 goes to Alice:
                THEN Prize2 can go to Bob or Carol (2 choices).
                IF Prize2 goes to Bob, THEN Prize3 must go to Carol (1 choice). (Alice-Prize1, Bob-Prize2, Carol-Prize3)
                IF Prize2 goes to Carol, THEN Prize3 must go to Bob (1 choice). (Alice-Prize1, Carol-Prize2, Bob-Prize3)
            3.  IF Prize1 goes to Bob:
                THEN Prize2 can go to Alice or Carol (2 choices).
                ... and so on.
            *   This involves careful iteration through possibilities and ensuring constraints (one prize per person) are met. This is a permutation problem P(3,3) = 3! = 6 ways.
            *   This problem helps illustrate how one might systematically list possibilities, perhaps using iteration or a decision tree structure in one's mind.
    *   **Distinction between Multiple Separate Iterations vs. Nested Iterations**:
        *   Multiple Separate Iterations: Involve two or more loops that execute one after another. The first loop completes all its iterations before the second loop begins.
            *   Example:
                ```pseudocode
                // First loop: Process items in ListA
                FOR each_itemA IN ListA DO
                    DISPLAY itemA
                ENDFOR

                // Second loop: Process items in ListB (starts after first loop finishes)
                FOR each_itemB IN ListB DO
                    DISPLAY itemB
                ENDFOR
                ```
        *   Nested Iterations (covered in Week 4): Involve one loop entirely contained within another loop. The inner loop completes all its iterations for *each single* iteration of the outer loop.
4.  **Nested Iterations**
    *   **Nested Iterations (Loops inside Loops)**:
        *   Concept: A control structure where one loop (the "inner loop") is placed inside the body of another loop (the "outer loop"). The inner loop executes completely for each single iteration of the outer loop.
        *   Structure Example (Pseudocode):
            ```
            FOR i FROM 1 TO OuterLimit DO       // Outer loop
                (Outer loop statements - execute OuterLimit times)
                FOR j FROM 1 TO InnerLimit DO   // Inner loop
                    (Inner loop statements - execute InnerLimit times for EACH outer iteration)
                    // Total executions of this block: OuterLimit * InnerLimit
                ENDFOR
                (More outer loop statements)
            ENDFOR
            ```
        *   Analogy:
            *   Clock: The hour hand (outer loop) moves from 1 to 12. For each hour, the minute hand (inner loop) moves from 0 to 59 minutes.
            *   Calendar: Iterating through months of a year (outer loop), and for each month, iterating through its days (inner loop).
            *   Grid/Table: To process each cell in a grid, you might iterate through each row (outer loop), and for each row, iterate through each column (inner loop).
        *   Examples:
            *   Printing a 3x3 grid of asterisks:
                ```pseudocode
                FOR row FROM 1 TO 3 DO
                    FOR col FROM 1 TO 3 DO
                        PRINT "*" (on the same line)
                    ENDFOR
                    PRINT newline // Move to the next line after each row
                ENDFOR
                ```
                Output:
                ***
                ***
                ***
            *   Finding all pairs of students from a class list to form a team of two (order doesn't matter for the pair itself, but the loops help generate unique pairs).
    *   **Birthday Paradox (Conceptual Simulation/Logic)**:
        *   Problem Statement: In a group of N people, what's the likelihood that at least two people share the same birthday (day and month)? (It's surprisingly high for relatively small N).
        *   Computational Thinking Approach (Manual Simulation Logic):
            1.  Imagine you have a list of N people's birthdays.
            2.  To find a match:
                *   Take the first person's birthday.
                *   Compare it with the second person's birthday. If it matches, you found a pair.
                *   If not, compare it with the third person's birthday, and so on, up to the Nth person.
                *   (This is the outer loop selecting person `i`)
            3.  If no match was found for the first person, take the second person's birthday.
            4.  Compare it with the third person's birthday (no need to compare with the first again, as that was already done).
            5.  Continue comparing with the fourth, ..., Nth person.
            6.  (This is the inner loop selecting person `j`, where `j` starts from `i+1`)
            *   This thought process involves a nested comparison:
                ```pseudocode
                FOR i FROM 1 TO N-1 DO  // Select the first person
                    FOR j FROM i+1 TO N DO // Select the second person (must be different from the first)
                        IF (birthday[i] == birthday[j]) THEN
                            DISPLAY "Match found between person " + i + " and person " + j
                            // Could stop or count matches
                        ENDIF
                    ENDFOR
                ENDFOR
                ```
            *   The focus here is on the nested iteration logic required to compare all unique pairs.
    *   **Binning Data into Ranges**:
        *   Concept: Categorizing numerical data into predefined intervals or "bins".
        *   Example: Given exam scores [85, 92, 75, 68, 90, 78, 72, 88, 61, 55], bin them into:
            *   A: 80-100
            *   B: 70-79
            *   C: 60-69
            *   D: 50-59
            *   F: 0-49
        *   Algorithmic Approach (using a single loop over data and IF-ELSEIF for bins):
            ```pseudocode
            DECLARE scores = [85, 92, 75, 68, 90, 78, 72, 88, 61, 55]
            DECLARE countA = 0, countB = 0, countC = 0, countD = 0, countF = 0

            FOR each score IN scores DO
                IF (score >= 80 AND score <= 100) THEN
                    INCREMENT countA
                ELSE IF (score >= 70 AND score <= 79) THEN
                    INCREMENT countB
                ELSE IF (score >= 60 AND score <= 69) THEN
                    INCREMENT countC
                ELSE IF (score >= 50 AND score <= 59) THEN
                    INCREMENT countD
                ELSE IF (score >= 0 AND score <= 49) THEN
                    INCREMENT countF
                ENDIF
            ENDFOR

            DISPLAY "Grade A: " + countA
            DISPLAY "Grade B: " + countB
            // ... and so on
            ```
            *   While this example uses a single loop over the data items, the process of checking against multiple bin conditions is a form of case analysis. Nested loops *could* be used if, for instance, you had a list of bin definitions and iterated through bins for each score, but the IF-ELSEIF is more direct here.
    *   **Complexity Considerations (Introduction - Algorithmic Efficiency)**:
        *   Concept: An informal understanding of how the number of steps an algorithm takes (its "running time") or the amount of memory it uses grows as the size of its input grows.
        *   Why it matters: An algorithm that is efficient will run faster and use less memory, especially for large inputs. An inefficient algorithm might become too slow to be useful.
        *   Nested Loops Impact: Nested loops are a common way algorithms become less efficient.
            *   If an outer loop runs N times, and for each of those N times, an inner loop also runs N times, then the statements inside the inner loop will execute N * N = N² times.
            *   Example: The Birthday Paradox simulation logic above has an outer loop that runs roughly N times and an inner loop that also runs roughly N times. This leads to approximately N² comparisons. If N=100 people, that's about 100*100 = 10,000 comparisons. If N=1000, it's 1,000,000 comparisons. The work grows much faster than N.
        *   Simple Examples of "Order":
            *   Algorithm with one loop iterating N times: Roughly N steps. We might say it's "Order N".
            *   Algorithm with two nested loops, each iterating N times: Roughly N² steps. "Order N-squared".
        *   Goal: Generally, we prefer algorithms with a lower order of growth (e.g., Order N is better than Order N-squared for large N). This is a very early, intuitive introduction to a concept formally known as "Big O notation."
5.  **Lists**
    *   **Introduction to Collections/Data Structures**:
        *   Why we need them: Algorithms often need to work with groups of related data items. Data structures provide ways to organize, store, and manage these collections efficiently.
        *   Analogy: A shopping list helps organize items you need to buy. A phone book organizes contacts. A library's card catalog organizes books.
    *   **Lists (Arrays/Sequences - Conceptual)**:
        *   Definition: A list is an ordered collection of items, called elements. The order of elements is preserved.
        *   Properties:
            *   Ordered: Elements are stored in a specific sequence. The position of each element matters.
            *   Indexed: Each element in a list can be accessed by its position, called an index. Indices usually start from 0 (for the first element) or 1. Example: If `my_list = ["apple", "banana", "cherry"]`, then `my_list[0]` could be "apple" and `my_list[1]` could be "banana".
            *   Dynamic Size (Conceptual): For computational thinking, we often imagine lists as being flexible; they can grow when new items are added or shrink when items are removed. (Some programming languages have fixed-size arrays, while others have dynamic lists/arrays).
            *   Element Types: A list can contain items of the same type (e.g., a list of numbers) or sometimes mixed types (e.g., a list containing a number, some text, and a true/false value), though often lists of the same type are easier to reason about.
    *   **Common List Operations (Conceptual - how one would manually think about them)**:
        *   Creating a list: Defining a new list with some initial items. E.g., `SET shopping_list TO ["milk", "eggs", "bread"]`.
        *   Accessing elements: Getting the value of an item at a specific index. E.g., "What is the second item on my shopping list?" -> Access `shopping_list[1]` (if 0-indexed).
        *   Updating elements: Changing the value of an item at a specific index. E.g., "Change the second item on my shopping list from 'eggs' to 'butter'." -> `SET shopping_list[1] TO "butter"`.
        *   Adding elements:
            *   Append: Adding a new item to the end of the list. E.g., "Add 'cheese' to my shopping list."
            *   Insert: Adding a new item at a specific position/index in the list, shifting subsequent items. E.g., "Insert 'juice' as the new second item."
        *   Removing elements:
            *   Remove from end: Deleting the last item.
            *   Remove at index: Deleting the item at a specific position, shifting subsequent items.
        *   Finding the length: Determining how many items are currently in the list. E.g., "How many items are on my shopping list?"
        *   Iterating through a list: Processing each element in the list one by one, from the first to the last. This is typically done using a loop.
            ```pseudocode
            FOR EACH item IN my_list DO
                // Do something with 'item'
                DISPLAY item
            ENDFOR
            ```
    *   **Using Lists to Store Dynamic Data**:
        *   Examples:
            *   Storing a list of scores entered by a user, where you don't know beforehand how many scores will be entered.
            *   Keeping track of tasks in a to-do list; tasks can be added or removed.
            *   Managing a queue of customers waiting for service.
    *   **Searching in a List (Linear Search - Manual Walkthrough)**:
        *   Problem: Given a list and a target value, determine if the target value exists in the list. If it does, optionally return its position (index).
        *   Algorithm (Linear Search):
            1.  START with the first item in the list (e.g., at index 0).
            2.  COMPARE the current item with the target value.
            3.  IF they are the same, THEN the target is found. STOP and report "Found" (and its index).
            4.  IF they are not the same, MOVE to the next item in the list.
            5.  IF there are no more items to check (i.e., you've reached the end of the list), THEN the target is not in the list. STOP and report "Not found".
        *   Trace Example: `my_list = [10, 30, 5, 15, 20]`, `target = 15`
            | Current Item | Index | Compare with 15? | Result      |
            |--------------|-------|------------------|-------------|
            | 10           | 0     | No               | Continue    |
            | 30           | 1     | No               | Continue    |
            | 5            | 2     | No               | Continue    |
            | 15           | 3     | Yes              | Found at index 3 |
    *   **Sorting a List (Introduction)**:
        *   Why sort?: Arranging items in a list into a specific order (e.g., ascending or descending for numbers, alphabetical for text).
        *   Benefits: Makes searching for items much faster (e.g., enabling binary search), helps in identifying duplicates, makes data easier to read and analyze, useful for finding min/max values.
    *   **Insertion Sort (Manual Walkthrough)**:
        *   Concept: A simple sorting algorithm that builds the final sorted list one item at a time. It iterates through the input elements and, for each element, it inserts it into its correct position within the already sorted portion of the list.
        *   Analogy: How many people sort a hand of playing cards. You pick up cards one by one. For each new card, you insert it into the correct position relative to the cards you are already holding (which are already sorted).
        *   Algorithm Steps (High-level for manual trace):
            1.  Start with the second element of the list (assume the first element by itself is a "sorted sublist" of one).
            2.  Pick the current element (let's call it `key`).
            3.  Compare `key` with the elements in the sorted sublist to its left, moving from right to left.
            4.  While an element in the sorted sublist is greater than `key`, shift that element one position to the right to make space.
            5.  Insert `key` into the now-empty slot where it belongs.
            6.  Repeat steps 2-5 for all remaining unsorted elements.
        *   Detailed Trace: Example list `[5, 1, 4, 2, 8]`
            *   **Initial:** `[5, 1, 4, 2, 8]` (Sorted part considered `[5]`)
            *   **Pass 1 (consider element `1`):**
                *   `key = 1`. Compare `1` with `5`. `5 > 1`, so shift `5` right: `[_, 5, 4, 2, 8]`
                *   Insert `1`: `[1, 5, 4, 2, 8]` (Sorted part: `[1, 5]`)
            *   **Pass 2 (consider element `4`):**
                *   `key = 4`. Compare `4` with `5`. `5 > 4`, so shift `5` right: `[1, _, 5, 2, 8]`
                *   Compare `4` with `1`. `1 < 4`, so insert `4` in the empty slot: `[1, 4, 5, 2, 8]` (Sorted part: `[1, 4, 5]`)
            *   **Pass 3 (consider element `2`):**
                *   `key = 2`. Compare `2` with `5`. `5 > 2`, shift `5`: `[1, 4, _, 5, 8]`
                *   Compare `2` with `4`. `4 > 2`, shift `4`: `[1, _, 4, 5, 8]`
                *   Compare `2` with `1`. `1 < 2`, so insert `2`: `[1, 2, 4, 5, 8]` (Sorted part: `[1, 2, 4, 5]`)
            *   **Pass 4 (consider element `8`):**
                *   `key = 8`. Compare `8` with `5`. `5 < 8`. No shifts needed, `8` is in place relative to sorted part.
                *   List remains: `[1, 2, 4, 5, 8]` (Sorted part: `[1, 2, 4, 5, 8]`)
            *   List is now sorted.
6.  **Tables & Dictionaries**
    *   **Limitations of Lists for Certain Tasks**:
        *   Searching for a specific item in an unsorted list requires checking each item one by one (linear search), which can be slow for long lists.
        *   Accessing items is based on numerical position (index). If you want to access an item based on a non-numerical identifier (e.g., finding a person's phone number by their name), lists are not ideal.
    *   **Tables (Conceptual - Key-Value Pairs)**:
        *   Concept: A data structure that stores a collection of items, where each item consists of a unique *key* and an associated *value*. The key is used to look up the value.
        *   Analogy:
            *   A physical dictionary: The word (key) is used to look up its definition (value).
            *   A phone book: A person's name (key) is used to find their phone number (value).
            *   Student records: Student ID (key) maps to a record containing all student details (value).
        *   Key Properties:
            *   Keys must be unique within the table. Each key maps to exactly one value.
            *   Keys are used for efficient retrieval of their associated values.
    *   **Dictionaries (Associative Arrays, Hash Maps, Maps - Conceptual)**:
        *   These are common terms for the data structure that implements the key-value table concept in computational systems.
        *   Operations (Conceptual - how one would manually think about them):
            *   Adding a new key-value pair: `STORE key_A WITH value_1 IN my_dictionary`. Example: `my_dictionary["apple"] = "a red fruit"`.
            *   Accessing a value: `GET value FOR key_A FROM my_dictionary`. Example: `definition = my_dictionary["apple"]`.
            *   Updating a value: If the key already exists, assign a new value to it. `UPDATE key_A WITH new_value_1 IN my_dictionary`. Example: `my_dictionary["apple"] = "a delicious red fruit"`.
            *   Removing a key-value pair: `REMOVE entry FOR key_A FROM my_dictionary`.
            *   Checking if a key exists: "Does `my_dictionary` contain `key_A`?"
            *   Iterating: You can iterate through all keys, all values, or all key-value pairs.
    *   **Hashing Concepts (Simplified Intuition)**:
        *   Problem: If you have many key-value pairs, how do you quickly find the value for a given key without checking every single key (like in a list)?
        *   Hash Function: A special function that takes a key as input and computes a numerical value called a "hash code" or simply "hash". This hash code is then often used to determine an index or position where the key-value pair should be stored in memory (e.g., in an array).
        *   Analogy: Imagine a large filing cabinet with many drawers. A hash function is like a rule that tells you which drawer to look in based on the key (e.g., for a name, the first letter might tell you the drawer). This is much faster than opening every drawer.
        *   Ideal Hash Function:
            *   Deterministic: The same key always produces the same hash code.
            *   Uniform Distribution: Spreads keys out evenly across possible hash codes/indices to minimize collisions.
        *   Collisions: Occur when two different keys produce the same hash code (i.e., they are mapped to the same storage location/index).
            *   Brief mention: This is a common issue. Systems have strategies to handle collisions (e.g., storing multiple items at that location in a list, or finding another nearby empty spot). A deep dive into collision resolution is not needed here, just the awareness.
        *   How it helps dictionaries: By using a hash function, dictionaries can typically store and retrieve values very quickly, often in nearly constant time on average, regardless of the number of items.
    *   **Dictionary-Based Counting**:
        *   Problem: Efficiently count the frequency of occurrence of each unique item in a collection (e.g., words in a text, numbers in a list).
        *   Example: Count occurrences of each fruit in the list `["apple", "orange", "apple", "banana", "orange", "apple"]`.
        *   Algorithm using a dictionary (e.g., `fruit_counts`):
            1.  Initialize an empty dictionary: `fruit_counts = {}`.
            2.  Iterate through the list of fruits. For each `fruit`:
                a.  `IF fruit IS A KEY IN fruit_counts THEN` (check if we've seen this fruit before)
                b.    `INCREMENT the value (count) associated with fruit_counts[fruit]`.
                c.  `ELSE` (it's the first time we've seen this fruit)
                d.    `ADD fruit AS A NEW KEY TO fruit_counts WITH VALUE 1`.
        *   Trace:
            *   `apple`: `fruit_counts = {"apple": 1}`
            *   `orange`: `fruit_counts = {"apple": 1, "orange": 1}`
            *   `apple`: `fruit_counts["apple"]` becomes 2. `fruit_counts = {"apple": 2, "orange": 1}`
            *   `banana`: `fruit_counts = {"apple": 2, "orange": 1, "banana": 1}`
            *   `orange`: `fruit_counts["orange"]` becomes 2. `fruit_counts = {"apple": 2, "orange": 2, "banana": 1}`
            *   `apple`: `fruit_counts["apple"]` becomes 3. `fruit_counts = {"apple": 3, "orange": 2, "banana": 1}`
        *   Result: `{"apple": 3, "orange": 2, "banana": 1}`.
    *   **When to use Dictionaries vs. Lists**:
        *   Lists: Use when the order of items is important, and you primarily access items by their numerical position (index). Good for sequences of things.
        *   Dictionaries: Use when you need to store and retrieve items based on a unique identifier (key) and the order of items is not the primary concern. Excellent for fast lookups, associations, and counting.
7.  **Graphs & Matrices**
    *   **Introduction to Graphs (Recap/Introduction)**:
        *   Definition: A graph G=(V,E) is a structure made of a set of *vertices* (V) (also called nodes or points) and a set of *edges* (E) (also called links or arcs) that connect pairs of vertices.
        *   Purpose: Graphs are used to model relationships and connections between objects or entities.
        *   Real-world Examples:
            *   Social networks: People are vertices, friendships/connections are edges.
            *   Road maps: Cities are vertices, roads between them are edges.
            *   The internet: Web pages are vertices, hyperlinks are directed edges.
            *   Task dependencies in a project: Tasks are vertices, an edge from task A to task B means A must be completed before B.
    *   **Types of Graphs (Brief Review/Introduction)**:
        *   Undirected Graph: Edges have no direction (e.g., a friendship between A and B is the same as B and A).
        *   Directed Graph (Digraph): Edges have a direction (e.g., a one-way street, a hyperlink from page A to page B).
        *   Weighted Graph: Each edge has an associated numerical value called a weight (e.g., distance between cities, cost of a flight).
        *   Unweighted Graph: Edges do not have weights (or all weights are implicitly 1).
    *   **Representing Relationships with Graphs**:
        *   Think about a scenario: "Friendship network". Vertices = people. Edge exists if two people are friends.
        *   Scenario: "Course prerequisites". Vertices = courses. Directed edge from Course A to Course B if A is a prerequisite for B.
    *   **Matrix Representations of Graphs**:
        *   **Adjacency Matrix**:
            *   Definition: A square matrix A of size V x V (where V is the number of vertices). The rows and columns are typically labeled by the vertices.
            *   For an unweighted graph: `A[i][j] = 1` if there is an edge connecting vertex `i` to vertex `j`. `A[i][j] = 0` if there is no direct edge.
            *   For a directed graph, `A[i][j] = 1` means an edge from `i` to `j`.
            *   For an undirected graph, the matrix is symmetric (i.e., `A[i][j] = A[j][i]`).
            *   If loops (edges from a vertex to itself) are allowed, `A[i][i]` can be 1.
            *   Example: Graph: Vertices {1,2,3}. Edges: (1,2), (2,3), (1,3) (undirected)
                Adjacency Matrix:
                ```
                  1 2 3
                1[0 1 1]
                2[1 0 1]
                3[1 1 0]
                ```
    *   **Adjacency List Representation of Graphs**:
        *   Definition: An array (or list) of lists. For each vertex `v`, `AdjacencyList[v]` stores a list of all vertices that are adjacent to `v` (i.e., directly connected by an edge).
        *   For weighted graphs, the list can store pairs: (adjacent_vertex, weight_of_edge).
        *   Example (same graph as above): Vertices {1,2,3}. Edges: (1,2), (2,3), (1,3)
            Adjacency List:
            `1: [2, 3]`
            `2: [1, 3]`
            `3: [1, 2]`
    *   **Adjacency Matrix vs. Adjacency List**:
        *   **Space Usage**:
            *   Matrix: Requires V<sup>2</sup> space. If the graph has many vertices but few edges (sparse graph), most of the matrix will be zeros, wasting space.
            *   List: Requires space proportional to V + E (number of vertices + number of edges). More space-efficient for sparse graphs.
        *   **Time for Common Operations**:
            *   Check if an edge exists between vertex `u` and `v`:
                *   Matrix: O(1) - just look up `Matrix[u][v]`.
                *   List: O(degree(u)) in the worst case - need to scan the list for `u`.
            *   Find all neighbors of a vertex `u`:
                *   Matrix: O(V) - need to scan the entire row for `u`.
                *   List: O(degree(u)) - just iterate through the list for `u`.
            *   Adding an edge: Matrix O(1). List O(1) (add to end of list).
            *   Removing an edge: Matrix O(1). List O(degree(u)) or O(degree(v)).
        *   **Preference**:
            *   Adjacency Matrix: Better for dense graphs (many edges, E approaching V<sup>2</sup>) or when you need to frequently and quickly check for specific edges.
            *   Adjacency List: Better for sparse graphs (few edges, E closer to V), which are common in many real-world scenarios. Most graph algorithms run more efficiently with adjacency lists on sparse graphs.
    *   **Simple Graph Algorithms (Conceptual Walkthroughs)**:
        *   **Finding the Degree of a Vertex (Undirected Graph)**:
            *   Using Adjacency Matrix: Sum all the 1s in the row (or column) corresponding to that vertex.
            *   Using Adjacency List: Count the number of elements in the list for that vertex.
        *   **Checking if a Graph is Connected (Undirected Graph - Intuitive Idea)**:
            *   Concept: A graph is connected if there is a path between every pair of distinct vertices.
            *   Manual Check (Small Graphs): Start at any vertex. Can you "walk" along edges to reach every other vertex? If yes for all starting vertices, it's connected.
            *   This introduces the idea of graph traversal (like BFS or DFS, which are formal algorithms for this, possibly covered later or in BSMA1001). The core idea is systematically exploring the graph.
        *   **Counting Number of Edges**:
            *   Using Adjacency Matrix (Undirected): Sum all the 1s in the matrix and divide by 2 (since each edge is counted twice, e.g., A[i][j] and A[j][i]). For directed, just sum all 1s.
            *   Using Adjacency List (Undirected): Sum the lengths of all the adjacency lists and divide by 2. For directed, sum the lengths of all lists.
8.  **Adjacency Matrices (Deeper Dive / Applications)**
    *   **Review Adjacency Matrix**:
        *   Structure: V x V matrix, A[i][j] indicates connection from i to j.
        *   Symmetry for undirected graphs.
    *   **Storing Weighted Edges in Adjacency Matrix**:
        *   Modification: Instead of just 0 (no edge) or 1 (edge exists), the cell `A[i][j]` stores the actual weight `w_ij` of the edge from vertex `i` to vertex `j`.
        *   If no edge exists between `i` and `j`:
            *   Store 0: If edge weights are strictly positive. However, this can be ambiguous if an edge could legitimately have a weight of 0.
            *   Store a special value like ∞ (infinity) or a very large number: Often used in shortest path algorithms where you want to represent non-existent paths as having infinite cost initially.
            *   Store a sentinel value like -1 (if weights are non-negative).
        *   Example: A road network graph where vertices are cities and edge weights are distances.
            Graph: A --(10km)--> B, B --(5km)--> C, A --(20km)--> C
            Weighted Adjacency Matrix (using 0 for no direct path, assuming positive weights):
            ```
              A  B  C
            A[0 10 20]
            B[0  0  5]  // Assuming directed or A-B already listed
            C[0  0  0]
            ```
            If undirected and A-B means B-A:
            ```
              A  B  C
            A[0 10 20]
            B[10 0  5]
            C[20 5  0]
            ```
    *   **Exploring Edge-Labelled Graphs (Conceptually)**:
        *   Concept: Sometimes, edges have qualitative attributes (labels or types) in addition to or instead of numerical weights.
        *   Example: A transportation network where an edge between cities could be labeled "Train," "Bus," or "Flight," and each might have a different associated cost or time (weight).
        *   Representing with Adjacency Matrix (Challenges/Approaches):
            *   Standard adjacency matrix is designed for a single numerical value (0/1 or weight).
            *   Multiple Matrices: If there's a small, fixed set of labels, you could have a separate adjacency matrix for each label type (e.g., `Matrix_Train`, `Matrix_Bus`). `Matrix_Train[i][j] = 1` if a train link exists.
            *   Complex Cell Values: The cell `A[i][j]` could store a pointer or reference to a list or structure containing multiple pieces of information about the edge(s) between `i` and `j` (e.g., `[(label:"Train", weight:50), (label:"Bus", weight:30)]`). This makes the matrix cells more complex than simple numbers.
            *   Adjacency lists are often more naturally suited for storing rich information about edges, as the list elements can easily be complex objects or structures.
    *   **Memory Usage Trade-offs (Revisited with Examples)**:
        *   Adjacency Matrix: Always V<sup>2</sup> entries.
            *   Example 1 (Sparse): 5 vertices, 4 edges. Matrix uses 5*5 = 25 cells.
            *   Example 2 (Dense/Complete K<sub>5</sub>): 5 vertices, 10 edges. Matrix uses 5*5 = 25 cells.
            *   Example 3 (Larger Sparse): 100 vertices, 200 edges. Matrix uses 100*100 = 10,000 cells.
        *   Adjacency List: V lists, total number of elements in all lists is 2E for undirected, E for directed.
            *   Example 1 (Sparse): 5 lists. Total elements ~2*4 = 8. (Plus list overhead).
            *   Example 2 (Dense/Complete K<sub>5</sub>): 5 lists. Total elements ~2*10 = 20.
            *   Example 3 (Larger Sparse): 100 lists. Total elements ~2*200 = 400.
        *   Conclusion: For graphs with many vertices but relatively few edges (sparse), adjacency lists save significant memory compared to adjacency matrices.
    *   **Powers of Adjacency Matrix (A<sup>k</sup>) (for unweighted graphs)**:
        *   Let A be the adjacency matrix of an unweighted graph (0s and 1s).
        *   A<sup>2</sup> = A * A (matrix multiplication). The entry `(A^2)[i][j]` represents the number of distinct paths of length exactly 2 from vertex `i` to vertex `j`.
            *   Intuition: `(A^2)[i][j] = Σ (A[i][k] * A[k][j])` for all k. A term `A[i][k] * A[k][j]` is 1 if there's an edge from `i` to `k` AND an edge from `k` to `j` (i.e., a path i-k-j). Summing these counts paths through all possible intermediaries `k`.
        *   A<sup>k</sup>[i][j]: The entry `(A^k)[i][j]` represents the number of distinct paths of length exactly `k` from vertex `i` to vertex `j`.
        *   Example: For a simple graph, calculate A and A<sup>2</sup>.
            Graph: 1-2, 2-3
            A =
            ```
              1 2 3
            1[0 1 0]
            2[1 0 1]
            3[0 1 0]
            ```
            A<sup>2</sup> =
            ```
              1 2 3
            1[1 0 1]  // 1->2->1 (len 2), 1->2->3 (len 2)
            2[0 2 0]  // 2->1->2 (len 2), 2->3->2 (len 2)
            3[1 0 1]  // 3->2->1 (len 2), 3->2->3 (len 2)
            ```
            Interpretation: (A<sup>2</sup>)[1][3] = 1 means there is 1 path of length 2 from vertex 1 to 3 (which is 1-2-3). (A<sup>2</sup>)[1][1] = 1 means 1 path of length 2 from 1 to 1 (1-2-1).
    *   **Reachability/Transitive Closure (Conceptual Introduction)**:
        *   Question: Can vertex `i` reach vertex `j` through any path of any length?
        *   Transitive Closure Matrix (R): `R[i][j] = 1` if `j` is reachable from `i`, and `0` otherwise.
        *   One way to think about it: If there's a path from `i` to `j`, it must have length 1, or 2, or ..., or V-1 (for simple paths without cycles in a graph with V vertices).
        *   So, reachability can be related to checking `A[i][j] > 0` OR `(A^2)[i][j] > 0` ... OR `(A^(V-1))[i][j] > 0`.
        *   More formally, let B = I + A + A<sup>2</sup> + ... + A<sup>V-1</sup> (where I is the identity matrix). Then `R[i][j] = 1` if `B[i][j] > 0`.
        *   Other algorithms like Floyd-Warshall or running BFS/DFS from each vertex can also determine reachability and compute the transitive closure. This is just an introduction to the concept via matrix powers.
9.  **Backtracking & Trees**
    *   **Introduction to Trees (Data Structure)**:
        *   Definition: A tree is a hierarchical data structure consisting of *nodes* connected by *edges*. Unlike general graphs, trees are characterized by:
            *   A designated *root* node (unless the tree is empty).
            *   Every node (except the root) has exactly one *parent* node.
            *   There are no cycles in a tree.
            *   There is a unique path from the root to any other node.
        *   Terminology:
            *   Root: The topmost node of the tree, which has no parent.
            *   Parent: A node that is connected to other nodes below it (its children).
            *   Child: A node that is connected to a node above it (its parent).
            *   Siblings: Nodes that share the same parent.
            *   Leaf Node (External Node): A node that has no children.
            *   Internal Node (Non-Leaf Node): A node that has at least one child.
            *   Subtree: A tree formed by a node and all its descendants.
            *   Depth of a node: The number of edges on the path from the root to that node. The depth of the root is 0.
            *   Height of a tree: The number of edges on the longest path from the root to a leaf node. The height of an empty tree is often defined as -1, and a tree with a single node has height 0.
        *   Binary Trees: A specific type of tree where each node has at most two children, referred to as the *left child* and the *right child*.
        *   Examples:
            *   Family trees (ancestors and descendants).
            *   Organizational charts (hierarchy of employees).
            *   File system directory structures (folders containing files and subfolders).
            *   Decision trees (used in Week 12).
    *   **Recursion (Conceptual Introduction/Revisit)**:
        *   Definition: A problem-solving technique where a procedure or function calls itself, directly or indirectly, to solve smaller, self-similar subproblems.
        *   Key Components:
            *   Base Case(s): One or more simple cases of the problem that can be solved directly without further recursion. This is crucial to prevent infinite recursion.
            *   Recursive Step: The part of the procedure where it calls itself with modified input, moving closer to a base case. The problem is broken down into smaller versions of itself.
        *   Analogy: Russian nesting dolls (each doll contains a smaller version of itself). A function to calculate factorial: `factorial(n) = n * factorial(n-1)`, with base case `factorial(0) = 1`.
        *   How it relates to trees: Many tree operations are naturally defined and implemented recursively because of the tree's hierarchical structure. For example, to process a tree, you might process the root, then recursively process its left subtree and its right subtree.
    *   **Tree Traversal (Conceptual, relating to DFS)**:
        *   Definition: The process of systematically visiting (e.g., reading or processing the data in) each node in a tree exactly once.
        *   Depth-First Search (DFS) Idea on Trees: Explores as far down as possible along each branch before backtracking. For trees, this is implemented by various traversal orders:
            *   **Pre-order Traversal (Root-Left-Right)**:
                1.  Visit/Process the current node (Root).
                2.  Recursively traverse the left subtree.
                3.  Recursively traverse the right subtree.
                *   Use: Copying a tree, creating a prefix expression from an expression tree.
            *   **In-order Traversal (Left-Root-Right - primarily for Binary Trees)**:
                1.  Recursively traverse the left subtree.
                2.  Visit/Process the current node (Root).
                3.  Recursively traverse the right subtree.
                *   Use: For binary search trees, this traversal visits nodes in ascending order.
            *   **Post-order Traversal (Left-Right-Root)**:
                1.  Recursively traverse the left subtree.
                2.  Recursively traverse the right subtree.
                3.  Visit/Process the current node (Root).
                *   Use: Deleting nodes in a tree (process children before parent), calculating the size of subtrees.
        *   Manual Trace Example: Consider a binary tree:
            ```
                  A
                 / \
                B   C
               / \
              D   E
            ```
            *   Pre-order: A, B, D, E, C
            *   In-order: D, B, E, A, C
            *   Post-order: D, E, B, C, A
    *   **Backtracking**:
        *   Concept: A systematic algorithmic technique, often implemented using recursion, for solving problems by trying to build a solution incrementally, one piece at a time. If an incremental choice leads to a dead end or violates problem constraints, the algorithm "backtracks" by undoing the previous choice and trying an alternative.
        *   Analogy: Finding your way through a maze. You explore one path. If you hit a dead end, you retrace your steps (backtrack) to the last junction where you had a choice of paths, and then try a different path.
        *   Core Idea:
            1.  Choose: Make a choice at the current decision point.
            2.  Explore: Recursively try to solve the problem with the choice made.
            3.  If solution found, return success.
            4.  If no solution found from current choice (dead end), Undo the choice (backtrack) and try another alternative.
    *   **Solving Puzzles via Backtracking (Manual Walkthroughs)**:
        *   **N-Queens Problem (Conceptual for 4-Queens)**:
            *   Problem: Place N chess queens on an N×N chessboard such that no two queens can attack each other (i.e., no two queens on the same row, column, or diagonal).
            *   Backtracking Application:
                1.  Start by trying to place a queen in the first column of the first row.
                2.  Move to the next row, try to place a queen in the first "safe" column (not attacked by previously placed queens).
                3.  If a safe column is found, place the queen and move to the next row.
                4.  If no safe column is found in the current row, backtrack to the previous row, remove the queen placed there, and try placing it in the next safe column in that previous row.
                5.  Repeat until all N queens are placed or all possibilities are exhausted.
            *   Illustrative Steps for 4-Queens:
                *   Row 1: Place Queen at (1,1).
                *   Row 2: Try (2,1) - conflict. Try (2,2) - conflict. Try (2,3) - OK. Place Queen at (2,3).
                *   Row 3: Try (3,1) - conflict. Try (3,2) - OK. Place Queen at (3,2).
                *   Row 4: Try (4,1)-conflict, (4,2)-conflict, (4,3)-conflict, (4,4)-conflict. No place. Backtrack!
                *   Row 3: Remove Queen from (3,2). Try next safe: (3,4) - conflict. No more options. Backtrack!
                *   Row 2: Remove Queen from (2,3). Try next safe: (2,4) - OK. Place Queen at (2,4).
                *   Row 3: Try (3,1) - OK. Place Queen at (3,1).
                *   Row 4: Try (4,2) - conflict. Try (4,3) - OK. Place Queen at (4,3). Solution found: [(1,1), (2,4), (3,1), (4,3)] (one possible solution).
        *   **Sudoku Solving (Conceptual)**:
            *   Problem: Fill a 9x9 grid so that each column, each row, and each of the nine 3x3 subgrids contain all digits from 1 to 9.
            *   Backtracking Application:
                1.  Find an empty cell.
                2.  Try filling it with a digit from 1 to 9.
                3.  Check if this digit is valid (doesn't violate Sudoku rules for that row, column, and 3x3 subgrid).
                4.  If valid, move to the next empty cell and repeat recursively.
                5.  If the digit is not valid, or if a later recursive call returns "no solution", then backtrack: erase the digit and try the next possible digit for the current cell.
                6.  If all digits 1-9 have been tried for a cell and none lead to a solution, return "no solution" to the previous call.
        *   **Pathfinding in a Maze**:
            *   Problem: Find a path from a start point to an end point in a maze.
            *   Backtracking Application:
                1.  Start at the entry point. Mark current cell as visited.
                2.  IF current cell is the exit, THEN solution found.
                3.  ELSE, for each unvisited neighboring cell:
                    a.  Move to that neighbor.
                    b.  Recursively try to find a path from this new cell.
                    c.  IF a path is found from the neighbor, THEN solution found.
                    d.  ELSE (path not found from neighbor), "unmark" the neighbor (backtrack - this path was a dead end) and try another neighbor from the original cell.
        *   General Pseudocode Structure for Backtracking:
            ```pseudocode
            FUNCTION CanSolve(problem_state)
                IF problem_state is a final success_state THEN
                    RETURN TRUE
                ENDIF

                FOR EACH possible_next_step FROM problem_state
                    IF is_valid_step(possible_next_step) THEN
                        apply_step_to_reach(new_state)
                        IF CanSolve(new_state) THEN  // Recursive call
                            RETURN TRUE
                        ENDIF
                        undo_step_to_revert_to(problem_state) // Backtrack
                    ENDIF
                ENDFOR
                RETURN FALSE // No move from this state leads to a solution
            ENDFUNCTION
            ```
10. **Object-Oriented Concepts (Conceptual Introduction)**
    *   **Limitations of Procedural Approach for Complex Systems**:
        *   In purely procedural programming (sequences of instructions, procedures/functions), as programs grow larger and more complex, managing shared data across many functions can become difficult.
        *   It can be harder to model real-world entities that have both properties (data) and actions (behavior) in a cohesive way. Data and the functions that operate on that data might be loosely connected.
    *   **Core Idea of Object-Oriented Thinking**:
        *   Instead of focusing primarily on procedures, object-oriented thinking focuses on "objects" as the primary building blocks.
        *   An object is a self-contained unit that bundles together:
            *   Data (called attributes or properties) that describe its state.
            *   Behavior (called methods or functions) that define what it can do or what can be done to it. These methods typically operate on the object's own data.
        *   Analogy:
            *   Real-world "car" object: Attributes: color, make, model, current speed, fuel level. Behaviors: startEngine(), stopEngine(), accelerate(), brake().
            *   Real-world "dog" object: Attributes: breed, age, name. Behaviors: bark(), eat(), sleep().
    *   **Classes**:
        *   Concept: A blueprint, template, or a user-defined data type for creating objects. It defines the common structure (what attributes its objects will have) and behavior (what methods its objects can perform).
        *   Analogy: A cookie cutter is a class; it defines the shape of cookies. The actual cookies made from it are objects. A building blueprint is a class; the buildings constructed from it are objects.
    *   **Objects (Instances of a Class)**:
        *   Concept: A specific, concrete realization (or instance) of a class. When an object is created from a class, it gets its own set of attribute values (its state). It shares the method definitions with other objects of the same class.
        *   Example: If `Dog` is a class, then `myDogFido` (an object) might have `name="Fido"`, `breed="Labrador"`, and `myOtherDogBuddy` (another object) might have `name="Buddy"`, `breed="Poodle"`. Both can `bark()`.
    *   **Attributes (Properties/Fields/Instance Variables)**:
        *   These are the data elements that belong to an object. They define the state or characteristics of an object.
        *   Example: For a `Student` class, attributes could be `studentID`, `name`, `major`, `gpa`. Each `Student` object would have its own values for these attributes.
    *   **Methods (Behaviors/Functions/Instance Methods)**:
        *   These are the functions or procedures that are defined within a class and operate on the data (attributes) of objects of that class. They define what an object can do.
        *   Example: For a `Student` class, methods could be `enrollInCourse(course_name)`, `calculateGPA()`, `getStudentName()`.
    *   **Constructors**:
        *   Concept: A special type of method within a class that is automatically called when a new object of that class is created (instantiated).
        *   Purpose: Its primary role is to initialize the attributes of the newly created object, ensuring it starts in a valid state.
        *   Example: When creating a `Student` object like `newStudent = CREATE_OBJECT Student("Alice", "S1001")`, the `Student` constructor would take "Alice" and "S1001" and assign them to the new object's `name` and `studentID` attributes.
    *   **Encapsulation**:
        *   Concept: One of the fundamental principles of OOP. It means bundling the data (attributes) and the methods that operate on that data together within a single unit (the object/class).
        *   Information Hiding: A key part of encapsulation. It involves restricting direct access to some of an object's internal data (attributes) from outside the object. Instead, access (to read or modify) is often provided through specific methods (getters and setters, or other public methods).
        *   Benefits:
            *   Protects an object's internal state from accidental or incorrect modification from outside.
            *   Makes code more modular: The internal implementation of an object can be changed without affecting other parts of the program, as long as the public interface (methods) remains the same.
            *   Hides complexity: Users of an object only need to know what it does (its methods), not necessarily how it does it.
        *   Analogy: A car driver uses the steering wheel, accelerator, and brakes (public methods/interface) to control the car. They don't need to directly manipulate the engine's internal components (hidden data/implementation).
    *   **Other OO Concepts (Brief Mention - No Deep Dive for CT focus)**:
        *   Inheritance: A mechanism where a new class (subclass or derived class) can acquire (inherit) the properties (attributes and methods) of an existing class (superclass or base class). This promotes code reuse and creates an "is-a" relationship (e.g., an `ElectricCar` is a type of `Car`).
        *   Polymorphism ("Many Forms"): The ability of objects of different classes to respond to the same method call in ways specific to their class. (e.g., if `Circle` and `Square` classes both have a `draw()` method, calling `draw()` on a `Circle` object behaves differently than on a `Square` object).
    *   Focus for CT: Understanding how these concepts help in organizing complex problems by modeling real-world or conceptual entities as self-contained objects with their own data and behaviors, making the system easier to design, understand, and maintain.
11. **Concurrency (Conceptual Introduction)**
    *   **Sequential vs. Concurrent Execution**:
        *   Sequential Execution: Instructions or tasks are performed one after another, in a single sequence. Only one task is active at any given moment.
        *   Concurrent Execution: Multiple tasks appear to be progressing or executing at the same time.
            *   On a single CPU/core system, this is achieved by *interleaving* the execution of tasks (the CPU rapidly switches between tasks). This is often called multitasking or logical concurrency.
            *   On a multi-CPU/core system, tasks can run in *true parallelism*, with different tasks executing simultaneously on different cores.
        *   Analogy:
            *   Sequential: A person reading one book from start to finish before starting another.
            *   Concurrent (interleaved): A chef preparing a meal by switching between chopping vegetables, stirring a pot, and checking the oven.
            *   Parallel: Multiple chefs each working on a different dish simultaneously in a large kitchen.
    *   **Why Concurrency?**:
        *   Responsiveness: In applications with user interfaces, concurrency allows the program to remain responsive to user input (e.g., mouse clicks) while performing a long-running task in the background (e.g., downloading a file, complex calculation).
        *   Performance/Speedup: By dividing a large task into sub-tasks that can run in parallel on multi-core processors, the overall time to complete the task can be reduced.
        *   Resource Utilization: Allows a CPU to do other work while one task is waiting for a slow operation (like reading from a disk or network).
        *   Modeling Real-World Systems: Many real-world systems are inherently concurrent (e.g., multiple users accessing a website, multiple ATMs connected to a bank).
    *   **Processes vs. Threads (Simplified for CT)**:
        *   Process: An instance of a computer program that is being executed. Each process typically has its own independent memory space, meaning data is not directly shared between processes. (Think of separate applications running on your computer, like a web browser and a word processor).
        *   Thread: A lightweight unit of execution *within* a process. Multiple threads can exist within a single process and they share the same memory space (meaning they can access and modify the same data). This makes communication between threads easier but also introduces risks.
    *   **Remote Procedure Calls (RPC)**:
        *   Concept: A mechanism that allows a procedure (function or method) in one program (or process) to be executed by another program (or process), which may be located on a different computer connected via a network.
        *   How it works (simplified): The calling program (client) makes a request that looks like a normal local procedure call. The RPC system handles the underlying network communication to send the request and parameters to the remote program (server), execute the procedure there, and return the results to the client.
        *   Analogy: Ordering food via a food delivery app. You (client) make a request (call a "place order" procedure). The app (RPC system) sends it to the restaurant (server). The restaurant processes it. The app brings you the result (food). You don't directly interact with the restaurant's kitchen.
    *   **Challenges in Concurrency**: When multiple tasks/threads access shared resources or data, problems can arise.
        *   **Race Conditions**:
            *   Definition: A situation where the outcome of a computation depends on the unpredictable timing or interleaving of operations from multiple threads or processes accessing shared data. The "race" is about which thread gets to access/modify the data first.
            *   Example: Two threads (T1, T2) want to increment a shared counter `C` (initially 0).
                1. T1 reads `C` (gets 0).
                2. T2 reads `C` (gets 0).
                3. T1 calculates `C+1` (is 1).
                4. T2 calculates `C+1` (is 1).
                5. T1 writes 1 to `C`. (`C` is now 1).
                6. T2 writes 1 to `C`. (`C` is still 1).
                The correct result should be 2, but due to interleaving, it's 1.
            *   This illustrates how shared data can become inconsistent.
        *   **Synchronization Primitives (to manage shared access)**:
            *   **Locks (Mutexes - MUTual EXclusion)**:
                *   Concept: A synchronization mechanism that ensures only one thread can access a specific shared resource or execute a particular section of code (called a "critical section") at any given time.
                *   Operation: A thread must "acquire" or "obtain" the lock before entering the critical section. If the lock is already held by another thread, the current thread must wait until the lock is "released." Once done, the thread releases the lock, allowing another waiting thread to acquire it.
                *   Analogy: A single key for a bathroom. Only the person with the key can enter. Others must wait for the key to be returned.
        *   **Deadlocks**:
            *   Definition: A situation where two or more concurrent tasks are blocked indefinitely, each waiting for a resource that is held by another task in the same group, resulting in a standstill.
            *   Classic Example (Conceptual - Dining Philosophers): Imagine five philosophers sitting around a circular table. There's one chopstick between each pair of philosophers (5 chopsticks in total). Each philosopher needs two chopsticks (one from their left, one from their right) to eat.
                If every philosopher simultaneously picks up the chopstick on their left, then each philosopher will be holding one chopstick and waiting for the chopstick on their right, which is held by their neighbor. No one can eat, and no one will release their chopstick – a deadlock.
            *   Conditions often leading to deadlock (Coffman conditions - brief mention, not for memorization but for understanding the problem):
                1.  Mutual Exclusion: Resources cannot be shared.
                2.  Hold and Wait: A task holds at least one resource and is waiting for another.
                3.  No Preemption: Resources cannot be forcibly taken away.
                4.  Circular Wait: A circular chain of tasks exists, where each task waits for a resource held by the next task in the chain.
    *   Focus for CT: Appreciating that when tasks run "at the same time" and share things, new kinds of problems (like race conditions and deadlocks) can occur, and we need mechanisms (like locks) to coordinate them.
12. **Problem Solving Strategies**
    *   **Recap: What is an Algorithm?**
        *   A clear, unambiguous, step-by-step sequence of instructions to solve a specific problem or achieve a defined outcome.
        *   It should be correct, efficient (enough), and finite (terminate).
    *   **General Problem-Solving Heuristics (Polya's Steps as a framework)**:
        *   1. **Understand the Problem**:
            *   Read or listen to the problem statement carefully. What is being asked?
            *   Identify the inputs (givens), the outputs (what is required), and any constraints or conditions.
            *   Can you restate the problem in your own words? Can you draw a diagram or make a small example?
        *   2. **Devise a Plan (Strategy)**:
            *   Consider similar problems you've solved before. Can you adapt those solutions?
            *   Break the problem down into smaller, more manageable subproblems (Decomposition).
            *   Simplify the problem if it's too complex. Solve the simpler version first.
            *   Work backwards from the desired output.
            *   Look for patterns (Pattern Recognition).
            *   Use logical reasoning. Consider edge cases and typical cases.
        *   3. **Carry out the Plan (Implementation)**:
            *   Translate your plan into a sequence of steps (e.g., pseudocode, flowchart, or actual code).
            *   Check each step as you go.
        *   4. **Look Back (Review and Reflect)**:
            *   Test your solution with various inputs (including edge cases) to verify its correctness.
            *   Does it produce the correct output for all valid inputs? Does it handle invalid inputs gracefully?
            *   Can the solution be improved (e.g., made simpler, more efficient)?
            *   Did you learn anything new from solving this problem?
    *   **Decomposition (Breaking Problems Down)**:
        *   The strategy of dividing a large, complex problem into smaller, more manageable, and often independent subproblems.
        *   Each subproblem can then be solved individually.
        *   The solutions to the subproblems are then combined to form the solution to the original complex problem.
        *   Example: To write a book (complex problem), you might decompose it into: Outline chapters -> Write content for Chapter 1 -> Write content for Chapter 2 -> ... -> Edit manuscript -> Design cover.
        *   This is a core part of top-down design and leads to modularity in algorithms (e.g., using procedures/functions for each subproblem).
    *   **Problem-Solving Approaches**:
        *   **Top-Down Design (Stepwise Refinement)**:
            *   Start with a high-level, abstract statement of the problem or the main task.
            *   Systematically break it down into smaller, more detailed sub-tasks.
            *   Continue this process of refinement for each sub-task until the steps are simple and concrete enough to be directly translated into algorithmic instructions (or code).
            *   Focuses on the overall structure and flow first.
        *   **Bottom-Up Design**:
            *   Start by identifying and implementing the most basic or fundamental operations and components that will be needed.
            *   Once these low-level building blocks are created and tested, they are combined to form larger, more complex modules or procedures.
            *   This process continues, building up layer by layer, until the complete solution is assembled.
            *   Focuses on building and testing individual components first.
        *   In practice, problem-solving often involves a mix of both top-down and bottom-up thinking.
    *   **Abstraction**:
        *   The process of focusing on the essential features of a problem or system while ignoring unnecessary or distracting details.
        *   Procedural Abstraction: When you use a procedure (or function), you focus on *what* it does (its purpose, inputs, and outputs) rather than *how* it does it (its internal implementation details). This allows you to use complex operations as simple building blocks.
        *   Data Abstraction: Focusing on the properties and behaviors of a data type or data structure (like a List or Dictionary) rather than the specifics of how it's stored in memory.
    *   **Pattern Recognition**:
        *   The ability to identify similarities, regularities, or recurring patterns within a problem itself, or between the current problem and problems solved previously.
        *   Recognizing a pattern can help you apply a known solution strategy or adapt an existing algorithm.
        *   Example: Realizing that multiple parts of a problem involve "finding an item in a collection" might suggest reusing a search procedure.
    *   **Decision Trees (for Problem Solving and Classification - Simple Introduction)**:
        *   Concept: A tree-like graphical model where each internal node represents a "decision" or a "test" on an attribute (e.g., "Is it raining?"), each branch leading from a node represents an outcome or answer to that test (e.g., "Yes" or "No"), and each leaf node represents a final outcome, decision, or class label.
        *   Use in Problem Solving: Helps to structure a sequence of decisions to reach a conclusion. Useful for systematically exploring possibilities.
        *   Example: A simple diagnostic tree for a malfunctioning lamp.
            *   Root: "Is the lamp plugged in?"
                *   No -> Leaf: "Plug in the lamp."
                *   Yes -> Internal Node: "Is the bulb burned out?"
                    *   Yes -> Leaf: "Replace the bulb."
                    *   No -> Leaf: "Lamp might be broken or other issue."
        *   Basic Classification: Decision trees can be used to assign an item to one of several predefined categories based on its features.
            *   Example: Classifying an email as "Spam" or "Not Spam" based on features like "contains word 'free'?", "sender known?".
            *   Brief mention: In machine learning, decision trees can be automatically "learned" from data to make predictions. Here, the focus is on them as a way to structure human problem-solving logic.
    *   **Developing and Testing Algorithms**:
        *   Importance of Testing: Crucial to ensure the algorithm is correct and reliable.
        *   Test Cases: Use a variety of inputs:
            *   Normal/Typical Cases: Expected inputs.
            *   Edge Cases: Inputs at the boundaries of valid ranges (e.g., smallest/largest allowed numbers, empty lists).
            *   Invalid Inputs: Data that the algorithm shouldn't accept (to check error handling, though error handling itself might be an advanced topic).
        *   Debugging: The process of finding and fixing errors (bugs) in an algorithm or its implementation.
            *   Techniques: Manual tracing (desk checking), simplifying the problem to isolate the error, adding display statements to see intermediate values.

## Glossary
- **Pseudocode**: a simplified, language-agnostic way to describe algorithms.
- **Recursion**: a technique where a function calls itself to solve subproblems.
- **Encapsulation**: bundling data with methods that operate on that data.
- **Race Condition**: a flaw that occurs when operations depend on timing of events in concurrent systems.


## Additional Topics
- **Heuristics** – strategies for approaching complex problems when an exact solution is impractical
- **Greedy Algorithms** – making the locally optimal choice at each step
- **Complexity Analysis** – big O notation to understand algorithm efficiency

## Further Reading
- *Introduction to Algorithms* by Cormen et al.
