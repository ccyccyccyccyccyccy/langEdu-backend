# Hash Table

## Questions

### Questions on Hash Tables

**Question 1:** What is the primary purpose of a hash function in a hash table?  
a) To encrypt data  
b) To compute an index for storing data  
c) To sort data  
d) To delete data  
**Answer:** b) To compute an index for storing data

---

**Question 2:** Given the student IDs 12345, 54325, and 98765, which index will they all hash to if the hash function returns the last digit of the student ID?  
a) 1  
b) 2  
c) 3  
d) 5  
**Answer:** d) 5

---

**Question 3:** In a hash table that uses chaining to handle collisions, what data structure is typically used at each index?  
a) Array  
b) Stack  
c) Linked List  
d) Queue  
**Answer:** c) Linked List

---

**Question 4:** If a hash table has a size of 10 and uses the modulo operation as a hash function, what index will the student ID 12345 hash to?  
a) 3  
b) 5  
c) 7  
d) 9  
**Answer:** b) 5 (since 12345 % 10 = 5)

---

**Question 5:** Consider the following code snippet for inserting a student record into a hash table. What will happen if the student ID 54325 is inserted after 12345, given that both hash to the same index?

```python
class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10)]  # Size of hash table is 10

    def hash_function(self, student_id):
        return student_id % 10

    def insert(self, student_id, record):
        index = self.hash_function(student_id)
        self.table[index].append(record)  # Chaining
```

a) The record for 54325 will overwrite the record for 12345.  
b) The record for 54325 will be added to a linked list at the same index.  
c) An error will occur because of the collision.  
d) The record for 54325 will not be added.  
**Answer:** b) The record for 54325 will be added to a linked list at the same index.

---

**Question 6:** What is a potential drawback of using a simple hash function that only considers the last digit of the student ID?  
a) It is too complex to implement.  
b) It can lead to a high number of collisions.  
c) It requires more memory.  
d) It is not secure.  
**Answer:** b) It can lead to a high number of collisions.

---

**Question 7:** Which of the following statements is true regarding hash tables?  
a) They are always faster than arrays for searching.  
b) They require a fixed size and cannot grow.  
c) They can provide average-case constant time complexity for search operations.  
d) They do not handle collisions.  
**Answer:** c) They can provide average-case constant time complexity for search operations.

---

# Hash Function

## Questions

### Question 1:
What is the output of the hash function `hash(key) = (key * 3 + 1) % 7` for the key 5?

a) 1  
b) 2  
c) 3  
d) 4  

**Answer:** a) 1  
**Explanation:** hash(5) = (5 * 3 + 1) % 7 = (15 + 1) % 7 = 16 % 7 = 2.

---

### Question 2:
In a hash table of size 10, what index will the key 25 be stored at using the hash function `hash(key) = key % 10`?

a) 2  
b) 5  
c) 0  
d) 7  

**Answer:** b) 5  
**Explanation:** hash(25) = 25 % 10 = 5.

---

### Question 3:
If we have a hash table of size 7 and we insert the keys 1, 2, and 3 using the hash function `hash(key) = (key * 3 + 1) % 7`, what will be the index for key 3?

a) 0  
b) 3  
c) 4  
d) 5  

**Answer:** b) 3  
**Explanation:** hash(3) = (3 * 3 + 1) % 7 = (9 + 1) % 7 = 10 % 7 = 3.

---

### Question 4:
What happens when you try to insert the key 10 into the hash table after inserting keys 1, 2, and 3, using the hash function `hash(key) = (key * 3 + 1) % 7`?

a) It will be stored at index 2, causing a collision with key 2.  
b) It will be stored at index 5, causing a collision with key 1.  
c) It will be stored at index 0, causing a collision with key 1.  
d) It will be stored at index 6, causing no collision.  

**Answer:** a) It will be stored at index 2, causing a collision with key 2.  
**Explanation:** hash(10) = (10 * 3 + 1) % 7 = (30 + 1) % 7 = 31 % 7 = 3, which collides with key 2.

---

### Question 5:
Which of the following statements is true regarding hash functions?

a) A good hash function always produces unique indices for different keys.  
b) Hash functions can lead to collisions, which require resolution strategies.  
c) The size of the hash table does not affect the performance of the hash function.  
d) Hash functions are only used for integer keys.  

**Answer:** b) Hash functions can lead to collisions, which require resolution strategies.  
**Explanation:** Collisions are a common issue in hash tables, and various strategies exist to handle them.

---

# Applications of Hashing

## Questions

### Question 1:
What is the primary purpose of using a hash table in a compiler's symbol table?
a) To store the actual values of variables  
b) To quickly check if a variable has been declared  
c) To optimize memory usage  
d) To sort variables alphabetically  
**Answer:** b) To quickly check if a variable has been declared

### Question 2:
In the context of hashing, what is a collision?
a) When two different variables are stored at the same index in a hash table  
b) When a variable is declared multiple times  
c) When the hash function produces a unique index for every variable  
d) When a variable is not found in the symbol table  
**Answer:** a) When two different variables are stored at the same index in a hash table

### Question 3:
Given the following code snippet, what will happen if the hash function used for the symbol table causes a collision for 'count1' and 'count2'?

```c
int count1;
int count2;
```
a) The compiler will throw an error for undeclared variables  
b) The compiler will store both variables correctly without issues  
c) The compiler may retrieve the wrong type or value for one of the variables  
d) The compiler will ignore one of the variables  
**Answer:** c) The compiler may retrieve the wrong type or value for one of the variables

### Question 4:
Which of the following is a potential consequence of a poorly designed hash function in a symbol table?
a) Increased speed of variable retrieval  
b) Reduced memory consumption  
c) Increased likelihood of variable name collisions  
d) Enhanced readability of code  
**Answer:** c) Increased likelihood of variable name collisions

### Question 5:
What is one way to mitigate collisions in a hash table?
a) Use a larger hash table  
b) Use a more complex hash function  
c) Store all variables in a single linked list  
d) Avoid using hash tables altogether  
**Answer:** b) Use a more complex hash function

---

# Hash Table

## Questions

### Question 1:
What is the primary purpose of a hash table?
a) To store data in a sorted manner  
b) To provide quick access to data using a key  
c) To store data in a linear format  
d) To perform mathematical calculations  

**Answer:** b) To provide quick access to data using a key

---

### Question 2:
Given the following hash function: `hash(key) = len(key)`, what will be the index for the string 'hello' when inserted into a hash table?
a) 4  
b) 5  
c) 6  
d) 0  

**Answer:** b) 5

---

### Question 3:
In a hash table that uses chaining to handle collisions, what data structure is typically used at each index to store multiple entries?
a) Array  
b) Stack  
c) Linked List  
d) Queue  

**Answer:** c) Linked List

---

### Question 4:
If the hash table has a size of 10 and the hash function is defined as `hash(key) = key % 10`, what will be the index for the student ID 12345?
a) 3  
b) 5  
c) 0  
d) 9  

**Answer:** b) 5

---

### Question 5:
Consider the following code snippet for inserting a value into a hash table using chaining:

```python
class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    def insert(self, key, value):
        index = len(key) % len(self.table)
        self.table[index].append((key, value))
```

What will happen if you insert the following pairs: ('cat', 1), ('dog', 2), and ('bat', 3)?
a) All pairs will be stored at different indices  
b) All pairs will cause a collision and be stored at index 3  
c) Only 'cat' will be stored at index 3  
d) The hash table will throw an error  

**Answer:** b) All pairs will cause a collision and be stored at index 3

---

### Question 6:
What is a potential drawback of using a simple hash function like `hash(key) = len(key)`?
a) It is too complex to compute  
b) It can lead to a high number of collisions  
c) It requires too much memory  
d) It is not deterministic  

**Answer:** b) It can lead to a high number of collisions

---

### Question 7:
When searching for a value in a hash table that uses chaining, what is the worst-case time complexity if all entries hash to the same index?
a) O(1)  
b) O(log n)  
c) O(n)  
d) O(n log n)  

**Answer:** c) O(n)

---

### Question 8:
If a hash table uses a hash function that returns the ASCII value of the first character of the key, which of the following keys would hash to the same index if the table size is 26?
a) 'apple' and 'banana'  
b) 'cat' and 'car'  
c) 'dog' and 'deer'  
d) 'elephant' and 'eagle'  

**Answer:** d) 'elephant' and 'eagle'

---

# Hashing

## Questions

### Question 1:
What is the purpose of a hash function in a hash table?
a) To encrypt data  
b) To determine the index for storing data  
c) To sort data  
d) To compress data  
**Answer:** b) To determine the index for storing data

### Question 2:
Given the hash function `ID % 10`, what index will the student ID `987654` be stored at?
a) 4  
b) 5  
c) 6  
d) 7  
**Answer:** b) 4 (since 987654 % 10 = 4)

### Question 3:
What is a common method to handle collisions in a hash table?
a) Deleting the older entry  
b) Using a different hash function  
c) Chaining  
d) Increasing the size of the hash table  
**Answer:** c) Chaining

### Question 4:
If two usernames, 'user1' and 'user11', both hash to index 1 using the hash function `key % 10`, what data structure can be used at index 1 to store both entries?
a) Array  
b) Stack  
c) Linked list  
d) Queue  
**Answer:** c) Linked list

### Question 5:
In a hash table, what happens when a collision occurs and chaining is used?
a) The new entry overwrites the existing entry  
b) The new entry is ignored  
c) The new entry is added to a linked list at the same index  
d) The hash table is resized  
**Answer:** c) The new entry is added to a linked list at the same index

### Question 6:
Consider the following code snippet for a hash function:
```python
def hash_function(key):
    return key % 10
```
What will be the output of `hash_function(123456)`?
a) 0  
b) 6  
c) 5  
d) 4  
**Answer:** b) 6

### Question 7:
If a hash table has a size of 10 and the following student IDs are added: 123456, 234567, and 345678, what index will the student ID `234567` be stored at using the hash function `ID % 10`?
a) 7  
b) 8  
c) 9  
d) 6  
**Answer:** a) 7 (since 234567 % 10 = 7)

### Question 8:
Which of the following statements about hash tables is true?
a) Hash tables always store data in sorted order.  
b) Hash tables can have multiple entries at the same index if collisions occur.  
c) Hash tables do not require a hash function.  
d) Hash tables are always implemented using arrays.  
**Answer:** b) Hash tables can have multiple entries at the same index if collisions occur.

---

# Key Universe

## Questions

### Question 1:
What is the key universe in a hash table designed to store usernames that can be any combination of letters and numbers up to 20 characters long?

a) All possible strings of length 20  
b) All valid email formats  
c) All possible usernames that users can choose  
d) Only usernames that contain letters  

**Answer:** c) All possible usernames that users can choose

---

### Question 2:
In a hash table using email addresses as keys, which of the following is a valid example of a key from the key universe?

a) user@subdomain.example.com  
b) user@.com  
c) user@subdomain..example.com  
d) user@subdomain@example.com  

**Answer:** a) user@subdomain.example.com

---

### Question 3:
Why can the key universe for email addresses be considered tricky?

a) Because all email addresses must be unique  
b) Because some email addresses are case-sensitive  
c) Because some email addresses may have different representations  
d) Because email addresses can only contain letters  

**Answer:** c) Because some email addresses may have different representations

---

### Question 4:
Given the following code snippet, which of the following usernames would be considered valid based on the key universe defined?

```python
def is_valid_username(username):
    return len(username) <= 20 and username.isalnum()

usernames = ['user123', 'john_doe', 'alice2023', 'user@name']
valid_usernames = [username for username in usernames if is_valid_username(username)]
```

a) ['user123', 'john_doe', 'alice2023']  
b) ['user123', 'alice2023']  
c) ['john_doe', 'alice2023']  
d) ['user123', 'john_doe', 'alice2023', 'user@name']  

**Answer:** b) ['user123', 'alice2023']

---

### Question 5:
If a hash table uses email addresses as keys, which of the following email addresses would be treated as equivalent due to case insensitivity?

a) user@example.com and USER@example.com  
b) user.name@gmail.com and username@gmail.com  
c) user.name+tag@gmail.com and user.name@gmail.com  
d) user@subdomain.example.com and user@subdomain.example.com  

**Answer:** a) user@example.com and USER@example.com

---

# Slots in Hash Table

## Questions

### Questions on Slots in Hash Table

**Question 1:** What is the hash value for the key 25 using the hash function h(k) = k % 10?  
a) 2  
b) 5  
c) 7  
d) 0  
**Answer:** b) 5

---

**Question 2:** In a hash table with 10 slots, if the keys 15, 25, and 35 are inserted using the hash function h(k) = k % 10, what will be the contents of T[5] after all insertions?  
a) 15  
b) 25  
c) 15 -> 25 -> 35  
d) 15, 25, 35  
**Answer:** c) 15 -> 25 -> 35

---

**Question 3:** If we use chaining to resolve collisions in a hash table, what data structure is typically used to store multiple items in the same slot?  
a) Array  
b) Stack  
c) Linked List  
d) Queue  
**Answer:** c) Linked List

---

**Question 4:** Given a hash table with 5 slots and the hash function h(k) = k % 5, what will be the final state of the hash table after inserting keys 10, 15, and 20 using open addressing?  
a) T[0] = 10, T[1] = 15, T[2] = 20, T[3] = null, T[4] = null  
b) T[0] = 10, T[1] = 20, T[2] = 15, T[3] = null, T[4] = null  
c) T[0] = 15, T[1] = 10, T[2] = 20, T[3] = null, T[4] = null  
d) T[0] = 20, T[1] = 10, T[2] = 15, T[3] = null, T[4] = null  
**Answer:** a) T[0] = 10, T[1] = 15, T[2] = 20, T[3] = null, T[4] = null

---

**Question 5:** If the hash table is implemented using open addressing and we attempt to insert the key 15 after inserting the key 10 at T[0], which slot will key 15 be placed in?  
a) T[0]  
b) T[1]  
c) T[2]  
d) T[3]  
**Answer:** b) T[1]

---

**Question 6:** What is the primary disadvantage of using open addressing for collision resolution in a hash table?  
a) It requires more memory  
b) It can lead to clustering  
c) It is slower than chaining  
d) It cannot handle collisions  
**Answer:** b) It can lead to clustering

---

**Question 7:** If we have a hash table with 10 slots and we insert keys 5, 15, and 25 using the hash function h(k) = k % 10, what will be the contents of T[5]?  
a) 5  
b) 15  
c) 25  
d) 5 -> 15 -> 25  
**Answer:** d) 5 -> 15 -> 25

---

**Question 8:** Which of the following statements is true regarding the hash function h(k) = k % 5 when inserting the key 22?  
a) It will be placed in slot 0  
b) It will be placed in slot 1  
c) It will be placed in slot 2  
d) It will be placed in slot 3  
**Answer:** c) It will be placed in slot 2

---

---

# Limitations of Hash Tables

## Questions

### Questions on Limitations of Hash Tables

1. **Question:** What is a primary limitation of hash tables regarding key order?
   a) They store keys in a sorted manner  
   b) They do not maintain any order of keys  
   c) They can only store integer keys  
   d) They automatically remove duplicate keys  
   **Answer:** b) They do not maintain any order of keys

2. **Question:** Given the hash table `{"apple": 1, "banana": 2, "cherry": 3}`, how would you find the minimum key?
   a) Directly access the minimum key using a built-in function  
   b) Iterate through all keys and compare them  
   c) Use a sorting algorithm on the keys  
   d) Both b and c  
   **Answer:** d) Both b and c

3. **Question:** If you have a hash table storing student IDs and grades as `{1001: 85, 1002: 90, 1003: 78}`, how can you find students with grades between 80 and 90?
   a) Directly query the hash table for the range  
   b) Extract all key-value pairs, sort them, and filter based on grades  
   c) Use a binary search on the hash table  
   d) None of the above  
   **Answer:** b) Extract all key-value pairs, sort them, and filter based on grades

4. **Question:** Which of the following operations is NOT efficient when using a hash table?
   a) Inserting a new key-value pair  
   b) Retrieving a value by its key  
   c) Finding the maximum key in the hash table  
   d) Deleting a key-value pair  
   **Answer:** c) Finding the maximum key in the hash table

5. **Question:** Consider the following code snippet:
   ```python
   hash_table = {"apple": 1, "banana": 2, "cherry": 3}
   min_key = min(hash_table.keys())
   ```
   What does this code do?
   a) It retrieves the value associated with the minimum key  
   b) It finds the minimum key in the hash table  
   c) It raises an error because hash tables do not support min operations  
   d) It sorts the keys of the hash table  
   **Answer:** b) It finds the minimum key in the hash table

6. **Question:** Why might using a hash table be inefficient for range queries?
   a) Hash tables are designed for range queries  
   b) They require sorting and filtering of all entries  
   c) They can only store numeric keys  
   d) They automatically maintain sorted order  
   **Answer:** b) They require sorting and filtering of all entries

---

# Unrealistic Solution

## Questions

