# Operating System Services

## Questions

Question 1: Which of the following is NOT a service provided by an operating system?  
a) File management  
b) Process scheduling  
c) Network routing  
d) Memory management  
**Answer:** c) Network routing  

Question 2: In a scenario where a video player, web browser, and word processor are running simultaneously, which operating system service is primarily responsible for allocating CPU time to these applications?  
a) File management  
b) Process scheduling  
c) Memory management  
d) Device management  
**Answer:** b) Process scheduling  

Question 3: What is the main purpose of file management in an operating system?  
a) To allocate CPU time to processes  
b) To manage the physical memory of the computer  
c) To handle the creation, deletion, and organization of files and directories  
d) To control the input and output devices  
**Answer:** c) To handle the creation, deletion, and organization of files and directories  

Question 4: If a lower-priority process is experiencing starvation in a multitasking environment, what might be a potential solution?  
a) Increase the priority of the lower-priority process  
b) Decrease the priority of all other processes  
c) Terminate the lower-priority process  
d) Allocate more memory to the lower-priority process  
**Answer:** a) Increase the priority of the lower-priority process  

Question 5: Which of the following algorithms is commonly used for process scheduling in operating systems?  
a) First-Come, First-Served (FCFS)  
b) Last-In, First-Out (LIFO)  
c) Round Robin (RR)  
d) Both a and c  
**Answer:** d) Both a and c  

Question 6: If an operating system uses a round-robin scheduling algorithm with a time quantum of 10 milliseconds, and three processes arrive at the same time, how much CPU time will each process receive in one complete cycle?  
a) 10 milliseconds  
b) 20 milliseconds  
c) 30 milliseconds  
d) 10 milliseconds per process  
**Answer:** d) 10 milliseconds per process  

---

# User Interface

## Questions

Question 1: Which of the following is a characteristic of a Graphical User Interface (GUI)?  
a) Requires memorization of commands  
b) Utilizes windows, icons, and menus  
c) Operates solely through text input  
d) Is only available on mobile devices  
**Answer:** b) Utilizes windows, icons, and menus  

Question 2: In a Command-Line Interface (CLI), what does the command 'sudo apt-get install package-name' primarily do?  
a) Uninstalls a software package  
b) Updates the system  
c) Installs a software package  
d) Lists all installed packages  
**Answer:** c) Installs a software package  

Question 3: Which of the following statements about user interfaces is true?  
a) GUIs are always more efficient than CLIs  
b) CLIs require less system resources than GUIs  
c) GUIs do not allow for multitasking  
d) CLIs are only used in programming environments  
**Answer:** b) CLIs require less system resources than GUIs  

Question 4: What is a potential disadvantage of using a Command-Line Interface (CLI)?  
a) It is visually appealing  
b) It requires knowledge of specific commands  
c) It is slower than a GUI  
d) It cannot be used for automation  
**Answer:** b) It requires knowledge of specific commands  

Question 5: Which of the following best describes a scenario where a GUI would be preferred over a CLI?  
a) Writing a script for automated tasks  
b) Managing files and folders visually  
c) Installing software via command line  
d) Configuring server settings  
**Answer:** b) Managing files and folders visually  

---

# Program Execution

## Questions

Question 1: What is the first step the operating system takes when a user opens a word processing application?  
a) It saves the document.  
b) It locates the program file on the disk.  
c) It closes all other applications.  
d) It updates the software.  
**Answer:** b) It locates the program file on the disk.

Question 2: In the context of program execution, what happens when a user closes an application?  
a) The application continues to run in the background.  
b) The operating system saves any unsaved work and frees up memory.  
c) The operating system deletes the program file from the disk.  
d) The application automatically updates itself.  
**Answer:** b) The operating system saves any unsaved work and frees up memory.

Question 3: What issue may arise from a program that has a memory leak?  
a) The program will run faster over time.  
b) The operating system will automatically update the program.  
c) The program may slow down the system due to excessive memory usage.  
d) The program will consume less memory as it runs.  
**Answer:** c) The program may slow down the system due to excessive memory usage.

