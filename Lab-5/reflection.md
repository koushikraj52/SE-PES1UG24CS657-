# Lab 5 — Reflection

**Student:** B Koushikraj  
**SRN:** PES1UG24CS657  
**Project:** Gym Membership System

## 1. What is static code analysis?

Static code analysis examines source code without executing the program to identify potential bugs, security vulnerabilities, and coding-style violations.

## 2. What did Pylint, Bandit, and Flake8 help identify?

Pylint helped identify code-quality and maintainability problems. Bandit identified potentially insecure coding practices, including unsafe expression evaluation, weak hashing, insecure random-number generation, shell execution, and a hard-coded secret. Flake8 identified style violations such as unused imports, long lines, and incorrect exception handling.

## 3. What changes were made?

The program was updated to use a safe numeric renewal calculation, SHA-256 hashing, a secure PIN generator, specific exception handling, context-managed file handling, and improved Python naming and formatting. Unused code and the hard-coded secret were removed.

## 4. What were the results?

The initial Pylint score was 4.81/10. After the changes, the score reached 10.00/10. The final Bandit scan reported no issues, and Flake8 reported no violations after the formatting fix.

## 5. What did you learn?

I learned that static analysis tools can identify code-quality, security, and style problems before deployment. Running the tools again after making changes helps verify that the reported issues have been addressed.