### Question 1:
What is the primary drawback of using a hash table with a very large array size but only a few keys inserted?

a) Increased time complexity for operations  
b) Significant memory wastage  
c) Difficulty in retrieving keys  
d) Increased collision rates  

**Answer:** b) Significant memory wastage

---

### Question 2:
In the context of hash tables, what does O(1) time complexity imply?

a) The operation time increases linearly with the number of keys  
b) The operation time is constant regardless of the number of keys  
c) The operation time is dependent on the size of the array  
d) The operation time is logarithmic  

**Answer:** b) The operation time is constant regardless of the number of keys

---

### Question 3:
Given the following code snippet, what is the main issue with the hash table implementation?

```python
class HashTable:
    def __init__(self):
        self.size = 1000000
        self.table = [None] * self.size

    def insert(self, key):
        self.table[key] = True
```

a) The hash table does not handle collisions  
b) The array size is too small  
c) The insertion operation is not O(1)  
d) The hash table does not allow for deletion  

**Answer:** a) The hash table does not handle collisions

---

### Question 4:
If a hash table is designed to store 64-bit user IDs and an array of size 2^64 is allocated, what is the most significant issue with this design?

a) It will lead to high collision rates  
b) It will be inefficient in terms of time complexity  
c) The memory requirement is impractically large  
d) It will not allow for dynamic resizing  

**Answer:** c) The memory requirement is impractically large

---

### Question 5:
Which of the following scenarios best illustrates an unrealistic solution in hash table design?

a) Using a hash function that distributes keys evenly across a small array  
b) Allocating a hash table with an array size equal to the maximum possible key value  
c) Implementing a linked list to handle collisions in a hash table  
d) Using a dynamic array that resizes based on the number of elements  

**Answer:** b) Allocating a hash table with an array size equal to the maximum possible key value

---

# Hash Function

## Questions

### Multiple Choice Questions on Hash Functions

**Question 1:** What is the hash value of the string 'dog' if the hash function sums the ASCII values of its characters and takes the modulus with the size of the hash table, which has 7 slots?  
a) 3  
b) 5  
c) 1  
d) 0  
**Answer:** a) 3  
*(Explanation: ASCII values are 100 (d), 111 (o), and 103 (g), which sum to 314. 314 % 7 = 3.)*

---

**Question 2:** Given a hash table with 4 slots, what will be the hash value of the integer 9 using a hash function that returns the integer modulo the size of the hash table?  
a) 1  
b) 2  
c) 3  
d) 0  
**Answer:** a) 1  
*(Explanation: 9 % 4 = 1.)*

---

**Question 3:** If a hash function takes a string input and computes its hash value by summing the ASCII values of its characters, what will be the hash value of the string 'bat' for a hash table with 5 slots?  
a) 2  
b) 3  
c) 4  
d) 0  
**Answer:** b) 3  
*(Explanation: ASCII values are 98 (b), 97 (a), and 116 (t), which sum to 311. 311 % 5 = 1.)*

---

**Question 4:** In a hash table with 6 slots, if the integers 12, 18, and 24 are hashed using a simple modulo function, which slot will they all map to?  
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** a) 0  
*(Explanation: 12 % 6 = 0, 18 % 6 = 0, and 24 % 6 = 0.)*

---

**Question 5:** What is a potential issue that can arise when using a hash function that simply returns the input integer modulo the size of the hash table?  
a) It is always efficient.  
b) It can lead to collisions.  
c) It guarantees unique slots for each input.  
d) It is not deterministic.  
**Answer:** b) It can lead to collisions.  
*(Explanation: Multiple integers can hash to the same slot, causing collisions.)*

---

**Question 6:** If the string 'hello' is hashed using the described hash function with a hash table of size 10, what is the hash value?  
a) 5  
b) 7  
c) 8  
d) 9  
**Answer:** c) 8  
*(Explanation: ASCII values are 104 (h), 101 (e), 108 (l), 108 (l), and 111 (o), which sum to 540. 540 % 10 = 0.)*

---

**Question 7:** Which of the following statements about hash functions is true?  
a) Hash functions can never produce collisions.  
b) Hash functions can map multiple inputs to the same output.  
c) Hash functions are always reversible.  
d) Hash functions only work with strings.  
**Answer:** b) Hash functions can map multiple inputs to the same output.  
*(Explanation: This is a fundamental property of hash functions, known as collisions.)*

---

# Key Universe Size

## Questions

### Question 1:
What is the total number of possible unique identifiers for an 8-digit student ID system?
a) 5,000  
b) 10,000  
c) 100,000  
d) 100,000,000  

**Answer:** d) 100,000,000

---

### Question 2:
In a university with 8-digit student IDs, if there are 5,000 enrolled students, what is the ratio of actual student IDs in use to the total possible combinations?
a) 1:20,000  
b) 1:1,000  
c) 1:200  
d) 1:20  

**Answer:** a) 1:20,000

---

### Question 3:
If a university has 10^8 possible 8-digit student IDs but 2,000 IDs are assigned to students who have graduated, how many active student IDs are currently in use?
a) 5,000  
b) 3,000  
c) 8,000  
d) 10,000  

**Answer:** b) 3,000

---

### Question 4:
Which of the following statements best describes the concept of key universe size?
a) It refers to the total number of students enrolled in a university.  
b) It is the total number of possible unique identifiers compared to the actual number in use.  
c) It indicates the number of students who have graduated.  
d) It is the number of IDs that are currently active.  

**Answer:** b) It is the total number of possible unique identifiers compared to the actual number in use.

---

### Question 5:
Given the following code snippet, what will be the output if the variable `active_ids` is set to 3,000 and `total_ids` is set to 10^8?

```python
active_ids = 3000
total_ids = 10**8
ratio = total_ids / active_ids
print(ratio)
```
a) 33,333.33  
b) 100,000  
c) 20,000  
d) 10,000  

**Answer:** a) 33,333.33

---

### Question 6:
If a university has a key universe size of 10^8 but only 3,000 IDs are active, what percentage of the total possible IDs are currently in use?
a) 0.003%  
b) 0.03%  
c) 0.3%  
d) 3%  

**Answer:** a) 0.003%

---

# Hash Value

## Questions

### Question 1:
What is the hash value of the string 'banana' using the hash function described (summing ASCII values and taking modulus with respect to 10)?

a) 1  
b) 2  
c) 3  
d) 4  

**Answer:** b) 2  
*Explanation: The ASCII values are: 'b' = 98, 'a' = 97, 'n' = 110, 'a' = 97, 'n' = 110, 'a' = 97. The sum is 98 + 97 + 110 + 97 + 110 + 97 = 609. Thus, h('banana') = 609 % 10 = 9.*

### Question 2:
Given the hash function h(k) = (k mod 7), which of the following pairs of keys will cause a collision?

a) k1 = 8 and k2 = 15  
b) k1 = 14 and k2 = 21  
c) k1 = 5 and k2 = 12  
d) k1 = 3 and k2 = 10  

**Answer:** b) k1 = 14 and k2 = 21  
*Explanation: Both yield the same hash value: h(14) = 14 mod 7 = 0 and h(21) = 21 mod 7 = 0.*

### Question 3:
If the hash function h(k) is defined as h(k) = (sum of ASCII values of characters in k) % 5, what is the hash value of the string 'cat'?

a) 0  
b) 1  
c) 2  
d) 3  

**Answer:** c) 2  
*Explanation: The ASCII values are: 'c' = 99, 'a' = 97, 't' = 116. The sum is 99 + 97 + 116 = 312. Thus, h('cat') = 312 % 5 = 2.*

### Question 4:
Which of the following statements about hash functions is true?

a) Hash functions always produce unique hash values for different keys.  
b) Hash functions can lead to collisions where different keys produce the same hash value.  
c) Hash functions are not useful for data retrieval.  
d) Hash functions can only be applied to integer keys.  

**Answer:** b) Hash functions can lead to collisions where different keys produce the same hash value.  
*Explanation: This is a fundamental property of hash functions, as demonstrated in the tricky example with k1 = 14 and k2 = 21.*

### Question 5:
What is the hash value of the key 'grape' using the hash function h(k) = (sum of ASCII values of characters in k) % 10?

a) 5  
b) 6  
c) 7  
d) 8  

**Answer:** a) 5  
*Explanation: The ASCII values are: 'g' = 103, 'r' = 114, 'a' = 97, 'p' = 112, 'e' = 101. The sum is 103 + 114 + 97 + 112 + 101 = 527. Thus, h('grape') = 527 % 10 = 7.*

---

# Storage in Hash Table

## Questions

### Question 1:
What is the hash value for the key 'apple' using the hash function h(k) = ASCII sum of characters % 10?

a) 5  
b) 0  
c) 4  
d) 9  

**Answer:** b) 0

---

### Question 2:
If the key 'banana' is hashed using the same function, what is the resulting index in the hash table?

a) 8  
b) 9  
c) 7  
d) 6  

**Answer:** b) 9

---

### Question 3:
What issue arises when both 'banana' and 'grape' hash to the same index in the hash table?

a) Data loss  
b) Collision  
c) Underflow  
d) Overflow  

**Answer:** b) Collision

---

### Question 4:
Which of the following is a common strategy to resolve collisions in a hash table?

a) Linear search  
b) Chaining  
c) Binary search  
d) Sorting  

**Answer:** b) Chaining

---

### Question 5:
Given the following code snippet, what will be the output when the key 'grape' is hashed using the provided hash function?

```python
def hash_function(key):
    return sum(ord(char) for char in key) % 10

print(hash_function('grape'))
```

a) 5  
b) 9  
c) 0  
d) 4  

**Answer:** a) 5

---

### Question 6:
If a hash table uses open addressing for collision resolution, what happens when a collision occurs?

a) The new key is discarded  
b) The new key is stored in a different table  
c) The algorithm searches for the next available index  
d) The existing key is overwritten  

**Answer:** c) The algorithm searches for the next available index

---

### Question 7:
What is the primary purpose of a hash function in a hash table?

a) To sort the data  
b) To encrypt the data  
c) To compute an index for storing data  
d) To compress the data  

**Answer:** c) To compute an index for storing data

---

### Question 8:
If the ASCII sum of the characters in 'orange' is 111 + 114 + 97 + 110 + 103 + 101 = 636, what index will it be stored at in a hash table of size 10?

a) 6  
b) 5  
c) 0  
d) 1  

**Answer:** b) 6

---

---

# Collision Problem

## Questions

### Questions on Collision Problem

**Question 1:** What is a collision in the context of hash tables?  
a) When two different keys hash to the same index  
b) When a key is not found in the hash table  
c) When the hash table is full  
d) When two keys hash to different indices  
**Answer:** a) When two different keys hash to the same index

---

**Question 2:** Given the hash function `hash(key) = key % 10`, what will be the result of `hash(25)`?  
a) 5  
b) 2  
c) 0  
d) 1  
**Answer:** a) 5

---

**Question 3:** If we have the keys 12 and 22, what index do they both hash to using the function `hash(key) = key % 10`?  
a) 1  
b) 2  
c) 3  
d) 4  
**Answer:** b) 2

---

**Question 4:** Using the hash function `hash(key) = (key * 31) % 10`, what is the hash value for the key 3?  
a) 3  
b) 4  
c) 5  
d) 6  
**Answer:** a) 3

---

**Question 5:** Which of the following pairs of keys will cause a collision using the hash function `hash(key) = (key * 31) % 10`?  
a) 1 and 2  
b) 3 and 13  
c) 5 and 15  
d) 7 and 17  
**Answer:** b) 3 and 13

---

**Question 6:** What is the output of the following code snippet?
```python
def hash_function(key):
    return (key * 31) % 10

print(hash_function(10))
```
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** a) 0

---

**Question 7:** If a hash table has a collision resolution strategy of chaining, what happens when a collision occurs?  
a) The new key is discarded  
b) The new key is added to a linked list at the colliding index  
c) The hash table is resized  
d) The existing key is overwritten  
**Answer:** b) The new key is added to a linked list at the colliding index

---

**Question 8:** Which of the following statements is true regarding hash collisions?  
a) Collisions can be completely avoided in hash tables.  
b) Collisions are a sign of a poorly designed hash function.  
c) Collisions can be resolved using various strategies.  
d) All keys will always hash to unique indices.  
**Answer:** c) Collisions can be resolved using various strategies.

---

# Hash Function Design

## Questions

### Question 1:
Which of the following statements about the SHA-256 hash function is true?
a) It produces a 128-bit hash value.  
b) It is designed to be slow to compute.  
c) It has strong collision resistance.  
d) It is not suitable for secure applications.  
**Answer:** c) It has strong collision resistance.

### Question 2:
What is the output of the following code snippet if `x = 25`?
```python
def simple_hash(x):
    return x % 10

result = simple_hash(25)
```
a) 5  
b) 10  
c) 0  
d) 25  
**Answer:** a) 5

### Question 3:
Why is the modulo operation (hash(x) = x % 10) considered a poor choice for a hash function in many applications?
a) It is too complex to compute.  
b) It has a high likelihood of collisions.  
c) It produces a hash value that is too large.  
d) It is not a valid mathematical operation.  
**Answer:** b) It has a high likelihood of collisions.

### Question 4:
In the context of hash functions, what does "collision resistance" mean?
a) It refers to the ability to compute the hash value quickly.  
b) It means that two different inputs will always produce different hash outputs.  
c) It indicates that finding two different inputs that produce the same hash output is computationally infeasible.  
d) It describes the size of the hash output.  
**Answer:** c) It indicates that finding two different inputs that produce the same hash output is computationally infeasible.

### Question 5:
Which of the following hash functions is known for its use in blockchain technology?
a) MD5  
b) SHA-1  
c) SHA-256  
d) CRC32  
**Answer:** c) SHA-256

---

# Hash Function Example

## Questions

### Question 1:
What is the hash value of the key k = 45 when using a hash table of size m = 10?

a) 5  
b) 4  
c) 3  
d) 0  

**Answer:** a) 5

---

### Question 2:
In the given hash table example, what happens when we try to insert the key k = 33 after k = 23 has already been inserted?

a) The key 33 is placed in index 4.  
b) The key 33 is placed in index 3, causing a collision.  
c) The key 33 is ignored.  
d) The key 33 replaces the key 23.  

**Answer:** b) The key 33 is placed in index 3, causing a collision.

---

### Question 3:
If we have a hash function defined as h(k) = k mod 10, what will be the index for the key k = 57?

a) 7  
b) 5  
c) 3  
d) 0  

**Answer:** a) 7

---

### Question 4:
Given the hash table size m = 10, which of the following keys will cause a collision with the key k = 23?

a) k = 13  
b) k = 43  
c) k = 33  
d) All of the above  

**Answer:** d) All of the above

---

### Question 5:
Consider the following code snippet for a hash function:

```python
def hash_function(key):
    return key % 10

print(hash_function(27))
```
What will be the output of this code?

a) 7  
b) 8  
c) 9  
d) 0  

**Answer:** a) 7

---

### Question 6:
If a hash table uses chaining to resolve collisions, what will happen when we insert the key k = 23 and then the key k = 33?

a) Both keys will be placed in index 3, and the second will replace the first.  
b) Both keys will be placed in index 3, and the second will be ignored.  
c) Both keys will be placed in index 3, and the second will be added to a linked list at that index.  
d) Both keys will be placed in separate indices.  

**Answer:** c) Both keys will be placed in index 3, and the second will be added to a linked list at that index.

---

# Avoiding Certain Values for m

## Questions

### Question 1:
What is the potential issue with choosing m = 16 for a hash function?
a) It will always produce unique hash values.  
b) It may lead to many collisions due to clustering.  
c) It will make the hash function faster.  
d) It will use more memory than necessary.  
**Answer:** b) It may lead to many collisions due to clustering.

### Question 2:
If we have a hash table with m = 100 and our input data consists of multiples of 10, what is likely to happen?
a) There will be no collisions.  
b) The hash values will be evenly distributed.  
c) Many collisions will occur.  
d) The hash function will be inefficient.  
**Answer:** c) Many collisions will occur.

### Question 3:
Which value of m would likely provide a better distribution of hash values when dealing with multiples of 10?
a) m = 100  
b) m = 50  
c) m = 99  
d) m = 10  
**Answer:** c) m = 99

### Question 4:
Consider the following code snippet for a hash function:
```python
def hash_function(key, m):
    return key % m
```
If `m` is set to 16, what is a potential drawback of this implementation?
a) It will always return 0.  
b) It may produce a high number of collisions for certain input sets.  
c) It will not work for negative keys.  
d) It will be slower than other hash functions.  
**Answer:** b) It may produce a high number of collisions for certain input sets.

### Question 5:
Why might choosing m = 15 instead of m = 16 be beneficial in a hash function?
a) It simplifies the hash function.  
b) It avoids clustering of hash values.  
c) It reduces the number of collisions to zero.  
d) It increases the size of the hash table.  
**Answer:** b) It avoids clustering of hash values.

---

# Using Prime Numbers for m

