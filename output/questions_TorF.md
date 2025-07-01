# Hash Table

## Questions

1. Question: In a hash table, each key must be unique to avoid collisions. True or false?  
   Answer: True.

2. Question: A hash function can return the same index for different keys, leading to a collision. True or false?  
   Answer: True.

3. Question: If a hash table uses chaining for collision resolution, each index in the array can point to multiple records. True or false?  
   Answer: True.

4. Question: The hash function for a hash table must always return an index that is less than the size of the array. True or false?  
   Answer: True.

5. Question: In the example provided, if the student ID is 12345 and the hash function returns an index of 5, the record will be stored at index 5 in the array. True or false?  
   Answer: True.

6. Question: If a hash table uses the length of the key string as the hash function, keys with the same length will always be stored at different indices. True or false?  
   Answer: False.

7. Question: The process of searching for a record in a hash table is always faster than searching in a linked list. True or false?  
   Answer: False.

8. Question: In a hash table that uses chaining, if two keys collide, they will be stored in the same linked list at the same index. True or false?  
   Answer: True.

---

# Hash Function

## Questions

1. Question: A hash function that sums the ASCII values of characters in a string and takes the modulus with the size of the array is an example of a hash function. True or false?  
   Answer: True.

2. Question: If the input string is 'dog', the ASCII values are 100 (d) + 111 (o) + 103 (g) = 314. If the size of the array is 10, the hash value would be 314 % 10 = 4. True or false?  
   Answer: False. (The correct hash value is 314 % 10 = 4, but the statement is misleading as it implies the calculation is incorrect.)

3. Question: A hash function that returns the input value modulo the size of the array will always produce unique hash values for unique inputs. True or false?  
   Answer: False.

4. Question: In the example provided, both the inputs 15 and 25 produce the same hash value of 5 when the size of the array is 10. True or false?  
   Answer: True.

5. Question: If a hash function is designed to minimize collisions, it should ensure that different inputs always produce different hash values. True or false?  
   Answer: True.

6. Question: The hash value for the input string 'bat' with ASCII values 98 (b) + 97 (a) + 116 (t) and an array size of 10 would be 311 % 10 = 1. True or false?  
   Answer: False. (The correct hash value is 311 % 10 = 1, but the statement is misleading as it implies the calculation is incorrect.)

7. Question: A hash function that uses the input value directly without any transformation will always lead to a collision if the input values exceed the size of the array. True or false?  
   Answer: True.

---

# Applications of Hashing

## Questions

1. Question: In a compiler, a hash table is used to store symbol tables for efficient lookups and updates of identifiers. True or false?  
   Answer: True.

2. Question: A poorly designed hash function in a spell checker can lead to faster lookups and fewer incorrect suggestions. True or false?  
   Answer: False.

3. Question: The hash of an identifier's name is computed to find its entry in the symbol table during the compilation process. True or false?  
   Answer: True.

4. Question: If two different words hash to the same index in a hash table, it is known as a collision. True or false?  
   Answer: True.

5. Question: A hash table can only store integer values and cannot be used for strings or other data types. True or false?  
   Answer: False.

6. Question: In the context of a hash table, a collision resolution strategy is unnecessary if the hash function is perfect. True or false?  
   Answer: True.

7. Question: The efficiency of a hash table is unaffected by the number of collisions that occur. True or false?  
   Answer: False.

8. Question: The following code snippet correctly demonstrates how to insert a value into a hash table:
   ```python
   hash_table[key] = value
   ```
   True or false?  
   Answer: True.

---

# Hash Table

## Questions

1. Question: In a hash table, the student ID is used as the key to store student records. True or false?  
   Answer: True.

2. Question: When a new student is added to a hash table, their ID is stored at a random index in the array. True or false?  
   Answer: False.

3. Question: If a student ID hashes to index 5, the record can be retrieved in constant time by applying the same hash function to the ID again. True or false?  
   Answer: True.

4. Question: A hash table can experience collisions when multiple keys hash to the same index. True or false?  
   Answer: True.

5. Question: In the example provided, if the hash function returns the length of the key string modulo the size of the table, the keys 'cat', 'dog', and 'bat' will always hash to different indices. True or false?  
   Answer: False.

6. Question: Chaining is a method used to handle collisions in a hash table by linking entries that hash to the same index. True or false?  
   Answer: True.

7. Question: If many collisions occur in a hash table using chaining, the time complexity for searching for an entry can be O(1). True or false?  
   Answer: False.

8. Question: The worst-case time complexity for searching in a hash table with many collisions can be O(n), where n is the number of entries in the linked list at a given index. True or false?  
   Answer: True.

---

# Hashing

## Questions

1. Question: Hashing is a method used to create a unique key for data storage, ensuring that each piece of data can be retrieved quickly. True or false?  
   Answer: True.

2. Question: In a hash table, if two different inputs produce the same hash value, it is known as a hash collision. True or false?  
   Answer: True.

3. Question: The SHA-256 hash function will always produce the same hash value for the same input. True or false?  
   Answer: True.

4. Question: If the username 'john_doe' is hashed using SHA-256, it will produce a hash value that is guaranteed to be shorter than the original username. True or false?  
   Answer: False.

5. Question: In the context of hash tables, chaining is a method used to resolve hash collisions by linking entries that hash to the same index. True or false?  
   Answer: True.

6. Question: The following code snippet correctly demonstrates how to handle a hash collision using chaining in a hash table:
   ```python
   hash_table = {}
   def insert(username):
       hash_value = hash(username) % 10
       if hash_value in hash_table:
           hash_table[hash_value].append(username)
       else:
           hash_table[hash_value] = [username]
   ```
   True or false?  
   Answer: True.

7. Question: If a hash table has a load factor of 1.0, it means that the number of entries is equal to the number of buckets in the table. True or false?  
   Answer: True.

8. Question: Hash functions are designed to be reversible, allowing the original input to be retrieved from the hash value. True or false?  
   Answer: False.

---

# Key Universe

## Questions

1. Question: In a hash table that stores user information, the key universe includes all possible usernames that can be created, such as 'user1', 'admin', and 'guest'. True or false?  
   Answer: True.

2. Question: The key universe for a hash table storing product IDs formatted as 'PROD-XXXX' includes only the IDs that are currently in use. True or false?  
   Answer: False.

3. Question: If a hash table allows usernames to be alphanumeric and up to 20 characters long, the key universe would include every possible combination of letters and numbers within those constraints. True or false?  
   Answer: True.

4. Question: The actual usable key universe for a hash table can be larger than the theoretical key universe if certain keys are reserved for specific categories. True or false?  
   Answer: False.

5. Question: In the context of a hash table, the key universe is defined as the set of all possible keys that can be used, regardless of whether they are valid or reserved. True or false?  
   Answer: True.

---

# Slots in Hash Table

## Questions

1. Question: In a hash table with 10 slots, the hash function h(k) = k % 10 will store the key 15 in slot T[5]. True or false?  
   Answer: True.

2. Question: If a hash table uses chaining for collision resolution, multiple keys can be stored in the same slot as a linked list. True or false?  
   Answer: True.

3. Question: In the example provided, the keys 25 and 35 will be stored in separate slots from key 15 due to the use of open addressing. True or false?  
   Answer: False.

4. Question: When using the hash function h(k) = k % 5, the keys 1, 6, 11, and 16 will all hash to the same slot T[1]. True or false?  
   Answer: True.

5. Question: In the open addressing method, if T[1] is occupied, the next key will always be placed in T[2] regardless of its availability. True or false?  
   Answer: False.

6. Question: After inserting keys 1, 6, 11, and 16 into a hash table with 5 slots using open addressing, T[4] will contain the key 16. True or false?  
   Answer: True.

7. Question: The final state of the hash table after inserting the keys 1, 6, 11, and 16 will have T[1] = 1, T[2] = 6, T[3] = 11, and T[4] = 16. True or false?  
   Answer: True.

---

# Limitations of Hash Tables

## Questions

1. Question: A hash table allows for efficient retrieval of the minimum or maximum key without iterating through all entries. True or false?  
   Answer: False.

2. Question: If a hash table is used to store student records with their IDs as keys, finding the student with the highest ID requires iterating through all entries. True or false?  
   Answer: True.

3. Question: You can directly query a hash table to find all people aged between 20 and 30 without iterating through the entries. True or false?  
   Answer: False.

4. Question: A balanced tree structure is more efficient than a hash table for retrieving a range of values, such as ages between 20 and 30. True or false?  
   Answer: True.

5. Question: The order of keys in a hash table is maintained, allowing for quick retrieval of keys in sorted order. True or false?  
   Answer: False.

---

# Unrealistic Solution

## Questions

1. Question: A hash table that uses an array of size 1,000,000 to store only 10 elements has a space utilization of 0.001%. True or false?  
   Answer: True.

2. Question: Inserting, deleting, and searching for elements in a hash table with a large unused array size still takes O(1) time regardless of the number of elements stored. True or false?  
   Answer: True.