Question 4: If an operating system detects that a program is consuming too many resources, what action might it take?  
a) It will increase the program's priority.  
b) It may terminate the program abnormally.  
c) It will automatically save all data to the cloud.  
d) It will notify the user to upgrade their hardware.  
**Answer:** b) It may terminate the program abnormally.

Question 5: Consider the following code snippet that simulates opening a program. What will be the output if the program is successfully opened?  
```python
def open_program():
    return "Program is now running."

status = open_program()
print(status)
```
a) Program is now closed.  
b) Program is now running.  
c) Error: Program not found.  
d) Program is loading.  
**Answer:** b) Program is now running.

---

# I/O Operations

## Questions

Question 1: In a text editor application, what type of I/O operation occurs when a user opens a file?  
a) Output operation  
b) Input operation  
c) Both input and output operation  
d) None of the above  
**Answer:** b) Input operation  

Question 2: When a user saves changes in a text editor, which I/O operation is performed?  
a) Input operation  
b) Output operation  
c) Both input and output operation  
d) None of the above  
**Answer:** b) Output operation  

Question 3: In the context of a web server handling multiple client requests, what is a potential solution for managing concurrent I/O operations?  
a) Synchronous I/O  
b) Asynchronous I/O  
c) Blocking I/O  
d) None of the above  
**Answer:** b) Asynchronous I/O  

Question 4: If a web server receives requests for the same file from multiple clients, which of the following is a challenge it faces?  
a) Performing input operations  
b) Managing concurrent I/O operations  
c) Writing output to the disk  
d) None of the above  
**Answer:** b) Managing concurrent I/O operations  

Question 5: Which of the following best describes the role of a text editor when a user types and saves changes?  
a) It only performs input operations.  
b) It only performs output operations.  
c) It performs both input and output operations.  
d) It does not perform any I/O operations.  
**Answer:** c) It performs both input and output operations.  

Question 6: In a scenario where a web server uses threading to handle multiple requests, what is the primary benefit?  
a) Increased memory usage  
b) Simplified code structure  
c) Non-blocking I/O operations  
d) Reduced server response time  
**Answer:** c) Non-blocking I/O operations  

---

# System Calls

## Questions

Question 1: What is the purpose of the 'open' system call in Unix-like operating systems?  
a) To create a new process  
b) To request the operating system to open a file  
c) To terminate a running process  
d) To allocate memory for a program  
**Answer:** b) To request the operating system to open a file  

Question 2: When a program calls the 'fork' system call, what is created?  
a) A new thread  
b) A new process  
c) A new file descriptor  
d) A new memory segment  
**Answer:** b) A new process  

Question 3: After a successful 'fork' system call, how many processes are executing the same code?  
a) One  
b) Two  
c) Three  
d) None  
**Answer:** b) Two  

Question 4: Which of the following statements is true about the child process created by the 'fork' system call?  
a) It has the same process ID as the parent process  
b) It shares the same memory space as the parent process  
c) It is an exact copy of the parent process but with a different process ID  
d) It cannot access any resources used by the parent process  
**Answer:** c) It is an exact copy of the parent process but with a different process ID  

Question 5: In the context of system calls, what does a file descriptor represent?  
a) The name of the file  
b) The location of the file on disk  
c) An integer that uniquely identifies an open file within a process  
d) The permissions of the file  
**Answer:** c) An integer that uniquely identifies an open file within a process  

Question 6: If a program calls 'fork' and both the parent and child processes attempt to write to the same file, what could potentially happen?  
a) The file will be overwritten  
b) The writes will be serialized automatically  
c) Data corruption may occur if not handled properly  
d) The child process will be terminated  
**Answer:** c) Data corruption may occur if not handled properly  

Question 7: Which of the following is NOT a typical mode used with the 'open' system call?  
a) O_RDONLY  
b) O_WRONLY  
c) O_RDWR  
d) O_EXECUTE  
**Answer:** d) O_EXECUTE  

---

# Operating System Design Strategies

## Questions

Question 1: Which of the following is a characteristic of a monolithic operating system design?  
a) All system services run in separate address spaces  
b) High performance due to efficient communication between components  
c) Strict modularity of components  
d) Limited access to hardware resources  
**Answer:** b) High performance due to efficient communication between components  