## Questions

### Question 1:
Why is it beneficial to use a prime number for the size of a hash table?

a) It makes the hash table easier to implement.  
b) It helps in distributing hash values more evenly, reducing collisions.  
c) It allows for faster insertion of elements.  
d) It simplifies the code for hashing functions.  

**Answer:** b) It helps in distributing hash values more evenly, reducing collisions.

---

### Question 2:
Given the following code snippet, what will be the output if the hash table size is set to 50?

```python
def hash_function(key, size):
    return key % size

keys = [10, 20, 30, 40, 50]
size = 50
hash_table = [None] * size

for key in keys:
    index = hash_function(key, size)
    hash_table[index] = key

print(hash_table)
```

a) [10, 20, 30, 40, 50]  
b) [None, None, None, None, None, None, None, None, None, None, 10, 20, 30, 40, 50]  
c) [10, None, 20, None, 30, None, 40, None, 50]  
d) [10, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]  

**Answer:** b) [None, None, None, None, None, None, None, None, None, None, 10, 20, 30, 40, 50]

---

### Question 3:
If you change the hash table size to a prime number, such as 53, what is the expected outcome when hashing the same keys?

a) The keys will be distributed more evenly across the hash table.  
b) The keys will still collide at the same indices.  
c) The performance will decrease due to increased complexity.  
d) The hash table will not be able to store all keys.  

**Answer:** a) The keys will be distributed more evenly across the hash table.

---

### Question 4:
Which of the following sizes would be the best choice for a hash table to minimize collisions?

a) 100  
b) 102  
c) 97  
d) 200  

**Answer:** c) 97

---

### Question 5:
In the context of hash tables, what is a collision?

a) When two keys hash to the same index in the table.  
b) When the hash table is full.  
c) When a key is not found in the hash table.  
d) When the hash function is not working correctly.  

**Answer:** a) When two keys hash to the same index in the table.

---

# Example of Good m Value

## Questions

### Question 1:
What is the load factor (¦Ë) when storing 2,000 integers in a hash table with m = 701?

a) 1.5  
b) 2.0  
c) 2.85  
d) 3.5  

**Answer:** c) 2.85

---

### Question 2:
If a hash table has m = 701 and the expected average number of collisions is 3, what is the expected average number of entries per slot?

a) 1.0  
b) 2.0  
c) 2.85  
d) 3.0  

**Answer:** c) 2.85

---

### Question 3:
In the scenario where all numbers being hashed are multiples of 7, which of the following statements is true?

a) The choice of m = 701 guarantees no collisions.  
b) The choice of m = 701 is irrelevant if the hash function is poor.  
c) The load factor will decrease significantly.  
d) All entries will be evenly distributed across the hash table.  

**Answer:** b) The choice of m = 701 is irrelevant if the hash function is poor.

---

### Question 4:
Which of the following best describes the impact of a poorly designed hash function on a hash table with m = 701?

a) It will always result in zero collisions.  
b) It can lead to clustering and increased collisions despite a good choice of m.  
c) It will improve the load factor.  
d) It will have no effect on the performance of the hash table.  

**Answer:** b) It can lead to clustering and increased collisions despite a good choice of m.

---

### Question 5:
Given the following code snippet for a hash function, what will be the output for the input value 14?

```python
def hash_function(x, m):
    return x % m

m = 701
print(hash_function(14, m))
```

a) 0  
b) 7  
c) 14  
d) 701  

**Answer:** c) 14

---

### Question 6:
If you want to minimize collisions in a hash table, which of the following strategies is most effective?

a) Increasing the size of m without considering the hash function.  
b) Using a well-designed hash function that distributes values uniformly.  
c) Decreasing the number of entries n in the hash table.  
d) Ignoring the load factor when choosing m.  

**Answer:** b) Using a well-designed hash function that distributes values uniformly.

---

# String Keys in Hashing

## Questions

### Multiple Choice Questions on String Keys in Hashing

**Question 1:** What is the ASCII value of the character 'b'?  
a) 97  
b) 98  
c) 99  
d) 100  
**Answer:** b) 98

---

**Question 2:** If the string 'abc' is hashed by summing its ASCII values, what is the resulting hash value?  
a) 294  
b) 295  
c) 293  
d) 296  
**Answer:** a) 294

---

**Question 3:** What is the hash value for the string 'AAA' when calculated using ASCII values?  
a) 195  
b) 196  
c) 197  
d) 198  
**Answer:** a) 195

---

**Question 4:** If we use the string 'aaa', what is the resulting hash value based on its ASCII values?  
a) 291  
b) 292  
c) 293  
d) 290  
**Answer:** a) 291

---

**Question 5:** Given the following code snippet, what will be the output for the string 'abc'?

```python
def hash_string(s):
    return sum(ord(char) for char in s)

print(hash_string('abc'))
```
a) 294  
b) 295  
c) 293  
d) 296  
**Answer:** a) 294

---

**Question 6:** Which of the following statements is true regarding the strings 'AAA' and 'aaa' in the context of hashing?  
a) They produce the same hash value.  
b) They produce different hash values due to case sensitivity.  
c) The hash value for 'AAA' is greater than 'aaa'.  
d) The hash value for 'aaa' is greater than 'AAA'.  
**Answer:** b) They produce different hash values due to case sensitivity.

---

**Question 7:** If a hashing function uses the ASCII values of characters, which of the following strings will yield the highest hash value?  
a) 'abc'  
b) 'AAA'  
c) 'aaa'  
d) 'ZZZ'  
**Answer:** d) 'ZZZ' (ASCII value for 'Z' is 90, so 90 + 90 + 90 = 270)

---

**Question 8:** What is the primary reason that different cases of the same letter yield different hash values in a hashing context?  
a) Different lengths of strings  
b) Different ASCII values for uppercase and lowercase letters  
c) Different characters in the string  
d) Different encoding formats  
**Answer:** b) Different ASCII values for uppercase and lowercase letters

---

# Hash Function Limitations

## Questions

### Question 1:
What is a potential issue with using hash functions like MD5 for strings that are permutations of each other, such as 'abc' and 'acb'?

a) They always produce different hash values.  
b) They may produce the same hash value, leading to a collision.  
c) They are too slow to compute.  
d) They require too much memory.  

**Answer:** b) They may produce the same hash value, leading to a collision.

---

### Question 2:
Given the strings 'abcd' and 'abdc', which of the following statements is true if a simple checksum is used as the hash function?

a) Both strings will produce different hash values.  
b) Both strings will produce the same hash value.  
c) The hash value will depend on the length of the strings.  
d) The hash function will fail to compute the hash.  

**Answer:** b) Both strings will produce the same hash value.

---

### Question 3:
What is a collision in the context of hash functions?

a) When two different inputs produce the same hash output.  
b) When the hash function takes too long to compute.  
c) When the hash function is unable to process an input.  
d) When the hash output is longer than the input.  

**Answer:** a) When two different inputs produce the same hash output.

---

### Question 4:
Consider the following code snippet that uses a simple checksum to hash a string:

```python
def simple_checksum(s):
    return sum(ord(char) for char in s)

hash1 = simple_checksum('abcd')
hash2 = simple_checksum('abdc')
```

What will be the values of `hash1` and `hash2`?

a) hash1 = 394, hash2 = 394  
b) hash1 = 394, hash2 = 395  
c) hash1 = 395, hash2 = 394  
d) hash1 = 396, hash2 = 396  

**Answer:** a) hash1 = 394, hash2 = 394

---

### Question 5:
Which of the following hash functions is known to be more robust against collisions compared to simple checksum methods?

a) MD5  
b) SHA-1  
c) SHA-256  
d) All of the above  

**Answer:** d) All of the above

---

# Distribution Issues

## Questions

### Question 1:
What issue can arise when a hash function generates hash values based on the first few characters of string keys, such as usernames?
a) Increased memory usage  
b) Clustering of entries  
c) Faster access times  
d) Decreased collision rates  
**Answer:** b) Clustering of entries

### Question 2:
In the context of hash tables, what is a potential consequence of using a hash function that returns the key modulo 1000 when all keys are even numbers?
a) Uniform distribution of entries  
b) Increased collision rates  
c) Decreased memory usage  
d) Faster retrieval times  
**Answer:** b) Increased collision rates

### Question 3:
Given the following code snippet, what will be the output if the hash function is poorly designed and leads to clustering?
```python
def hash_function(username):
    return ord(username[0]) % 10

usernames = ['alice', 'adam', 'bob', 'charlie']
hash_table = [[] for _ in range(10)]

for username in usernames:
    index = hash_function(username)
    hash_table[index].append(username)

print(hash_table)
```
a) A balanced distribution of usernames  
b) All usernames in the same bucket  
c) Usernames spread evenly across all buckets  
d) Only 'alice' and 'adam' in one bucket  
**Answer:** b) All usernames in the same bucket

### Question 4:
What is a potential solution to avoid clustering in a hash table when using string keys?
a) Use a hash function that considers the entire string  
b) Limit the number of entries in the hash table  
c) Use only numeric keys  
d) Increase the size of the hash table  
**Answer:** a) Use a hash function that considers the entire string

### Question 5:
If a hash table is designed to store numeric keys ranging from 1 to 1000, but only even numbers are inserted, what is the likely outcome?
a) All keys will be stored in odd indices  
b) The hash table will be empty  
c) Poor distribution of entries across the hash table  
d) Increased performance due to fewer collisions  
**Answer:** c) Poor distribution of entries across the hash table

---

# Example of Key Range

## Questions

### Question 1:
In a hash table with a prime size of m = 10,007, which of the following string keys would likely hash to the same index as 'apple' if it hashes to index 1234?

a) 'grape'  
b) 'orange'  
c) 'banana'  
d) 'kiwi'  

**Answer:** a) 'grape' (assuming it hashes to the same index)

---

### Question 2:
What is the primary benefit of using a prime number as the size of a hash table?

a) It allows for faster retrieval of keys.  
b) It minimizes collisions by distributing keys uniformly.  
c) It simplifies the implementation of the hash function.  
d) It reduces the memory usage of the hash table.  

**Answer:** b) It minimizes collisions by distributing keys uniformly.

---

### Question 3:
Given the hash function \( h(k) = k \mod 10,007 \), what will be the index for the key 10,007?

a) 1  
b) 0  
c) 10,007  
d) 10,006  

**Answer:** b) 0

---

### Question 4:
If you have numeric keys ranging from 0 to 1,016 and you use the hash function \( h(k) = k \mod 10,007 \), which of the following keys will cause a collision with the key 0?

a) 1  
b) 10,007  
c) 5  
d) 1,016  

**Answer:** b) 10,007

---

### Question 5:
In the context of hash tables, what does the term "collision" refer to?

a) When two different keys hash to the same index.  
b) When a key is not found in the hash table.  
c) When the hash table is full.  
d) When the hash function is not defined.  

**Answer:** a) When two different keys hash to the same index.

---

### Question 6:
If 'banana' hashes to index 5678 in a hash table of size 10,007, which of the following keys would likely hash to a different index?

a) 'apple'  
b) 'banana'  
c) 'cherry'  
d) 'grape'  

**Answer:** d) 'grape' (assuming it hashes to a different index)

---

### Question 7:
Which of the following statements is true regarding the hash function \( h(k) = k \mod 10,007 \)?

a) It guarantees no collisions for all possible keys.  
b) It can produce the same index for different keys.  
c) It is only effective for string keys.  
d) It requires the keys to be prime numbers.  

**Answer:** b) It can produce the same index for different keys.

---

# Hash Function Method 2

## Questions

### Question 1:
What is the hash value for the key 'cat' using the given hash function?

a) 0  
b) 2  
c) 4  
d) 6  

**Answer:** c) 4

---

### Question 2:
Using the same hash function, what is the hash value for the key 'aaa'?

a) 0  
b) 2  
c) 4  
d) 6  

**Answer:** b) 2

---

### Question 3:
If we hash the key 'aab', what is the resulting hash value?

a) 0  
b) 2  
c) 4  
d) 6  

**Answer:** a) 0

---

### Question 4:
Which of the following statements best describes the sensitivity of the hash function demonstrated in the examples?

a) The hash function is not sensitive to input variations.  
b) A small change in the input can lead to a significant change in the hash value.  
c) The hash function always produces the same hash value for similar inputs.  
d) The hash function is only sensitive to the first character of the input.  

**Answer:** b) A small change in the input can lead to a significant change in the hash value.

---

### Question 5:
Given the hash function \( h(k) = (ASCII(k[0]) + 27 \cdot ASCII(k[1]) + 272 \cdot ASCII(k[2])) \mod 10 \), what will be the hash value for the key 'dog'?

a) 1  
b) 3  
c) 5  
d) 7  

**Answer:** b) 3  
*(Calculation: h('dog') = (100 + 27¡¤111 + 272¡¤103) mod 10 = (100 + 2997 + 27976) mod 10 = 30973 mod 10 = 3)*

---

### Question 6:
If the hash table size is increased to 20, what will be the new hash value for the key 'cat'?

a) 4  
b) 14  
c) 6  
d) 8  

**Answer:** a) 4  
*(The hash value remains the same since it is calculated modulo 10, and 88674 mod 20 = 14, but the original calculation gives 4.)*

--- 

### Question 7:
What is the primary purpose of a hash function in data structures?

a) To sort data  
b) To encrypt data  
c) To map data to a fixed size  
d) To compress data  

**Answer:** c) To map data to a fixed size

---

# Limitations of Method 2

## Questions

### Question 1:
What is the primary limitation of using a simple hashing function based on the first three letters of English words?

a) It can only hash words with unique letters.  
b) It leads to a high likelihood of collisions due to limited combinations.  
c) It requires a very large hash table to function effectively.  
d) It can only hash words that are longer than three letters.  

**Answer:** b) It leads to a high likelihood of collisions due to limited combinations.

---

### Question 2:
Given the words 'cat' and 'bat', what issue arises when using a simple hashing function based on their ASCII values?

a) Both words will have unique hash values.  
b) They may hash to the same index, causing a collision.  
c) The hash values will be too large to store.  
d) The hashing function will fail to process these words.  

**Answer:** b) They may hash to the same index, causing a collision.

---

### Question 3:
If a hash table has a size of 10,007 and only 2,851 unique combinations of the first three letters in English, what percentage of the table is effectively utilized?

a) 50%  
b) 28%  
c) 75%  
d) 10%  

**Answer:** b) 28%

---

### Question 4:
Consider the following code snippet that hashes a word by summing the ASCII values of its first three letters:

```python
def simple_hash(word):
    return sum(ord(char) for char in word[:3]) % 10007
```

What will be the output of `simple_hash('cat')`?

a) 312  
b) 99  
c) 97  
d) 10007  

**Answer:** a) 312 (ASCII values: c=99, a=97, t=116; sum = 312)

---

### Question 5:
Why is it problematic to use a hash function that only considers the first three letters of a word?

a) It makes the hash function too complex.  
b) It limits the number of unique hash values, increasing the chance of collisions.  
c) It requires more memory than necessary.  
d) It can only hash words that start with a vowel.  

**Answer:** b) It limits the number of unique hash values, increasing the chance of collisions.

---

# Hash Function Method 3

## Questions

### Multiple Choice Questions on Hash Function Method

**Question 1:** What is the hash value for the key 'abc' when using the provided hash function with modulo m = 1000?  
a) 698  
b) 999  
c) 132973  
d) 136698  
**Answer:** a) 698

---

**Question 2:** In the hash function example for the key 'aaa', what is the weighted sum for the second character (i = 1)?  
a) 1369 * 97  
b) 37 * 97  
c) 1 * 97  
d) 37^1 * 98  
**Answer:** b) 37 * 97

---

**Question 3:** What is the final hash value for the key 'aaa' after applying modulo m = 1000?  
a) 136669  
b) 669  
c) 97  
d) 3599  
**Answer:** b) 669

---

**Question 4:** Which of the following statements is true regarding the hash function used for the keys 'abc' and 'aaa'?  
a) Both keys will produce the same hash value.  
b) The hash value for 'abc' is greater than that for 'aaa'.  
c) The hash value for 'aaa' is greater than that for 'abc'.  
d) The hash function does not depend on the position of characters.  
**Answer:** b) The hash value for 'abc' is greater than that for 'aaa'.

---

**Question 5:** If the ASCII value for 'a' is 97, what is the contribution of the first character in the key 'abc' to the weighted sum?  
a) 132973  
b) 3626  
c) 99  
d) 1369  
**Answer:** a) 132973

---

**Question 6:** What is the purpose of applying modulo m in the hash function?  
a) To increase the hash value.  
b) To ensure the hash value fits within a specific range.  
c) To make the hash function deterministic.  
d) To reduce the computational complexity.  
**Answer:** b) To ensure the hash value fits within a specific range.

---

**Question 7:** In the context of the hash function, what does the term "weighted sum" refer to?  
a) The total ASCII values of the characters in the key.  
b) The sum of contributions from each character based on its position.  
c) The average of the ASCII values of the characters.  
d) The sum of the hash values of all characters.  
**Answer:** b) The sum of contributions from each character based on its position.

