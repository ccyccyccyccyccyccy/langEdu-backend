# Firebase

## Questions

### Question 1:
What is the primary purpose of Firebase Authentication in a mobile app?
a) To store user data  
b) To allow users to sign in using third-party accounts  
c) To send push notifications  
d) To manage app performance  

**Answer:** b) To allow users to sign in using third-party accounts

---

### Question 2:
In the context of Firebase Cloud Messaging, what could be a consequence of misconfiguring notification settings to target a specific geographical region?
a) All users receive notifications  
b) Only users in the targeted region receive notifications  
c) Notifications are sent to users' email addresses  
d) Notifications are delayed indefinitely  

**Answer:** b) Only users in the targeted region receive notifications

---

### Question 3:
Which of the following Firebase services is primarily used for real-time data synchronization?
a) Firebase Authentication  
b) Firebase Cloud Firestore  
c) Firebase Cloud Messaging  
d) Firebase Hosting  

**Answer:** b) Firebase Cloud Firestore

---

### Question 4:
Consider the following code snippet for Firebase Authentication:

```javascript
firebase.auth().signInWithEmailAndPassword(email, password)
  .then((userCredential) => {
    // Signed in 
    var user = userCredential.user;
  })
  .catch((error) => {
    var errorCode = error.code;
    var errorMessage = error.message;
  });
```

What does the `signInWithEmailAndPassword` method do?
a) Signs in a user with their Google account  
b) Signs in a user using their email and password  
c) Registers a new user with an email and password  
d) Logs out the current user  

**Answer:** b) Signs in a user using their email and password

---

### Question 5:
What is a potential drawback of using Firebase Cloud Messaging for sending notifications?
a) It can only send notifications to Android devices  
b) Notifications may not reach users if they are not in the targeted region  
c) It requires a paid subscription  
d) It does not support multimedia messages  

**Answer:** b) Notifications may not reach users if they are not in the targeted region

---

### Question 6:
Which Firebase feature would you use to manage user sessions and authentication states?
a) Firebase Cloud Functions  
b) Firebase Realtime Database  
c) Firebase Authentication  
d) Firebase Storage  

**Answer:** c) Firebase Authentication

---

### Question 7:
If a developer wants to send a notification to all users of their app using Firebase Cloud Messaging, which of the following configurations is necessary?
a) Target specific user IDs  
b) Use a topic that all users are subscribed to  
c) Set geographical targeting  
d) Send notifications only to users who have opted in  

**Answer:** b) Use a topic that all users are subscribed to

---

### Question 8:
What is the main benefit of using Firebase for mobile app development?
a) It requires no coding skills  
b) It provides a comprehensive suite of tools for backend services  
c) It is only suitable for web applications  
d) It is limited to Android development  

**Answer:** b) It provides a comprehensive suite of tools for backend services

---

# Realtime Database

## Questions

### Question 1:
What is a primary benefit of using a Realtime Database in a chat application?
a) It allows users to send messages without an internet connection.  
b) It stores messages as plain text files.  
c) It enables all connected clients to receive new messages instantly.  
d) It requires users to refresh the app to see new messages.  
**Answer:** c) It enables all connected clients to receive new messages instantly.

### Question 2:
In a collaborative document editing application using a Realtime Database, what is a potential issue that may arise when multiple users edit the same section of a document?
a) The database will automatically delete the section.  
b) Users will not be able to see any changes made by others.  
c) There may be conflicts that require resolution to ensure all changes are reflected.  
d) The application will crash if too many users edit simultaneously.  
**Answer:** c) There may be conflicts that require resolution to ensure all changes are reflected.

### Question 3:
Given the following JSON structure for a chat message in a Realtime Database, which of the following represents a correctly formatted message?
```json
{
  "message": {
    "user": "Alice",
    "text": "Hello, Bob!",
    "timestamp": "2023-10-01T12:00:00Z"
  }
}
```
a) { "message": "Hello, Bob!" }  
b) { "user": "Alice", "text": "Hello, Bob!" }  
c) { "message": { "user": "Alice", "text": "Hello, Bob!" } }  
d) { "message": { "user": "Alice", "text": "Hello, Bob!", "timestamp": 2023-10-01 } }  
**Answer:** c) { "message": { "user": "Alice", "text": "Hello, Bob!" } }

### Question 4:
What is a common strategy for conflict resolution in a Realtime Database when two users edit the same document section simultaneously?
a) The last edit made is always kept.  
b) All edits are discarded.  
c) A version control system is implemented to track changes.  
d) The application ignores the edits.  
**Answer:** c) A version control system is implemented to track changes.

### Question 5:
Which of the following statements is true regarding the use of a Realtime Database in a mobile application?
a) It can only be used for storing images.  
b) It requires manual refreshing to see updates.  
c) It allows for real-time synchronization of data across multiple clients.  
d) It is limited to text-based data only.  
**Answer:** c) It allows for real-time synchronization of data across multiple clients.

---

# Firebase Services

## Questions

### Question 1:
What Firebase service is best suited for real-time data synchronization in a mobile app?
a) Firebase Cloud Firestore  
b) Firebase Realtime Database  
c) Firebase Authentication  
d) Firebase Hosting  
**Answer:** b) Firebase Realtime Database

### Question 2:
In the context of Firebase Cloud Firestore, which of the following statements is true?
a) Firestore supports complex queries that require joining multiple collections.  
b) Firestore is optimized for simple queries and does not support joins.  
c) Firestore automatically indexes all fields in every document.  
d) Firestore is only suitable for storing images and videos.  
**Answer:** b) Firestore is optimized for simple queries and does not support joins.

### Question 3:
Given the following code snippet, which Firebase service is being used to add a new document to a collection?