Question 2: What is a potential drawback of a monolithic operating system design?  
a) Increased performance  
b) Simplicity in maintenance  
c) Complexity and difficulty in maintaining the system  
d) Enhanced security features  
**Answer:** c) Complexity and difficulty in maintaining the system  

Question 3: Which operating system is an example of a hybrid design?  
a) Linux  
b) Windows NT  
c) macOS  
d) FreeBSD  
**Answer:** b) Windows NT  

Question 4: In a microkernel architecture, which of the following services is typically included in the kernel?  
a) File management  
b) Process scheduling  
c) Device drivers  
d) All of the above  
**Answer:** b) Process scheduling  

Question 5: Which of the following statements about Windows NT is true?  
a) It is purely a monolithic operating system.  
b) It uses a microkernel architecture for all services.  
c) It incorporates both monolithic and microkernel elements.  
d) It does not support modular components.  
**Answer:** c) It incorporates both monolithic and microkernel elements.  

Question 6: If a monolithic operating system has a kernel size of 2 MB and the total memory available is 512 MB, what percentage of the memory is occupied by the kernel?  
a) 0.39%  
b) 0.25%  
c) 0.5%  
d) 1%  
**Answer:** a) 0.39%  

Question 7: Which of the following is NOT a benefit of a monolithic operating system design?  
a) High performance  
b) Easy to debug  
c) Efficient communication  
d) Direct access to hardware  
**Answer:** b) Easy to debug  

---

# File-system manipulation

## Questions

1. Question: What does the following Python code do?
   ```python
   import os
   os.makedirs('my_folder', exist_ok=True)
   with open('my_folder/my_file.txt', 'w') as f:
       f.write('Hello, World!')
   ```
   a) Creates a new file named 'my_file.txt' in the current directory  
   b) Creates a new directory named 'my_folder' and writes 'Hello, World!' to a file inside it  
   c) Deletes the directory 'my_folder'  
   d) Creates a symbolic link named 'my_file.txt'  
   **Answer:** b) Creates a new directory named 'my_folder' and writes 'Hello, World!' to a file inside it  

2. Question: What will happen if you run the following code after executing the previous code snippet?
   ```python
   os.rmdir('my_folder')
   ```
   a) It will delete 'my_file.txt' only  
   b) It will delete 'my_folder' and 'my_file.txt'  
   c) It will raise an error because 'my_folder' is not empty  
   d) It will create a new directory named 'my_folder'  
   **Answer:** c) It will raise an error because 'my_folder' is not empty  

3. Question: In the following code snippet, what will be the output when trying to list the contents of 'link_to_folder' after deleting 'original_folder'?
   ```python
   import os
   os.makedirs('original_folder', exist_ok=True)
   os.symlink('original_folder', 'link_to_folder')
   os.rmdir('original_folder')
   print(os.listdir('link_to_folder'))
   ```
   a) It will list the contents of 'original_folder'  
   b) It will raise a FileNotFoundError  
   c) It will print an empty list  
   d) It will raise a PermissionError  
   **Answer:** b) It will raise a FileNotFoundError  

4. Question: Which of the following statements about symbolic links is true?
   a) Deleting the original directory will also delete all symbolic links pointing to it  
   b) Symbolic links can point to files or directories  
   c) Symbolic links are the same as hard links  
   d) You cannot create symbolic links in Python  
   **Answer:** b) Symbolic links can point to files or directories  

5. Question: If you want to ensure that a directory is created only if it does not already exist, which parameter should you use with `os.makedirs()`?
   a) `force=True`  
   b) `exist_ok=True`  
   c) `create_if_not_exists=True`  
   d) `overwrite=False`  
   **Answer:** b) `exist_ok=True`  

---

# Communications

## Questions

1. Question: In a multi-threaded application, what is the primary advantage of using shared memory for communication between threads?  
   a) It allows for slower communication  
   b) It requires more complex synchronization mechanisms  
   c) It enables fast communication since both threads access the same memory space  
   d) It eliminates the need for any form of data consistency  
   Answer: c) It enables fast communication since both threads access the same memory space  

