## ATTENDANCE RISK PREDICTOR
# OVERVIEW:
The Attendance Risk Predictor is a Python-based utility designed to help students
and academic advisors monitor attendance trends over a 60-class semester. By
calculating current percentages and projected outcomes, the program identifies
whether a student is at risk of falling below the mandatory 75% attendance
threshold.
# WHY THIS PROJECT:
In many academic institutions, a minimum of 75% attendance is a prerequisite for
appearing in final examinations. Students often lose track of their attendance count
amidst busy schedules. This project was developed to:
 Provide an early warning system for "at-risk" students.
 Eliminate the "math anxiety" of calculating how many classes one can afford
to miss.
 Encourage responsible digital citizenship by using data to manage academic
obligations.
#FEATURES:
 Real-time Percentage Calculation: Instant feedback on current standing.
 Predictive Analysis: Determines if reaching the 75% goal is mathematically
possible based on remaining classes.
 Dynamic Advice: Provides specific instructions (e.g., "You must attend 12 out
of the next 15 classes").
 Buffer Tracking: For safe students, it calculates exactly how many more
classes can be missed without falling below the threshold.
# HOW THE PROGRAM WORKS:
The program operates on a Deterministic Logic Model:
1. Input Phase: The user enters total classes held and classes attended.
2. Processing Phase: It calculates the current percentage and identifies the
"Target Number" (45 out of 60 classes).
3. Simulation Phase: It subtracts the current attended count from the target to
see if the remaining classes are sufficient to bridge the gap.
4. Output Phase: Categorizes the student as SAFE, AT RISK, or IMPOSSIBLE.
# TECHNOLOGIES / TOOLS USED:
 Language: Python 3.x
 Environment: VS Code (Visual Studio Code)
 Logic: Conditional Branching and Arithmetic Operators.
# STEPS TO INSTALL AND RUN THE PROGRAM:
1. Install Python: Ensure Python 3 is installed on your system (download from
python.org).
2. Setup VS Code: Install the Python Extension in VS Code.
3. Create File: Create a new file named attendance_predictor.py.
4. Copy Code: Paste the provided Python script into the file.
5. Run: Open the terminal in VS Code and type: python attendance_predictor.py
6. Interact: Follow the on-screen prompts to enter your data.
# LIMITATIONS:
 Manual Entry: The program currently relies on user input rather than syncing
automatically with university databases.
 Weightage: It treats all classes as equal and does not account for "Medical
Leaves" or "Duty Leaves" unless manually adjusted in the attendance count.
 Static Threshold: The 75% limit is hardcoded and would need manual code
adjustment for different institutional rules.
# FUTURE IMPROVEMENTS:
 GUI Development: Creating a graphical interface using Tkinter or PyQt.
 Data Persistence: Adding a CSV or SQL database to save student records
over time.
 Visualization: Using Matplotlib to generate pie charts showing "Attended" vs
"Missed" vs "Remaining" classes.
 AI Integration: Implementing Machine Learning to predict risk based on
external factors like travel distance or past midterm scores.
# CONCLUSION:
The Attendance Risk Predictor serves as a bridge between simple data entry and
meaningful academic management. It empowers students to take control of their
attendance through transparency and mathematical foresight, ensuring that they
remain eligible for their evaluations without last-minute surprises.