3. Question: If a hash table is designed to store user IDs ranging from 0 to 10,000,000 but only has 1,000 active users, the space utilization is 0.01%. True or false?  
   Answer: True.

4. Question: A hash table with a small number of elements compared to its array size is an example of an efficient use of space. True or false?  
   Answer: False.

5. Question: The following code snippet demonstrates an efficient use of space in a hash table:
   ```python
   hash_table = [None] * 10000000
   for i in range(1000):
       hash_table[i] = i
   ```
   True or false?  
   Answer: False.

---

# Hash Function

## Questions

1. Question: In a hash table of size 10, the keys 15, 25, and 35 will all produce different hash values when using the hash function Hash(key) = key % 10. True or false?  
   Answer: False.

2. Question: A hash function that takes a string as input and computes the hash value by summing the ASCII values of the characters can lead to collisions if different strings produce the same sum. True or false?  
   Answer: True.

3. Question: The hash function Hash(key) = key % 10 will always produce unique hash values for unique integer keys. True or false?  
   Answer: False.

4. Question: If two different strings 'abc' and 'cab' produce the same hash value using the hash function that sums their ASCII values, it is an example of a collision. True or false?  
   Answer: True.

5. Question: In the example provided, Hash(15), Hash(25), and Hash(35) all map to the same index in the hash table, demonstrating that the hash function is effective. True or false?  
   Answer: False.

---

# Hash Table Size

## Questions

1. Question: A hash table can be effectively sized to hold fewer entries than the total number of possible keys in the universe. True or false?  
   Answer: True.

2. Question: If a hash table is designed to store user IDs and has a size of 1 million entries, it can store all possible user IDs if the universe of possible user IDs is 1 billion. True or false?  
   Answer: False.

3. Question: In a hash table with a size of 500,000 entries, if the universe of possible email addresses is 2 billion, it is guaranteed that there will be no collisions. True or false?  
   Answer: False.

4. Question: The efficiency of a hash table can be affected by the number of collisions that occur when storing keys. True or false?  
   Answer: True.

5. Question: The following code snippet correctly initializes a hash table with a size of 1 million entries in Python:
   ```python
   hash_table = [None] * 1000000
   ```
   True or false?  
   Answer: True.

---

# Hash Value

## Questions

1. Question: The hash value for the key k = 23 using the hash function h(k) = k mod 10 is 3. True or false?  
   Answer: True.

2. Question: In a hash table of size 5, the hash value for the key k = 4 using the hash function h(k) = (k * 3 + 1) mod 5 is 4. True or false?  
   Answer: False.

3. Question: The hash function h(k) = (k * 3 + 1) mod 5 can produce the same hash value for different keys. True or false?  
   Answer: True.

4. Question: If we use the hash function h(k) = k mod 10, the key k = 15 will have a hash value of 5. True or false?  
   Answer: False.

5. Question: A good hash function should minimize collisions, meaning that different keys should ideally map to different hash values. True or false?  
   Answer: True.

---

# Collision Problem

## Questions

1. Question: In a simple hash function that returns the remainder when divided by 10, hashing the keys 12 and 22 results in a collision. True or false?  
   Answer: True.

2. Question: The hash function h(key) = (key * 7 + 3) % 10 produces a collision when hashing the keys 1 and 4. True or false?  
   Answer: False.

3. Question: If we hash the key 6 using the function h(key) = (key * 7 + 3) % 10, the result is 5. True or false?  
   Answer: True.

4. Question: The keys 4 and 13 hash to the same slot using the hash function h(key) = (key * 7 + 3) % 10, indicating a collision. True or false?  
   Answer: True.

5. Question: A collision occurs when two different keys hash to different slots in a hash table. True or false?  
   Answer: False.

---

# Hash Function Design

## Questions

1. Question: The SHA-256 algorithm produces a variable-size hash value based on the input message. True or false?  
   Answer: False.

2. Question: A good hash function should minimize collisions, meaning that different inputs should ideally produce different hash values. True or false?  
   Answer: True.

3. Question: Using the simple modulo operation as a hash function guarantees that all inputs will produce unique hash values. True or false?  
   Answer: False.

4. Question: The string 'Hello, World!' will always produce the same hash value when hashed using SHA-256. True or false?  
   Answer: True.

5. Question: If two different strings, 'abc' and 'cab', produce the same hash value using a naive hash function, it indicates a collision. True or false?  
   Answer: True.

6. Question: The efficiency of a hash function is irrelevant when it comes to applications like blockchain technology. True or false?  
   Answer: False.

7. Question: The output of a hash function can be used to verify the integrity of data. True or false?  
   Answer: True.

---

# Hash Function Example

## Questions

1. Question: In a hash table of size m = 10, the key k = 23 will be stored at index 3 after calculating the hash value as h(23) = 23 mod 10. True or false?  
   Answer: True.

2. Question: If we have a hash table of size m = 5 and we insert the key k = 15, the hash value will be calculated as h(15) = 15 mod 5 = 1. True or false?  
   Answer: False.

3. Question: In the scenario where both keys k = 15 and k = 5 are inserted into a hash table of size m = 5, they will both be stored at index 0 due to a collision. True or false?  
   Answer: True.

4. Question: The hash function h(k) = k mod m will always produce unique hash values for different keys k in a hash table of size m. True or false?  
   Answer: False.

5. Question: If we have a hash table of size m = 10 and we insert the key k = 30, the hash value will be calculated as h(30) = 30 mod 10 = 0. True or false?  
   Answer: True.

---

# Avoiding Certain Values of m

## Questions

1. Question: Choosing a modulus value of m = 16 for a hash function will lead to a uniform distribution of hash values. True or false?  
   Answer: False.

2. Question: Using a modulus value of m = 15, which is not a power of 2 or 10, can improve the distribution of hash values in a hash table. True or false?  
   Answer: True.

3. Question: If you use m = 100 for a hash table, it is guaranteed that there will be no collisions. True or false?  
   Answer: False.

4. Question: Selecting m = 99 instead of m = 100 can help reduce the number of collisions in a hash table. True or false?  
   Answer: True.

5. Question: The choice of modulus value m in a hash function has no impact on the performance of the hash table. True or false?  
   Answer: False.

---

# Using Prime Numbers for m

## Questions

1. Question: A hash table with a size of 11, which is a prime number, is less likely to have collisions compared to a hash table with a size of 10, which is not prime. True or false?  
   Answer: True.

2. Question: Choosing a hash table size of 15, which is not a prime number, guarantees that there will be no collisions when hashing keys. True or false?  
   Answer: False.

3. Question: If a hash table has a size of 13, it is guaranteed that all keys will hash to unique indices. True or false?  
   Answer: False.

4. Question: A prime number has exactly two distinct positive divisors: 1 and itself. True or false?  
   Answer: True.

5. Question: The following code snippet will create a hash table with a size of 9, which is not a prime number:
   ```python
   hash_table = [None] * 9
   ```
   True or false?  
   Answer: True.

6. Question: Using a prime number as the size of a hash table can help in achieving a more uniform distribution of hashed keys. True or false?  
   Answer: True.

7. Question: If two different keys hash to the same index in a hash table, it is called a collision. True or false?  
   Answer: True.

8. Question: The number 21 is a prime number because it can only be divided by 1 and 21. True or false?  
   Answer: False.

---

# Example of Good m Value

## Questions

1. Question: In a hash table designed to store 2,000 integers, choosing m = 701 will result in an average of 3 collisions per slot. True or false?  
   Answer: True.

2. Question: The load factor (¦Ë) is calculated as ¦Ë = n/m, where n is the number of entries and m is the number of slots in the hash table. True or false?  
   Answer: True.

3. Question: If a hash function maps many integers to the same index, it can lead to fewer collisions than expected, regardless of the value of m. True or false?  
   Answer: False.

4. Question: A poor hash function can negate the benefits of choosing an appropriate m value in a hash table. True or false?  
   Answer: True.

5. Question: If we have a hash table with m = 701 and we use a hash function that returns the last three digits of a number, it is guaranteed that we will have at most 3 collisions. True or false?  
   Answer: False.

6. Question: The choice of m in a hash table is the only factor that affects the number of collisions. True or false?  
   Answer: False.

---

# String Keys in Hashing

## Questions

1. Question: The string 'cat' can be represented by the natural number 312 in a hashing context based on the sum of its ASCII values. True or false?  
   Answer: True.

2. Question: The ASCII values for the characters 'a', 'b', and 'c' are 97, 98, and 99 respectively, and the sum of these values is 294. True or false?  
   Answer: True.

3. Question: The strings 'abc' and 'cab' will hash to different values when using the sum of their ASCII values. True or false?  
   Answer: False.

4. Question: A collision in a hash table occurs when two different strings hash to the same value. True or false?  
   Answer: True.

5. Question: The ASCII value for the character 't' is 116, which contributes to the hash value of the string 'cat'. True or false?  
   Answer: True.

---