2. Question: In a distributed system, what is a potential issue when using message passing for communication?  
   a) Messages are always received in the order they are sent  
   b) The sender can always confirm that the message was received  
   c) A receiving computer may crash before processing a message, leading to potential data loss  
   d) All messages are guaranteed to be processed immediately  
   Answer: c) A receiving computer may crash before processing a message, leading to potential data loss  

3. Question: Which of the following mechanisms can be used to ensure reliable communication in a distributed system?  
   a) Shared memory  
   b) Acknowledgments and retries  
   c) Direct variable access  
   d) Thread pooling  
   Answer: b) Acknowledgments and retries  

4. Question: If Thread A writes the value 10 to a shared variable and Thread B reads from that variable immediately after, what value will Thread B read if no other operations occur in between?  
   a) 0  
   b) 5  
   c) 10  
   d) Undefined  
   Answer: c) 10  

5. Question: In a multi-threaded application, which of the following is a common method to prevent race conditions when accessing shared memory?  
   a) Using global variables  
   b) Implementing locks or mutexes  
   c) Allowing threads to run without any restrictions  
   d) Increasing the number of threads  
   Answer: b) Implementing locks or mutexes  

---

# Error detection

## Questions

Question 1: What action does an operating system typically take when it detects a memory error due to an invalid memory address access?  
a) Ignore the error  
b) Trigger a page fault  
c) Restart the program  
d) Log the error and continue  

**Answer:** b) Trigger a page fault  

---

Question 2: In the case of an I/O device error, what might the operating system do if it receives an interrupt signal indicating a read operation failure?  
a) Immediately terminate the program  
b) Retry the operation a few times  
c) Log the error and shut down  
d) Ignore the error and continue  

**Answer:** b) Retry the operation a few times  

---

Question 3: If an operating system detects that a program is trying to access an invalid memory address, what is the likely outcome?  
a) The program will continue to run without issues  
b) The operating system will terminate the program  
c) The program will be moved to a different memory address  
d) The operating system will automatically fix the memory address  

**Answer:** b) The operating system will terminate the program  

---

Question 4: What is a potential risk of an operating system retrying an I/O operation after an intermittent error?  
a) The system will become faster  
b) Data corruption may occur  
c) The program will be terminated  
d) The operating system will crash  

**Answer:** b) Data corruption may occur  

---

Question 5: Which of the following best describes a page fault?  
a) A successful memory access  
b) An error that occurs when a program accesses a memory address that is not currently mapped to physical memory  
c) A type of hardware failure  
d) A method of increasing memory speed  

**Answer:** b) An error that occurs when a program accesses a memory address that is not currently mapped to physical memory  

---

# Debugging facilities

## Questions

Question 1: Which of the following is a built-in debugging tool commonly found in Integrated Development Environments (IDEs)?  
a) Code Formatter  
b) Version Control  
c) Breakpoints  
d) Code Linter  
**Answer:** c) Breakpoints  

Question 2: When using remote debugging tools like Chrome DevTools, what is a common challenge developers face?  
a) Lack of internet connection  
b) Difficulty in tracing errors due to asynchronous code execution  
c) Inability to set breakpoints  
d) Limited access to server resources  
**Answer:** b) Difficulty in tracing errors due to asynchronous code execution  

Question 3: In an IDE, what does stepping through code line by line allow a programmer to do?  
a) Compile the code  
b) Execute the entire program at once  
c) Inspect the flow of execution and variable states  
d) Optimize the code for performance  
**Answer:** c) Inspect the flow of execution and variable states  

Question 4: Which of the following debugging facilities would be most useful for inspecting the state of a web application running in a browser?  
a) Command Line Interface  
b) Integrated Development Environment  
c) Remote Debugging Tools  
d) Static Code Analysis  
**Answer:** c) Remote Debugging Tools  

Question 5: If a developer sets a breakpoint in their JavaScript code but the code execution does not pause, what could be a possible reason?  
a) The code is syntactically incorrect  
b) The breakpoint is set on an asynchronous function that has already completed  
c) The developer is using an outdated version of the browser  
d) The code has been optimized by the browser  
**Answer:** b) The breakpoint is set on an asynchronous function that has already completed  

---

# Resource Allocation

## Questions