```javascript
firebase.firestore().collection("posts").add({
  title: "New Post",
  content: "This is the content of the new post."
});
```
a) Firebase Realtime Database  
b) Firebase Cloud Firestore  
c) Firebase Authentication  
d) Firebase Storage  
**Answer:** b) Firebase Cloud Firestore

### Question 4:
What is a potential drawback of using Firebase Cloud Firestore for a social media app that requires complex querying?
a) Firestore does not support real-time updates.  
b) Firestore can lead to performance issues due to its lack of support for joins.  
c) Firestore is not scalable for large datasets.  
d) Firestore requires a paid plan for all features.  
**Answer:** b) Firestore can lead to performance issues due to its lack of support for joins.

### Question 5:
Which Firebase service would you use to manage user authentication in your app?
a) Firebase Realtime Database  
b) Firebase Cloud Firestore  
c) Firebase Authentication  
d) Firebase Functions  
**Answer:** c) Firebase Authentication

---

# Cloud Firestore

## Questions

### Question 1:
In a Cloud Firestore database for a bookstore, which of the following is the correct way to represent a book document within a 'books' collection?

a) 
```json
{
  "book": {
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian",
    "price": 9.99
  }
}
```

b) 
```json
{
  "title": "1984",
  "author": "George Orwell",
  "genre": "Dystopian",
  "price": 9.99
}
```

c) 
```json
{
  "books": [
    {
      "title": "1984",
      "author": "George Orwell",
      "genre": "Dystopian",
      "price": 9.99
    }
  ]
}
```

d) 
```json
{
  "collection": "books",
  "document": {
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian",
    "price": 9.99
  }
}
```

**Answer:** b) 
```json
{
  "title": "1984",
  "author": "George Orwell",
  "genre": "Dystopian",
  "price": 9.99
}
```

---

### Question 2:
In a social media application using Cloud Firestore, if you want to query all comments made by a specific user across all posts, which of the following approaches would be most effective?

a) Query the 'comments' sub-collection directly.

b) Use a separate collection for user comments to facilitate the query.

c) Query the 'posts' collection and filter comments in the application code.

d) Firestore automatically supports querying across sub-collections.

**Answer:** b) Use a separate collection for user comments to facilitate the query.

---

### Question 3:
Which of the following statements about Cloud Firestore is true?

a) Firestore allows you to perform complex joins across multiple collections.

b) Firestore supports real-time synchronization of data across clients.

c) Firestore requires you to define a fixed schema for your data.

d) Firestore does not support offline data access.

**Answer:** b) Firestore supports real-time synchronization of data across clients.

---

### Question 4:
Given the following code snippet, what will be the result of the query?

```javascript
const db = firebase.firestore();
db.collection("books").where("price", "<", 10).get().then((querySnapshot) => {
  querySnapshot.forEach((doc) => {
    console.log(doc.id, " => ", doc.data());
  });
});
```

a) It will log all books with a price greater than or equal to 10.

b) It will log all books with a price less than 10.

c) It will log an error because Firestore does not support querying by price.

d) It will log all books regardless of their price.

**Answer:** b) It will log all books with a price less than 10.

---

### Question 5:
In the context of Cloud Firestore, what does denormalization mean?

a) Storing data in a highly structured format.

b) Storing duplicate data to optimize read performance.

c) Automatically removing duplicate entries from the database.

d) Creating relationships between different collections.

**Answer:** b) Storing duplicate data to optimize read performance.

---

# Data Structure - Collections and Documents

## Questions

### Multiple Choice Questions on Data Structure - Collections and Documents

1. **Question:** In a NoSQL database like MongoDB, what does a collection represent?
   a) A single record  
   b) A group of related documents  
   c) A type of data structure  
   d) A query language  
   **Answer:** b) A group of related documents

2. **Question:** Given the following document in a 'Users' collection:  
   ```json
   { 'name': 'Alice', 'age': 30, 'email': 'alice@example.com' }
   ```
   What type of data does this document primarily represent?
   a) A user profile  
   b) A product listing  
   c) A transaction record  
   d) A system configuration  
   **Answer:** a) A user profile

3. **Question:** Which of the following statements is true about documents in a NoSQL collection?
   a) All documents must have the same structure  
   b) Documents can have varying fields and data types  
   c) Documents are always stored in a fixed schema  
   d) Documents cannot contain nested objects  
   **Answer:** b) Documents can have varying fields and data types

4. **Question:** Consider the following document in a 'Products' collection:  
   ```json
   { 'productName': 'E-Book', 'price': 9.99, 'fileFormat': 'PDF', 'downloadLink': 'http://example.com/download' }
   ```
   What type of product does this document represent?
   a) A physical product  
   b) A digital product  
   c) A service  
   d) A subscription  
   **Answer:** b) A digital product

5. **Question:** In the context of NoSQL databases, what is a key advantage of using a document-based structure?
   a) It requires a predefined schema  
   b) It allows for complex joins between tables  
   c) It provides flexibility in data representation  
   d) It enforces data normalization  
   **Answer:** c) It provides flexibility in data representation

6. **Question:** If you wanted to add an address field to the following document in the 'Users' collection:  
   ```json
   { 'name': 'Bob', 'age': 25, 'email': 'bob@example.com' }
   ```
   Which of the following would be a valid modification?
   a) Add 'address': '123 Main St'  
   b) Add 'address': { 'street': '123 Main St', 'city': 'Anytown' }  
   c) Add 'address': [ '123 Main St', 'Anytown' ]  
   d) Add 'address': null  
   **Answer:** b) Add 'address': { 'street': '123 Main St', 'city': 'Anytown' }

7. **Question:** In a NoSQL database, what is the primary purpose of a collection?
   a) To store user credentials  
   b) To group similar documents for efficient retrieval  
   c) To enforce data integrity  
   d) To manage transactions  
   **Answer:** b) To group similar documents for efficient retrieval