---

**Question 8:** If the key is changed from 'abc' to 'acb', how would the hash value change?  
a) It would remain the same.  
b) It would increase.  
c) It would decrease.  
d) It would depend on the ASCII values of the characters.  
**Answer:** b) It would increase or decrease depending on the position of 'b'. 

--- 

These questions assess the understanding of the hash function method and its application to different keys.

---

# Expected Distribution of Method 3

## Questions

### Question 1:
What is the primary goal of Method 3 in a hash table designed to store user IDs?  
a) To maximize the number of entries in each index  
b) To uniformly distribute user IDs across the table  
c) To minimize the size of the hash table  
d) To ensure all user IDs are stored in the same index  

**Answer:** b) To uniformly distribute user IDs across the table

---

### Question 2:
In the context of Method 3, what is a potential issue when hashing usernames that are not uniformly distributed?  
a) Increased memory usage  
b) Decreased retrieval speed  
c) Clustering of hash values leading to collisions  
d) Inability to store any usernames  

**Answer:** c) Clustering of hash values leading to collisions

---

### Question 3:
Given the following code snippet that implements a simple hash function for usernames, what is the potential problem with the output for similar usernames?

```python
def hash_username(username):
    return sum(ord(char) for char in username) % 10

print(hash_username("john"))   # Output: ?
print(hash_username("john1"))  # Output: ?
print(hash_username("john2"))  # Output: ?
```

a) All usernames will produce the same hash value  
b) The hash function will always return 0  
c) The hash values may collide for similar usernames  
d) The hash function is too complex  

**Answer:** c) The hash values may collide for similar usernames

---

### Question 4:
If Method 3 is applied to user IDs ranging from 1 to 1000, what is the expected outcome regarding the distribution of hash values?  
a) Most user IDs will map to the same index  
b) Each index will have a large number of entries  
c) Hash values will be distributed such that no index has more than a few entries  
d) The hash values will be random and unpredictable  

**Answer:** c) Hash values will be distributed such that no index has more than a few entries

---

### Question 5:
Which of the following scenarios best illustrates the effectiveness of Method 3 in a hash table?  
a) A hash table where all entries are stored at index 0  
b) A hash table where user IDs are evenly spread across all available indices  
c) A hash table that only stores even user IDs  
d) A hash table that uses a fixed index for all user IDs  

**Answer:** b) A hash table where user IDs are evenly spread across all available indices

---

# Separate Chaining

## Questions

### Multiple Choice Questions on Separate Chaining

**Question 1:** In a hash table of size 5, if we insert the keys 10, 15, 20, and 25 using the hash function `key % 5`, what will be the structure at index 0 after all insertions?  
a) 10  
b) 10 -> 15 -> 20 -> 25  
c) 15 -> 10 -> 20 -> 25  
d) 25 -> 20 -> 15 -> 10  
**Answer:** b) 10 -> 15 -> 20 -> 25

---

**Question 2:** What is the main advantage of using separate chaining in a hash table?  
a) It allows for faster retrieval of keys.  
b) It can handle collisions by storing multiple keys at the same index.  
c) It requires less memory than open addressing.  
d) It guarantees that all keys will be stored in a sorted order.  
**Answer:** b) It can handle collisions by storing multiple keys at the same index.

---

**Question 3:** Given a hash table of size 3 and the keys 3, 6, and 9, what will be the linked list at index 0 after inserting all keys using the hash function `key % 3`?  
a) 3  
b) 3 -> 6 -> 9  
c) 9 -> 6 -> 3  
d) 6 -> 3 -> 9  
**Answer:** b) 3 -> 6 -> 9

---

**Question 4:** When retrieving the key 6 from the linked list at index 0 in the previous example, what is the worst-case time complexity?  
a) O(1)  
b) O(log n)  
c) O(n)  
d) O(n log n)  
**Answer:** c) O(n)

---

**Question 5:** If a hash table uses separate chaining and the load factor (number of keys / number of buckets) is high, what is a potential consequence?  
a) Increased memory usage  
b) Faster retrieval times  
c) Increased likelihood of collisions  
d) Decreased number of linked lists  
**Answer:** c) Increased likelihood of collisions

---

**Question 6:** Consider the following code snippet for inserting a key into a hash table using separate chaining. What will happen if the key already exists in the linked list at the computed index?

```python
def insert(hash_table, key):
    index = key % len(hash_table)
    if hash_table[index] is None:
        hash_table[index] = LinkedList()
    hash_table[index].add(key)
```

a) The key will be added again, resulting in duplicates.  
b) The key will be ignored, preventing duplicates.  
c) An error will be raised.  
d) The key will replace the existing key.  
**Answer:** a) The key will be added again, resulting in duplicates.

---

**Question 7:** Which of the following statements about separate chaining is true?  
a) It is always more efficient than open addressing.  
b) It can lead to longer search times if many keys collide.  
c) It requires a fixed size for the linked lists.  
d) It eliminates the need for a hash function.  
**Answer:** b) It can lead to longer search times if many keys collide.

---

# Hash Function

## Questions

### Question 1:
What is the result of the hash function h(k) = k mod 10 when k = 45?

a) 5  
b) 4  
c) 0  
d) 9  

**Answer:** a) 5

---

### Question 2:
If we have a hash table of size 10 and we want to store the keys 15 and 25 using the hash function h(k) = k mod 10, what will happen?

a) Both keys will be stored at index 5 without any issues.  
b) Both keys will cause a collision at index 5.  
c) Only key 15 will be stored, and key 25 will be ignored.  
d) Both keys will be stored at different indices.  

**Answer:** b) Both keys will cause a collision at index 5.

---

### Question 3:
Which of the following is a common method for resolving collisions in a hash table?

a) Linear regression  
b) Chaining  
c) Binary search  
d) Quick sort  

**Answer:** b) Chaining

---

### Question 4:
Consider the following code snippet for a hash function:

```python
def hash_function(k):
    return k % 10

index = hash_function(32)
```
What will be the value of `index` after executing the code?

a) 2  
b) 3  
c) 0  
d) 5  

**Answer:** b) 2

---

### Question 5:
If a hash table uses open addressing for collision resolution, what happens when a collision occurs?

a) The new key is simply ignored.  
b) The new key is stored in a linked list at the same index.  
c) The algorithm searches for the next available index in the table.  
d) The existing key is removed from the table.  

**Answer:** c) The algorithm searches for the next available index in the table.

---

# Insertion in Separate Chaining

## Questions

### Question 1:
What is the result of the hash function h(k) = k % table_size when k = 25 and table_size = 10?
a) 2  
b) 5  
c) 0  
d) 25  

**Answer:** b) 5

---

### Question 2:
When inserting the key 15 into the hash table, what will the linked list at index 5 look like after the insertion?
a) (25 -> NULL)  
b) (15 -> NULL)  
c) (15 -> 25 -> NULL)  
d) (25 -> 15 -> NULL)  

**Answer:** c) (15 -> 25 -> NULL)

---

### Question 3:
In a hash table using separate chaining, what happens if two keys hash to the same index?
a) The second key is discarded.  
b) The second key is added to the end of the linked list.  
c) The second key overwrites the first key.  
d) The hash table is resized.  

**Answer:** b) The second key is added to the end of the linked list.

---

### Question 4:
Given the following code snippet, what will be the output if we insert the keys 25 and 15 into the hash table?

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        index = key % self.size
        self.table[index].insert(0, key)

hash_table = HashTable(10)
hash_table.insert(25)
hash_table.insert(15)
print(hash_table.table)
```

a) [ , , , , , [25], , , , , ]  
b) [ , , , , , [15, 25], , , , , ]  
c) [ , , , , , [25, 15], , , , , ]  
d) [ , , , , , [15], , , , , ]  

**Answer:** b) [ , , , , , [15, 25], , , , , ]

---

### Question 5:
What is the primary advantage of using separate chaining in a hash table?
a) It allows for faster lookups.  
b) It prevents collisions entirely.  
c) It allows multiple keys to be stored at the same index.  
d) It reduces memory usage.  

**Answer:** c) It allows multiple keys to be stored at the same index.

---

# Deletion in Separate Chaining

## Questions

### Question 1:
What is the hash function used in the examples provided for the hash table?
a) h(k) = k + 10  
b) h(k) = k * 10  
c) h(k) = k % 10  
d) h(k) = k - 10  
**Answer:** c) h(k) = k % 10

### Question 2:
If we want to delete the key 23 from the hash table, what is the first step we take?
a) Remove the key from the linked list  
b) Compute h(23)  
c) Traverse the entire hash table  
d) Check if the key exists in the hash table  
**Answer:** b) Compute h(23)

### Question 3:
After deleting the key 23 from the linked list at index 3, what will the updated list look like?
a) [23, 33]  
b) [13, 23]  
c) [13, 33]  
d) [20, 30, 40]  
**Answer:** c) [13, 33]

### Question 4:
In the tricky example, what is the result of deleting the key 30 from the linked list at index 0?
a) [20, 30, 40]  
b) [20, 40]  
c) [30, 40]  
d) [20]  
**Answer:** b) [20, 40]

### Question 5:
What is the main challenge when deleting a key that is in the middle of a linked list in a hash table?
a) Finding the key  
b) Adjusting the pointers correctly  
c) Traversing the entire list  
d) Rehashing the table  
**Answer:** b) Adjusting the pointers correctly

### Question 6:
Given the hash table size of 10, what index will the key 40 be hashed to using the function h(k) = k % 10?
a) 0  
b) 4  
c) 5  
d) 10  
**Answer:** b) 0

### Question 7:
If the linked list at index 0 contains [20, 30, 40], what will the linked list look like after deleting the key 20?
a) [30, 40]  
b) [20, 40]  
c) [20, 30]  
d) [40]  
**Answer:** a) [30, 40]

---

# Separate Chaining

## Questions

### Question 1:
What is the primary purpose of separate chaining in a hash table?
a) To increase the size of the hash table  
b) To handle collisions by storing multiple elements at the same index  
c) To improve the speed of the hash function  
d) To sort the elements in the hash table  

**Answer:** b) To handle collisions by storing multiple elements at the same index

---

### Question 2:
Given a hash table of size 10 and the keys 15, 25, and 35, what will be the contents of the linked list at index 5 after inserting these keys?
a) 15 -> 25 -> 35  
b) 25 -> 15 -> 35  
c) 35 -> 25 -> 15  
d) 15 -> 35 -> 25  

**Answer:** a) 15 -> 25 -> 35

---

### Question 3:
If a hash table has a load factor that is low, what is the expected time complexity for searching for a key using separate chaining?
a) O(n)  
b) O(log n)  
c) O(1)  
d) O(n^2)  

**Answer:** c) O(1)

---

### Question 4:
In the tricky example, if we want to delete the key 6 from the linked list at index 1, what will the linked list look like after the deletion?
a) 1 -> 6 -> 11 -> 16  
b) 1 -> 11 -> 16  
c) 6 -> 11 -> 16  
d) 1 -> 16  

**Answer:** b) 1 -> 11 -> 16

---

### Question 5:
Consider the following code snippet for inserting a key into a hash table using separate chaining. What will happen if the key 6 is inserted after the keys 1, 11, and 16?

```python
hash_table = [[] for _ in range(5)]
keys = [1, 11, 16]
for key in keys:
    index = key % 5
    hash_table[index].append(key)
hash_table[1].append(6)
```

What will be the contents of the linked list at index 1 after inserting the key 6?
a) [1, 6, 11, 16]  
b) [6, 1, 11, 16]  
c) [1, 11, 16, 6]  
d) [1, 11, 16]  

**Answer:** a) [1, 11, 16, 6]

---

### Question 6:
What is the worst-case time complexity for searching for a key in a hash table using separate chaining when many keys hash to the same index?
a) O(1)  
b) O(log n)  
c) O(n)  
d) O(n log n)  

**Answer:** c) O(n)

---

# Advantages of Separate Chaining

## Questions

### Question 1:
What is the primary advantage of using separate chaining in a hash table?
a) It allows for faster access times.  
b) It can handle collisions by storing multiple entries in a linked list.  
c) It requires less memory than open addressing.  
d) It simplifies the hash function.  
**Answer:** b) It can handle collisions by storing multiple entries in a linked list.

### Question 2:
In a hash table using separate chaining, if you have a bucket containing the linked list: ["apple" -> "banana" -> "cherry"], what will the list look like after deleting "banana"?
a) ["apple" -> "banana" -> "cherry"]  
b) ["apple" -> "cherry"]  
c) ["banana" -> "cherry"]  
d) ["apple" -> "banana"]  
**Answer:** b) ["apple" -> "cherry"]  

### Question 3:
When deleting an entry from a linked list in a hash table, what must you do if you want to delete a node that is not the head of the list?
a) Simply remove the node without any additional steps.  
b) Traverse the list to find the node before it and update its pointer.  
c) Delete the entire linked list.  
d) Change the hash function.  
**Answer:** b) Traverse the list to find the node before it and update its pointer.

### Question 4:
Given the linked list in a bucket: ["dog" -> "cat" -> "fish"], what is the correct procedure to delete "cat"?
a) Remove "cat" directly without any traversal.  
b) Adjust the head of the list to point to "fish".  
c) Traverse the list to find "cat" and update the pointer of the previous node.  
d) Delete the entire bucket.  
**Answer:** c) Traverse the list to find "cat" and update the pointer of the previous node.

### Question 5:
What could happen if you forget to update the previous node's pointer when deleting a node from a linked list in a hash table?
a) The hash table will become empty.  
b) The linked list will become broken, leading to potential memory leaks.  
c) The hash table will automatically fix itself.  
d) The deletion will be successful without any issues.  
**Answer:** b) The linked list will become broken, leading to potential memory leaks.

---

# Disadvantages of Separate Chaining

## Questions

### Question 1:
What is a primary disadvantage of using separate chaining in a hash table?

a) It requires more memory than open addressing.  
b) It can lead to fragmentation due to frequent memory allocations and de-allocations.  
c) It does not handle collisions effectively.  
d) It is slower than using a binary search tree.  

**Answer:** b) It can lead to fragmentation due to frequent memory allocations and de-allocations.

---

### Question 2:
In a hash table using separate chaining, what does each bucket typically contain?

a) An array of entries.  
b) A single entry.  
c) A linked list of entries.  
d) A binary tree of entries.  

**Answer:** c) A linked list of entries.

---

### Question 3:
Consider the following code snippet for inserting an entry into a hash table using separate chaining:

```python
def insert(hash_table, key, value):
    index = hash_function(key) % len(hash_table)
    new_node = Node(key, value)
    hash_table[index].append(new_node)
```

What potential issue could arise from this implementation if many entries are added and removed frequently?

a) The hash function may become inefficient.  
b) The linked lists in each bucket may grow and shrink rapidly, leading to memory fragmentation.  
c) The hash table will automatically resize itself.  
d) The code will throw an error due to the use of `append`.  

**Answer:** b) The linked lists in each bucket may grow and shrink rapidly, leading to memory fragmentation.

---

### Question 4:
In a web application using a hash table with separate chaining to store user sessions, what is a potential performance issue that could occur?

a) The hash table will not be able to store all user sessions.  
b) Searching for a specific session can take longer than expected if the linked lists become very long due to collisions.  
c) The application will crash if too many users log in at once.  
d) The hash table will automatically delete old sessions.  

**Answer:** b) Searching for a specific session can take longer than expected if the linked lists become very long due to collisions.

---

### Question 5:
Which of the following statements is true regarding the performance of a hash table using separate chaining?

a) It guarantees O(1) time complexity for all operations.  
b) Performance can degrade to O(n) in the worst case if many collisions occur.  
c) It is always faster than open addressing.  
d) It does not require any additional memory for linked lists.  

**Answer:** b) Performance can degrade to O(n) in the worst case if many collisions occur.

---

# Open Addressing

## Questions

### Question 1:
What is the primary purpose of open addressing in hash tables?
a) To store keys in a sorted order  
b) To resolve collisions by finding the next available index  
c) To increase the size of the hash table dynamically  
d) To encrypt the keys before storing them  
**Answer:** b) To resolve collisions by finding the next available index

### Question 2:
Given a hash table of size 10 and a hash function `hash(key) = key % 10`, what will be the final state of the hash table after inserting the keys 12, 22, and 32 using open addressing?
a) [ , , 12, 22, 32, , , , , ]  
b) [12, 22, 32, , , , , , , ]  
c) [ , , 12, , 22, 32, , , , ]  
d) [ , , , , 12, 22, 32, , , ]  
**Answer:** a) [ , , 12, 22, 32, , , , , ]

### Question 3:
In the tricky example with a hash table of size 5, what happens when you try to insert the key 20 after inserting keys 5, 10, and 15?
a) It will be placed at index 0  
b) It will be placed at index 1  
c) It will be placed at index 2  
d) It will be placed at index 3  
**Answer:** d) It will be placed at index 3

### Question 4:
What issue can arise when using open addressing with a poor hash function and a larger set of keys?
a) Increased memory usage  
b) Clustering, leading to longer search times  
c) Data loss  
d) Automatic resizing of the hash table  
**Answer:** b) Clustering, leading to longer search times

### Question 5:
Consider the following code snippet for inserting a key into a hash table using open addressing. What will be the output if the key 25 is inserted into the table `[5, 10, 15, , , , , , , ]` with a hash function `hash(key) = key % 5`?
```python
def insert_key(table, key):
    index = key % len(table)
    while table[index] is not None:
        index = (index + 1) % len(table)
    table[index] = key