# Hash Function Limitations

## Questions

1. Question: A good hash function should produce the same hash value for different inputs that contain the same characters in different orders. True or false?  
   Answer: False.

2. Question: The hash function SHA-256 will produce different hash values for the strings 'abc' and 'acb'. True or false?  
   Answer: True.

3. Question: A poorly designed hash function can lead to many collisions, where different inputs yield the same hash value. True or false?  
   Answer: True.

4. Question: If a hash function produces the same hash value for all permutations of the string 'abc', it is considered a good hash function. True or false?  
   Answer: False.

5. Question: The following code snippet demonstrates a good hash function: 
   ```python
   def poor_hash(input_string):
       return '12345'
   ```
   True or false?  
   Answer: False.

---

# Example of Key Range

## Questions

1. Question: In a hash table with a size of m = 10,007, the index for the key 'banana' can be greater than 10,006. True or false?  
   Answer: False.

2. Question: If a hash function simply returns the key itself, a key of 10,007 will result in a valid index for a hash table of size 10,007. True or false?  
   Answer: False.

3. Question: The indices generated by a hash function for string keys must always fall within the range of 0 to m-1, where m is the size of the hash table. True or false?  
   Answer: True.

4. Question: If the key 'apple' hashes to index 1234 in a hash table of size 10,007, it is guaranteed that the key 'cherry' will hash to a different index. True or false?  
   Answer: False.

5. Question: A hash function that maps a numeric key of 1,016 to an index of 1,016 is valid for a hash table of size 10,007. True or false?  
   Answer: True.

---

# Hash Function Method 2

## Questions

1. Question: The hash function h(key) = (key[0] + 27¡¤key[1] + 272¡¤key[2]) mod m will always produce the same hash value for keys that are anagrams of each other. True or false?  
   Answer: False.

2. Question: In the example provided, the hash value for the key 'cat' is calculated to be 2. True or false?  
   Answer: True.

3. Question: The ASCII value of the character 'a' is 97, which is used in the hash function calculation for the key 'cat'. True or false?  
   Answer: True.

4. Question: The hash value for the key 'dog' is 0, according to the calculations provided. True or false?  
   Answer: False.

5. Question: The hash function h(key) can lead to different hash values for the keys 'dog' and 'god', demonstrating the importance of character arrangement in hashing. True or false?  
   Answer: True.

6. Question: If the size of the hash table is m = 10, the maximum possible hash value generated by the function h(key) is 9. True or false?  
   Answer: True.

---

# Limitations of Method 2

## Questions

1. Question: If a hash table is sized at 10,007 and only 2,851 unique combinations are possible from the first three letters of English words, then approximately 72% of the hash table will be utilized effectively. True or false?  
   Answer: False.

2. Question: In a hash table where words are hashed based on their first three letters, the words 'apple', 'apricot', and 'application' will hash to different indices. True or false?  
   Answer: False.

3. Question: A hash table that only considers the first three letters of words can lead to many empty slots due to the limited number of unique combinations. True or false?  
   Answer: True.

4. Question: If a hash function is designed to only use the first three letters of a word, it can create a unique hash for every English word. True or false?  
   Answer: False.

5. Question: The following code snippet will create a hash table that can store all possible combinations of the first three letters of English words:
   ```python
   hash_table = [None] * 10007
   ```
   True or false?  
   Answer: False.

---

# Hash Function Method 3

## Questions

1. Question: The hash value for the key 'abc' is calculated as 698 using the given hash function method. True or false?  
   Answer: True.

2. Question: The ASCII value of the character 'b' is 98, and it is used in the hash calculation for the key 'abc'. True or false?  
   Answer: True.

3. Question: In the hash function calculation for the key 'aab', the weighted sum for the first character 'a' is 132973. True or false?  
   Answer: True.

4. Question: The hash value for the key 'aab' is the same as the hash value for the key 'abc'. True or false?  
   Answer: False.

5. Question: The modulus operation in the hash function is applied to ensure that the hash value remains within a certain range. True or false?  
   Answer: True.

6. Question: The weighted sum for the second character in the key 'aab' is calculated as 37^1 * 98. True or false?  
   Answer: False (it should be 37^1 * 97).

7. Question: The hash function method described uses a base of 37 for the calculations. True or false?  
   Answer: True.

8. Question: The final hash value for the key 'abc' is obtained by summing the weighted sums and applying the modulus operation with m = 500. True or false?  
   Answer: False (it should be m = 1000).

---

# Expected Distribution of Method 3

## Questions

1. Question: Method 3 in a hash table is designed to produce hash values that evenly distribute user IDs across the table. True or false?  
   Answer: True.

2. Question: If user IDs range from 1 to 1000, Method 3 guarantees that each index from 0 to 999 will be filled exactly equally. True or false?  
   Answer: False.

3. Question: A well-designed hashing function in Method 3 will prevent clustering in the hash table, ensuring efficient retrieval. True or false?  
   Answer: True.

4. Question: If two email addresses hash to the same index in a hash table using Method 3, it indicates that the hashing function is well-designed. True or false?  
   Answer: False.

5. Question: The expected outcome of Method 3 is to minimize collisions in the hash table. True or false?  
   Answer: True.

6. Question: In a poorly designed hashing function, similar inputs can lead to different hash values, which is desirable for even distribution. True or false?  
   Answer: False.

7. Question: The performance of a hash table using Method 3 can degrade if certain indices become overloaded with entries due to poor hash value distribution. True or false?  
   Answer: True.

---

# Separate Chaining

## Questions

1. Question: In a hash table using separate chaining, if multiple keys hash to the same index, they are stored in a linked list at that index. True or false?  
   Answer: True.

2. Question: If a hash table has a size of 5 and we insert the keys 10, 15, 20, and 25, they will be stored in separate indices due to their unique hash values. True or false?  
   Answer: False.

3. Question: In the example of a hash table of size 3, inserting the keys 3, 6, and 9 will result in a linked list at index 0 containing the nodes for keys 3, 6, and 9. True or false?  
   Answer: True.

4. Question: When retrieving a key from a hash table that uses separate chaining, if the key is at the end of the linked list, it will take longer to find compared to a key at the beginning of the list. True or false?  
   Answer: True.

5. Question: The following code snippet correctly demonstrates the insertion of keys into a hash table using separate chaining:
   ```python
   class Node:
       def __init__(self, key):
           self.key = key
           self.next = None

   class HashTable:
       def __init__(self, size):
           self.size = size
           self.table = [None] * size

       def insert(self, key):
           index = key % self.size
           new_node = Node(key)
           if self.table[index] is None:
               self.table[index] = new_node
           else:
               current = self.table[index]
               while current.next:
                   current = current.next
               current.next = new_node
   ```
   True or false?  
   Answer: True.

6. Question: In separate chaining, if a hash table has a low load factor, it guarantees that all keys will be stored in separate indices without any collisions. True or false?  
   Answer: False.

---

# Hash Function

## Questions

1. Question: The hash function h(k) = k mod 10 will store the key 27 at index 7 in a hash table of size 10. True or false?  
   Answer: True.

2. Question: Using the hash function h(k) = k mod 10, the key 20 will be stored at index 2 in a hash table of size 10. True or false?  
   Answer: False.

3. Question: If both keys 20 and 30 are stored in a hash table using the hash function h(k) = k mod 10, they will both occupy index 0, resulting in a collision. True or false?  
   Answer: True.

4. Question: A collision in a hash table can be resolved using methods such as chaining or open addressing. True or false?  
   Answer: True.

5. Question: The hash function h(k) = k mod 10 will always produce unique indices for every key stored in the hash table. True or false?  
   Answer: False.

---

# Insertion Operation

## Questions

1. Question: When inserting the key k = 15 into a hash table with a size of 10 using the hash function h(k) = k % 10, the linked list at index 5 will contain the element 15 after the insertion. True or false?  
   Answer: True.

2. Question: If we insert the key k = 25 into the same hash table, the linked list at index 5 will contain only the element 25 after the insertion. True or false?  
   Answer: False.

3. Question: When inserting a duplicate key k = 15 into the linked list at index 5, the linked list will automatically contain two instances of the element 15. True or false?  
   Answer: False.

4. Question: The hash function h(k) = k % 10 will always produce a unique index for every unique key k in a hash table of size 10. True or false?  
   Answer: False.

5. Question: In a hash table, if the linked list at a computed index is empty, a new linked list is created to store the first element. True or false?  
   Answer: True.

---

# Deletion Operation

## Questions

1. Question: In a hash table with a size of 10 and a hash function h(k) = k % 10, deleting the key k = 23 will result in the linked list at index 3 containing the keys [13, 23, 33]. True or false?  
   Answer: False.

2. Question: When deleting a key from a hash table, it is necessary to update the head of the linked list if the key being deleted is the first element in the list. True or false?  
   Answer: True.

3. Question: If a hash table has a size of 5 and the hash function is h(k) = k % 5, deleting the key k = 10 will always result in the linked list at index 0 being empty. True or false?  
   Answer: False.