8. **Question:** Which of the following best describes the 'Products' collection example provided?
   a) It contains only physical products  
   b) It demonstrates the use of a single document structure  
   c) It showcases the ability to store different types of products in one collection  
   d) It requires all products to have the same attributes  
   **Answer:** c) It showcases the ability to store different types of products in one collection

---

# CRUD Operations - Create Data

## Questions

### Questions on CRUD Operations - Create Data

**Question 1:** What method is used to create a new document in a Firestore collection?  
a) add()  
b) create()  
c) set()  
d) insert()  
**Answer:** c) set()

---

**Question 2:** In the provided code snippet, what is the purpose of `db.collection('users').doc();`?  
a) It retrieves a document from the 'users' collection.  
b) It creates a reference to a new document with a generated ID.  
c) It deletes a document from the 'users' collection.  
d) It updates an existing document in the 'users' collection.  
**Answer:** b) It creates a reference to a new document with a generated ID.

---

**Question 3:** What will happen if the `set()` method is called with an object that contains the same document ID as an existing document?  
a) It will create a new document with a different ID.  
b) It will overwrite the existing document with the new data.  
c) It will throw an error.  
d) It will append the new data to the existing document.  
**Answer:** b) It will overwrite the existing document with the new data.

---

**Question 4:** In the tricky example, what is the significance of `const productCode = 'PROD123';`?  
a) It is a randomly generated ID for the product.  
b) It is the ID used to create a new product document instead of a generated ID.  
c) It is the name of the product.  
d) It is the price of the product.  
**Answer:** b) It is the ID used to create a new product document instead of a generated ID.

---

**Question 5:** What will be logged to the console if the product document is created successfully in the tricky example?  
a) 'Error creating product document: '  
b) 'Product document created successfully with specific ID!'  
c) 'User document created successfully!'  
d) 'Product document creation failed.'  
**Answer:** b) 'Product document created successfully with specific ID!'

---

**Question 6:** If an error occurs during the document creation process, which part of the code handles the error?  
a) The `then()` method  
b) The `catch()` method  
c) The `set()` method  
d) The `doc()` method  
**Answer:** b) The `catch()` method

---

**Question 7:** Which of the following statements is true regarding Firestore document IDs?  
a) Document IDs must always be generated by Firestore.  
b) Document IDs can be either generated by Firestore or specified by the user.  
c) Document IDs cannot be changed once created.  
d) Document IDs are always numeric.  
**Answer:** b) Document IDs can be either generated by Firestore or specified by the user.

---

# Use cases

## Questions

### Question 1:
What is a typical use case for Cloud Firestore in a social media application?
a) Storing user passwords securely  
b) Managing user profiles, posts, comments, and likes in real-time  
c) Hosting images and videos  
d) Sending push notifications to users  

**Answer:** b) Managing user profiles, posts, comments, and likes in real-time

---

### Question 2:
In an e-commerce platform using Cloud Firestore, what is a critical consideration when implementing flash sales?
a) Ensuring all users can see the same product images  
b) Handling concurrent updates to inventory levels  
c) Allowing users to leave reviews after purchase  
d) Providing a discount code for all users  

**Answer:** b) Handling concurrent updates to inventory levels

---

### Question 3:
Which of the following best describes a challenge when using Cloud Firestore for managing inventory during flash sales?
a) Users being unable to create accounts  
b) Ensuring that users do not oversell items due to rapid inventory changes  
c) Difficulty in retrieving user data  
d) Slow loading times for product images  

**Answer:** b) Ensuring that users do not oversell items due to rapid inventory changes

---

### Question 4:
Given the following code snippet, what will happen if two users try to purchase the last item in stock simultaneously?

```javascript
const db = firebase.firestore();
const itemRef = db.collection('inventory').doc('item123');

db.runTransaction(async (transaction) => {
    const doc = await transaction.get(itemRef);
    if (!doc.exists) {
        throw "Document does not exist!";
    }
    const newStock = doc.data().stock - 1;
    if (newStock < 0) {
        throw "Not enough stock!";
    }
    transaction.update(itemRef, { stock: newStock });
});
```

a) One user will succeed, and the other will fail due to insufficient stock.  
b) Both users will succeed, and the stock will go negative.  
c) Both users will fail due to a transaction error.  
d) The transaction will automatically resolve to allow both purchases.  

**Answer:** a) One user will succeed, and the other will fail due to insufficient stock.

---

### Question 5:
What feature of Cloud Firestore allows users to see updates from their friends instantly in a social media application?
a) Batch writes  
b) Real-time listeners  
c) Offline persistence  
d) Data modeling  

**Answer:** b) Real-time listeners

---

# Cloud Firestore

## Questions

### Question 1:
In a mobile application using Cloud Firestore, which of the following fields would you typically find in a user document?

a) username  
b) post content  
c) timestamp  
d) chat room ID  

**Answer:** a) username

---

### Question 2:
When a user creates a new post in a Cloud Firestore-based application, where is the new post stored?

a) In the user's document  
b) In the 'posts' collection  
c) In the 'users' collection  
d) In the 'comments' sub-collection  

**Answer:** b) In the 'posts' collection

---

### Question 3:
In a real-time chat application using Cloud Firestore, how are messages typically organized?

a) Each message is a document in the 'messages' collection  
b) Each message is a sub-collection within the room document  
c) Each message is stored in the user's document  
d) Each message is stored in a global 'chat' collection  

**Answer:** b) Each message is a sub-collection within the room document

---

### Question 4:
What is a critical consideration when implementing a feature to delete a message in a Firestore chat application?

a) Ensuring the message is deleted from the user's document  
b) Ensuring that all users are notified of the change  
c) Ensuring that the message is archived  
d) Ensuring that the message is logged  