hash_table = [5, 10, 15, None, None]
insert_key(hash_table, 25)
print(hash_table)
```
a) [5, 10, 15, 25, None]  
b) [5, 10, 15, None, 25]  
c) [25, 10, 15, None, None]  
d) [5, 10, 15, None, None]  
**Answer:** b) [5, 10, 15, None, 25]

---

# Collision Handling in Open Addressing

## Questions

### Question 1:
In a hash table using linear probing, if the key '42' hashes to index 5 and both index 5 and index 6 are occupied, which index will be checked next for insertion?

a) 4  
b) 7  
c) 8  
d) 6  

**Answer:** b) 7

---

### Question 2:
When using quadratic probing for collision handling, if the key '15' hashes to index 3 and index 3 is occupied, which index will be checked first after index 3?

a) 4  
b) 5  
c) 6  
d) 7  

**Answer:** a) 4

---

### Question 3:
In the context of collision handling in hash tables, what is the main disadvantage of using linear probing?

a) It requires more memory.  
b) It can lead to clustering of keys.  
c) It is slower than chaining.  
d) It cannot handle collisions.  

**Answer:** b) It can lead to clustering of keys.

---

### Question 4:
Consider the following code snippet for inserting a key into a hash table using quadratic probing:

```python
def insert_key(hash_table, key):
    index = hash_function(key)
    i = 0
    while hash_table[index] is not None:
        i += 1
        index = (index + i**2) % len(hash_table)
    hash_table[index] = key
```

If the key '27' hashes to index 3 and index 3 is occupied, which index will be checked after the first iteration?

a) 4  
b) 5  
c) 6  
d) 7  

**Answer:** a) 4

---

### Question 5:
What could happen if a hash table using quadratic probing does not handle collisions properly?

a) It will always find an empty slot.  
b) It may lead to an infinite loop.  
c) It will automatically resize the table.  
d) It will lose all previously stored keys.  

**Answer:** b) It may lead to an infinite loop.

---

# Hash Function Example

## Questions

### Multiple Choice Questions on Hash Functions

**Question 1:** What is the result of the hash function `hash(k) = k mod 10` when the key is 45?  
a) 4  
b) 5  
c) 0  
d) 9  
**Answer:** b) 5

---

**Question 2:** If we have the keys 15 and 25, what will be the indices they hash to using the function `hash(k) = k mod 10`?  
a) Both hash to 5  
b) Both hash to 0  
c) 5 and 0  
d) 5 and 1  
**Answer:** a) Both hash to 5

---

**Question 3:** Which of the following strategies can be used to resolve collisions in a hash table?  
a) Chaining  
b) Open addressing  
c) Both a and b  
d) None of the above  
**Answer:** c) Both a and b

---

**Question 4:** Given the following code snippet, what will be the output when `key` is set to 32?  
```python
def hash_function(k):
    return k % 10

key = 32
index = hash_function(key)
print(index)
```
a) 2  
b) 3  
c) 0  
d) 4  
**Answer:** b) 2

---

**Question 5:** If a hash table uses the function `hash(k) = k mod 10`, which of the following keys will cause a collision with the key 12?  
a) 22  
b) 32  
c) 42  
d) All of the above  
**Answer:** d) All of the above

---

**Question 6:** What is the primary purpose of a hash function in data structures?  
a) To sort data  
b) To encrypt data  
c) To map data to a fixed-size table  
d) To compress data  
**Answer:** c) To map data to a fixed-size table

---

**Question 7:** In the context of hash tables, what does the term "load factor" refer to?  
a) The number of keys stored in the hash table  
b) The ratio of the number of stored keys to the size of the hash table  
c) The maximum number of collisions allowed  
d) The time complexity of the hash function  
**Answer:** b) The ratio of the number of stored keys to the size of the hash table

---

**Question 8:** If a hash table has a size of 10 and the load factor exceeds 0.7, what action is typically taken?  
a) Increase the size of the hash table  
b) Decrease the size of the hash table  
c) Stop inserting new keys  
d) Change the hash function  
**Answer:** a) Increase the size of the hash table

--- 

These questions cover various aspects of hash functions, including their implementation, collision resolution strategies, and related concepts.

---

# Open Addressing

## Questions

### Question 1:
What is the initial index for the key 22 when using the hash function `key % 10`?
a) 0  
b) 2  
c) 3  
d) 5  
**Answer:** b) 2

### Question 2:
In the final hash table after inserting keys 12, 22, and 32, what value is stored at index 4?
a) 12  
b) 22  
c) 32  
d) -  
**Answer:** d) -

### Question 3:
When inserting the key 10 into the hash table of size 5, which index does it check first?
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** a) 0

### Question 4:
After inserting keys 5, 10, and 15 into a hash table of size 5, what is the value at index 1?
a) 5  
b) 10  
c) 15  
d) -  
**Answer:** b) 10

### Question 5:
Given the following code snippet, what will be the output after inserting keys 12, 22, and 32 into the hash table?

```python
hash_table = [-1] * 10
keys = [12, 22, 32]
for key in keys:
    index = key % 10
    while hash_table[index] != -1:
        index += 1
    hash_table[index] = key
print(hash_table)
```
a) [-1, -1, 12, 22, 32, -1, -1, -1, -1, -1]  
b) [-1, -1, 12, 32, 22, -1, -1, -1, -1, -1]  
c) [12, 22, 32, -1, -1, -1, -1, -1, -1, -1]  
d) [12, -1, -1, 22, 32, -1, -1, -1, -1, -1]  
**Answer:** a) [-1, -1, 12, 22, 32, -1, -1, -1, -1, -1]

### Question 6:
In the tricky example, what is the final state of the hash table after inserting keys 5, 10, and 15?
a) [5, 10, 15, -1, -1]  
b) [5, -1, -1, -1, -1]  
c) [5, 10, -1, -1, -1]  
d) [5, 10, 15, -1, -1]  
**Answer:** a) [5, 10, 15, -1, -1]

---

# Collision Resolution Strategies

## Questions

### Questions on Collision Resolution Strategies

**Question 1:** In linear probing, if a hash table has a size of 10 and the key 'X' hashes to index 5, but that index is occupied, which index will be checked next?  
a) 4  
b) 6  
c) 7  
d) 5  
**Answer:** b) 6

---

**Question 2:** In quadratic probing, if the key 'Y' hashes to index 1 in a hash table of size 10, and that index is occupied, which index will be checked first?  
a) 2  
b) 3  
c) 4  
d) 5  
**Answer:** b) 2 (1 + 1^2)

---

**Question 3:** Given the following code snippet for quadratic probing, what will be the next index checked if the initial hash index is 3 and the probing attempt is the second one?

```python
hash_index = 3
attempt = 2
next_index = (hash_index + attempt**2) % 10
```
a) 4  
b) 5  
c) 6  
d) 7  
**Answer:** b) 7 (3 + 2^2 = 7)

---

**Question 4:** If a hash table of size 10 uses linear probing and the keys 'A', 'B', and 'C' hash to indices 2, 2, and 2 respectively, where will 'C' be placed?  
a) 2  
b) 3  
c) 4  
d) 5  
**Answer:** b) 3

---

**Question 5:** In a hash table of size 10, if the key 'D' hashes to index 4 and is occupied, and the next key 'E' hashes to index 4 as well, which index will 'E' be placed in using linear probing?  
a) 4  
b) 5  
c) 6  
d) 7  
**Answer:** b) 5

---

**Question 6:** In quadratic probing, if the key 'F' hashes to index 0 and that index is occupied, what will be the third index checked?  
a) 1  
b) 4  
c) 9  
d) 6  
**Answer:** c) 9 (0 + 3^2 = 9)

---

**Question 7:** If a hash table of size 10 uses quadratic probing and the key 'G' hashes to index 7, but that index is occupied, which index will be checked after the first attempt?  
a) 8  
b) 9  
c) 0  
d) 1  
**Answer:** c) 0 (7 + 1^2 = 8, then 7 + 2^2 = 11 % 10 = 1)

---

**Question 8:** Which of the following statements is true regarding linear probing?  
a) It can lead to clustering of keys.  
b) It guarantees a constant time complexity for all operations.  
c) It uses a secondary hash function to resolve collisions.  
d) It is the most efficient method for all types of data.  
**Answer:** a) It can lead to clustering of keys.

---

# Basic Strategy of Open Addressing

## Questions

### Multiple Choice Questions on Open Addressing in Hash Tables

**Question 1:** What is the hash index for the key 22 when using a hash table of size 10 with the hash function `key % table_size`?  
a) 0  
b) 2  
c) 3  
d) 4  
**Answer:** b) 2

---

**Question 2:** After inserting the keys 12, 22, and 32 into a hash table of size 10, what will be the contents of index 4?  
a) 12  
b) 22  
c) 32  
d) Empty  
**Answer:** c) 32

---

**Question 3:** In the tricky example with a hash table of size 5, what will be the contents of index 1 after inserting the keys 5, 10, and 15?  
a) 5  
b) 10  
c) 15  
d) Empty  
**Answer:** b) 10

---

**Question 4:** If we attempt to insert the key 20 into the hash table of size 5 after inserting 5, 10, and 15, which index will it be inserted into?  
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** d) 3

---

**Question 5:** Given the following code snippet, what will be the output when inserting the key 22 into the hash table?

```python
table_size = 10
hash_table = [None] * table_size
hash_table[2] = 12  # Inserting 12 at index 2
hash_index = 22 % table_size
if hash_table[hash_index] is not None:
    hash_index += 1  # Probing to the next index
hash_table[hash_index] = 22
print(hash_table)
```

a) [None, None, 12, 22, None, None, None, None, None, None]  
b) [None, None, 12, None, 22, None, None, None, None, None]  
c) [None, None, None, 12, 22, None, None, None, None, None]  
d) [None, None, 12, None, None, 22, None, None, None, None]  
**Answer:** a) [None, None, 12, 22, None, None, None, None, None, None]

---

**Question 6:** What will happen if we try to insert the key 15 into the hash table of size 5 after inserting 5 and 10?  
a) It will be inserted at index 0  
b) It will be inserted at index 1  
c) It will be inserted at index 2  
d) It will cause a collision and not be inserted  
**Answer:** c) It will be inserted at index 2

---

**Question 7:** In the context of open addressing, what does "probing" refer to?  
a) The process of calculating the hash index  
b) The method of searching for an empty slot in the hash table  
c) The technique of resizing the hash table  
d) The act of deleting an entry from the hash table  
**Answer:** b) The method of searching for an empty slot in the hash table

---

**Question 8:** If a hash table of size 10 is full and we try to insert a new key, what will happen?  
a) The key will be inserted at the first index  
b) The key will replace an existing key  
c) The insertion will fail  
d) The hash table will automatically resize  
**Answer:** c) The insertion will fail

---

# Probing Function

## Questions

### Multiple Choice Questions

**Question 1:** What is the initial position of the key 22 when using the hash function `hash(k) = k mod 10`?  
a) 0  
b) 2  
c) 3  
d) 4  
**Answer:** b) 2  

---

**Question 2:** In the first example, after inserting the key 12, what is the value of `i` for the insertion of the key 22?  
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** b) 1  

---

**Question 3:** What is the final index of the key 32 in the hash table after all insertions in the first example?  
a) 2  
b) 3  
c) 4  
d) 5  
**Answer:** c) 4  

---

**Question 4:** In the tricky example, what is the probing function defined as for the second example?  
a) f(i) = i  
b) f(i) = 2i  
c) f(i) = i^2  
d) f(i) = 3i  
**Answer:** b) f(i) = 2i  

---

**Question 5:** After inserting the key 11 in the tricky example, what is the final state of the hash table?  
a) Index 0: 1, Index 1: 6, Index 2: 11, Index 3: -, Index 4: -  
b) Index 0: 11, Index 1: 1, Index 2: -, Index 3: 6, Index 4: -  
c) Index 0: -, Index 1: 1, Index 2: 6, Index 3: 11, Index 4: -  
d) Index 0: 1, Index 1: -, Index 2: 6, Index 3: 11, Index 4: -  
**Answer:** b) Index 0: 11, Index 1: 1, Index 2: -, Index 3: 6, Index 4: -  

---

**Question 6:** If we were to insert the key 6 in the first example using the same hash function, what would be the index after resolving the collision?  
a) 2  
b) 3  
c) 4  
d) 5  
**Answer:** b) 3  

---

**Question 7:** What is the value of `f(2)` in the tricky example?  
a) 1  
b) 2  
c) 4  
d) 6  
**Answer:** c) 4  

---

**Question 8:** In the first example, how many collisions occur when inserting the keys 22 and 32?  
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** c) 2  

---

**Question 9:** What is the purpose of the probing function `f(i)` in the context of hash tables?  
a) To calculate the hash value  
b) To resolve collisions  
c) To determine the size of the hash table  
d) To insert keys in sorted order  
**Answer:** b) To resolve collisions  

---

**Question 10:** If the hash table size is increased to 20, what would be the new index for the key 22 using the original hash function?  
a) 2  
b) 12  
c) 22  
d) 32  
**Answer:** a) 2  

---

# Linear Probing

## Questions

### Question 1:
What is the result of inserting the key 12 into a hash table of size 10 using the hash function `Hash(key) = key % 10`?

a) 0  
b) 1  
c) 2  
d) 3  

**Answer:** c) 2

---

### Question 2:
After inserting the keys 12 and 22 into a hash table of size 10, what will be the value at index 3?

a) 12  
b) 22  
c) 32  
d) -  

**Answer:** b) 22

---

### Question 3:
In the tricky example, what will be the value at index 2 after inserting the keys 5, 10, and 15 into a hash table of size 5?

a) 5  
b) 10  
c) 15  
d) -  

**Answer:** c) 15

---

### Question 4:
If we attempt to insert the key 22 into a hash table of size 10 after inserting the key 12, which index will be checked first?

a) 0  
b) 1  
c) 2  
d) 3  

**Answer:** c) 2

---

### Question 5:
Given the following code snippet, what will be the output after inserting the keys 5, 10, and 15 into a hash table of size 5?

```python
hash_table = [-1] * 5
keys = [5, 10, 15]

for key in keys:
    index = key % 5
    while hash_table[index] != -1:
        index = (index + 1) % 5
    hash_table[index] = key

print(hash_table)
```

a) [5, 10, 15, -1, -1]  
b) [15, -1, -1, -1, 5]  
c) [5, 10, -1, -1, 15]  
d) [5, 10, 15, -1, -1]  

**Answer:** d) [5, 10, 15, -1, -1]

---

### Question 6:
What is the final state of the hash table after inserting the keys 12, 22, and 32 into a hash table of size 10?

a) [-, -, 12, 22, 32, -, -, -, -, -]  
b) [-, -, 12, 22, -, 32, -, -, -, -]  
c) [-, -, -, -, 12, 22, 32, -, -, -]  
d) [12, 22, 32, -, -, -, -, -, -, -]  

**Answer:** a) [-, -, 12, 22, 32, -, -, -, -, -]

---

# Hash Function

## Questions

### Questions on Hash Functions

1. **Question:** What is the result of the hash function `hash(k) = k mod 10` when hashing the key 45?  
   a) 4  
   b) 5  
   c) 6  
   d) 7  
   **Answer:** b) 5

2. **Question:** If we use the hash function `hash(k) = k mod 10`, what will be the index for the key 33?  
   a) 2  
   b) 3  
   c) 4  
   d) 5  
   **Answer:** b) 3

3. **Question:** Given the hash function `hash(k) = k mod 10`, which of the following keys will cause a collision when hashed?  
   a) 12  
   b) 22  
   c) 32  
   d) All of the above  
   **Answer:** d) All of the above

4. **Question:** In a hash table using the function `hash(k) = k mod 10`, what is the index for the key 50?  
   a) 0  
   b) 1  
   c) 5  
   d) 10  
   **Answer:** a) 0

5. **Question:** If we have the following keys: 15, 25, and 35, what will be the hash values using the function `hash(k) = k mod 10`?  
   a) 5, 5, 5  
   b) 5, 5, 0  
   c) 5, 0, 5  
   d) 5, 0, 0  
   **Answer:** a) 5, 5, 5

6. **Question:** Which of the following statements is true regarding the hash function `hash(k) = k mod 10`?  
   a) It guarantees no collisions for any input.  
   b) It can produce the same hash value for different keys.  
   c) It is a perfect hash function.  
   d) It can only hash positive integers.  
   **Answer:** b) It can produce the same hash value for different keys.

7. **Question:** Consider the following code snippet that uses a hash function. What will be the output for `hash(27)`?  
   ```python
   def hash(k):
       return k % 10

   print(hash(27))
   ```  
   a) 7  
   b) 27  
   c) 10  
   d) 0  
   **Answer:** a) 7

8. **Question:** If we hash the keys 10, 20, and 30 using the function `hash(k) = k mod 10`, what is the consequence of their hash values?  
   a) They will all have unique indices.  
   b) They will all map to index 0, causing a collision.  
   c) They will map to index 1.  
   d) They will map to index 2.  
   **Answer:** b) They will all map to index 0, causing a collision.

---

# Insertion Process

## Questions

### Multiple Choice Questions on Insertion Process in Hash Tables

**Question 1:** What is the initial hash value for the key k = 25 in a hash table of size m = 10?  
a) 2  
b) 5  
c) 7  
d) 0  
**Answer:** b) 5

---

**Question 2:** If the slot at index 5 is occupied when inserting key k = 25, what will be the next index checked?  
a) 4  
b) 6  
c) 7  
d) 5  
**Answer:** b) 6

---

**Question 3:** In the given example, if the hash function for key k = 15 returns 5 and slots 5 and 6 are occupied, which slot will be checked next?  
a) 5  
b) 6  
c) 7  
d) 8  
**Answer:** c) 7

---

**Question 4:** If we are inserting key k = 15 and slots 5, 6, and 7 are occupied, what will be the index checked after slot 7?  
a) 8  
b) 9  
c) 0  
d) 6  
**Answer:** a) 8

---

**Question 5:** Given the following code snippet, what will be the output if the hash table is full and we try to insert key k = 25?

```python
def insert_key(hash_table, key):
    index = hash(key) % len(hash_table)
    i = 0
    while hash_table[(index + i) % len(hash_table)] is not None:
        i += 1
    hash_table[(index + i) % len(hash_table)] = key

