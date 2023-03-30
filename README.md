## *Loan Qualifier App* 
**A loan qualilfication tool that's built to run from a CLI (Command Line Interface) and designed to collect information such as the uploading of a banker rate sheet and the prompting of financial information.   With the help of helper functions, the app performs calculations and then generates a list of qualifying loans that the user has an option to export to .csv file that can be displayed and shared on a spreadsheet.**

---
## Technologies
This project leverages python 3.7 with the following libraries:
* Fire - Create a CLI for a Python program and ease tranistioning between the command line and Python.  
* Questionary - Interactive command line prompts
* Sys - For exiting the program.
* pathlib - For setting a path for a .csv file.
* csv - For writing rows of data to a .csv file.

---
## Installation 
* Visual Studio Code or an IDE (Integrated Development Environment) program 
* pip install Fire 
* pip install Questionary 

---
## Usage

Process flow of how the 'Run' main function of the CLI app is executed.

![Run](https://user-images.githubusercontent.com/111409358/228761877-d8ffb366-a336-4ccc-973a-39e13d2e5409.png)


1. The 'load_bank_data' function - The latest bank data is loaded via a Questionary prompt.  The 'load_csv' function located in the fileio.py module, reads the CSV file from the path provided.

![Load_bank_data](https://user-images.githubusercontent.com/111409358/228761428-1f8b711b-1c3a-40a9-914b-bd335b70e53f.png)


2. The 'get_applicant_info' function - The applicant's financial information is entered through a series of Questionary prompts and arguments returned.  

![get_applicant_info](https://user-images.githubusercontent.com/111409358/228762284-7bc7c6c0-f06e-4b67-acc8-0b799f681303.png)


3. The 'find_qualifying_loans' function - The arguments are passed off to modules that perform the calculations and filters located in the qualifier and utils folder.  This function eturns a list of the banks willing to underwrite the loan.


![find_qualifying_loans 01](https://user-images.githubusercontent.com/111409358/228764076-3727ce58-8a82-4171-99bc-df4e7b506a51.png)

![find_qualifying_loans 02](https://user-images.githubusercontent.com/111409358/228764098-c6bf1482-8515-4536-b54a-47be9dc0daf1.png)


4. The 'save_qualifying_loans' function - If qualifying loans exist, a Questionary prompt to save the list of qualifying loans will appear and if opted to save, will pass arguments to the 'save_csv' function in the fileio.py module to be written to a CSV file.

![save_qualifying_loans](https://user-images.githubusercontent.com/111409358/228764215-a763cc7b-4f3f-4671-a84b-c117aa61a0e5.png)



Sample Output - From an IDE program or a command line such as Terminal(Mac) or Git Bash(Windows), enter into a dev environment and then run the primary aplication file, app.py.

![Sample Output](https://user-images.githubusercontent.com/111409358/228773177-13426bb6-3609-4719-a78f-c37f991512bd.png)

Sample CSV File of List of Qualifying Loans
![sample_qualifying_loans](https://user-images.githubusercontent.com/111409358/228773817-c3f4bbe8-abd8-41ec-bd55-9de90f3d6df3.png)

---
## Contributors
Alexander Valenzuela<br>
[LinkedIn Profile](<https://www.linkedin.com/in/alex-valenzuela-97826842/>)

---
## License
The Unlicense