**Answer:** b) Ensuring that all users are notified of the change

---

### Question 5:
Given the following code snippet, what does the `onSnapshot` method do in the context of Firestore?

```javascript
const unsubscribe = firestore.collection('posts').onSnapshot(snapshot => {
    snapshot.docChanges().forEach(change => {
        if (change.type === 'added') {
            console.log('New post: ', change.doc.data());
        }
    });
});
```

a) It retrieves all posts from the 'posts' collection once.  
b) It listens for real-time updates to the 'posts' collection.  
c) It deletes a post from the 'posts' collection.  
d) It updates a post in the 'posts' collection.  

**Answer:** b) It listens for real-time updates to the 'posts' collection.

---

### Question 6:
In a Firestore-based application, what happens if a user deletes a message while others are viewing the chat room?

a) The message is deleted only for the user who deleted it.  
b) The message is deleted for all users, and they are notified of the change.  
c) The message remains visible until the app is refreshed.  
d) The message is archived instead of deleted.  

**Answer:** b) The message is deleted for all users, and they are notified of the change.

---

# CRUD Operations - Read Data

## Questions

### Questions on CRUD Operations - Read Data

**Question 1:** What does the following code snippet do?
```javascript
const db = firebase.firestore();

db.collection('users').get().then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
        console.log(`${doc.id} => ${JSON.stringify(doc.data())}`);
    });
});
```
a) It updates all documents in the 'users' collection.  
b) It deletes all documents in the 'users' collection.  
c) It retrieves and logs all documents in the 'users' collection.  
d) It creates a new document in the 'users' collection.  
**Answer:** c) It retrieves and logs all documents in the 'users' collection.

---

**Question 2:** In the following code snippet, what is the purpose of the `where` clause?
```javascript
const emailToFind = 'example@example.com';

db.collection('users').where('email', '==', emailToFind).get().then((querySnapshot) => {
    if (querySnapshot.empty) {
        console.log('No matching documents.');
        return;
    }
    querySnapshot.forEach((doc) => {
        console.log(`${doc.id} => ${JSON.stringify(doc.data())}`);
    });
});
```
a) It updates the email field of all documents in the 'users' collection.  
b) It retrieves documents where the email field matches 'example@example.com'.  
c) It deletes documents where the email field matches 'example@example.com'.  
d) It creates a new document with the email 'example@example.com'.  
**Answer:** b) It retrieves documents where the email field matches 'example@example.com'.

---

**Question 3:** What will happen if no documents match the query in the second code snippet?
a) The program will crash.  
b) It will log 'No matching documents.' to the console.  
c) It will log all documents in the 'users' collection.  
d) It will create a new document with the specified email.  
**Answer:** b) It will log 'No matching documents.' to the console.

---

**Question 4:** Which of the following statements is true about the `querySnapshot` object in the second code snippet?
a) It contains all documents in the 'users' collection regardless of the query.  
b) It contains only the documents that match the specified query.  
c) It can only be used to delete documents.  
d) It automatically updates the documents in the 'users' collection.  
**Answer:** b) It contains only the documents that match the specified query.

---

**Question 5:** If you wanted to retrieve users with a specific role in addition to filtering by email, which of the following code snippets would be correct?
```javascript
const emailToFind = 'example@example.com';
const roleToFind = 'admin';

db.collection('users').where('email', '==', emailToFind).where('role', '==', roleToFind).get().then((querySnapshot) => {
    // Handle the results
});
```
a) This code will retrieve users with the specified email and role.  
b) This code will only retrieve users with the specified email.  
c) This code will only retrieve users with the specified role.  
d) This code will not work because you cannot chain multiple where clauses.  
**Answer:** a) This code will retrieve users with the specified email and role.

---

# CRUD Operations - Update Data

## Questions

### Questions on CRUD Operations - Update Data

**Question 1:** What method is used to update a specific field in a Firestore document?  
a) set()  
b) update()  
c) merge()  
d) save()  
**Answer:** b) update()

---

**Question 2:** In the provided code snippet, what will happen if the document with ID 'user_id_123' does not exist when calling the `update()` method?  
a) A new document will be created.  
b) An error will be thrown.  
c) The operation will succeed with no changes.  
d) The email will be set to null.  
**Answer:** b) An error will be thrown.

---

**Question 3:** What is the purpose of the `merge: true` option in the `set()` method?  
a) It creates a new document regardless of existing data.  
b) It updates the document and removes all other fields not included in the update.  
c) It updates only the fields provided in the request, leaving other fields unchanged.  
d) It prevents any updates to the document.  
**Answer:** c) It updates only the fields provided in the request, leaving other fields unchanged.

---

**Question 4:** Given the following code snippet, which field will remain unchanged if it is not included in the `updatedData` object?  
```javascript
const updatedData = {
  email: 'newemail@example.com',
  // Assume 'age' is not provided in the request
};
```
a) email  
b) age  
c) user_id  
d) None, all fields will be updated.  
**Answer:** b) age

---

**Question 5:** What will the console log if the email update is successful in the first code snippet?  
a) 'Error updating user email: '  
b) 'User email updated successfully!'  
c) 'User profile updated successfully!'  
d) 'User email not found.'  
**Answer:** b) 'User email updated successfully!'

---

**Question 6:** If you want to update multiple fields in a Firestore document at once, which method would you use?  
a) set()  
b) update()  
c) merge()  
d) Both a and b  
**Answer:** d) Both a and b

---

**Question 7:** In the context of Firestore, what does the `update()` method do if the specified field does not exist in the document?  
a) It creates the field with the specified value.  
b) It throws an error.  
c) It ignores the update request.  
d) It sets the field to null.  
**Answer:** b) It throws an error.

---

# Cloud Firestore

## Questions