4. Question: In the example where the linked list at index 0 contains the keys [10, 15, 20], after deleting the key 10, the linked list will be updated to [15, 20]. True or false?  
   Answer: True.

5. Question: The deletion operation in a hash table does not require traversing the linked list if the key to be deleted is located at the end of the list. True or false?  
   Answer: False.

---

# Separate Chaining

## Questions

1. Question: In separate chaining, if multiple keys hash to the same index, they are stored in a linked list at that index. True or false?  
   Answer: True.

2. Question: If a hash table has a size of 10 and we insert the keys 15, 25, and 35, they will hash to different indices. True or false?  
   Answer: False.

3. Question: In the example provided, the linked list at index 5 after inserting keys 15, 25, and 35 would be represented as 15 -> 25 -> 35. True or false?  
   Answer: True.

4. Question: Searching for a key in a linked list at a hash table index takes constant time on average, regardless of the length of the list. True or false?  
   Answer: False.

5. Question: If we have a hash table of size 5 and insert the keys 5, 10, 15, and 20, they will all be stored in a single linked list at index 0. True or false?  
   Answer: True.

6. Question: A poor hash function can lead to performance degradation in separate chaining by causing many keys to hash to the same index. True or false?  
   Answer: True.

7. Question: The time complexity for searching a key in a linked list can be constant time if the list is short. True or false?  
   Answer: True.

8. Question: The hash function used in the tricky example is defined as `key % 5`. True or false?  
   Answer: True.

---

# Advantages of Separate Chaining

## Questions

1. Question: In a hash table using separate chaining, each index of the table contains a linked list of entries that hash to the same index. True or false?  
   Answer: True.

2. Question: Deleting an entry from a linked list in a hash table using separate chaining requires traversing the entire list, regardless of the position of the entry. True or false?  
   Answer: False.

3. Question: If a hash table index contains a linked list of entries (A -> B -> C), deleting entry B involves adjusting the pointers so that A now points directly to C. True or false?  
   Answer: True.

4. Question: In a hash table with separate chaining, if we want to delete an entry located deep within a long linked list, we do not need to keep track of the previous node. True or false?  
   Answer: False.

5. Question: If we mistakenly delete the wrong node in a linked list during a deletion operation, it can lead to a broken list or lost entries. True or false?  
   Answer: True.

6. Question: The following code snippet correctly deletes the second node from a linked list in a hash table:
   ```python
   def delete_node(head, key):
       if head is None:
           return None
       if head.data == key:
           return head.next
       current = head
       while current.next is not None:
           if current.next.data == key:
               current.next = current.next.next
               return head
           current = current.next
       return head
   ```
   True or false?  
   Answer: True.

---

# Disadvantages of Separate Chaining

## Questions

1. Question: In a hash table using separate chaining, each bucket contains a linked list of entries. True or false?  
   Answer: True.

2. Question: Frequent resizing of a hash table using separate chaining can lead to memory fragmentation. True or false?  
   Answer: True.

3. Question: If a hash table with separate chaining is used to store user sessions, the linked lists in each bucket will never grow or shrink. True or false?  
   Answer: False.

4. Question: The constant allocation and deallocation of memory in a hash table using separate chaining can improve the overall performance of the hash table operations. True or false?  
   Answer: False.

5. Question: In a scenario where many users log in and out rapidly, the performance of a hash table using separate chaining may be negatively impacted due to inefficient memory management. True or false?  
   Answer: True.

6. Question: The following code snippet correctly implements a bucket in a hash table using separate chaining:
   ```python
   class Bucket:
       def __init__(self):
           self.entries = []
   ```
   True or false?  
   Answer: True.

7. Question: In a hash table with separate chaining, if the linked lists become long, it can lead to faster search times. True or false?  
   Answer: False.

---

# Open Addressing

## Questions

1. Question: In open addressing, if a hash table index is occupied, the next index checked for insertion is always the next sequential index. True or false?  
   Answer: True.

2. Question: In the example provided, when inserting the keys 12, 22, and 32 into a hash table of size 10, the final arrangement of the table is [ , , 12, 22, 32, , , , , ]. True or false?  
   Answer: True.

3. Question: If a hash table of size 5 uses a hash function that returns the key modulo 5, inserting the keys 5, 10, and 15 will result in the final table arrangement being [5, 10, 15, , ]. True or false?  
   Answer: True.

4. Question: In the tricky example, if the keys are inserted in the order of 15, 5, and then 10, the final arrangement of the hash table will be [15, 5, 10, , ]. True or false?  
   Answer: True.

5. Question: Open addressing allows for multiple keys to occupy the same index in a hash table. True or false?  
   Answer: False.

6. Question: The order of key insertions does not affect the final arrangement of the hash table when using open addressing. True or false?  
   Answer: False.

7. Question: In the context of open addressing, if a key hashes to an occupied index, the algorithm will always find an empty index by checking the next index in a circular manner. True or false?  
   Answer: True.

---

# Collision Handling in Open Addressing

## Questions

1. Question: In linear probing, if a key hashes to an occupied index, we check the next slot sequentially until we find a free slot. True or false?  
   Answer: True.

2. Question: In quadratic probing, if a key hashes to an occupied index, we check the next slot by adding the square of the probe number to the original index. True or false?  
   Answer: True.

3. Question: If a hash table using linear probing has a load factor of 1.0, it means that every slot in the table is occupied. True or false?  
   Answer: True.

4. Question: In the example of quadratic probing, if the key '15' hashes to index 3 and the first two slots checked are occupied, the next slot checked will be index 6. True or false?  
   Answer: False. (The next slot checked would be index 7, calculated as 3 + 2^2.)

5. Question: In a hash table using linear probing, if two different keys hash to the same index, they will always end up in the same slot after probing. True or false?  
   Answer: False. (They will follow the same probing sequence but may end up in different slots depending on the order of insertion and availability of slots.)

6. Question: The probing sequence in quadratic probing can lead to clustering issues, where multiple keys end up in the same area of the hash table. True or false?  
   Answer: True.

---

# Hash Function Example

## Questions

1. Question: The hash function defined as hash(k) = k mod 10 will store the key 27 at index 7 in the hash table. True or false?  
   Answer: True.

2. Question: Using the hash function hash(k) = k mod 10, the key 20 will be stored at index 0 in the hash table. True or false?  
   Answer: True.

3. Question: If both keys 20 and 30 are stored using the hash function hash(k) = k mod 10, they will occupy different indices in the hash table. True or false?  
   Answer: False.

4. Question: A collision occurs in a hash table when two different keys hash to the same index. True or false?  
   Answer: True.

5. Question: The hash function hash(k) = k mod 10 will always produce unique indices for every integer key. True or false?  
   Answer: False.

6. Question: To resolve a collision in a hash table, one can use strategies such as chaining or open addressing. True or false?  
   Answer: True.

---

# Open Addressing

## Questions

1. Question: In open addressing, when a collision occurs, the next available slot is always found by checking the next index sequentially. True or false?  
   Answer: True.

2. Question: In the example provided, the final hash table after inserting the keys 12, 22, and 32 using open addressing will look like this: [ , , 12, 22, 32, , , , , ]. True or false?  
   Answer: False.

3. Question: When using a hash function that returns the key modulo 5, inserting the keys 5, 10, and 15 will result in all keys being placed at index 0. True or false?  
   Answer: False.

4. Question: In the tricky example, after inserting the keys 5, 10, and 15, the final hash table will look like this: [5, 10, 15, , ]. True or false?  
   Answer: True.

5. Question: Open addressing can lead to a linear distribution of keys in a hash table. True or false?  
   Answer: False.

---

# Relocation Scheme

## Questions

1. Question: In a hash table using chaining for collision resolution, each index can contain multiple keys stored in a linked list. True or false?  
   Answer: True.

2. Question: In open addressing with linear probing, if a key hashes to an occupied index, it will always go to the next available slot. True or false?  
   Answer: True.

3. Question: If keys 'A', 'B', and 'C' hash to index 2 in a hash table using open addressing, 'C' will be placed at index 2. True or false?  
   Answer: False.

4. Question: Chaining in a hash table can lead to longer search times if many keys hash to the same index. True or false?  
   Answer: True.

5. Question: In the following code snippet, if keys 'A' and 'B' hash to index 3, the linked list at index 3 will contain 'B' -> 'A'. 
   ```python
   hash_table[3] = ['A', 'B']
   ```
   True or false?  
   Answer: False.

6. Question: Clustering in a hash table occurs when a sequence of filled slots leads to longer search times, particularly in open addressing methods. True or false?  
   Answer: True.

---

# Searching for Key

## Questions

1. Question: In a hash table with a size of 10, if we insert keys 12, 22, and 32 using a hash function that returns the remainder of the key divided by 10, they will all hash to the same index. True or false?  
   Answer: True.