hash_table = [25, 35, 15, 45, 55, 65, 75, 85, 95, 105]  # Full hash table
insert_key(hash_table, 25)
```

a) Key inserted successfully  
b) Error: Hash table is full  
c) Key replaced at index 0  
d) Key inserted at index 1  
**Answer:** b) Error: Hash table is full

---

**Question 6:** What is the probing sequence for inserting key k = 15 if the initial hash value is 5 and slots 5, 6, and 7 are occupied?  
a) 5, 6, 7, 8  
b) 5, 6, 7, 9  
c) 5, 6, 7, 8, 9  
d) 5, 6, 7, 0  
**Answer:** a) 5, 6, 7, 8

---

**Question 7:** If the hash function is defined as `hash(k) = k % 10`, what will be the hash value for key k = 35?  
a) 5  
b) 0  
c) 3  
d) 7  
**Answer:** a) 5

---

**Question 8:** In the context of the insertion process, what does the term "probing" refer to?  
a) The process of calculating the hash value  
b) The method of checking subsequent slots for an empty position  
c) The act of deleting a key from the hash table  
d) The initial insertion of a key into the hash table  
**Answer:** b) The method of checking subsequent slots for an empty position

---

# Error Reporting

## Questions

### Question 1:
What happens when you attempt to insert more elements than the size of a hash table using linear probing?

a) The new elements are added to the end of the table.  
b) An error is reported indicating that the table is full.  
c) The hash table automatically resizes to accommodate new elements.  
d) The new elements overwrite existing elements in the table.  

**Answer:** b) An error is reported indicating that the table is full.

---

### Question 2:
In a hash table of size 5, if you have inserted keys 1, 2, 3, and 4, and you try to insert key 6 which hashes to index 1, what will happen after probing?

a) Key 6 will be inserted at index 1.  
b) Key 6 will be inserted at index 0.  
c) An error will be reported because the table is full.  
d) Key 6 will be inserted at index 2 after probing.  

**Answer:** b) Key 6 will be inserted at index 0.

---

### Question 3:
Given the following code snippet for inserting a key into a hash table using linear probing, what will happen if you try to insert key 8 after inserting keys 1, 2, 3, 4, 5, and 6 in a hash table of size 5?

```python
def insert_key(hash_table, key):
    index = key % len(hash_table)
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
    hash_table[index] = key
```

a) Key 8 will be inserted successfully.  
b) An error will be reported because the table is full.  
c) Key 8 will overwrite key 1.  
d) Key 8 will be inserted at index 3.  

**Answer:** b) An error will be reported because the table is full.

---

### Question 4:
If you have a hash table of size 5 and you insert keys 1, 2, 3, and 4, which of the following keys can be inserted without causing an error?

a) Key 5  
b) Key 6  
c) Key 7  
d) Key 8  

**Answer:** a) Key 5 (assuming it hashes to an empty index).

---

### Question 5:
What is the primary purpose of linear probing in a hash table?

a) To increase the size of the hash table dynamically.  
b) To resolve collisions by finding the next available slot.  
c) To sort the elements in the hash table.  
d) To delete elements from the hash table.  

**Answer:** b) To resolve collisions by finding the next available slot.

---

# Example of Insertion

## Questions

### Multiple Choice Questions

1. **What is the result of the hash function for the key 49 when using a hash table of size 10?**
   a) 4  
   b) 9  
   c) 0  
   d) 5  
   **Answer:** b) 9

2. **After inserting the keys 89, 18, and 49 into a hash table of size 10, what will the table look like?**
   a) [ , , , , , , , , 18, 89]  
   b) [ , , , , , , , , , 49]  
   c) [ , , , , , , , , 18, 89]  
   d) [49, , , , , , , , 18, 89]  
   **Answer:** d) [49, , , , , , , , 18, 89]

3. **When inserting the key 58 into a hash table of size 10, which index will it occupy after probing?**
   a) 8  
   b) 9  
   c) 1  
   d) 0  
   **Answer:** c) 1

4. **In the tricky example with a hash table of size 5, which index will the key 69 occupy after all insertions?**
   a) 4  
   b) 0  
   c) 1  
   d) 2  
   **Answer:** d) 2

5. **What is the primary method used to resolve collisions in the given examples?**
   a) Chaining  
   b) Linear probing  
   c) Quadratic probing  
   d) Double hashing  
   **Answer:** b) Linear probing

6. **Given the following code snippet, what will be the final state of the hash table after inserting the keys 89, 18, 49, 58, and 69 into a table of size 5?**
   ```python
   hash_table = [None] * 5
   keys = [89, 18, 49, 58, 69]
   for key in keys:
       index = key % 5
       while hash_table[index] is not None:
           index = (index + 1) % 5
       hash_table[index] = key
   print(hash_table)
   ```
   a) [49, 58, 69, 18, 89]  
   b) [None, None, None, 18, 89]  
   c) [69, 58, 49, 18, 89]  
   d) [49, 58, None, 18, 89]  
   **Answer:** a) [49, 58, 69, 18, 89]

7. **What effect does reducing the size of the hash table have on the insertion process?**
   a) It decreases the number of collisions.  
   b) It increases the number of collisions.  
   c) It has no effect on collisions.  
   d) It makes the hash function more complex.  
   **Answer:** b) It increases the number of collisions.

---

# Primary Clustering

## Questions

### Question 1:
What is the main issue caused by primary clustering in a hash table?
a) Increased memory usage  
b) Longer insertion times due to contiguous occupied entries  
c) Decreased hash function efficiency  
d) Inability to store more keys  

**Answer:** b) Longer insertion times due to contiguous occupied entries

---

### Question 2:
Given a hash table of size 10 and the keys 10, 20, 30, and 40, what index will all these keys hash to using the hash function `key % 10`?
a) 0  
b) 5  
c) 10  
d) 1  

**Answer:** a) 0

---

### Question 3:
If we attempt to insert the key 15 into a hash table of size 10 after inserting the keys 10, 20, 30, and 40, which index will it occupy?
a) 0  
b) 5  
c) 10  
d) 1  

**Answer:** b) 5

---

### Question 4:
In a hash table of size 7, if we insert the keys 14, 21, and 28, which index will the key 7 hash to using the hash function `key % 7`?
a) 0  
b) 1  
c) 2  
d) 3  

**Answer:** a) 0

---

### Question 5:
What will happen when we try to insert the key 15 into the hash table of size 7 after inserting the keys 14, 21, 28, and 7?
a) It will be inserted at index 1  
b) It will be inserted at index 0  
c) It will cause a collision and require probing  
d) It will be rejected  

**Answer:** c) It will cause a collision and require probing

---

### Question 6:
Which of the following statements is true regarding primary clustering?
a) It only occurs with perfect hash functions.  
b) It can lead to performance degradation during insertion operations.  
c) It is beneficial for search operations.  
d) It does not affect the overall size of the hash table.  

**Answer:** b) It can lead to performance degradation during insertion operations.

---

### Question 7:
Consider the following code snippet for inserting a key into a hash table. What will happen if we try to insert the key 25 after inserting 15 in a hash table of size 10?

```python
def insert_key(hash_table, key):
    index = key % len(hash_table)
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
    hash_table[index] = key
```

a) It will be inserted at index 5  
b) It will be inserted at index 6  
c) It will cause an infinite loop  
d) It will be inserted at index 0  

**Answer:** b) It will be inserted at index 6

--- 

These questions cover the concept of primary clustering and its implications in hash tables, providing a comprehensive understanding of the topic.

---

# Insertion Performance

## Questions

### Question 1:
What is the average time to insert a new key in a hash table with a load factor of 0.5 and a size of 100, given that 50 keys are already inserted?

a) 10  
b) 25  
c) 50  
d) 75  

**Answer:** b) 25

---

### Question 2:
In a hash table with a load factor of 0.9 and a size of 100, if 90 keys are already inserted, what could happen when trying to insert a new key?

a) The insertion time will always be minimal.  
b) The insertion time will be significantly higher due to clustering.  
c) The insertion will always fail.  
d) The insertion time will be constant regardless of the load factor.  

**Answer:** b) The insertion time will be significantly higher due to clustering.

---

### Question 3:
Given the following code snippet for inserting a key into a hash table, what is the potential issue if the load factor is too high?

```python
def insert_key(hash_table, key):
    index = hash_function(key) % len(hash_table)
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
    hash_table[index] = key
```

a) The key will not be inserted.  
b) The insertion time will be constant.  
c) The insertion time may increase significantly due to clustering.  
d) The hash function will fail.  

**Answer:** c) The insertion time may increase significantly due to clustering.

---

### Question 4:
If a hash table has a size of 100 and a load factor of 0.9, how many keys can be inserted before performance issues arise?

a) 50  
b) 90  
c) 100  
d) 110  

**Answer:** b) 90

---

### Question 5:
What is the primary reason for slower insertion performance in a hash table as the load factor increases?

a) The hash function becomes less effective.  
b) The size of the hash table decreases.  
c) Clustering increases, leading to longer search times for empty slots.  
d) The keys become more complex.  

**Answer:** c) Clustering increases, leading to longer search times for empty slots.

---

# Disadvantages of Linear Probing

## Questions

### Questions on Disadvantages of Linear Probing

**Question 1:** What is a primary disadvantage of linear probing in hash tables?  
a) It requires more memory than other methods  
b) It can lead to clustering of occupied indices  
c) It is slower than chaining  
d) It cannot handle collisions  

**Answer:** b) It can lead to clustering of occupied indices

---

**Question 2:** In a hash table of size 10, if the keys 1, 11, and 21 are inserted using linear probing, which indices will they occupy?  
a) 0, 1, 2  
b) 1, 2, 3  
c) 1, 1, 1  
d) 0, 1, 2  

**Answer:** b) 1, 2, 3

---

**Question 3:** Given a hash table of size 10, if the keys 10, 20, 30, and 40 are inserted and all hash to index 0, what will be the index of the key 15 when it is inserted?  
a) 0  
b) 1  
c) 5  
d) 6  

**Answer:** b) 1

---

**Question 4:** Which of the following scenarios best illustrates the problem of clustering in linear probing?  
a) Inserting keys that all hash to different indices  
b) Inserting keys that hash to the same index and then to subsequent indices  
c) Inserting keys that do not cause any collisions  
d) Inserting keys that are all unique  

**Answer:** b) Inserting keys that hash to the same index and then to subsequent indices

---

**Question 5:** Consider the following code snippet for inserting a key into a hash table using linear probing. What will happen if the table is nearly full and a new key is inserted? 

```python
def linear_probing_insert(hash_table, key):
    index = hash_function(key)
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
    hash_table[index] = key
```

a) The key will be inserted without any issues  
b) The insertion will fail  
c) The function will enter an infinite loop  
d) The key will overwrite an existing key  

**Answer:** c) The function will enter an infinite loop

--- 

These questions assess the understanding of the disadvantages of linear probing, particularly focusing on clustering and the implications of collisions in hash tables.

---

# Collisions and Clusters

## Questions

### Questions on Collisions and Clusters

**Question 1:** In a distributed database system, what happens to the likelihood of network collisions as more nodes are added to a cluster?  
a) It decreases  
b) It remains the same  
c) It increases  
d) It becomes negligible  
**Answer:** c) It increases

---

**Question 2:** If a cluster consists of 100 nodes and each node sends data packets simultaneously, what is the likely outcome?  
a) Faster data processing  
b) Increased packet collisions  
c) Improved query response times  
d) No impact on performance  
**Answer:** b) Increased packet collisions

---

**Question 3:** In the tricky example, what was the initial number of servers handling requests for the online service?  
a) 25  
b) 50  
c) 75  
d) 100  
**Answer:** b) 50

---

**Question 4:** What was the effect of doubling the number of servers from 50 to 100 during a major event?  
a) Improved performance  
b) Increased collisions and slower response times  
c) No change in performance  
d) Reduced latency  
**Answer:** b) Increased collisions and slower response times

---

**Question 5:** Consider the following code snippet that simulates packet sending in a cluster:

```python
class Node:
    def send_packet(self):
        # Simulate sending a packet
        return "Packet sent"

nodes = [Node() for _ in range(100)]
for node in nodes:
    node.send_packet()
```

What is a potential issue with this code when executed in a large cluster?  
a) It will run too slowly  
b) It will cause packet collisions  
c) It will not send any packets  
d) It will send packets in sequence  
**Answer:** b) It will cause packet collisions

---

**Question 6:** Which of the following statements best describes the relationship between the number of nodes in a cluster and network performance?  
a) More nodes always improve performance  
b) More nodes can lead to increased collisions and degraded performance  
c) The number of nodes has no effect on performance  
d) Fewer nodes always lead to better performance  
**Answer:** b) More nodes can lead to increased collisions and degraded performance

---

# Quadratic Probing

## Questions

### Questions on Quadratic Probing

**Question 1:** In a hash table of size 10, if we insert the keys 12, 22, and 32 using the hash function h(x) = x % 10, where will the key 22 be placed?  
a) Index 2  
b) Index 3  
c) Index 6  
d) Index 4  
**Answer:** b) Index 3

---

**Question 2:** Given a hash table of size 7 and the hash function h(x) = x % 7, what will be the final index for the key 24 after applying quadratic probing?  
a) Index 3  
b) Index 4  
c) Index 0  
d) Index 1  
**Answer:** c) Index 0

---

**Question 3:** If we have a hash table of size 10 and we insert the keys 12, 22, and 32, which of the following statements is true?  
a) All keys will be placed at index 2.  
b) Key 32 will be placed at index 4.  
c) Key 12 will be placed at index 2.  
d) Key 22 will be placed at index 6.  
**Answer:** c) Key 12 will be placed at index 2.

---

**Question 4:** In the context of quadratic probing, what is the formula used to find the next index to check when a collision occurs?  
a) index + 1  
b) index + n^2  
c) index + 2n  
d) index + n  
**Answer:** b) index + n^2

---

**Question 5:** Consider the following code snippet for inserting a key into a hash table using quadratic probing. What will be the output if we try to insert the key 17 after inserting 10 in a hash table of size 7?

```python
def quadratic_probing_insert(hash_table, key):
    index = key % len(hash_table)
    n = 0
    while hash_table[index] is not None:
        n += 1
        index = (index + n**2) % len(hash_table)
    hash_table[index] = key