### Question 1:
What is the primary purpose of Cloud Firestore in a mobile application for a social media platform?

a) To manage user authentication  
b) To store user profiles, posts, and comments  
c) To handle payment processing  
d) To send push notifications  

**Answer:** b) To store user profiles, posts, and comments

---

### Question 2:
In the context of Cloud Firestore, what happens when a user creates a new post in a social media application?

a) The post is saved locally and uploaded later  
b) The post is saved in Firestore and all users see it in real-time  
c) The post is sent to a server for approval before being displayed  
d) The post is stored in a SQL database  

**Answer:** b) The post is saved in Firestore and all users see it in real-time

---

### Question 3:
What issue can arise in an e-commerce application using Cloud Firestore when two users add the same item to their cart simultaneously?

a) The application crashes  
b) A race condition occurs, leading to incorrect inventory levels  
c) The item is removed from the inventory  
d) The application sends duplicate notifications  

**Answer:** b) A race condition occurs, leading to incorrect inventory levels

---

### Question 4:
Which feature of Cloud Firestore can be used to ensure that inventory updates are atomic and consistent in the case of simultaneous updates?

a) Real-time listeners  
b) Firestore rules  
c) Transactions  
d) Offline persistence  

**Answer:** c) Transactions

---

### Question 5:
Given the following code snippet, what will happen when two users execute the `addToCart` function at the same time?

```javascript
function addToCart(itemId) {
    const itemRef = firestore.collection('inventory').doc(itemId);
    itemRef.update({
        quantity: firebase.firestore.FieldValue.increment(-1)
    });
}
```

a) Both users will successfully decrement the inventory count  
b) One user's update will overwrite the other's, leading to incorrect inventory  
c) The application will throw an error  
d) The inventory count will remain unchanged  

**Answer:** b) One user's update will overwrite the other's, leading to incorrect inventory

---

### Question 6:
What is a recommended practice to avoid race conditions when updating inventory levels in Cloud Firestore?

a) Use local storage for inventory management  
b) Implement Firestore transactions for inventory updates  
c) Allow users to refresh the app to see updated inventory  
d) Use a separate database for inventory management  

**Answer:** b) Implement Firestore transactions for inventory updates

---

# CRUD Operations - Delete Data

## Questions

### Questions on CRUD Operations - Delete Data

**Question 1:** What is the purpose of the `delete()` method in the following code snippet?
```javascript
const db = firebase.firestore();
db.collection('users').doc('user123').delete()
  .then(() => {
    console.log('User successfully deleted!');
  })
  .catch((error) => {
    console.error('Error removing user: ', error);
  });
```
a) To update a user's information  
b) To retrieve a user's data  
c) To delete a user from the database  
d) To create a new user  

**Answer:** c) To delete a user from the database

---

**Question 2:** In the tricky example, what is the purpose of using `Promise.all(deletePromises)`?
```javascript
const db = firebase.firestore();
const query = db.collection('orders').where('status', '==', 'canceled');

query.get().then((querySnapshot) => {
  const deletePromises = [];
  querySnapshot.forEach((doc) => {
    deletePromises.push(doc.ref.delete());
  });
  return Promise.all(deletePromises);
}).then(() => {
  console.log('All canceled orders successfully deleted!');
}).catch((error) => {
  console.error('Error deleting canceled orders: ', error);
});
```
a) To ensure that all delete operations are completed before logging the success message  
b) To create a new order  
c) To update the status of the orders  
d) To retrieve all canceled orders  

**Answer:** a) To ensure that all delete operations are completed before logging the success message

---

**Question 3:** What will happen if an error occurs during the deletion of a user in the first code snippet?
```javascript
const db = firebase.firestore();
db.collection('users').doc('user123').delete()
  .then(() => {
    console.log('User successfully deleted!');
  })
  .catch((error) => {
    console.error('Error removing user: ', error);
  });
```
a) The program will crash  
b) The error will be logged to the console  
c) The user will be deleted anyway  
d) The deletion will be retried automatically  

**Answer:** b) The error will be logged to the console

---

**Question 4:** In the context of the tricky example, what could potentially go wrong if you delete documents in a loop without handling asynchronous operations properly?
a) The program will run faster  
b) Some deletions may not complete before the next iteration starts, leading to unhandled promises  
c) All deletions will succeed without any issues  
d) The database will automatically handle the deletions  

**Answer:** b) Some deletions may not complete before the next iteration starts, leading to unhandled promises

---

**Question 5:** Which of the following statements is true regarding the `where` clause in the tricky example?
```javascript
const query = db.collection('orders').where('status', '==', 'canceled');
```
a) It retrieves all orders regardless of their status  
b) It filters the orders to only include those with a status of 'canceled'  
c) It updates the status of all orders to 'canceled'  
d) It deletes all orders from the database  

**Answer:** b) It filters the orders to only include those with a status of 'canceled'

---

# Realtime Update

## Questions

### Question 1:
What is the primary purpose of setting up a Firestore listener in a web application?

a) To store data permanently  
b) To monitor changes in a collection and update the UI in real-time  
c) To delete data from the database  
d) To create new collections  

**Answer:** b) To monitor changes in a collection and update the UI in real-time

---

### Question 2:
In the context of Firestore listeners, what does the callback function do when a new message is added to the 'messages' collection?

a) It deletes the old messages  
b) It updates the UI to display the new message  
c) It sends an email notification  
d) It logs the message to the console  

**Answer:** b) It updates the UI to display the new message

---

### Question 3:
Given the following code snippet, what will happen when a new order with the status 'pending' is added to the 'orders' collection?

```javascript
const ordersRef = firestore.collection('orders');
ordersRef.where('status', '==', 'pending').onSnapshot(snapshot => {
    snapshot.docChanges().forEach(change => {
        if (change.type === 'added') {
            console.log('New pending order: ', change.doc.data());
        }
    });
});
```