2. Question: When using linear probing to resolve collisions in a hash table, if the first key is placed at index 2, the second key will always be placed at index 3, regardless of the keys being inserted. True or false?  
   Answer: False.

3. Question: In a hash table of size 5, if we insert keys 5, 10, and 15 using a hash function that returns the key modulo 5, all three keys will hash to index 0. True or false?  
   Answer: True.

4. Question: If we use quadratic probing to resolve collisions and place the first key at index 0, the second key will be placed at index 1. True or false?  
   Answer: True.

5. Question: When searching for key 15 in the hash table described, if we had used linear probing instead of quadratic probing, the search would be more straightforward. True or false?  
   Answer: False.

---

# Collision Resolution Strategies

## Questions

1. Question: In linear probing, if a hash table has a size of 10 and a key hashes to index 5, it will check index 6, then index 7, and then index 8 for an empty slot. True or false?  
   Answer: True.

2. Question: In quadratic probing, if a key hashes to index 5 and index 5 is occupied, the next index checked will be index 6 (5 + 1^2). True or false?  
   Answer: True.

3. Question: In quadratic probing, if the first index checked is occupied, the next index checked will always be the next sequential index. True or false?  
   Answer: False.

4. Question: If a hash table has a size of 10 and a key hashes to index 5, in linear probing, it will check indices in a circular manner starting from index 5. True or false?  
   Answer: True.

5. Question: In quadratic probing, if the key '15' hashes to index 5 and both index 5 and index 9 are occupied, it will check index 4 next. True or false?  
   Answer: True.

6. Question: In linear probing, if a key hashes to an index that is already occupied, it will skip that index and check the next index without wrapping around the table. True or false?  
   Answer: False.

7. Question: In a hash table using quadratic probing, if the size of the table is 10, the maximum number of indices that will be checked for a single insertion is limited to 10. True or false?  
   Answer: True.

---

# Linear Probing

## Questions

1. Question: In linear probing, if a key hashes to an occupied index, the next index checked will always be the next consecutive index. True or false?  
   Answer: True.

2. Question: In the example provided, when inserting the key 22 into the hash table, it is placed at index 3 because index 2 is occupied. True or false?  
   Answer: True.

3. Question: In the tricky example, when inserting the key 20, it is placed at index 3 because both index 0 and index 1 are occupied. True or false?  
   Answer: True.

4. Question: If a hash table has a size of 5 and we insert keys that all hash to index 0, the final state of the hash table will have no empty cells. True or false?  
   Answer: False.

5. Question: The final state of the hash table in the typical example is [ , , 12, 22, 32, , , , , ]. True or false?  
   Answer: False (the correct final state is [ , , 12, 22, 32, , , , , ] with only the first five indices filled).

6. Question: Linear probing can lead to clustering, which may increase the time complexity for future insertions. True or false?  
   Answer: True.

7. Question: The hash function used in the tricky example is defined as `key % 5`. True or false?  
   Answer: True.

8. Question: In the typical example, the keys 12, 22, and 32 all hash to the same index due to the hash function used. True or false?  
   Answer: True.

---

# Quadratic Probing

## Questions

1. Question: In quadratic probing, if a collision occurs at index 2, the first probe will always be at index 3. True or false?  
   Answer: False.

2. Question: When using the hash function h(k) = k % 10, the key 22 will be inserted at index 3 after a collision occurs at index 2. True or false?  
   Answer: True.

3. Question: In the example provided, the key 32 is inserted at index 6 after two probing attempts. True or false?  
   Answer: True.

4. Question: In the tricky example, the key 24 is inserted at index 0 after one probing attempt. True or false?  
   Answer: False.

5. Question: The probing sequence for the key 17 in the tricky example is 3, 4. True or false?  
   Answer: True.

6. Question: Quadratic probing can lead to a situation where the probing sequence wraps around the hash table. True or false?  
   Answer: True.

7. Question: If a hash table of size 7 is used, the maximum number of probes needed for a single key insertion is always 7. True or false?  
   Answer: False.

---

# Double Hashing

## Questions

1. Question: In double hashing, the primary hash function is used to determine the initial index for a key, while the secondary hash function is used to resolve collisions. True or false?  
   Answer: True.

2. Question: If the primary hash function h1(x) = x % 10 results in a collision, the secondary hash function h2(x) = 7 - (x % 7) is always guaranteed to produce a unique index for each key. True or false?  
   Answer: False.

3. Question: In the example provided, the key 22 is placed in index 4 of the hash table after resolving the collision. True or false?  
   Answer: True.

4. Question: The secondary hash function h2(x) = 1 + (x % 9) will always produce a value between 1 and 9 for any integer x. True or false?  
   Answer: False.

5. Question: In the tricky example, the final hash table after inserting keys 10, 20, and 30 is [10, _, 20, _, 30, _, _, _, _, _]. True or false?  
   Answer: True.

6. Question: If a fourth key, 40, is inserted into the hash table after 10, 20, and 30, it will not cause any additional collisions since it hashes to index 0. True or false?  
   Answer: False.

7. Question: The final hash table after inserting the keys 12, 22, and 32 is [32, _, _, _, 22, _, 12, _, _, _]. True or false?  
   Answer: True.

8. Question: The secondary hash function h2(x) = 7 - (x % 7) can produce negative values for certain inputs. True or false?  
   Answer: True.

---

# Probing Sequence

## Questions

1. Question: In a hash table using linear probing, if a collision occurs at index 5, the algorithm will check index 6 first. True or false?  
   Answer: True.

2. Question: In a hash table using quadratic probing, if a collision occurs at index 3, the algorithm will check index 4 first. True or false?  
   Answer: True.

3. Question: In a hash table using linear probing, if a collision occurs at index 5, the algorithm will check index 7 before checking index 6. True or false?  
   Answer: False.

4. Question: In a hash table using quadratic probing, if a collision occurs at index 3, the algorithm will check index 6 (3 + 1^2 + 1^2) next. True or false?  
   Answer: False.

5. Question: The probing sequence in linear probing always checks the next consecutive index until an empty cell is found. True or false?  
   Answer: True.

6. Question: In a hash table using quadratic probing, the probing sequence can potentially skip over empty cells. True or false?  
   Answer: True.

---

# Function f(i)

## Questions

1. Question: In open addressing for hash tables, linear probing means that the probing function f(i) is defined as f(i) = i. True or false?  
   Answer: True.

2. Question: If a hash function h(i) returns the initial index and the probing function f(i) is defined as f(i) = i, the probing sequence will always find an empty slot without wrapping around. True or false?  
   Answer: False.

3. Question: In the example where h(i) = (key + i) mod 7, if the keys 10, 17, and 24 all hash to the same index, it indicates a collision. True or false?  
   Answer: True.

4. Question: The probing function f(i) defined as f(i) = (i^2) mod 7 will always produce a linear probing sequence. True or false?  
   Answer: False.

5. Question: Given the hash function h(0) = 3 and a table size of 10, the probing sequence for the first index will be 3, 4, 5, 6, 7, 8, 9, 0, 1, 2. True or false?  
   Answer: True.

6. Question: In the probing sequence defined by f(i) = (i^2) mod 7, it is possible for some indices to be checked multiple times before finding an empty slot. True or false?  
   Answer: True.

---

# Linear Probing

## Questions

1. Question: In linear probing, if a hash table index is occupied, the next index checked is always the next sequential index. True or false?  
   Answer: True.

2. Question: In the example provided, when inserting the keys 12, 22, and 32 into a hash table of size 10, all three keys will be placed in index 2. True or false?  
   Answer: False.

3. Question: The final state of the hash table after inserting the keys 12, 22, and 32 is [ , , 12, 22, 32, , , , , ]. True or false?  
   Answer: True.

4. Question: If a hash table has a size of 5 and a hash function that returns the key modulo 5, inserting the keys 5, 10, and 15 will result in all keys being placed in index 0. True or false?  
   Answer: True.

5. Question: In the tricky example, after inserting the keys 5, 10, and 15, the final state of the hash table is [5, 10, 15, , ]. True or false?  
   Answer: True.

6. Question: The choice of hash function does not affect the performance of linear probing. True or false?  
   Answer: False.

7. Question: In the context of linear probing, if a collision occurs, the algorithm will always check the next index in a circular manner. True or false?  
   Answer: False.

---

# Hash Function

## Questions

1. Question: The hash function defined as hash(k) = k mod 10 will always produce unique indices for every key. True or false?  
   Answer: False.

2. Question: When hashing the key 23 using the function hash(k) = k mod 10, the resulting index is 3. True or false?  
   Answer: True.

3. Question: Using the hash function hash(k) = k mod 10, both keys 30 and 40 will produce the same index of 0, resulting in a collision. True or false?  
   Answer: True.

4. Question: If we hash the key 15 using the function hash(k) = k mod 10, the index will be 5. True or false?  
   Answer: True.

5. Question: The hash function hash(k) = k mod 10 can be used to hash negative keys, and it will always return a non-negative index. True or false?  
   Answer: False.

---