1. Question: In a cloud computing environment, if VM1 is allocated 2 CPU cores, 4GB of RAM, and 50GB of storage, while VM2 is allocated 1 CPU core, 2GB of RAM, and 20GB of storage, what is the total amount of RAM allocated to both VMs?
   a) 4GB  
   b) 6GB  
   c) 8GB  
   d) 10GB  
   Answer: b) 6GB

2. Question: If a web server is hosting multiple websites and one website experiences a surge in traffic, what is a potential consequence of static resource allocation?
   a) Increased performance for all websites  
   b) Slow response times for the website with high traffic  
   c) Equal distribution of resources among all websites  
   d) Automatic scaling of resources  
   Answer: b) Slow response times for the website with high traffic

3. Question: Which of the following strategies can be implemented to improve resource allocation in a scenario with fluctuating traffic loads?
   a) Static resource allocation  
   b) Dynamic resource allocation  
   c) Manual resource allocation  
   d) No resource allocation  
   Answer: b) Dynamic resource allocation

4. Question: If a hypervisor manages resource allocation for VMs, what is one of its primary functions?
   a) To increase the physical server's hardware  
   b) To ensure each VM has the resources it needs without interference  
   c) To limit the number of VMs on a server  
   d) To monitor internet traffic  
   Answer: b) To ensure each VM has the resources it needs without interference

5. Question: In a scenario where a web server is experiencing high traffic, which of the following would be a sign that resource allocation needs to be adjusted?
   a) All websites are loading quickly  
   b) One website is down while others are functioning normally  
   c) The server is using less than 50% of its CPU capacity  
   d) All websites are receiving equal traffic  
   Answer: b) One website is down while others are functioning normally

---

# Logging

## Questions

1. Question: What information does a logging system typically record when an employee logs into their workstation?  
   a) Username, time of login, applications used, duration of use  
   b) Username, password, IP address, location  
   c) Time of login, time of logout, total hours worked  
   d) Applications used, duration of use, employee's department  
   **Answer:** a) Username, time of login, applications used, duration of use  

2. Question: If John logs into his computer at 9 AM and spends 2 hours on design software and 1 hour on a project management tool, what is the total duration of his computer usage?  
   a) 1 hour  
   b) 2 hours  
   c) 3 hours  
   d) 4 hours  
   **Answer:** c) 3 hours  

3. Question: In a scenario where Alice logs into Computer A at 8 AM and logs out at 12 PM, and Bob logs in at 1 PM and logs out at 5 PM, how many hours should the logging system attribute to Alice and Bob respectively?  
   a) Alice: 4 hours, Bob: 4 hours  
   b) Alice: 8 hours, Bob: 0 hours  
   c) Alice: 0 hours, Bob: 8 hours  
   d) Alice: 2 hours, Bob: 6 hours  
   **Answer:** a) Alice: 4 hours, Bob: 4 hours  

4. Question: What could be a potential issue if a logging system fails to accurately differentiate between users on a shared computer?  
   a) Increased software performance  
   b) Incorrect billing for software licenses  
   c) Enhanced user experience  
   d) Improved resource allocation  
   **Answer:** b) Incorrect billing for software licenses  

5. Question: If the IT department generates a report showing that John used 40 hours of design software and 20 hours of project management tools, what is the total number of hours John spent using both applications?  
   a) 40 hours  
   b) 60 hours  
   c) 20 hours  
   d) 80 hours  
   **Answer:** b) 60 hours  

6. Question: Which of the following is NOT typically captured by a logging system when monitoring employee computer usage?  
   a) Username  
   b) Time of login  
   c) Employee's salary  
   d) Applications used  
   **Answer:** c) Employee's salary  

---

# Protection and Security

## Questions

Question 1: In a multiuser database system, what is the primary purpose of user login credentials and permissions?  
a) To allow users to access all data freely  
b) To ensure that users can only access data they are authorized to view  
c) To enable users to change any data in the database  
d) To prevent users from logging into the system  
**Answer:** b) To ensure that users can only access data they are authorized to view  

Question 2: In a cloud storage service, what should happen if two users attempt to edit the same document simultaneously?  
a) The system should automatically save both users' changes without any prompts  
b) The system should lock the document for one user until the other is finished  
c) The system should prompt the second user to merge changes or save a new version  
d) The system should discard the changes made by the first user  
**Answer:** c) The system should prompt the second user to merge changes or save a new version  