a) It will log all orders regardless of their status  
b) It will log only the new pending orders  
c) It will log all pending orders, including those that are completed  
d) It will not log anything  

**Answer:** b) It will log only the new pending orders

---

### Question 4:
What is a potential challenge when using a Firestore listener to track orders that can change status?

a) The listener can only track new orders, not updates  
b) The listener may not capture changes to existing orders that change from 'pending' to 'completed'  
c) The listener can only be set up for one collection at a time  
d) The listener will automatically delete completed orders  

**Answer:** b) The listener may not capture changes to existing orders that change from 'pending' to 'completed'

---

### Question 5:
Which of the following statements is true regarding Firestore listeners and real-time updates?

a) Listeners can only be set up for read operations  
b) Listeners automatically refresh the entire database  
c) Listeners provide real-time updates by listening for changes in the specified collection  
d) Listeners require manual intervention to update the UI  

**Answer:** c) Listeners provide real-time updates by listening for changes in the specified collection

---

# addSnapshotListener

## Questions

### Question 1:
What is the purpose of the `addSnapshotListener` method in Firestore?

a) To add a new document to a collection  
b) To listen for real-time updates to a Firestore collection  
c) To delete a document from a collection  
d) To fetch a single document from a collection  

**Answer:** b) To listen for real-time updates to a Firestore collection

---

### Question 2:
In the provided code snippet, what will happen when a new user is added to the 'users' collection?

```swift
let db = Firestore.firestore()
db.collection("users").addSnapshotListener { (querySnapshot, error) in
    guard let snapshot = querySnapshot else {
        print("Error fetching snapshots: \(error!)")
        return
    }
    snapshot.documentChanges.forEach { diff in
        if (diff.type == .added) {
            print("New user: \(diff.document.data())")
            // Update your UI here
        }
    }
}
```

a) The application will crash  
b) The new user's data will be printed to the console  
c) The listener will stop working  
d) The existing users will be deleted  

**Answer:** b) The new user's data will be printed to the console

---

### Question 3:
In the tricky example, what condition is checked before handling updates to orders?

```swift
let db = Firestore.firestore()
db.collection("orders").addSnapshotListener { (querySnapshot, error) in
    guard let snapshot = querySnapshot else {
        print("Error fetching snapshots: \(error!)")
        return
    }
    snapshot.documentChanges.forEach { diff in
        if (diff.type == .modified) {
            let orderData = diff.document.data()
            if let status = orderData["status"] as? String, status == "pending" {
                print("Updated pending order: \(diff.document.data())")
                // Handle the update for pending orders only
            }
        }
    }
}
```

a) The order must be in 'completed' status  
b) The order must be in 'pending' status  
c) The order must be in 'canceled' status  
d) The order must be in 'shipped' status  

**Answer:** b) The order must be in 'pending' status

---

### Question 4:
What type of changes does the listener in the tricky example respond to?

a) Only new documents added  
b) Only documents that have been deleted  
c) Only modified documents  
d) All types of document changes  

**Answer:** c) Only modified documents

---

### Question 5:
What will the following line of code do in the context of the provided examples?

```swift
snapshot.documentChanges.forEach { diff in
```

a) It will fetch all documents in the collection  
b) It will iterate over all changes made to the documents in the snapshot  
c) It will delete all documents in the snapshot  
d) It will create a new document in the snapshot  

**Answer:** b) It will iterate over all changes made to the documents in the snapshot

---

# DocumentChange.Type

## Questions

### Question 1:
In Firestore, what change type is classified when a new document is added to a collection?

a) MODIFIED  
b) REMOVED  
c) ADDED  
d) UPDATED  

**Answer:** c) ADDED

---

### Question 2:
If a user profile in Firestore is updated to change the user's email address while keeping the name the same, what is the change type?

a) ADDED  
b) REMOVED  
c) MODIFIED  
d) UNCHANGED  

**Answer:** c) MODIFIED

---

### Question 3:
What will be the change type if a user profile is deleted and then a new profile with the same name is created in Firestore?

a) MODIFIED  
b) ADDED  
c) REMOVED  
d) UNCHANGED  

**Answer:** b) ADDED

---

### Question 4:
Given the following code snippet, what will be the change type when the `userProfile` document is created?

```javascript
const userProfile = {
  name: "Jane Doe",
  email: "jane@example.com"
};
firestore.collection('users').add(userProfile);
```

a) MODIFIED  
b) ADDED  
c) REMOVED  
d) UPDATED  

**Answer:** b) ADDED

---

### Question 5:
In a scenario where a user profile is deleted and then a new profile with the same email is created, which of the following statements is true?

a) The change type will be MODIFIED.  
b) The change type will be ADDED.  
c) The change type will be REMOVED.  
d) The change type will be UNCHANGED.  

**Answer:** b) The change type will be ADDED.

---

# Cloud Firestore

## Questions

### Question 1:
In a mobile application using Cloud Firestore for managing to-do lists, what is the primary structure used to store each user's to-do items?

a) Collection  
b) Document  
c) Database  
d) Node  

**Answer:** a) Collection

---

### Question 2:
What feature of Cloud Firestore allows users to see real-time updates to their to-do lists across multiple devices?

a) Offline support  
b) Real-time synchronization  
c) Data encryption  
d) Batch writes  

**Answer:** b) Real-time synchronization

---

### Question 3:
In the context of an e-commerce application using Cloud Firestore, what is the best way to handle the situation where two users attempt to purchase the last item in stock?

a) Allow both purchases and update the stock later  
b) Use Firestore's transactions to ensure atomic updates  
c) Notify one user that the item is out of stock after the purchase  
d) Implement a first-come, first-served basis without any checks  

**Answer:** b) Use Firestore's transactions to ensure atomic updates