# Insertion Process

## Questions

1. Question: The hash function used in the example is `hash(key) = key % table_size`. True or false?  
   Answer: True.

2. Question: When inserting the key 15 into the hash table, it is placed at index 5. True or false?  
   Answer: False.

3. Question: After inserting the keys 25, 15, and 35, the hash table looks like this: [ , , , , , 25, 15, 35, , ]. True or false?  
   Answer: False.

4. Question: If we try to insert a key that hashes to 5 again, like 5, we will check indices 5, 6, and 7 before finding an empty slot at index 8. True or false?  
   Answer: True.

5. Question: Once all slots in the hash table are occupied, further insertions will succeed without any errors. True or false?  
   Answer: False.

6. Question: The hash table size in the example is 10. True or false?  
   Answer: True.

7. Question: The final state of the hash table after inserting keys 25, 15, 35, and 5 is [ , , , , , 25, 15, 35, 5, ]. True or false?  
   Answer: True.

---

# Probing Sequence

## Questions

1. Question: In a hash table with size m = 10, the keys 12, 22, and 32 will all be inserted at index 2 due to the same hash value. True or false?  
   Answer: False.

2. Question: When inserting the key 22 into a hash table with size m = 10, it will be placed at index 3 after probing. True or false?  
   Answer: True.

3. Question: In the probing sequence for key 32 in a hash table of size m = 10, the first index checked is 2. True or false?  
   Answer: True.

4. Question: In a hash table with size m = 5, inserting the keys 5, 10, and 15 will result in all keys being placed at index 0. True or false?  
   Answer: False.

5. Question: The probing sequence for key 10 in a hash table of size m = 5 will result in it being inserted at index 1. True or false?  
   Answer: True.

6. Question: If a hash function returns the key modulo the size of the hash table, it guarantees that there will be no collisions. True or false?  
   Answer: False.

7. Question: In the case of the hash table with size m = 5, the key 15 will be inserted at index 2 after probing. True or false?  
   Answer: True.

---

# Example of Insertion

## Questions

1. Question: In a hash table of size 10, the key 49 will be placed at index 9 when using the hash function h(key) = key % 10. True or false?  
   Answer: False.

2. Question: When inserting the key 58 into a hash table of size 10, it will be placed at index 8 if that index is empty. True or false?  
   Answer: True.

3. Question: In the first example, the key 69 is placed at index 2 after probing through indices 9, 0, and 1. True or false?  
   Answer: True.

4. Question: In the tricky example with a hash table of size 5, the key 49 is placed at index 0 after probing. True or false?  
   Answer: True.

5. Question: The hash function h(key) = key % 5 will always result in unique indices for the keys 89, 18, 49, 58, and 69 in a hash table of size 5. True or false?  
   Answer: False.

6. Question: Linear probing is used to resolve collisions in a hash table when the calculated index is already occupied. True or false?  
   Answer: True.

7. Question: The final hash table after inserting all keys in the first example is [49, 58, 69, , , , , , 18, 89]. True or false?  
   Answer: True.

8. Question: The key 18 will be placed at index 3 in a hash table of size 5 when using the hash function h(key) = key % 5. True or false?  
   Answer: True.

---

# Primary Clustering

## Questions

1. Question: In a hash table of size 10, if the keys 10, 20, 30, and 40 are inserted using a hash function that returns the key modulo 10, they will all hash to index 0, resulting in primary clustering. True or false?  
   Answer: True.

2. Question: When using linear probing in a hash table, if a key hashes to an index that is already occupied, it will always find the next available index, preventing primary clustering. True or false?  
   Answer: False.

3. Question: In the given example, if we insert the keys 1, 11, 21, and 31 into a hash table of size 10, they will all hash to index 1, causing primary clustering at that index. True or false?  
   Answer: True.

4. Question: If a hash table uses a hash function that returns the key modulo 10, inserting the key 2 after the keys 1, 11, 21, and 31 will lead to primary clustering at index 2. True or false?  
   Answer: False.

5. Question: In the context of primary clustering, if a hash table has a size of 10 and we insert keys that hash to the same index, it can lead to a contiguous block of occupied entries. True or false?  
   Answer: True.

6. Question: The following code snippet will cause primary clustering if the keys 10, 20, 30, and 40 are inserted into a hash table of size 10 using linear probing:
   ```python
   hash_table = [None] * 10
   for key in [10, 20, 30, 40]:
       index = key % 10
       while hash_table[index] is not None:
           index = (index + 1) % 10
       hash_table[index] = key
   ```
   True or false?  
   Answer: True.

---

# Insertion Performance

## Questions

1. Question: In a hash table with a load factor of 0.5 and an average cluster size of 5 keys, inserting a new key would take time proportional to half the cluster size, which is 2.5 units of time. True or false?  
   Answer: True.

2. Question: If a hash table has a load factor of 0.8 and each cluster can hold 5 keys, inserting a new key into a full cluster will not require rehashing the entire table. True or false?  
   Answer: False.

3. Question: Increasing the number of keys in a hash table from 50 to 100 will always improve insertion performance due to a larger average cluster size. True or false?  
   Answer: False.

4. Question: In a hash table with a load factor of 0.8 and 40 keys, if each cluster can hold 5 keys, the average cluster size is 5 keys. True or false?  
   Answer: True.

5. Question: Inserting a new key into a hash table with a load factor of 0.8 and full clusters will always take less time than inserting into a hash table with a load factor of 0.5. True or false?  
   Answer: False.

---

# Disadvantages of Linear Probing

## Questions

1. Question: In a hash table using linear probing, if a key hashes to an index that is already occupied, the algorithm will check the next index in a sequential manner until it finds an empty slot. True or false?  
   Answer: True.

2. Question: Linear probing can lead to clustering, where a group of occupied indices forms, causing longer search times for future insertions. True or false?  
   Answer: True.

3. Question: In the example provided, if we insert keys 5, 10, and 15 into a hash table of size 5 using a hash function that returns the key modulo 5, they will occupy indices 0, 1, and 2 respectively. True or false?  
   Answer: True.

4. Question: If a key hashes to an index that is occupied in a linear probing hash table, the algorithm will skip that index and insert the new key at the same index. True or false?  
   Answer: False.

5. Question: In the provided example, if we attempt to insert key 6 after inserting keys 5, 10, and 15, it will be inserted at index 1. True or false?  
   Answer: False.

6. Question: The growth of clusters in a linear probing hash table can negatively impact the performance of search operations as the number of collisions increases. True or false?  
   Answer: True.

---

# Collisions and Clusters

## Questions

1. Question: In a distributed database system, increased contention and collisions can lead to improved performance. True or false?  
   Answer: False.

2. Question: A large cluster of nodes handling a high volume of requests is more likely to experience collisions than a small cluster. True or false?  
   Answer: True.

3. Question: An efficient load-balancing algorithm can help mitigate the impact of collisions in a cloud-based application. True or false?  
   Answer: True.

4. Question: If multiple nodes in a cluster attempt to access the same data simultaneously, it will always result in a performance degradation. True or false?  
   Answer: False.

5. Question: The following code snippet demonstrates a collision scenario in a distributed system:
   ```python
   def access_data(node_id):
       # Simulate data access
       if node_id == 1:
           return "Data accessed by Node 1"
       else:
           return "Data accessed by another node"
   ```
   True or false?  
   Answer: False.

---

# Quadratic Probing

## Questions

1. Question: In quadratic probing, if a collision occurs at index 2, the next probe will always be to index 3. True or false?  
   Answer: False.

2. Question: In the given example, the key 22 is inserted at index 3 because index 2 was occupied. True or false?  
   Answer: True.

3. Question: The final state of the hash table after inserting keys 12, 22, and 32 will have index 6 occupied by key 32. True or false?  
   Answer: True.

4. Question: In the tricky example, the key 24 is inserted at index 0 after probing from index 3. True or false?  
   Answer: True.

5. Question: If we try to insert key 31 into the hash table, it will be placed at index 5 after probing. True or false?  
   Answer: True.

6. Question: Quadratic probing guarantees that all keys will be placed in consecutive indices without any gaps. True or false?  
   Answer: False.

7. Question: The hash function used in the first example is h(x) = x % 10. True or false?  
   Answer: True.

8. Question: In the second example, the key 17 is inserted at index 4 because index 3 was free. True or false?  
   Answer: False.

---

# Hash Function

## Questions

1. Question: A hash function that returns the sum of the ASCII values of a string's characters modulo the size of the hash table is an example of a valid hash function. True or false?  
   Answer: True.

2. Question: In the example provided, the string 'cat' would be stored at index 3 in the hash table if the size of the hash table is 10. True or false?  
   Answer: False.

3. Question: A hash function that returns the length of a string modulo the size of the hash table can lead to collisions if different strings have the same length. True or false?  
   Answer: True.

4. Question: If the string 'hello' has a length of 5 and the hash table size is 5, the hash value for 'hello' would be 1. True or false?  
   Answer: False.

