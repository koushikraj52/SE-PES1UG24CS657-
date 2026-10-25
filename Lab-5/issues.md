# Lab 5 — Static Code Analysis Issues

**Student:** B Koushikraj  
**SRN:** PES1UG24CS657  
**Project:** Gym Membership System

## Issues Identified

| Issue | Description | Fix |
|---|---|---|
| Unused import | The math module is not used. | Remove the unused import. |
| Long lines | Some lines exceed the recommended length. | Split long lines. |
| Bare exception | The code catches every exception. | Catch the specific exception. |
| Mutable default argument | A list is used as a default function argument. | Use None and create a new list when needed. |
| Unsafe eval | eval() can execute Python code. | Replace it with safe arithmetic. |
| Unused variables | Some variables are assigned but not used. | Remove unnecessary variables. |
| None comparison | The code compares a value using == None. | Use is None. |
| File handling | The roster file is not handled using a context manager. | Use with open(). |
| Shell command | The code executes a shell command. | Replace it with a normal print statement. |
| Hard-coded secret | A secret is written directly in the source code. | Remove the hard-coded secret. |
| Missing final newline | The file does not end with a newline. | Add a final newline. |