---

### Question 4:
Given the following code snippet, what will happen if two users try to execute the transaction at the same time?

```javascript
const db = firebase.firestore();
const productRef = db.collection('products').doc('productId');

db.runTransaction(async (transaction) => {
    const doc = await transaction.get(productRef);
    if (!doc.exists) {
        throw "Document does not exist!";
    }
    const newStock = doc.data().stock - 1;
    transaction.update(productRef, { stock: newStock });
});
```

a) Both transactions will succeed, and the stock will be decremented twice.  
b) One transaction will succeed, and the other will fail due to a conflict.  
c) The stock will remain unchanged regardless of the transactions.  
d) An error will be thrown for both transactions.  

**Answer:** b) One transaction will succeed, and the other will fail due to a conflict.

---

### Question 5:
Which of the following statements about Cloud Firestore is NOT true?

a) It supports real-time data synchronization.  
b) It allows for complex querying of data.  
c) It requires a fixed schema for data storage.  
d) It can handle offline data persistence.  

**Answer:** c) It requires a fixed schema for data storage.

---

# Security Rules

## Questions

### Question 1:
What does the following Firebase security rule allow for the `/users/{userId}` path?

```plaintext
match /users/{userId} {
  allow read, write: if request.auth != null && request.auth.uid == userId;
}
```

a) Anyone can read and write user documents.  
b) Only authenticated users can read and write their own user documents.  
c) Only unauthenticated users can read their own user documents.  
d) Only admins can read and write user documents.  

**Answer:** b) Only authenticated users can read and write their own user documents.

---

### Question 2:
In the tricky example provided, who is allowed to write to the `publicPosts` collection?

```plaintext
match /publicPosts/{postId} {
  allow read: if true; // Anyone can read public posts
  allow write: if request.auth != null && request.auth.token.role == 'admin'; // Only admins can write
}
```

a) Anyone can write to the `publicPosts` collection.  
b) Only authenticated users can write to the `publicPosts` collection.  
c) Only users with an 'admin' role can write to the `publicPosts` collection.  
d) Only users with a 'guest' role can write to the `publicPosts` collection.  

**Answer:** c) Only users with an 'admin' role can write to the `publicPosts` collection.

---

### Question 3:
What is the purpose of the condition `request.auth != null` in the security rules?

a) It checks if the user is an admin.  
b) It ensures that the user is authenticated.  
c) It allows all users to access the data.  
d) It restricts access to only public data.  

**Answer:** b) It ensures that the user is authenticated.

---

### Question 4:
If a user with the UID `user123` tries to access their document in the `/users/{userId}` path, which of the following conditions must be true for them to successfully read or write their document?

```plaintext
allow read, write: if request.auth != null && request.auth.uid == userId;
```

a) The user must be authenticated and their UID must match `user123`.  
b) The user must be authenticated and their UID must not match `user123`.  
c) The user can access the document without authentication.  
d) The user can access the document if they are an admin.  

**Answer:** a) The user must be authenticated and their UID must match `user123`.

---

### Question 5:
In the context of the tricky example, what could be a potential security risk if role management is not implemented correctly?

a) Users might be able to read their own documents.  
b) Users might be able to write to the `publicPosts` collection without being an admin.  
c) Only admins can read public posts.  
d) All users can write to any document in the database.  

**Answer:** b) Users might be able to write to the `publicPosts` collection without being an admin.

---

# Firebase Authentication

## Questions

### Questions on Firebase Authentication

**Question 1:** What is the primary purpose of Firebase Authentication in a mobile app?  
a) To store user data  
b) To handle user registration and login securely  
c) To manage app performance  
d) To provide analytics for user behavior  
**Answer:** b) To handle user registration and login securely

---

**Question 2:** When a user signs up using Firebase Authentication, what action is typically taken to verify their email address?  
a) The user is redirected to a different website  
b) A verification email is sent to the user  
c) The user must call customer support  
d) The user is automatically logged in  
**Answer:** b) A verification email is sent to the user

---

**Question 3:** In the context of Firebase Authentication, what is a potential issue when allowing users to log in with multiple social media accounts?  
a) Users may forget their passwords  
b) Users may not receive verification emails  
c) Users may be confused about which account they are logging into  
d) Users will have to create a new account for each social media login  
**Answer:** c) Users may be confused about which account they are logging into

---

**Question 4:** Consider the following code snippet for signing in a user with email and password using Firebase Authentication. What will happen if the sign-in is successful?

```javascript
firebase.auth().signInWithEmailAndPassword(email, password)
  .then((userCredential) => {
    // Signed in 
    var user = userCredential.user;
    console.log("User signed in:", user);
  })
  .catch((error) => {
    var errorCode = error.code;
    var errorMessage = error.message;
    console.error("Error signing in:", errorCode, errorMessage);
  });
```

a) The user will be logged out  
b) The user will be redirected to a different page  
c) The user information will be logged to the console  
d) An error message will be displayed  
**Answer:** c) The user information will be logged to the console

---

**Question 5:** If a user initially signs up with an email/password and later tries to link their Google account, what must the developer ensure?  
a) The user must create a new account  
b) The accounts are merged correctly without losing any user data  
c) The user must log out before linking accounts  
d) The Google account must be deleted  
**Answer:** b) The accounts are merged correctly without losing any user data

---

**Question 6:** Which of the following is NOT a feature of Firebase Authentication?  
a) Email/password authentication  
b) Social media login integration  
c) Real-time database management  
d) Anonymous authentication  
**Answer:** c) Real-time database management

---

**Question 7:** What is the first step a developer should take when implementing Firebase Authentication in their app?  
a) Create a user interface for login  
b) Set up Firebase in their project  
c) Write the code for user data storage  
d) Design the app's layout  
**Answer:** b) Set up Firebase in their project