5. Question: The hash value for the string 'world' would be different from the hash value for the string 'hello' if both strings have the same length and the hash function is based on string length. True or false?  
   Answer: False.

---

# Probe Sequence

## Questions

1. Question: In a hash table with a size of 10, if a key hashes to index 7 and that index is occupied, the next index checked in a linear probing method would be index 8. True or false?  
   Answer: True.

2. Question: In a hash table of size 5, if the keys 3, 8, and 13 are inserted using a hash function that returns the index as the key modulo 5, the probe sequence for the key 8 would be [3, 4]. True or false?  
   Answer: True.

3. Question: In linear probing, if a key hashes to an index that is occupied, the probe sequence will always check the next index in a circular manner until an empty slot is found. True or false?  
   Answer: True.

4. Question: If a hash table has a size of 5 and a key hashes to index 3, the probe sequence for that key will always be [3] regardless of whether that index is occupied or not. True or false?  
   Answer: False.

5. Question: In the context of probing in hash tables, if a key hashes to index 3 and that index is occupied, the probe sequence could potentially include indices 4, 0, and 1 before finding an empty slot. True or false?  
   Answer: True.

---

# Table Size and Primality

## Questions

1. Question: A hash table of size 11 can accommodate more than 5 keys without worrying about collisions if it is currently 7 slots empty. True or false?  
   Answer: True.

2. Question: In a hash table of size 13, if 6 keys are inserted, it is impossible to insert another key without causing a collision. True or false?  
   Answer: False.

3. Question: If a hash table has more than half of its slots empty, it is guaranteed that new keys can be inserted without any collisions. True or false?  
   Answer: False.

4. Question: When using linear probing in a hash table, if the initial index is occupied, we check the next index sequentially until we find an empty slot. True or false?  
   Answer: True.

5. Question: If a hash function maps a key to an index that is already occupied, the key cannot be inserted into the hash table at all. True or false?  
   Answer: False.

6. Question: A hash table of size 13 with 6 keys inserted has 7 slots empty, which means it is more than half empty. True or false?  
   Answer: True.

7. Question: The hash function can map multiple keys to the same index in a hash table, leading to collisions. True or false?  
   Answer: True.

8. Question: If a hash table is full, it is still possible to insert new keys by using a collision resolution strategy. True or false?  
   Answer: False.

---

# Example of Insertion

## Questions

1. Question: In a hash table of size 10, using the hash function h(key) = key % 10, the key 49 can be inserted at index 9 without any collisions. True or false?  
   Answer: False.

2. Question: When inserting the key 58 into a hash table of size 10 using linear probing, it will be placed at index 1 after probing. True or false?  
   Answer: True.

3. Question: In the tricky example with a hash table of size 5, the key 49 can be inserted successfully using quadratic probing. True or false?  
   Answer: False.

4. Question: The hash function h(key) = key % 5 will result in a collision for the key 18 when inserting into a hash table of size 5. True or false?  
   Answer: False.

5. Question: Using linear probing, if a collision occurs at index 9, the next index checked will be index 0 in a hash table of size 10. True or false?  
   Answer: True.

6. Question: In the example provided, if the hash table size is increased to 15, all keys can be inserted without any collisions using the hash function h(key) = key % 10. True or false?  
   Answer: True.

7. Question: Quadratic probing allows for checking indices that are out of bounds when a collision occurs. True or false?  
   Answer: False.

---

# Secondary Clustering

## Questions

1. Question: In a hash table using linear probing, if two keys hash to the same index, they will always occupy consecutive indices. True or false?  
   Answer: True.

2. Question: In the given example, when inserting key 30 after key 20 using linear probing, key 30 will be placed at index 2. True or false?  
   Answer: True.

3. Question: Secondary clustering occurs when multiple keys hash to the same index and follow different probing sequences. True or false?  
   Answer: False.

4. Question: In the tricky example, when inserting key 10 after key 5 using quadratic probing, key 10 will first check index 0 and then index 1. True or false?  
   Answer: True.

5. Question: If a hash table has a size of 5 and keys 5, 10, and 15 are inserted, they will all hash to index 0 and will not cause any clustering issues. True or false?  
   Answer: False.

6. Question: In the context of secondary clustering, searching for key 15 will require checking index 0, index 1, and index 4 in the tricky example. True or false?  
   Answer: True.

7. Question: Using quadratic probing, if the first key is placed at index 0, the next key will always try to occupy index 1 first. True or false?  
   Answer: False.

---

# Double Hashing

## Questions

1. Question: In double hashing, the second hash function is used to determine the step size for probing when a collision occurs. True or false?  
   Answer: True.

2. Question: In the example provided, when inserting the key 15 into the hash table, the first index checked is index 6. True or false?  
   Answer: False.

3. Question: The second hash function h2(key) = 7 - (key % 7) can produce negative values when the key is greater than 7. True or false?  
   Answer: False.

4. Question: In the tricky example, if the first probe at index 0 is occupied, the next probe will be at index 9. True or false?  
   Answer: True.

5. Question: The probing sequence in double hashing is guaranteed to find an empty slot if the hash table is not full. True or false?  
   Answer: False.

6. Question: The choice of the second hash function h2 can significantly impact the performance of double hashing. True or false?  
   Answer: True.

7. Question: In the first example, if index 1 is also occupied after probing from index 5, the next index checked will be index 7. True or false?  
   Answer: True.

8. Question: The hash table size must always be a prime number for double hashing to work effectively. True or false?  
   Answer: False.

---

# Hash Functions

## Questions

1. Question: The primary hash function used in the examples is defined as `hash(key) = key % 10`. True or false?  
   Answer: True.

2. Question: When inserting the key 20 into the hash table, the primary position calculated is index 1. True or false?  
   Answer: False.

3. Question: The secondary hash function is defined as `hash2(key) = 7 - (key % 7)`. True or false?  
   Answer: True.

4. Question: After inserting keys 10, 20, and 30, the final hash table has keys at indices 0, 1, and 5. True or false?  
   Answer: True.

5. Question: The key 14 is placed at index 4 in the hash table. True or false?  
   Answer: True.

6. Question: The probing sequence for key 21 starts with the primary position index 3. True or false?  
   Answer: False.

7. Question: If a key hashes to an occupied index using the primary hash function, the secondary hash function is used to find the next available index. True or false?  
   Answer: True.

8. Question: The final hash table after inserting keys 10, 20, 30, 14, and 21 has all indices filled. True or false?  
   Answer: False.

9. Question: The key 30 is placed at index 5 after using the secondary hash function. True or false?  
   Answer: True.

10. Question: The probing sequence can lead to a situation where multiple keys hash to the same primary position, but the secondary hash function cannot help find an available slot. True or false?  
    Answer: False.

---

# Probe Sequence Formula

## Questions

1. Question: The probe sequence for the key 'apple' starts at index 3. True or false?  
   Answer: True.

2. Question: The secondary hash function hash2('banana') returns a value of 2. True or false?  
   Answer: False.

3. Question: In the probe sequence for 'cherry', the first index checked is 7. True or false?  
   Answer: True.

4. Question: The probe sequence for 'dog' results in a unique index on the first attempt. True or false?  
   Answer: True.

5. Question: The probe sequence for 'cat' results in a collision with 'dog' on the first attempt. True or false?  
   Answer: True.

6. Question: The value of m in the given examples is 5. True or false?  
   Answer: False.

7. Question: The probe sequence for 'fish' starts at index 4. True or false?  
   Answer: True.

8. Question: The formula for calculating the probe sequence is hi(i) = (hash(k) + i ¡Á hash2(k)) mod m. True or false?  
   Answer: True.

9. Question: If two keys have the same hash value, they will always have the same probe sequence. True or false?  
   Answer: False.

10. Question: The probe sequence for 'banana' includes the index 1. True or false?  
    Answer: False.

---

# Example of hash2(k)

## Questions

1. Question: For a key k = 15 and a prime number R = 7, the secondary hash value calculated as hash2(15) is 6. True or false?  
   Answer: True.

2. Question: When calculating hash2(k) for a key k = 21 with R = 7, the result is 7, which is a valid index for a hash table of size m = 10. True or false?  
   Answer: False.

3. Question: The formula for calculating the secondary hash value is hash2(k) = R - (k mod R). True or false?  
   Answer: True.

4. Question: If the hash table size m = 10 and R = 7, the secondary hash value for any key k that results in hash2(k) = 7 must be adjusted to fit within the range of 0 to 9. True or false?  
   Answer: True.

5. Question: The secondary hash value for a key k = 15 can be directly used as an index in the hash table without any adjustments. True or false?  
   Answer: True.

6. Question: If a key k = 21 results in hash2(k) = 7, the final index must always be adjusted to 0 for it to fit within the bounds of the hash table. True or false?  
   Answer: False.

---

# Double Hashing

## Questions

1. Question: In double hashing, if the first hash function results in an occupied index, the second hash function is always used to find a new index. True or false?  
   Answer: True.