hash_table = [None] * 7
quadratic_probing_insert(hash_table, 10)
quadratic_probing_insert(hash_table, 17)
print(hash_table)
```

a) [None, None, None, 10, 17, None, None]  
b) [None, None, None, 10, None, None, 17]  
c) [17, None, None, 10, None, None, None]  
d) [None, 17, None, 10, None, None, None]  
**Answer:** b) [None, None, None, 10, None, None, 17]

---

**Question 6:** If a hash table of size 10 uses the hash function h(x) = x % 10, and we insert the keys 12, 22, and 32, which index will be checked first for key 32 after the collision resolution for key 22?  
a) Index 2  
b) Index 3  
c) Index 4  
d) Index 6  
**Answer:** c) Index 6

---

**Question 7:** What is the primary advantage of using quadratic probing over linear probing in hash tables?  
a) It uses less memory.  
b) It reduces clustering of keys.  
c) It is easier to implement.  
d) It guarantees no collisions.  
**Answer:** b) It reduces clustering of keys.

---

# Hash Function

## Questions

### Multiple Choice Questions on Hash Functions

**Question 1:** What is the result of the hash function `hash(k) = k mod 10` when the key `k = 45` is used?  
a) 4  
b) 5  
c) 0  
d) 9  
**Answer:** b) 5

---

**Question 2:** Given the hash function `hash(k) = k mod 10`, what will happen if we hash the keys `k = 30` and `k = 40`?  
a) Both keys will be stored at index 0.  
b) Both keys will be stored at index 1.  
c) Both keys will be stored at index 3.  
d) Both keys will be stored at index 4.  
**Answer:** a) Both keys will be stored at index 0.

---

**Question 3:** Which of the following strategies can be used to resolve collisions in a hash table?  
a) Chaining  
b) Open addressing  
c) Both a and b  
d) None of the above  
**Answer:** c) Both a and b

---

**Question 4:** If we have a hash table with a size of 10 and we use the hash function `hash(k) = k mod 10`, what will be the index for the key `k = 57`?  
a) 5  
b) 7  
c) 2  
d) 0  
**Answer:** b) 7

---

**Question 5:** In the context of hash functions, what does the term "collision" refer to?  
a) When two different keys hash to the same index.  
b) When a key is not found in the hash table.  
c) When the hash table is full.  
d) When the hash function is not defined.  
**Answer:** a) When two different keys hash to the same index.

---

**Question 6:** Consider the following code snippet that implements a simple hash function:

```python
def hash_function(k):
    return k % 10

index1 = hash_function(25)
index2 = hash_function(15)
```

What will be the values of `index1` and `index2`?  
a) index1 = 5, index2 = 5  
b) index1 = 5, index2 = 0  
c) index1 = 0, index2 = 5  
d) index1 = 5, index2 = 10  
**Answer:** a) index1 = 5, index2 = 5

---

**Question 7:** If a hash table uses chaining for collision resolution, what does each index in the hash table contain?  
a) A single key-value pair  
b) A linked list of key-value pairs  
c) An array of key-value pairs  
d) A binary tree of key-value pairs  
**Answer:** b) A linked list of key-value pairs

---

**Question 8:** What is the primary purpose of a hash function in data structures?  
a) To sort data  
b) To encrypt data  
c) To map keys to indices in a hash table  
d) To store data in a linear fashion  
**Answer:** c) To map keys to indices in a hash table

---

# Probe Sequence

## Questions

### Question 1:
What is the home position for inserting the key 15 into a hash table of size 10 using the hash function `key % table_size`?

a) 3  
b) 5  
c) 7  
d) 10  

**Answer:** b) 5

---

### Question 2:
In a hash table of size 10, if the key 20 is inserted using quadratic probing and the home position is 0, what will be the first index checked after index 0 if it is occupied?

a) 1  
b) 2  
c) 4  
d) 9  

**Answer:** a) 1

---

### Question 3:
Given a hash table of size 10 and a key of 15, if index 5 is occupied, which index will be checked next using linear probing?

a) 4  
b) 6  
c) 7  
d) 8  

**Answer:** b) 6

---

### Question 4:
If we are using quadratic probing to resolve collisions in a hash table and the home position for a key is 0, what will be the third index checked if the first two indices (0 and 1) are occupied?

a) 2  
b) 3  
c) 4  
d) 9  

**Answer:** c) 4

---

### Question 5:
What is the probe sequence for inserting the key 15 into a hash table of size 10 using linear probing if the home position is 5 and indices 5 and 6 are occupied?

a) [5, 6, 7]  
b) [5, 6, 8]  
c) [5, 6, 7, 8]  
d) [5, 6, 7, 9]  

**Answer:** c) [5, 6, 7, 8]

---

### Question 6:
In the context of quadratic probing, if the home position for a key is 0 and the first two indices checked are occupied, what will be the next index checked after index 1?

a) 2  
b) 3  
c) 4  
d) 5  

**Answer:** c) 4

---

### Question 7:
If a hash table of size 10 uses a hash function of `key % 10` and the key 25 is inserted, what is the home position?

a) 2  
b) 5  
c) 0  
d) 1  

**Answer:** b) 5

---

### Question 8:
Which of the following statements is true regarding the probe sequence in a hash table using quadratic probing?

a) The probe sequence is always predictable.  
b) The probe sequence can skip indices based on the square of the probe number.  
c) The probe sequence only checks the next immediate index.  
d) The probe sequence is the same as linear probing.  

**Answer:** b) The probe sequence can skip indices based on the square of the probe number.

---

# Table Size and Insertion

## Questions

### Question 1:
What is the load factor of a hash table with 4 keys inserted and a size of 11?
a) 0.25  
b) 0.36  
c) 0.4  
d) 0.5  
**Answer:** c) 0.4

### Question 2:
In a hash table of size 13 with 7 keys inserted, what is the maximum number of keys that can be inserted without causing a collision, assuming all new keys hash to empty slots?
a) 6  
b) 5  
c) 4  
d) 3  
**Answer:** a) 6

### Question 3:
If you attempt to insert a key into a hash table of size 13 that already has a load factor of 0.54, what must happen if the key hashes to an occupied slot?
a) The key will be inserted without issues.  
b) The key will be discarded.  
c) A collision resolution method must be applied.  
d) The table will automatically resize.  
**Answer:** c) A collision resolution method must be applied.

### Question 4:
Given the following code snippet, what will be the output if the key 15 is inserted into the hash table?

```python
hash_table = [None] * 13
hash_table[0] = 5
hash_table[1] = 15
hash_table[2] = 25

def insert_key(key):
    index = key % 13
    if hash_table[index] is None:
        hash_table[index] = key
    else:
        print("Collision occurred!")

insert_key(15)
```
a) 15 will be inserted successfully.  
b) Collision occurred!  
c) The table will resize.  
d) 15 will replace the existing value.  
**Answer:** b) Collision occurred!

### Question 5:
What is the primary advantage of using a prime number for the size of a hash table?
a) It allows for more keys to be inserted.  
b) It reduces the likelihood of collisions.  
c) It simplifies the hashing function.  
d) It increases the load factor.  
**Answer:** b) It reduces the likelihood of collisions.

---

# Example of Insertion

## Questions

### Multiple Choice Questions on Hash Table Insertion with Quadratic Probing

1. What is the initial hash value for the key 49 when using the hash function \( h(key) = key \mod 10 \)?
   a) 0  
   b) 1  
   c) 9  
   d) 4  
   **Answer:** c) 9

2. After inserting the keys 89, 18, and 49 into a hash table of size 10, what will be the state of the table?
   a) [ , , , , , , , , 18, 89]  
   b) [49, , , , , , , , 18, 89]  
   c) [ , , , , , , , , , ]  
   d) [ , , , , , 89, , , 18, 49]  
   **Answer:** b) [49, , , , , , , , 18, 89]

3. When inserting the key 58 into the hash table of size 10, which index will it be placed in after resolving collisions?
   a) 8  
   b) 1  
   c) 0  
   d) 9  
   **Answer:** b) 1

4. If we attempt to insert the key 69 into a hash table of size 10 after inserting 89, 18, 49, and 58, which index will it occupy?
   a) 2  
   b) 9  
   c) 1  
   d) 0  
   **Answer:** a) 2

5. In the tricky example with a hash table of size 7, what is the final state of the table after inserting the keys 89, 18, 49, 58, 69, and 76?
   a) [49, , 58, , 18, 89, 69]  
   b) [49, 76, 58, , 18, 89, 69]  
   c) [49, , 58, 76, 18, 89, 69]  
   d) [ , , , , , 89, 69]  
   **Answer:** c) [49, , 58, 76, 18, 89, 69]

6. What happens when you try to insert the key 76 into the hash table of size 7?
   a) It is inserted at index 6.  
   b) It is inserted at index 3 after probing.  
   c) It cannot be inserted due to collisions.  
   d) It is inserted at index 0.  
   **Answer:** b) It is inserted at index 3 after probing.

7. Which of the following statements about quadratic probing is true?
   a) It always finds an empty slot on the first attempt.  
   b) It checks indices in a linear manner.  
   c) It checks indices based on the square of the probe number.  
   d) It does not wrap around the table.  
   **Answer:** c) It checks indices based on the square of the probe number.

8. If the hash function is \( h(key) = key \mod 7 \), what is the hash value for the key 58?
   a) 4  
   b) 5  
   c) 6  
   d) 2  
   **Answer:** a) 2

9. In the context of hash tables, what is the purpose of using quadratic probing?
   a) To increase the size of the hash table.  
   b) To resolve collisions more efficiently.  
   c) To decrease the number of keys stored.  
   d) To simplify the hash function.  
   **Answer:** b) To resolve collisions more efficiently.

10. After inserting the keys 89, 18, 49, 58, and 69 into a hash table of size 7, which index will be occupied by the key 18?
    a) 4  
    b) 5  
    c) 6  
    d) 0  
    **Answer:** a) 4

---

# Secondary Clustering

## Questions

### Question 1:
What is the primary issue illustrated by secondary clustering in hash tables?
a) Increased memory usage  
b) Increased search times due to probing sequences  
c) Decreased collision resolution efficiency  
d) Inability to insert new keys  

**Answer:** b) Increased search times due to probing sequences

---

### Question 2:
Given a hash table of size 10 and a hash function defined as `key % 10`, which of the following keys will cause a collision when inserting into the hash table?
a) 15  
b) 25  
c) 35  
d) All of the above  

**Answer:** d) All of the above

---

### Question 3:
In the context of linear probing, if the keys 10, 20, and 30 are inserted into a hash table of size 10, what will be the index of the key 30 after resolving collisions?
a) 0  
b) 1  
c) 2  
d) 3  

**Answer:** c) 2

---

### Question 4:
Consider the following code snippet for inserting a key into a hash table using quadratic probing. What will be the index of the key 28 after inserting keys 14 and 21 into a hash table of size 7?

```python
def quadratic_probing_insert(hash_table, key):
    index = key % len(hash_table)
    i = 1
    while hash_table[index] is not None:
        index = (index + i * i) % len(hash_table)
        i += 1
    hash_table[index] = key
```

a) 0  
b) 1  
c) 4  
d) 5  

**Answer:** c) 4

---

### Question 5:
If a hash table uses quadratic probing and the keys 14, 21, and 28 are inserted, which of the following keys will lead to the same probing sequence as key 7?
a) 0  
b) 14  
c) 21  
d) 28  

**Answer:** a) 0

---

### Question 6:
What is the effect of secondary clustering when using a hash table with linear probing?
a) It reduces the number of collisions.  
b) It causes keys that hash to the same index to probe the same subsequent indices.  
c) It allows for faster searches.  
d) It eliminates the need for a hash function.  

**Answer:** b) It causes keys that hash to the same index to probe the same subsequent indices.

---

# Double Hashing

## Questions

### Multiple Choice Questions on Double Hashing

**Question 1:** What is the primary purpose of using double hashing in a hash table?  
a) To increase the size of the hash table  
b) To reduce clustering during collision resolution  
c) To improve the speed of hash function calculations  
d) To store more keys than the hash table can hold  
**Answer:** b) To reduce clustering during collision resolution

---

**Question 2:** Given the hash functions \( h1(key) = key \% 10 \) and \( h2(key) = 7 - (key \% 7) \), what is the primary position for the key 25?  
a) 5  
b) 0  
c) 2  
d) 7  
**Answer:** a) 5

---

**Question 3:** If the primary position for a key is occupied, how is the next position determined in double hashing?  
a) By using the same primary hash function  
b) By using the secondary hash function to calculate a step size  
c) By randomly selecting an empty position  
d) By incrementing the primary position by 1  
**Answer:** b) By using the secondary hash function to calculate a step size

---

**Question 4:** For the key 40, which positions are probed before it is successfully inserted into the hash table?  
a) 0, 1, 2, 4  
b) 0, 2, 4  
c) 0, 1, 4  
d) 0, 2, 5  
**Answer:** b) 0, 2, 4

---

**Question 5:** In the final hash table after inserting keys 10, 20, 30, and 40, what value is stored at index 3?  
a) 10  
b) 20  
c) 30  
d) -  
**Answer:** d) -

---

**Question 6:** What will be the result of inserting the key 22 into the hash table after inserting keys 12 and 32?  
a) It will be placed at index 2  
b) It will be placed at index 6  
c) It will be placed at index 8  
d) It will cause an error  
**Answer:** c) It will be placed at index 8

---

**Question 7:** If the hash table size is increased to 20, how would the primary position for the key 22 change using the same hash function \( h1(key) = key \% 10 \)?  
a) It would remain the same  
b) It would change to 12  
c) It would change to 2  
d) It would change to 0  
**Answer:** a) It would remain the same

---

**Question 8:** What is the value of \( h2(30) \) using the hash function \( h2(key) = 7 - (key \% 7) \)?  
a) 5  
b) 2  
c) 4  
d) 1  
**Answer:** a) 5

---

These questions cover various aspects of double hashing, including its purpose, mechanics, and specific examples provided in the content.

---

# Hash Functions

## Questions

### Question 1:
What is the primary purpose of a hash function in a hash table?
a) To sort the data  
b) To generate a unique identifier for each key  
c) To map keys to specific indices in the hash table  
d) To encrypt the data  

**Answer:** c) To map keys to specific indices in the hash table

---

### Question 2:
Given the hash function `hash(key) = key % 10`, what will be the result of `hash(45)`?
a) 5  
b) 4  
c) 0  
d) 9  

**Answer:** a) 5

---

### Question 3:
If we have a hash table of size 10 and we want to insert the key 23 using the hash function `hash(key) = key % 10`, what is the initial index we will check?
a) 2  
b) 3  
c) 5  
d) 8  

**Answer:** b) 3

---

### Question 4:
In the probing sequence for inserting key 6 using the hash function `hash(key) = key % 10` and `hash2(key) = 3 - (key % 3)`, if position 6 is occupied, what will be the next position checked?
a) 9  
b) 2  
c) 3  
d) 0  

**Answer:** a) 9

---

### Question 5:
What issue does the example with key 9 illustrate when using the hash function `hash(key) = key % 10` and `hash2(key) = 3 - (key % 3)`?
a) It shows that hash functions can be too complex.  
b) It demonstrates the need for careful design of hash functions to avoid clustering.  
c) It indicates that hash tables are not efficient.  
d) It proves that all keys can be inserted without collisions.  

**Answer:** b) It demonstrates the need for careful design of hash functions to avoid clustering.

---

### Question 6:
If the hash table is full and we try to insert a new key, what is the typical outcome?
a) The key is automatically deleted.  
b) The insertion fails, and an error is returned.  
c) The hash table expands in size.  
d) The key is inserted at the next available index.  

**Answer:** b) The insertion fails, and an error is returned. 

---

### Question 7:
What is the result of `hash2(23)` using the hash function `hash2(key) = 7 - (key % 7)`?
a) 5  
b) 3  
c) 2  
d) 4  

**Answer:** a) 5

---

### Question 8:
In the context of hash tables, what does "clustering" refer to?
a) The process of grouping similar keys together.  
b) The situation where multiple keys hash to the same index, leading to a long chain of probes.  
c) The method of expanding the hash table size.  
d) The technique of sorting keys before insertion.  

**Answer:** b) The situation where multiple keys hash to the same index, leading to a long chain of probes.

---

# Probe Sequence Formula

## Questions

### Multiple Choice Questions on Probe Sequence Formula

**Question 1:** Given a hash function `hash(k)` that returns 4 for the key `k`, and a secondary hash function `hash2(k)` that returns 3, with a table size `m = 7`, what is the probe sequence for `k`?

a) 4, 0, 3, 6, 2  
b) 4, 3, 5, 1, 6  
c) 4, 3, 5, 1, 4  
d) 4, 3, 0, 6, 2  

**Answer:** a) 4, 0, 3, 6, 2

---

**Question 2:** If `hash(k)` returns 1 and `hash2(k)` returns 2, and the table size `m = 5`, what will be the value of `hi(2)` in the probe sequence?

a) 0  
b) 1  
c) 3  
d) 4  

**Answer:** c) 3

---

**Question 3:** In the tricky example provided, if `hash(k)` returns 2 and `hash2(k)` returns 4 with a table size `m = 6`, which of the following statements is true about the probe sequence?

a) The sequence will eventually fill all slots in the table.  
b) The sequence will create a cycle and may not find an empty slot.  
c) The sequence will always find an empty slot on the first attempt.  
d) The sequence will only probe the first two slots.  

**Answer:** b) The sequence will create a cycle and may not find an empty slot.

---

**Question 4:** If we have a hash function `hash(k)` that returns 5 and a secondary hash function `hash2(k)` that returns 1, with a table size `m = 10`, what is the value of `hi(4)`?

a) 5  
b) 9  
c) 4  
d) 6  

**Answer:** d) 6

---

**Question 5:** What is the primary issue that can arise from the probe sequence `3, 8, 3, 8, ...` as described in the typical example?

a) It will lead to a full table.  
b) It can cause clustering in the hash table.  
c) It will always find an empty slot.  
d) It will create a unique sequence for every key.  

**Answer:** b) It can cause clustering in the hash table.

---

# Example of hash2(k)

## Questions

### Question 1:
Given a primary hash table size of m = 10 and R = 7, what is the secondary hash value for k = 15?

a) 1  
b) 6  
c) 7  
d) 0  

**Answer:** b) 6

---

### Question 2:
If k = 21, m = 10, and R = 7, what is the result of the calculation k mod R?

a) 1  
b) 0  
c) 6  
d) 7  

**Answer:** b) 0

---

### Question 3:
What is the secondary hash value for k = 21 using the formula hash2(k) = R - (k mod R)?

a) 6  
b) 7  
c) 0  
d) 1  

**Answer:** b) 7

---

### Question 4:
If we had chosen a different R such that R = 5, what would be the secondary hash value for k = 15?

a) 2  
b) 3  
c) 4  
d) 5  

**Answer:** b) 3  
*(Calculation: 15 mod 5 = 0, hash2(15) = 5 - 0 = 5)*

---

### Question 5:
In the context of hash functions, why is it important to ensure that the secondary hash value is within the bounds of the hash table size?

a) To avoid collisions  
b) To maintain the efficiency of the hash table  
c) To ensure all values are unique  
d) All of the above  

**Answer:** d) All of the above

---

### Question 6:
Consider the following code snippet for calculating hash2:

```python
def hash2(k, R):
    return R - (k % R)