---

# User Registration and Login

## Questions

### Question 1:
What method is used in Firebase Authentication to create a new user account with an email and password?

a) signInWithEmailAndPassword  
b) createUserWithEmailAndPassword  
c) registerUser  
d) addUser  

**Answer:** b) createUserWithEmailAndPassword

---

### Question 2:
What happens if a user tries to register with an email that is already associated with an existing account in Firebase Authentication?

a) The user is registered successfully.  
b) An error is thrown indicating that the email is already in use.  
c) The user is logged in automatically.  
d) The app crashes.  

**Answer:** b) An error is thrown indicating that the email is already in use.

---

### Question 3:
In the context of user registration, what is the purpose of sending a verification email?

a) To confirm the user's password.  
b) To verify the user's email address.  
c) To notify the user of successful registration.  
d) To provide the user with promotional offers.  

**Answer:** b) To verify the user's email address.

---

### Question 4:
What should an app do if a user attempts to log in with incorrect credentials?

a) Log the user in anyway.  
b) Provide a clear message indicating that the login failed.  
c) Redirect the user to the registration page.  
d) Automatically reset the user's password.  

**Answer:** b) Provide a clear message indicating that the login failed.

---

### Question 5:
Consider the following code snippet for user registration using Firebase Authentication:

```javascript
firebase.auth().createUserWithEmailAndPassword(email, password)
  .then((userCredential) => {
    // User registered successfully
  })
  .catch((error) => {
    // Handle Errors here.
  });
```
What is the purpose of the `.catch((error) => { ... })` block in this code?

a) To handle successful user registration.  
b) To log the user out.  
c) To handle errors that occur during user registration.  
d) To redirect the user to the home screen.  

**Answer:** c) To handle errors that occur during user registration.

---

# Social Media Integration

## Questions

### Question 1:
What is the primary purpose of using Firebase Authentication in a mobile app for social media integration?
a) To create a separate username and password for each user  
b) To allow users to sign in using their social media accounts  
c) To store user data in a local database  
d) To prevent users from accessing the app  

**Answer:** b) To allow users to sign in using their social media accounts

---

### Question 2:
In the typical example of social media integration, what happens after a user successfully signs in with their Google account?
a) The user is logged out of the app  
b) Firebase retrieves the user's profile information and creates a new user account if necessary  
c) The user is redirected to the app's homepage without any authentication  
d) The app automatically deletes the user's profile  

**Answer:** b) Firebase retrieves the user's profile information and creates a new user account if necessary

---

### Question 3:
In the tricky example of handling multiple social media accounts, what must the app check when a user tries to log in with a different social media account?
a) If the user has a premium subscription  
b) If the new account has a different username  
c) If the email associated with the new account matches the existing account's email  
d) If the user has logged in within the last 30 days  

**Answer:** c) If the email associated with the new account matches the existing account's email

---

### Question 4:
Consider the following code snippet for signing in with Google using Firebase Authentication:

```javascript
firebase.auth().signInWithPopup(new firebase.auth.GoogleAuthProvider())
  .then((result) => {
    // User signed in
    var user = result.user;
    console.log(user.displayName);
  })
  .catch((error) => {
    console.error(error.message);
  });
```
What does the `signInWithPopup` method do in this context?
a) It creates a new user account without authentication  
b) It opens a popup for the user to sign in with their Google account  
c) It logs the user out of the app  
d) It retrieves the user's profile information without signing in  

**Answer:** b) It opens a popup for the user to sign in with their Google account

---

### Question 5:
What is a potential issue when a user tries to log in with a different social media account after initially signing up with another?
a) The app will crash  
b) The user will be required to create a new account  
c) The app must ensure that both accounts are linked to the same user profile  
d) The user will lose access to their previous data  

**Answer:** c) The app must ensure that both accounts are linked to the same user profile

---

# Access Control

## Questions

### Question 1:
In a mobile application using Firebase Authentication, which of the following roles typically has the ability to manage user accounts and moderate discussions?

a) Member  
b) Admin  
c) Guest  
d) Viewer  

**Answer:** b) Admin

---

### Question 2:
In the context of Firebase Firestore security rules, which of the following statements is true regarding access control for authenticated users?

a) All users can read and write to any collection regardless of their role.  
b) Only authenticated users can read or write to specific collections based on their roles.  
c) Only admins can access the Firestore database.  
d) Users can access any data without authentication.  

**Answer:** b) Only authenticated users can read or write to specific collections based on their roles.

---

### Question 3:
Consider the following Firestore security rule snippet:

```javascript
service cloud.firestore {
  match /databases/{database}/documents {
    match /projects/{projectId} {
      allow read, write: if request.auth != null && request.auth.token.role == 'owner';
    }
  }
}
```
What does this rule enforce regarding access to project documents?

a) Only users with a 'viewer' role can read project documents.  
b) Only authenticated users with the role of 'owner' can read and write to project documents.  
c) All authenticated users can read project documents.  
d) Anyone can read and write to project documents.  

**Answer:** b) Only authenticated users with the role of 'owner' can read and write to project documents.

---

### Question 4:
In a project management tool, if a project owner revokes access from a collaborator, what must happen to ensure the collaborator can no longer view or edit project details?

a) The collaborator's role must be changed to 'viewer'.  
b) The Firestore security rules must be updated to reflect the change in access.  
c) The collaborator must be logged out of the application.  
d) The project must be deleted.  

**Answer:** b) The Firestore security rules must be updated to reflect the change in access.

---

### Question 5:
Which of the following methods can users utilize to sign up for a fitness community application using Firebase Authentication?

a) Only email and password  
b) Only social media accounts  
c) Both email/password and social media accounts  
d) None of the above  

**Answer:** c) Both email/password and social media accounts

---