Question 3: What is a potential risk of not implementing proper access controls in a multiuser database system?  
a) Increased user satisfaction  
b) Unauthorized access to sensitive data  
c) Improved system performance  
d) Simplified user management  
**Answer:** b) Unauthorized access to sensitive data  

Question 4: If a bank's database allows tellers to access customer account information but restricts them from altering account balances, what type of security measure is being implemented?  
a) Data encryption  
b) Role-based access control  
c) Network security  
d) Physical security  
**Answer:** b) Role-based access control  

Question 5: In a version control system, what is the primary benefit of allowing users to save a new version of a document instead of overwriting the existing one?  
a) It reduces the amount of storage used  
b) It prevents users from making changes  
c) It preserves the history of changes made to the document  
d) It simplifies the editing process  
**Answer:** c) It preserves the history of changes made to the document  

---

# Access Control

## Questions

Question 1: What is the primary purpose of role-based access control (RBAC) in a corporate environment?  
a) To allow all employees access to all data  
b) To restrict access to sensitive information based on job functions  
c) To eliminate the need for passwords  
d) To enable employees to share accounts easily  
**Answer:** b) To restrict access to sensitive information based on job functions  

Question 2: In the context of access control, what is a potential risk of using shared accounts for application access?  
a) Increased security  
b) Difficulty in tracking user activity  
c) Simplified user management  
d) Enhanced data protection  
**Answer:** b) Difficulty in tracking user activity  

Question 3: Which of the following is NOT a benefit of implementing individual user accounts instead of shared accounts?  
a) Improved accountability  
b) Enhanced tracking of data access  
c) Simplified password management  
d) Reduced risk of unauthorized access  
**Answer:** c) Simplified password management  

Question 4: If a company has implemented RBAC and an employee from the marketing department tries to access HR records, what should happen?  
a) The employee should be granted access  
b) The employee should be denied access  
c) The employee should be prompted to request access  
d) The employee should be allowed to view only partial records  
**Answer:** b) The employee should be denied access  

Question 5: In a scenario where access control measures are in place, what is the main advantage of having distinct roles for different departments?  
a) It allows for easier collaboration between departments  
b) It ensures that only authorized personnel can access sensitive information  
c) It reduces the number of user accounts needed  
d) It simplifies the login process for all employees  
**Answer:** b) It ensures that only authorized personnel can access sensitive information  

---

# User Authentication

## Questions

1. Question: What is the primary purpose of user authentication in a login system?  
   a) To enhance user experience  
   b) To verify the identity of users  
   c) To store user data  
   d) To provide customer support  
   Answer: b) To verify the identity of users  

2. Question: In a multi-factor authentication (MFA) system, which of the following is NOT typically considered a form of verification?  
   a) Password  
   b) Fingerprint scan  
   c) Security question  
   d) Email address  
   Answer: d) Email address  

3. Question: If a user enters the correct username and password but fails to provide the second form of verification in an MFA system, what will happen?  
   a) The user will be granted access  
   b) The user will be prompted to reset their password  
   c) The user will be denied access  
   d) The user will be logged out automatically  
   Answer: c) The user will be denied access  

4. Question: Which of the following scenarios best illustrates a typical user authentication process?  
   a) A user receives a text message with a verification code after entering their password  
   b) A user logs into their email account by entering their email address and password  
   c) A user is automatically logged into their account without any credentials  
   d) A user is asked to answer a security question before accessing their account  
   Answer: b) A user logs into their email account by entering their email address and password  

5. Question: In a login system, if a user enters their credentials and receives an error message stating "Invalid username or password," what does this indicate?  
   a) The user has successfully logged in  
   b) The user has entered incorrect credentials  
   c) The user needs to reset their password  
   d) The user is locked out of their account  
   Answer: b) The user has entered incorrect credentials  

6. Question: Which of the following is an example of a second form of verification in an MFA system?  
   a) Entering a username  
   b) Providing a password  
   c) Using a one-time code sent to a mobile device  
   d) Answering a security question  
   Answer: c) Using a one-time code sent to a mobile device  

---