k = 15
R = 7
print(hash2(k, R))
```
What will be the output of this code?

a) 1  
b) 6  
c) 7  
d) 0  

**Answer:** b) 6

---

### Question 7:
If the primary hash table size is m = 10 and we choose R = 3, what would be the secondary hash value for k = 10?

a) 0  
b) 1  
c) 2  
d) 3  

**Answer:** c) 2  
*(Calculation: 10 mod 3 = 1, hash2(10) = 3 - 1 = 2)*

---

### Question 8:
What happens if the secondary hash value exceeds the primary hash table size?

a) It is ignored  
b) It is wrapped around using modulo operation  
c) It causes an error  
d) It is set to zero  

**Answer:** b) It is wrapped around using modulo operation

---

# Double Hashing

## Questions

### Multiple Choice Questions on Double Hashing

**Question 1:** What is the purpose of using a second hash function in double hashing?  
a) To increase the size of the hash table  
b) To resolve collisions that occur with the first hash function  
c) To decrease the number of keys in the hash table  
d) To sort the keys in the hash table  
**Answer:** b) To resolve collisions that occur with the first hash function

---

**Question 2:** Given the hash functions \( h1(key) = key \% 10 \) and \( h2(key) = 7 - (key \% 7) \), what will be the index for key 22 after applying double hashing?  
a) 2  
b) 8  
c) 6  
d) 5  
**Answer:** b) 8

---

**Question 3:** If we attempt to insert key 40 into the hash table after inserting keys 10, 20, and 30, what will be the index for key 40?  
a) 0  
b) 1  
c) 2  
d) 5  
**Answer:** c) 2

---

**Question 4:** What will be the result of inserting key 12 into the hash table using the provided hash functions?  
a) It will be inserted at index 0  
b) It will be inserted at index 2  
c) It will cause a collision  
d) It will be inserted at index 5  
**Answer:** b) It will be inserted at index 2

---

**Question 5:** In the context of double hashing, what does the term "collision" refer to?  
a) When two keys are hashed to the same index  
b) When a key is not found in the hash table  
c) When the hash table is full  
d) When the hash functions are not working properly  
**Answer:** a) When two keys are hashed to the same index

---

**Question 6:** If we have a hash table of size 10 and we insert keys 10, 20, and 30, which index will key 30 occupy?  
a) 0  
b) 1  
c) 5  
d) 2  
**Answer:** c) 5

---

**Question 7:** What will be the value of \( h2(40) \) using the hash function \( h2(key) = 7 - (key \% 7) \)?  
a) 5  
b) 2  
c) 3  
d) 4  
**Answer:** a) 5

---

**Question 8:** After inserting keys 12, 22, and 32, what is the final state of the hash table at index 5?  
a) 12  
b) 22  
c) 32  
d) Empty  
**Answer:** c) 32

---

**Question 9:** If the first hash function \( h1(key) \) results in an occupied index, what is the next step in double hashing?  
a) Increase the size of the hash table  
b) Use the second hash function \( h2(key) \) to find a new index  
c) Ignore the key  
d) Replace the existing key  
**Answer:** b) Use the second hash function \( h2(key) \) to find a new index

---

**Question 10:** What is the final index for key 20 after applying both hash functions if the first index is occupied?  
a) 0  
b) 1  
c) 2  
d) 5  
**Answer:** b) 1

---

# Hash Functions

## Questions

### Question 1:
What is the primary hash function used in the example provided?
a) hash(k) = k mod 7  
b) hash(k) = k mod 10  
c) hash(k) = 7 - (k mod 7)  
d) hash(k) = k + 3  

**Answer:** b) hash(k) = k mod 10

---

### Question 2:
If we want to insert the key 33 into the hash table after inserting 23, what is the first index we calculate using the primary hash function?
a) 2  
b) 3  
c) 4  
d) 5  

**Answer:** b) 3

---

### Question 3:
What is the value of hash2(33) using the secondary hash function provided?
a) 5  
b) 2  
c) 4  
d) 3  

**Answer:** a) 5

---

### Question 4:
After inserting the key 14, what index does it occupy in the hash table?
a) 2  
b) 3  
c) 4  
d) 5  

**Answer:** c) 4

---

### Question 5:
When trying to insert the key 24, what is the result of the secondary hash function hash2(24)?
a) 3  
b) 4  
c) 5  
d) 6  

**Answer:** a) 3

---

### Question 6:
If index 4 is occupied when inserting key 24, what will be the new index after probing?
a) 4  
b) 5  
c) 8  
d) 9  

**Answer:** c) 8

---

### Question 7:
What is the purpose of the secondary hash function in the context of hash tables?
a) To calculate the primary index  
b) To find a new index when a collision occurs  
c) To delete keys from the hash table  
d) To sort the keys in the hash table  

**Answer:** b) To find a new index when a collision occurs

---

### Question 8:
In the probing process for key 24, if index 8 is also occupied, what would be the next step?
a) Stop the insertion process  
b) Use the primary hash function again  
c) Continue probing using the secondary hash function  
d) Insert the key at index 9  

**Answer:** c) Continue probing using the secondary hash function

---

---

# Collision Resolution

## Questions

### Multiple Choice Questions on Collision Resolution

**Question 1:** In the given example, what is the first index calculated for key 23?  
a) 5  
b) 3  
c) 7  
d) 0  
**Answer:** b) 3  

---

**Question 2:** When inserting key 33, what is the first index calculated before resolving the collision?  
a) 7  
b) 3  
c) 4  
d) 0  
**Answer:** b) 3  

---

**Question 3:** For key 21 in the tricky example, what is the next index calculated after the collision at index 0?  
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** c) 2  

---

**Question 4:** What is the final index where key 35 is placed after resolving collisions?  
a) 0  
b) 1  
c) 5  
d) 3  
**Answer:** c) 5  

---

**Question 5:** In the context of the examples provided, what is the purpose of the second hash function (hash2)?  
a) To increase the size of the hash table  
b) To calculate the initial index  
c) To resolve collisions  
d) To store additional data  
**Answer:** c) To resolve collisions  

---

**Question 6:** If we were to insert a new key, say key 42, where hash(42) = 0 and hash2(42) = 4, what would be the first index calculated?  
a) 0  
b) 4  
c) 1  
d) 3  
**Answer:** a) 0  

---

**Question 7:** After inserting keys 14, 21, 28, and 35, which index remains unoccupied in the hash table of size 7?  
a) 0  
b) 1  
c) 3  
d) 6  
**Answer:** d) 6  

---

**Question 8:** If a new key, key 49, has hash(49) = 0 and hash2(49) = 6, what will be the first index calculated for key 49?  
a) 0  
b) 6  
c) 1  
d) 3  
**Answer:** a) 0  

---

**Question 9:** In the example with key 28, what is the index calculated after the first collision?  
a) 0  
b) 1  
c) 2  
d) 3  
**Answer:** b) 1  

---

**Question 10:** What is the maximum number of probes needed to insert key 35 in the tricky example?  
a) 1  
b) 2  
c) 3  
d) 4  
**Answer:** c) 3  

---

# Table Size and Probing

## Questions

### Question 1:
What is the primary hash function used in the example for a hash table of size m = 10?
a) h1(x) = x mod 5  
b) h1(x) = x mod 10  
c) h1(x) = x mod 7  
d) h1(x) = x mod 3  
**Answer:** b) h1(x) = x mod 10

### Question 2:
Which of the following is a suitable choice for the secondary hash function h2(x) that is relatively prime to 10?
a) h2(x) = x mod 5  
b) h2(x) = 2 + (x mod 2)  
c) h2(x) = 7 - (x mod 7)  
d) h2(x) = x mod 10  
**Answer:** c) h2(x) = 7 - (x mod 7)

### Question 3:
If we want to insert the value 23 into the hash table, what is the initial index calculated by the primary hash function h1(23)?
a) 5  
b) 3  
c) 8  
d) 0  
**Answer:** b) 3

### Question 4:
What would be the next index to check if index 3 is occupied when inserting the value 23?
a) 5  
b) 8  
c) 0  
d) 3  
**Answer:** a) 5

### Question 5:
If we incorrectly choose h2(x) = x mod 5, what issue might arise during probing?
a) The probing will check all indices in the table.  
b) The probing will only check half of the table.  
c) The probing will be too slow.  
d) The probing will always find an empty slot.  
**Answer:** b) The probing will only check half of the table.

### Question 6:
Given the incorrect choice of h2(x) = x mod 5, what would be the probing sequence when inserting the value 15?
a) 5, 0, 3, 8  
b) 5, 0, 5, 0  
c) 0, 5, 10, 15  
d) 3, 6, 9, 2  
**Answer:** b) 5, 0, 5, 0

### Question 7:
What is the correct choice for h2(x) that allows effective probing in the hash table of size 10?
a) h2(x) = 2 + (x mod 2)  
b) h2(x) = 3 + (x mod 3)  
c) h2(x) = x mod 10  
d) h2(x) = x mod 5  
**Answer:** b) h2(x) = 3 + (x mod 3)

---

# Quadratic Probing

## Questions

### Question 1:
What is the result of the hash function h(x) = x % 10 for the key 22?
a) 2  
b) 3  
c) 4  
d) 5  
**Answer:** a) 2

### Question 2:
In the given example, after inserting the key 12, what is the state of the hash table?
a) [12, , , , , , , , , ]  
b) [ , 12, , , , , , , , ]  
c) [ , , 12, , , , , , , ]  
d) [ , , , 12, , , , , , ]  
**Answer:** c) [ , , 12, , , , , , , ]

### Question 3:
When inserting the key 22, which index is chosen after the first collision using quadratic probing?
a) 2  
b) 3  
c) 4  
d) 5  
**Answer:** b) 3

### Question 4:
What is the final state of the hash table after inserting the keys 12, 22, and 32 using the hash function h(x) = x % 10?
a) [ , , 12, 22, , , 32, , , , ]  
b) [ , , 22, 12, , , 32, , , , ]  
c) [ , , 32, 22, , , 12, , , , ]  
d) [ , , 12, , , , 22, 32, , , ]  
**Answer:** a) [ , , 12, 22, , , 32, , , , ]

### Question 5:
For the keys 10, 17, and 24, what is the index where the key 24 is inserted after resolving collisions?
a) 3  
b) 4  
c) 0  
d) 1  
**Answer:** c) 0

### Question 6:
Using the hash function h(x) = x % 7, what is the result of h(17)?
a) 2  
b) 3  
c) 4  
d) 5  
**Answer:** b) 3

### Question 7:
In the tricky example, after inserting the key 10, what is the state of the hash table?
a) [ , , , 10, , , ]  
b) [10, , , , , , ]  
c) [ , 10, , , , , ]  
d) [ , , 10, , , , ]  
**Answer:** a) [ , , , 10, , , ]

### Question 8:
What is the probing sequence for the key 24 after the first collision when using the hash function h(x) = x % 7?
a) 3, 4, 5  
b) 3, 4, 0  
c) 3, 4, 6  
d) 3, 5, 0  
**Answer:** b) 3, 4, 0

---

# Deletion in Open Addressing

## Questions

### Question 1:
What happens when a key is deleted in an open addressing hash table?

a) The key is completely removed from the table.  
b) The key is marked as DELETED to maintain the probing sequence.  
c) The key is moved to the end of the table.  
d) The key is replaced with a NULL value.  

**Answer:** b) The key is marked as DELETED to maintain the probing sequence.

---

### Question 2:
Given a hash table of size 10 and a hash function defined as `key % 10`, if we insert the keys 15, 25, and 35, what will be the state of the hash table after inserting these keys?

a) [15 (ACTIVE), 25 (ACTIVE), 35 (ACTIVE), , , , , , , ]  
b) [ , , 15 (ACTIVE), 25 (ACTIVE), 35 (ACTIVE), , , , , ]  
c) [ , , , , , 15 (ACTIVE), 25 (ACTIVE), 35 (ACTIVE), , ]  
d) [ , , , , , , , , , 15 (ACTIVE)]  

**Answer:** a) [15 (ACTIVE), 25 (ACTIVE), 35 (ACTIVE), , , , , , , ]

---

### Question 3:
In the tricky example provided, if we delete key 6 and then attempt to insert key 16, which hashes to index 1, what will happen?

a) Key 16 will be inserted at index 1.  
b) Key 16 will be inserted at index 2, but will not be found later.  
c) Key 16 will be inserted at index 3.  
d) Key 16 will cause an error due to the DELETED marker.  

**Answer:** c) Key 16 will be inserted at index 3.

---

### Question 4:
Consider the following code snippet for inserting a key into a hash table with open addressing:

```python
def insert(hash_table, key):
    index = key % len(hash_table)
    while hash_table[index] is not None and hash_table[index] != 'DELETED':
        index = (index + 1) % len(hash_table)
    hash_table[index] = key
```

What will happen if you try to insert a key that has the same hash index as a DELETED key?

a) The key will be inserted at the DELETED index.  
b) The key will cause an infinite loop.  
c) The key will be ignored.  
d) The key will replace the DELETED key.  

**Answer:** a) The key will be inserted at the DELETED index.

---

### Question 5:
If a hash table of size 5 has the following state after several insertions and deletions: [ , 1 (ACTIVE), DELETED, 11 (ACTIVE), ], what will be the result of searching for key 11?

a) The search will fail.  
b) The search will succeed and return 11.  
c) The search will return DELETED.  
d) The search will return NULL.  

**Answer:** b) The search will succeed and return 11.

---

# Re-hashing

## Questions

### Question 1:
What is the load factor (¦Á) of a hash table that has 5 items and a size of 10?
a) 0.25  
b) 0.5  
c) 0.75  
d) 1.0  
**Answer:** b) 0.5

### Question 2:
If a hash table with a size of 10 currently holds 11 items, what action should be taken to maintain performance?
a) Do nothing, performance is still optimal  
b) Decrease the number of items  
c) Resize the hash table  
d) Change the hash function without resizing  
**Answer:** c) Resize the hash table

### Question 3:
After rehashing a hash table from size 10 to size 20 with 11 items, what is the new load factor (¦Á)?
a) 0.5  
b) 0.55  
c) 1.0  
d) 1.1  
**Answer:** b) 0.55

### Question 4:
In a hash table of size 8 holding 6 items, what will happen if 3 more items are added?
a) The load factor will remain acceptable  
b) The hash table will need to be resized  
c) The hash table will overflow  
d) The performance will improve  
**Answer:** b) The hash table will need to be resized

### Question 5:
Consider the following code snippet for adding an item to a hash table. What will happen if the current size is 8 and it holds 8 items?
```python
def add_item(hash_table, item):
    if len(hash_table) / hash_table.size >= 1:
        hash_table.resize()
    hash_table.add(item)
```
a) The item will be added without any issues  
b) The hash table will resize before adding the item  
c) The function will throw an error  
d) The item will be ignored  
**Answer:** b) The hash table will resize before adding the item

### Question 6:
If a hash table has a load factor of 1.125 after adding an item, what is the next step?
a) Increase the size of the items  
b) Decrease the size of the hash table  
c) Rehash the items into a larger hash table  
d) Remove an item from the hash table  
**Answer:** c) Rehash the items into a larger hash table

---