2. Question: Given the hash function h1(key) = key % 10, the key 22 will always hash to index 2 in a hash table of size 10. True or false?  
   Answer: False.

3. Question: In the provided example, the key 32 is inserted at index 5 because index 2 was occupied. True or false?  
   Answer: True.

4. Question: If two keys hash to the same index using h1, they will always hash to the same index using h2 as well. True or false?  
   Answer: False.

5. Question: The final state of the hash table after inserting keys 12, 22, and 32 is: Index 0: -, Index 1: -, Index 2: 12, Index 3: -, Index 4: -, Index 5: 32, Index 6: -, Index 7: -, Index 8: 22, Index 9: -. True or false?  
   Answer: True.

6. Question: In the tricky example, if key 50 is inserted before key 30, it will occupy index 5, preventing key 30 from being inserted there. True or false?  
   Answer: True.

7. Question: The second hash function h2(key) = 7 - (key % 7) will always produce a positive index for any integer key. True or false?  
   Answer: False.

8. Question: The order of insertion of keys can affect the final state of the hash table in double hashing. True or false?  
   Answer: True.

---

# Hash Functions

## Questions

1. Question: The hash function hash(k) = k mod 10 will produce the same index for the keys 13 and 23. True or false?  
   Answer: True.

2. Question: When using the hash function hash(k) = k mod 10, the key 23 will be stored at index 2 in the hash table. True or false?  
   Answer: False.

3. Question: A collision occurs in a hash table when two different keys produce the same index using the hash function. True or false?  
   Answer: True.

4. Question: The hash function hash(k) = k mod 10 can guarantee that there will be no collisions for any set of keys. True or false?  
   Answer: False.

5. Question: If we use chaining as a collision resolution strategy, multiple keys that hash to the same index can be stored in a linked list at that index. True or false?  
   Answer: True.

6. Question: The hash function hash(k) = k mod 10 will always produce unique indices for all integer keys. True or false?  
   Answer: False.

7. Question: In open addressing, if a collision occurs, the next available index is searched sequentially until an empty slot is found. True or false?  
   Answer: True.

---

# Collision Resolution

## Questions

1. Question: In a hash table using quadratic probing, if the hash function is h(k) = k % 7, the key 17 will be placed at index 3 if index 3 is occupied. True or false?  
   Answer: True.

2. Question: In the given example, when inserting key 10 into a hash table of size 5 using double hashing, the second hash function is h2(k) = 1 + (k % 4). True or false?  
   Answer: True.

3. Question: If a hash table of size 5 has keys 5, 10, and 15 inserted using the hash function h(k) = k % 5, all keys will be placed at index 0. True or false?  
   Answer: False.

4. Question: In the quadratic probing example, after placing key 10 at index 3, the next key to be inserted is key 20, which will be placed at index 6. True or false?  
   Answer: True.

5. Question: When inserting key 20 into the hash table of size 5, if index 0 is occupied, the next index checked will be index 1 after applying double hashing. True or false?  
   Answer: True.

6. Question: In the example with double hashing, if the first hash function results in an occupied index, the second hash function is always applied to find the next available index. True or false?  
   Answer: True.

7. Question: The quadratic probing method guarantees that all keys will be placed in the first available index without any collisions. True or false?  
   Answer: False.

8. Question: In the example provided, if we try to insert key 30 after inserting keys 10 and 20, it will be placed at index 2. True or false?  
   Answer: True.

---

# Prime Number Requirement

## Questions

1. Question: The hash function hash2(k) = k % 10 will produce values that are relatively prime to 10 for all integer values of k. True or false?  
   Answer: False.

2. Question: If k = 4 is used with the hash function hash2(k) = k % 12, the resulting hash value will be relatively prime to 12. True or false?  
   Answer: False.

3. Question: Choosing k values such as 1, 3, 7, and 9 for a hash table of size m = 10 will ensure effective probing due to their hash values being relatively prime to 10. True or false?  
   Answer: True.

4. Question: The greatest common divisor (gcd) of 4 and 12 is 2, which indicates that 4 is relatively prime to 12. True or false?  
   Answer: False.

5. Question: For a hash table of size m = 12, using k values like 1, 5, or 7 will yield hash values that are relatively prime to 12. True or false?  
   Answer: True.

---

# Quadratic Probing

## Questions

1. Question: In a hash table of size 10, using the hash function h(x) = x % 10, the key 12 will be placed at index 2. True or false?  
   Answer: True.

2. Question: When inserting the key 22 into the hash table, it will be placed at index 2 due to a collision with the key 12. True or false?  
   Answer: False.

3. Question: In the quadratic probing method, the new index for a key is calculated using the formula: new_index = (original_index + i^2) % table_size, where i is the number of attempts. True or false?  
   Answer: True.

4. Question: If we try to insert the key 32 after inserting keys 12 and 22, it will be placed at index 6. True or false?  
   Answer: True.

5. Question: In a hash table of size 7, if we insert the keys 10, 20, 30, and 40, the key 40 will be placed at index 3. True or false?  
   Answer: False.

6. Question: The key 50 will be placed at index 1 in the hash table of size 7 after inserting the keys 10, 20, 30, and 40. True or false?  
   Answer: True.

7. Question: When trying to insert the key 80 into the hash table, the first attempt for quadratic probing will check index 4. True or false?  
   Answer: True.

8. Question: The clustering effect of quadratic probing can lead to a situation where multiple collisions prevent a key from being inserted into the hash table. True or false?  
   Answer: True.

9. Question: If the key 60 hashes to index 4, it will be placed at index 5 if index 4 is occupied. True or false?  
   Answer: False.

10. Question: After several attempts to insert the key 80, it will eventually be placed in the hash table. True or false?  
    Answer: False.

---

# Insertion Example

## Questions

1. Question: The primary hash function used in the examples is defined as h(k) = k % 10. True or false?  
   Answer: True.

2. Question: When inserting the value 49, the secondary hash function h2(k) = 7 - (k % 7) is used only if the primary hash slot is empty. True or false?  
   Answer: False.

3. Question: The final hash table contains the value 28 at index 4 after all insertions. True or false?  
   Answer: True.

4. Question: The value 69 is inserted at index 1 because its primary hash slot was empty. True or false?  
   Answer: False.

5. Question: The secondary hash function h2(k) is used to resolve collisions in the hash table. True or false?  
   Answer: True.

6. Question: The value 58 is inserted at index 3 because its primary hash slot was empty. True or false?  
   Answer: False.

7. Question: The final hash table has a total of 5 occupied slots after all insertions. True or false?  
   Answer: True.

8. Question: The primary hash for the value 28 is calculated as h(28) = 8. True or false?  
   Answer: True.

9. Question: The value 49 is inserted at index 6 because it was the first value to collide with an occupied slot. True or false?  
   Answer: False.

10. Question: The final hash table has the following values: [69, -, -, 58, 28, -, 49, -, 18, 89]. True or false?  
    Answer: True.

---

# Deletion in Open Addressing

## Questions

1. Question: In open addressing, when a key is deleted, it is completely removed from the hash table. True or false?  
   Answer: False.

2. Question: Marking a deleted key as DELETED in open addressing allows for the integrity of the probing sequence to be maintained. True or false?  
   Answer: True.

3. Question: If a key is marked as DELETED in a hash table, it can still affect the search for other keys that were inserted before it. True or false?  
   Answer: True.

4. Question: In the given example, if we delete the key 2 and then insert the key 7, the key 7 will be placed at index 2. True or false?  
   Answer: False.

5. Question: After deleting a key in open addressing, if we search for that key, we will find it at the index where it was marked as DELETED. True or false?  
   Answer: True.

6. Question: In a hash table of size 5, if we insert keys 1, 2, and 3, and then delete key 2, the table will have the following values: [1, DELETED, 3, -, -]. True or false?  
   Answer: True.

7. Question: If a hash table uses a simple hash function that returns the index of the key modulo the table size, inserting a key that hashes to an index occupied by a DELETED key will not require probing. True or false?  
   Answer: False.

---

# Re-hashing

## Questions

1. Question: A hash table with a load factor of 0.8 will trigger a resize when more items are added, assuming the threshold is set at 0.75. True or false?  
   Answer: True.

2. Question: When a hash table is resized, all existing items must be re-hashed using the same hash function. True or false?  
   Answer: False.

3. Question: If a hash table starts with a size of 5 and has a load factor of 1.0 after inserting 5 items, inserting a 6th item will not cause a resize. True or false?  
   Answer: False.

4. Question: Resizing a hash table to a larger size can sometimes lead to performance degradation due to collisions with existing items. True or false?  
   Answer: True.

5. Question: The following code snippet will correctly calculate the load factor of a hash table with 8 items and a size of 10:
   ```python
   load_factor = 8 / 10
   ```
   True or false?  
   Answer: True.

6. Question: A hash table can maintain efficient operations like insertions and lookups without ever needing to resize. True or false?  
   Answer: False.

---

