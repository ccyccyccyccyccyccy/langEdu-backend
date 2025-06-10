# Firebase

## Questions

### Question 1:
What Firebase service would you use to manage user authentication in a mobile application?
a) Firestore  
b) Firebase Cloud Messaging  
c) Firebase Authentication  
d) Firebase Hosting  
**Answer:** c) Firebase Authentication

### Question 2:
In the context of Firebase, what is Firestore primarily used for?
a) Sending push notifications  
b) Storing user authentication data  
c) Storing and syncing data in real-time  
d) Hosting web applications  
**Answer:** c) Storing and syncing data in real-time

### Question 3:
What could be a consequence of setting Firestore security rules too permissively?
a) Users can only read their own data  
b) Unauthorized users can access private messages  
c) The application will crash  
d) Data will be stored in a different format  
**Answer:** b) Unauthorized users can access private messages

### Question 4:
Given the following Firestore security rule, what does it allow?
```plaintext
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null;
    }
  }
}
```
a) Anyone can read and write to the users collection  
b) Only authenticated users can read and write to their own user document  
c) Only the owner of the document can read and write to it  
d) No one can read or write to the users collection  
**Answer:** b) Only authenticated users can read and write to their own user document

### Question 5:
Which Firebase service would you use to send notifications to users when someone likes their post?
a) Firestore  
b) Firebase Cloud Messaging  
c) Firebase Storage  
d) Firebase Functions  
**Answer:** b) Firebase Cloud Messaging

### Question 6:
What is a potential risk of using Firestore without properly configured security rules?
a) Increased app performance  
b) Data redundancy  
c) Data breaches and unauthorized access  
d) Slower data retrieval times  
**Answer:** c) Data breaches and unauthorized access

### Question 7:
If a developer wants to implement a real-time chat feature using Firebase, which combination of services should they primarily use?
a) Firebase Hosting and Firebase Storage  
b) Firebase Authentication and Firestore  
c) Firebase Cloud Functions and Firebase Analytics  
d) Firebase Cloud Messaging and Firebase Hosting  
**Answer:** b) Firebase Authentication and Firestore

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

---

### Question 2:
In a collaborative document editor using a Realtime Database, what is a potential issue that may arise when multiple users edit the same section of the document simultaneously?

a) The database will automatically save all changes without conflict.  
b) One user's changes may overwrite another's if not managed properly.  
c) The document will become read-only for all users.  
d) All users will be logged out of the application.  

**Answer:** b) One user's changes may overwrite another's if not managed properly.

---

### Question 3:
Given the following JSON structure for a chat message in a Realtime Database, which of the following represents a correct way to store a new message?

```json
{
  "messages": {
    "message1": {
      "user": "Alice",
      "text": "Hello, everyone!",
      "timestamp": "2023-10-01T12:00:00Z"
    }
  }
}
```

a) `database.ref('messages').set({ user: 'Alice', text: 'Hello, everyone!', timestamp: '2023-10-01T12:00:00Z' });`  
b) `database.ref('messages/message1').push({ user: 'Alice', text: 'Hello, everyone!', timestamp: '2023-10-01T12:00:00Z' });`  
c) `database.ref('messages/message1').set({ user: 'Alice', text: 'Hello, everyone!', timestamp: '2023-10-01T12:00:00Z' });`  
d) `database.ref('messages').add({ user: 'Alice', text: 'Hello, everyone!', timestamp: '2023-10-01T12:00:00Z' });`  

**Answer:** c) `database.ref('messages/message1').set({ user: 'Alice', text: 'Hello, everyone!', timestamp: '2023-10-01T12:00:00Z' });`

---

### Question 4:
What data format is typically used to store messages in a Realtime Database?

a) XML  
b) CSV  
c) JSON  
d) HTML  

**Answer:** c) JSON

---

### Question 5:
In a Realtime Database, how can you ensure that all users see the latest version of a document when multiple users are editing it?

a) By allowing only one user to edit at a time.  
b) By implementing a conflict resolution strategy.  
c) By disabling real-time updates.  
d) By saving changes only at the end of the editing session.  

**Answer:** b) By implementing a conflict resolution strategy.

---

# Use cases for Realtime Database

## Questions

### Question 1:
What is a typical use case for a Realtime Database?
a) Storing static website content  
b) A chat application where users can send and receive messages in real-time  
c) A photo editing software  
d) A video streaming service  

**Answer:** b) A chat application where users can send and receive messages in real-time

---

### Question 2:
In a collaborative document editing tool using a Realtime Database, what is a potential challenge that developers must address?
a) Ensuring all users have the same internet speed  
b) Handling conflicts when two users edit the same section simultaneously  
c) Making sure the document is saved locally  
d) Preventing users from accessing the document  

**Answer:** b) Handling conflicts when two users edit the same section simultaneously

---

### Question 3:
Which of the following scenarios best illustrates the use of a Realtime Database?
a) A blog where articles are published once a week  
b) A social media platform where users can post updates and see them instantly  
c) An online store with a static product catalog  
d) A personal diary application  

**Answer:** b) A social media platform where users can post updates and see them instantly

---

### Question 4:
Consider the following code snippet for a chat application using a Realtime Database:

```javascript
const chatRef = database.ref('chats');
chatRef.on('child_added', (snapshot) => {
    const message = snapshot.val();
    displayMessage(message);
});
```
What does the `child_added` event listener do in this context?
a) It retrieves all messages at once  
b) It listens for new messages added to the chat in real-time  
c) It deletes messages from the chat  
d) It updates existing messages in the chat  

**Answer:** b) It listens for new messages added to the chat in real-time

---

### Question 5:
What feature of a Realtime Database is crucial for a collaborative document editing tool?
a) Data encryption  
b) Real-time synchronization of changes  
c) User authentication  
d) Data backup  

**Answer:** b) Real-time synchronization of changes

--- 

### Question 6:
In a chat application, if two users send messages at the same time, what must the Realtime Database ensure?
a) Only one message is sent  
b) Messages are sent in the order they were typed  
c) Both messages are received and displayed without conflicts  
d) Messages are stored for later retrieval  

**Answer:** c) Both messages are received and displayed without conflicts

---

# Main services provided by Firebase

## Questions

### Question 1:
What is one of the main services provided by Firebase that allows real-time data synchronization?
a) Firebase Hosting  
b) Firebase Realtime Database  
c) Firebase Cloud Functions  
d) Firebase Authentication  
**Answer:** b) Firebase Realtime Database

### Question 2:
In the context of a live sports scoreboard using Firebase, which feature is crucial for ensuring that fans see the most current game statistics without refreshing the page?
a) Firebase Storage  
b) Real-time data synchronization  
c) User authentication  
d) Static file hosting  
**Answer:** b) Real-time data synchronization

### Question 3:
Which of the following scenarios best illustrates a tricky implementation of Firebase's Realtime Database?
a) A blog that updates posts every hour  
b) A live auction platform where multiple users can place bids simultaneously  
c) A weather app that fetches data every 10 minutes  
d) A photo gallery that displays images from a local directory  
**Answer:** b) A live auction platform where multiple users can place bids simultaneously

### Question 4:
Consider the following code snippet for updating a score in a Firebase Realtime Database:

```javascript
firebase.database().ref('games/game1/score').set({
  home: 10,
  away: 5
});
```
What does this code do?
a) It retrieves the current score of the game.  
b) It deletes the score of the game.  
c) It updates the score of the home and away teams to 10 and 5, respectively.  
d) It initializes the score for the game to 10 and 5.  
**Answer:** c) It updates the score of the home and away teams to 10 and 5, respectively.

### Question 5:
Which Firebase service would you use to ensure that the highest bid in a live auction is always displayed correctly?
a) Firebase Cloud Messaging  
b) Firebase Realtime Database  
c) Firebase Authentication  
d) Firebase Analytics  
**Answer:** b) Firebase Realtime Database

---

# Cloud Firestore

## Questions

### Question 1:
In a collaborative task management tool using Cloud Firestore, what is the primary benefit of real-time updates for team members?
a) It reduces the need for internet connectivity  
b) It allows team members to see changes instantly, improving collaboration  
c) It eliminates the need for a user interface  
d) It ensures that tasks are completed faster  

**Answer:** b) It allows team members to see changes instantly, improving collaboration

---

### Question 2:
In a live polling application using Cloud Firestore, what is a critical challenge when multiple users vote simultaneously?
a) Ensuring that all users have the same internet speed  
b) Counting votes accurately and displaying results correctly  
c) Preventing users from voting more than once  
d) Making the application visually appealing  

**Answer:** b) Counting votes accurately and displaying results correctly

---

### Question 3:
Given the following code snippet for adding a task to a Firestore collection, what will happen if two users try to add a task at the same time?

```javascript
const db = firebase.firestore();
db.collection("tasks").add({
    title: "New Task",
    completed: false
});
```

a) One of the tasks will be lost  
b) Both tasks will be added successfully  
c) An error will occur due to simultaneous writes  
d) The application will crash  

**Answer:** b) Both tasks will be added successfully

---

### Question 4:
Which of the following features of Cloud Firestore is essential for maintaining consistency in a live polling application?
a) Offline support  
b) Real-time listeners  
c) Data encryption  
d) User authentication  

**Answer:** b) Real-time listeners

---

### Question 5:
In the context of a collaborative task management tool, which Firestore feature would you use to ensure that all team members receive updates when a task is marked as complete?
a) Firestore Security Rules  
b) Firestore Batch Writes  
c) Firestore Real-time Updates  
d) Firestore Indexing  

**Answer:** c) Firestore Real-time Updates

---

### Question 6:
What is the main advantage of using Cloud Firestore over traditional databases for a live polling application?
a) It requires less coding  
b) It automatically scales with the number of users  
c) It is free to use  
d) It does not require internet access  

**Answer:** b) It automatically scales with the number of users

---

# Data Structure - Collections and Documents

## Questions

### Question 1:
In a customer support chat system, which data structure is most suitable for storing messages exchanged between users and support agents in real-time?

a) Stack  
b) Queue  
c) Linked List  
d) Hash Table  

**Answer:** b) Queue

---

### Question 2:
In a multiplayer online game, which of the following is a key challenge when synchronizing player actions in real-time?

a) Ensuring all players have the same internet speed  
b) Managing the game state updates efficiently  
c) Limiting the number of players in the game  
d) Reducing the size of the game assets  

**Answer:** b) Managing the game state updates efficiently

---

### Question 3:
Consider the following code snippet for a chat system using a collection to store messages:

```javascript
const messages = [
    { user: 'Alice', text: 'Hello!', timestamp: 1620000000000 },
    { user: 'Bob', text: 'Hi Alice!', timestamp: 1620000001000 }
];
```
What data structure is being used to store the messages?

a) Array  
b) Object  
c) Set  
d) Map  

**Answer:** a) Array

---

### Question 4:
In a real-time database for a multiplayer game, which of the following strategies can help ensure all players see the same game state?

a) Allow players to update their game state independently  
b) Use a centralized server to manage game state updates  
c) Send game state updates only when a player requests them  
d) Limit the number of players in the game  

**Answer:** b) Use a centralized server to manage game state updates

---

### Question 5:
Which of the following best describes a "real-time database"?

a) A database that only stores data temporarily  
b) A database that allows for immediate data retrieval and updates  
c) A database that requires manual refreshing to see updates  
d) A database that is only accessible during business hours  

**Answer:** b) A database that allows for immediate data retrieval and updates

--- 

### Question 6:
In the context of a customer support chat system, what is the primary benefit of using a real-time database?

a) It reduces the cost of data storage  
b) It allows for instant communication between users and agents  
c) It simplifies the user interface  
d) It eliminates the need for internet connectivity  

**Answer:** b) It allows for instant communication between users and agents

--- 

### Question 7:
In a real-time multiplayer game, which data structure would be most effective for tracking the positions of all players?

a) Array  
b) Stack  
c) Queue  
d) Tree  

**Answer:** a) Array

--- 

### Question 8:
What is a potential drawback of using a real-time database in a multiplayer online game?

a) Increased latency in data updates  
b) Complexity in managing concurrent updates  
c) Limited scalability for large player bases  
d) All of the above  

**Answer:** d) All of the above

--- 

These questions aim to assess understanding of data structures and their applications in real-time systems, particularly in customer support and multiplayer gaming contexts.

---

# CRUD Operations - Create Data

## Questions

### Questions on CRUD Operations

**Question 1:** In a CRUD application, what does the 'C' stand for?  
a) Create  
b) Change  
c) Copy  
d) Clear  
**Answer:** a) Create

---

**Question 2:** Which of the following is an example of a 'Read' operation in a CRUD application?  
a) Adding a new user to the database  
b) Updating user information  
c) Retrieving user details from the database  
d) Deleting a user from the database  
**Answer:** c) Retrieving user details from the database

---

**Question 3:** In a real-time stock trading application, which of the following is crucial for ensuring that users see the most current stock prices?  
a) Regularly scheduled updates every minute  
b) Instantaneous updates across all users' screens  
c) Manual refresh by the user  
d) Sending daily summaries via email  
**Answer:** b) Instantaneous updates across all users' screens

---

**Question 4:** Consider the following code snippet for creating a new user in a database. What is the purpose of the `createUser` function?

```javascript
function createUser(username, password) {
    database.ref('users/' + username).set({
        password: password,
        createdAt: new Date().toISOString()
    });
}
```
a) To delete a user from the database  
b) To update an existing user's password  
c) To create a new user with a username and password  
d) To retrieve user information  
**Answer:** c) To create a new user with a username and password

---

**Question 5:** In the context of a live dashboard for monitoring website analytics, which of the following operations would be considered a 'Delete' operation?  
a) Adding a new metric for user engagement  
b) Removing outdated metrics from the dashboard  
c) Updating the visitor count  
d) Fetching page views data  
**Answer:** b) Removing outdated metrics from the dashboard

---

**Question 6:** What is a potential challenge when implementing CRUD operations in a real-time stock trading application?  
a) Ensuring that the database is always empty  
b) Handling rapid updates and ensuring data consistency  
c) Making the user interface visually appealing  
d) Limiting the number of users accessing the application  
**Answer:** b) Handling rapid updates and ensuring data consistency

---

**Question 7:** Which of the following best describes the 'Update' operation in a CRUD context?  
a) Adding new data to the database  
b) Modifying existing data in the database  
c) Removing data from the database  
d) Retrieving data from the database  
**Answer:** b) Modifying existing data in the database

---

**Question 8:** In a real-time application, what technology is often used to ensure that data is updated instantly across all users' screens?  
a) Static HTML pages  
b) WebSockets  
c) FTP transfers  
d) Email notifications  
**Answer:** b) WebSockets

--- 

These questions cover various aspects of CRUD operations, focusing on both theoretical understanding and practical application in real-time scenarios.

---

# Use Cases

## Questions

### Question 1:
What is a primary use case for Firebase Realtime Database?
a) Storing large files  
b) Real-time data synchronization across clients  
c) Image processing  
d) Video streaming  

**Answer:** b) Real-time data synchronization across clients

---

### Question 2:
In a chat application using Firebase Realtime Database, what is the benefit of using this database for message updates?
a) Messages are stored locally on each client  
b) Messages are updated only when the application is restarted  
c) Messages are instantly updated for all users without refreshing the page  
d) Messages can only be sent to one user at a time  

**Answer:** c) Messages are instantly updated for all users without refreshing the page

---

### Question 3:
Which of the following is a challenge when implementing custom authentication in Firebase?
a) Using built-in sign-in methods  
b) Handling user credentials securely  
c) Syncing data in real-time  
d) Storing user data  

**Answer:** b) Handling user credentials securely

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
a) Signs in a user with Google credentials  
b) Signs in a user with email and password  
c) Creates a new user account  
d) Logs out the current user  

**Answer:** b) Signs in a user with email and password

---

### Question 5:
When using Firebase Authentication, which of the following is NOT a built-in sign-in method?
a) Email and password  
b) Google  
c) Facebook  
d) Custom username and password  

**Answer:** d) Custom username and password

--- 

### Question 6:
What is a potential risk when managing sessions with custom authentication in Firebase?
a) Users can sign in with multiple accounts  
b) User sessions may not expire properly  
c) Users can only access their own data  
d) Sessions are automatically managed by Firebase  

**Answer:** b) User sessions may not expire properly

--- 

### Question 7:
In the context of Firebase Realtime Database, what does "data sync" refer to?
a) Backing up data to a local server  
b) Updating data across all connected clients in real-time  
c) Storing data in a cloud storage service  
d) Encrypting data for security  

**Answer:** b) Updating data across all connected clients in real-time

--- 

### Question 8:
Which of the following Firebase services is primarily used for user authentication?
a) Firebase Cloud Messaging  
b) Firebase Realtime Database  
c) Firebase Authentication  
d) Firebase Hosting  

**Answer:** c) Firebase Authentication

--- 

These questions cover the concepts of Firebase Realtime Database and Firebase Authentication, testing the understanding of their use cases, functionalities, and potential challenges.

---

# Cloud Firestore

## Questions

### Question 1:
What type of database is Cloud Firestore?
a) Relational database  
b) NoSQL database  
c) Graph database  
d) In-memory database  
**Answer:** b) NoSQL database

### Question 2:
In an e-commerce app using Cloud Firestore, which feature allows for real-time updates of product listings?
a) Batch processing  
b) Offline capabilities  
c) Real-time listeners  
d) Scheduled queries  
**Answer:** c) Real-time listeners

### Question 3:
What must developers handle when multiple users are editing the same document in Firestore?
a) Data redundancy  
b) Data integrity conflicts  
c) Data encryption  
d) Data normalization  
**Answer:** b) Data integrity conflicts

### Question 4:
Given the following code snippet, what will happen when the user comes back online after making changes while offline?

```javascript
const docRef = firestore.collection('products').doc('product1');

docRef.set({
  name: 'New Product',
  price: 20
}, { merge: true });
```

a) The changes will be discarded.  
b) The changes will overwrite the existing document.  
c) The changes will merge with the existing document.  
d) An error will occur.  
**Answer:** c) The changes will merge with the existing document.

### Question 5:
Which of the following is a benefit of using Cloud Firestore for an e-commerce application?
a) It requires a fixed schema.  
b) It supports complex queries and real-time updates.  
c) It is only accessible from mobile devices.  
d) It does not support offline capabilities.  
**Answer:** b) It supports complex queries and real-time updates.

---

# CRUD Operations - Read Data

## Questions

### Questions on CRUD Operations - Read Data

**Question 1:** What is the primary purpose of Firebase Authentication?  
a) To store user data  
b) To manage user sign-in methods  
c) To create mobile applications  
d) To send notifications  
**Answer:** b) To manage user sign-in methods

---

**Question 2:** Which of the following is NOT a sign-in method provided by Firebase Authentication?  
a) Email/Password  
b) Phone Number  
c) Social Media Logins  
d) Biometric Authentication  
**Answer:** d) Biometric Authentication

---

**Question 3:** In the context of Firebase Authentication, which of the following code snippets correctly initializes Firebase?  
```javascript
firebase.initializeApp({
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
});
```
a) Correct  
b) Incorrect  
**Answer:** a) Correct

---

**Question 4:** What is a potential challenge when implementing multi-factor authentication (MFA) with Firebase Authentication?  
a) Ensuring the user can only sign in with one method  
b) Integrating the second factor securely while maintaining user experience  
c) Allowing users to reset their passwords  
d) Providing a single sign-on experience  
**Answer:** b) Integrating the second factor securely while maintaining user experience

---

**Question 5:** Which of the following Firebase Authentication methods allows users to sign up using their Google account?  
a) Email/Password  
b) Phone Number  
c) Google Sign-In  
d) Anonymous Sign-In  
**Answer:** c) Google Sign-In

---

**Question 6:** When implementing MFA, which of the following is a common second factor used?  
a) Username  
b) Password  
c) SMS Verification Code  
d) Security Question  
**Answer:** c) SMS Verification Code

---

**Question 7:** In Firebase Authentication, which method would you use to sign in a user with their email and password?  
a) firebase.auth().signInWithEmail()  
b) firebase.auth().signInWithEmailAndPassword(email, password)  
c) firebase.auth().loginWithEmail(email, password)  
d) firebase.auth().authenticateUser(email, password)  
**Answer:** b) firebase.auth().signInWithEmailAndPassword(email, password)

---

**Question 8:** What is a key benefit of using Firebase Authentication for user management in mobile apps?  
a) It requires extensive backend development  
b) It simplifies user management with various sign-in options  
c) It eliminates the need for user data storage  
d) It provides a complex user interface  
**Answer:** b) It simplifies user management with various sign-in options

---

# CRUD Operations - Update Data

## Questions

### Question 1:
What does CRUD stand for in the context of database operations?
a) Create, Read, Update, Delete  
b) Create, Retrieve, Update, Destroy  
c) Create, Read, Upload, Download  
d) Create, Read, Use, Delete  
**Answer:** a) Create, Read, Update, Delete

### Question 2:
In a photo-sharing app using Cloud Storage, which operation would be used to change the metadata of an uploaded image?
a) Create  
b) Read  
c) Update  
d) Delete  
**Answer:** c) Update

### Question 3:
Which of the following is a key consideration when managing file permissions in Cloud Storage?
a) Ensuring all users can access all files  
b) Setting up security rules to restrict access  
c) Allowing anonymous uploads  
d) Automatically deleting old files  
**Answer:** b) Setting up security rules to restrict access

### Question 4:
Given the following code snippet, what operation is being performed?

```javascript
const storageRef = firebase.storage().ref();
const fileRef = storageRef.child('images/photo.jpg');
fileRef.delete().then(() => {
  console.log('File deleted successfully');
}).catch((error) => {
  console.error('Error deleting file:', error);
});
```
a) Create  
b) Read  
c) Update  
d) Delete  
**Answer:** d) Delete

### Question 5:
In a Cloud Storage scenario, which of the following would be an example of a "Read" operation?
a) Uploading a new image  
b) Changing the permissions of an existing file  
c) Retrieving a user's uploaded photo  
d) Deleting a video file  
**Answer:** c) Retrieving a user's uploaded photo

---

# Cloud Firestore CRUD Operations

## Questions

### Questions on Cloud Firestore CRUD Operations

**Question 1:** What does CRUD stand for in the context of database operations?  
a) Create, Read, Update, Delete  
b) Create, Retrieve, Update, Delete  
c) Create, Read, Upload, Delete  
d) Create, Read, Update, Download  
**Answer:** a) Create, Read, Update, Delete

---

**Question 2:** Which of the following is a method to add a document to a Firestore collection?  
a) `db.collection("users").add(data)`  
b) `db.collection("users").insert(data)`  
c) `db.collection("users").create(data)`  
d) `db.collection("users").push(data)`  
**Answer:** a) `db.collection("users").add(data)`

---

**Question 3:** In Firestore, which method would you use to retrieve all documents from a collection named "products"?  
a) `db.collection("products").getAll()`  
b) `db.collection("products").fetch()`  
c) `db.collection("products").get()`  
d) `db.collection("products").retrieve()`  
**Answer:** c) `db.collection("products").get()`

---

**Question 4:** What is the correct way to update a document in Firestore?  
```javascript
db.collection("users").doc("user_id").____(data);
```
a) `modify`  
b) `update`  
c) `change`  
d) `edit`  
**Answer:** b) `update`

---

**Question 5:** When deleting a document in Firestore, which method is used?  
```javascript
db.collection("users").doc("user_id").____();
```
a) `remove`  
b) `delete`  
c) `destroy`  
d) `clear`  
**Answer:** b) `delete`

---

**Question 6:** Which of the following statements is true regarding Firestore's real-time capabilities?  
a) Firestore does not support real-time updates.  
b) Firestore allows you to listen to changes in a document or collection in real-time.  
c) Firestore requires manual polling to check for updates.  
d) Firestore can only send updates to web applications.  
**Answer:** b) Firestore allows you to listen to changes in a document or collection in real-time.

---

**Question 7:** In the context of Firebase Cloud Messaging (FCM), what is the primary purpose of FCM?  
a) To store user data  
b) To send notifications to users across platforms  
c) To manage user authentication  
d) To host web applications  
**Answer:** b) To send notifications to users across platforms

---

**Question 8:** When handling notifications in FCM, which of the following is a best practice?  
a) Sending notifications without any formatting  
b) Ignoring background notifications  
c) Ensuring notifications are formatted correctly for different platforms  
d) Sending the same notification to all users without targeting  
**Answer:** c) Ensuring notifications are formatted correctly for different platforms

---

**Question 9:** Which of the following is NOT a valid way to send a notification using FCM?  
a) Using the FCM REST API  
b) Using Firebase Admin SDK  
c) Using Firebase Cloud Functions  
d) Using a direct database query  
**Answer:** d) Using a direct database query

---

**Question 10:** In FCM, what is the purpose of the "notification" payload?  
a) To store user preferences  
b) To display a message to the user  
c) To manage user sessions  
d) To log user activity  
**Answer:** b) To display a message to the user

---

# Delete Data in Cloud Firestore

## Questions

### Multiple Choice Questions on Deleting Data in Cloud Firestore

**Question 1:** What is the correct method to delete a document in Cloud Firestore using JavaScript?  
a) `firestore.collection('users').remove('userId')`  
b) `firestore.collection('users').delete('userId')`  
c) `firestore.collection('users').doc('userId').delete()`  
d) `firestore.collection('users').removeDocument('userId')`  
**Answer:** c) `firestore.collection('users').doc('userId').delete()`

---

**Question 2:** Which of the following statements is true regarding deleting data in Cloud Firestore?  
a) Deleting a document also deletes all its subcollections.  
b) Deleted data can be recovered easily.  
c) You can delete multiple documents in a single operation using a batch.  
d) Deleting data does not affect the billing.  
**Answer:** c) You can delete multiple documents in a single operation using a batch.

---

**Question 3:** If you want to delete all documents in a collection in Cloud Firestore, which approach is recommended?  
a) Use a loop to delete each document individually.  
b) Use the `delete()` method on the collection directly.  
c) Use a batch operation to delete all documents at once.  
d) There is no way to delete all documents in a collection at once.  
**Answer:** c) Use a batch operation to delete all documents at once.

---

**Question 4:** What will happen if you attempt to delete a document that does not exist in Cloud Firestore?  
a) An error will be thrown.  
b) The operation will succeed silently without any effect.  
c) The document will be created instead.  
d) The operation will fail and rollback any previous changes.  
**Answer:** b) The operation will succeed silently without any effect.

---

**Question 5:** Consider the following code snippet. What will it do?

```javascript
const batch = firestore.batch();
const docRef1 = firestore.collection('users').doc('user1');
const docRef2 = firestore.collection('users').doc('user2');

batch.delete(docRef1);
batch.delete(docRef2);
await batch.commit();
```

a) It will delete both 'user1' and 'user2' documents.  
b) It will delete only 'user1' document.  
c) It will throw an error if either document does not exist.  
d) It will delete the entire 'users' collection.  
**Answer:** a) It will delete both 'user1' and 'user2' documents.

---

# Realtime Update in Cloud Firestore

## Questions

### Questions on Realtime Update in Cloud Firestore

**Question 1:** What feature of Cloud Firestore allows developers to receive updates in real-time when data changes?  
a) Firestore Sync  
b) Firestore Listeners  
c) Firestore Caching  
d) Firestore Transactions  
**Answer:** b) Firestore Listeners

---

**Question 2:** Which of the following code snippets correctly sets up a listener for real-time updates on a Firestore collection named "users"?  
a) 
```javascript
firebase.firestore().collection("users").onSnapshot(snapshot => {
    snapshot.forEach(doc => {
        console.log(doc.data());
    });
});
```  
b) 
```javascript
firebase.firestore().collection("users").get().then(snapshot => {
    snapshot.forEach(doc => {
        console.log(doc.data());
    });
});
```  
c) 
```javascript
firebase.firestore().collection("users").addListener(snapshot => {
    console.log(snapshot.data());
});
```  
d) 
```javascript
firebase.firestore().collection("users").listen(snapshot => {
    console.log(snapshot.data());
});
```  
**Answer:** a) 
```javascript
firebase.firestore().collection("users").onSnapshot(snapshot => {
    snapshot.forEach(doc => {
        console.log(doc.data());
    });
});
```

---

**Question 3:** What is the primary benefit of using real-time updates in Cloud Firestore?  
a) It reduces the amount of data stored in the database.  
b) It allows applications to reflect changes in data instantly without needing to refresh.  
c) It improves the security of the database.  
d) It simplifies the database schema.  
**Answer:** b) It allows applications to reflect changes in data instantly without needing to refresh.

---

**Question 4:** When using Firestore listeners, what happens if the listener is no longer needed?  
a) It automatically stops listening after a certain time.  
b) It continues to listen and consume resources.  
c) It must be manually unsubscribed to stop listening.  
d) It will throw an error if not removed.  
**Answer:** c) It must be manually unsubscribed to stop listening.

---

**Question 5:** In the context of Firebase Hosting, what is a common challenge developers face when setting up redirects?  
a) Ensuring the hosting plan is sufficient.  
b) Configuring rules correctly to avoid broken links.  
c) Managing user authentication.  
d) Deploying the application to the correct environment.  
**Answer:** b) Configuring rules correctly to avoid broken links.

---

# Document Change Types

## Questions

### Questions on Document Change Types

**Question 1:** In a Cloud Firestore database for a bookstore, which of the following fields would NOT typically be included in a book document?  
a) title  
b) author  
c) publication date  
d) userId  

**Answer:** d) userId

---

**Question 2:** In a social media application, if you want to retrieve all comments made by a specific user across multiple posts, which of the following queries would be most appropriate?  
a) Query the 'comments' sub-collection of each post individually.  
b) Use a single query on the 'posts' collection to find all comments.  
c) Aggregate results from all 'comments' sub-collections after querying each post.  
d) Query the 'users' collection to find comments by userId.  

**Answer:** c) Aggregate results from all 'comments' sub-collections after querying each post.

---

**Question 3:** Given the following code snippet, what does the `get()` method do in this context?

```javascript
const booksRef = db.collection('books');
booksRef.get().then((snapshot) => {
    snapshot.forEach((doc) => {
        console.log(doc.id, '=>', doc.data());
    });
});
```

a) It updates all documents in the 'books' collection.  
b) It retrieves all documents in the 'books' collection.  
c) It deletes all documents in the 'books' collection.  
d) It creates a new document in the 'books' collection.  

**Answer:** b) It retrieves all documents in the 'books' collection.

---

**Question 4:** In the context of Cloud Firestore, what is a sub-collection?  
a) A collection that contains only documents with a specific field.  
b) A collection that is nested within a document.  
c) A collection that can only be accessed by admin users.  
d) A collection that stores metadata about other collections.  

**Answer:** b) A collection that is nested within a document.

---

**Question 5:** If you want to find all books priced under $20 in a Firestore query, which of the following code snippets would be correct?

```javascript
const booksRef = db.collection('books');
const query = booksRef.where('price', '<', 20);
```

a) This code snippet is incorrect; it should use `==` instead of `<`.  
b) This code snippet is correct and will retrieve all books under $20.  
c) This code snippet will only retrieve books priced exactly at $20.  
d) This code snippet will throw an error because of the comparison operator.  

**Answer:** b) This code snippet is correct and will retrieve all books under $20.

---

# Cloud Firestore

## Questions

### Question 1:
What is the primary characteristic of documents in a NoSQL database like Cloud Firestore?

a) All documents must have the same structure  
b) Documents are stored in tables  
c) Each document can have different fields and structures  
d) Documents are limited to text data only  

**Answer:** c) Each document can have different fields and structures

---

### Question 2:
Given the following document structure in a Firestore collection named 'Users':

```json
{ 
  'name': 'Charlie', 
  'age': 28, 
  'email': 'charlie@example.com', 
  'preferences': { 'newsletter': true, 'notifications': false } 
}
```

What type of data structure is used for the 'preferences' field?

a) Array  
b) String  
c) Object  
d) Number  

**Answer:** c) Object

---

### Question 3:
In a Firestore collection named 'Products', which of the following documents is valid?

a) `{ 'productName': 'Smartphone', 'price': 699.99 }`  
b) `{ 'productName': 'Smartphone', 'price': '699.99' }`  
c) `{ 'productName': 'Smartphone', 'price': 699.99, 'specs': [ '5G', '128GB' ] }`  
d) All of the above  

**Answer:** d) All of the above

---

### Question 4:
If you want to query all users who are older than 25 in a Firestore collection named 'Users', which of the following queries is correct?

a) `db.collection('Users').where('age', '>', 25)`  
b) `db.collection('Users').filter('age', '>', 25)`  
c) `db.collection('Users').find('age', '>', 25)`  
d) `db.collection('Users').select('age', '>', 25)`  

**Answer:** a) `db.collection('Users').where('age', '>', 25)`

---

### Question 5:
Consider the following document in a Firestore collection named 'Products':

```json
{ 
  'productName': 'E-Book', 
  'price': 9.99, 
  'fileSizeMB': 5, 
  'format': 'PDF' 
}
```

Which of the following fields is an example of a numeric data type?

a) 'productName'  
b) 'price'  
c) 'format'  
d) 'fileSizeMB'  

**Answer:** b) 'price' and d) 'fileSizeMB' (Note: This question can be tricky as it has two correct answers; you may choose to specify only one correct answer if desired.)

---

# Security Rules

## Questions

### Question 1:
What is the purpose of the `doc()` method in the following code snippet?

```javascript
const userRef = db.collection('users').doc();
```

a) To create a new collection  
b) To generate a new document reference with a unique ID  
c) To retrieve an existing document  
d) To delete a document  

**Answer:** b) To generate a new document reference with a unique ID

---

### Question 2:
In the provided code snippet, what will happen if the `set()` method is called on an existing document reference?

```javascript
userRef.set({
  name: 'John Doe',
  email: 'john.doe@example.com',
  age: 30
});
```

a) It will throw an error  
b) It will overwrite the existing document  
c) It will create a new document with a different ID  
d) It will append the new data to the existing document  

**Answer:** b) It will overwrite the existing document

---

### Question 3:
What does the following code check before creating a new product document?

```javascript
productRef.get().then((doc) => {
  if (doc.exists) {
    console.log('Product ID already exists. Choose a different ID.');
  } else {
    // Create a new product document
  }
});
```

a) If the product ID is valid  
b) If the product ID is unique  
c) If the product document is empty  
d) If the user is authenticated  

**Answer:** b) If the product ID is unique

---

### Question 4:
What will the output be if the product ID 'product123' already exists in the 'products' collection?

```javascript
if (doc.exists) {
  console.log('Product ID already exists. Choose a different ID.');
}
```

a) 'Product document created successfully!'  
b) 'Error creating product document: '  
c) 'Product ID already exists. Choose a different ID.'  
d) No output  

**Answer:** c) 'Product ID already exists. Choose a different ID.'

---

### Question 5:
In the context of Firestore, what does the `catch()` method do in the following code snippet?

```javascript
productRef.set({
  name: 'New Product',
  price: 29.99,
  stock: 100
}).catch((error) => {
  console.error('Error creating product document: ', error);
});
```

a) It handles successful document creation  
b) It logs an error if document creation fails  
c) It prevents the document from being created  
d) It retries the document creation  

**Answer:** b) It logs an error if document creation fails

---

# Firebase Authentication

## Questions

### Questions on Firebase Authentication and Firestore

**Question 1:** What is the primary purpose of Firebase Authentication in a social media application?  
a) To store user posts  
b) To manage user profiles and sign-in processes  
c) To handle real-time updates  
d) To manage inventory levels  
**Answer:** b) To manage user profiles and sign-in processes

---

**Question 2:** In a Firestore database, which of the following data structures is used to store user profiles?  
a) Arrays  
b) Documents  
c) Strings  
d) Functions  
**Answer:** b) Documents

---

**Question 3:** In the context of an e-commerce platform using Firestore, what is a potential issue when multiple users attempt to purchase the same item simultaneously?  
a) Users will not be able to log in  
b) Firestore will automatically refund users  
c) Concurrent writes may lead to overselling  
d) User profiles will be deleted  
**Answer:** c) Concurrent writes may lead to overselling

---

**Question 4:** Given the following code snippet, what does the `onSnapshot` method do in Firestore?  
```javascript
const unsubscribe = firestore.collection('posts').onSnapshot(snapshot => {
    snapshot.docChanges().forEach(change => {
        if (change.type === 'added') {
            console.log('New post: ', change.doc.data());
        }
    });
});
```  
a) It retrieves a single document from the collection  
b) It listens for real-time updates to the collection  
c) It deletes a document from the collection  
d) It updates a document in the collection  
**Answer:** b) It listens for real-time updates to the collection

---

**Question 5:** What is a common method to ensure that Firestore handles concurrent writes correctly in an e-commerce application?  
a) Use a single user account for all transactions  
b) Implement transactions or batched writes  
c) Disable real-time updates  
d) Store all data in local storage  
**Answer:** b) Implement transactions or batched writes

---

**Question 6:** In a social media application, which Firebase feature would you use to allow users to sign in with their Google accounts?  
a) Firestore  
b) Firebase Hosting  
c) Firebase Authentication  
d) Firebase Cloud Functions  
**Answer:** c) Firebase Authentication

---

**Question 7:** When using Firestore to manage user carts in an e-commerce platform, which of the following is a best practice to avoid data inconsistency?  
a) Allow users to edit their carts without restrictions  
b) Use Firestore's security rules to validate cart updates  
c) Store cart data in a separate database  
d) Disable real-time updates for cart data  
**Answer:** b) Use Firestore's security rules to validate cart updates

---

**Question 8:** If you want to ensure that a user's profile is updated in real-time across all devices, which Firestore feature should you utilize?  
a) Firestore Security Rules  
b) Firestore Transactions  
c) Firestore Real-time Listeners  
d) Firestore Batch Writes  
**Answer:** c) Firestore Real-time Listeners

---

# User Registration and Login

## Questions

### Questions on User Registration and Login in a CMS

1. **Question:** In a content management system (CMS), which of the following is NOT typically a part of user registration?  
   a) Username  
   b) Password  
   c) Article Title  
   d) Email Address  
   **Answer:** c) Article Title

2. **Question:** When implementing user permissions in a CMS, which of the following roles is most likely to have the highest level of access?  
   a) Editor  
   b) Author  
   c) Contributor  
   d) Administrator  
   **Answer:** d) Administrator

3. **Question:** In Firestore, which of the following data structures is commonly used to store user permissions?  
   a) Array  
   b) Map  
   c) String  
   d) Number  
   **Answer:** b) Map

4. **Question:** Given the following code snippet, what will be the output if the user is successfully logged in?  
   ```javascript
   function loginUser(username, password) {
       if (username === "admin" && password === "1234") {
           return "Login successful!";
       } else {
           return "Login failed!";
       }
   }
   console.log(loginUser("admin", "1234"));
   ```  
   a) Login failed!  
   b) Login successful!  
   c) Undefined  
   d) Error  
   **Answer:** b) Login successful!

5. **Question:** In a CMS that allows scheduling posts, which of the following is a potential issue when managing scheduled posts?  
   a) Users can edit posts that are scheduled for future publication.  
   b) Posts are published immediately regardless of the schedule.  
   c) Scheduled posts do not appear in the database.  
   d) All of the above.  
   **Answer:** d) All of the above.

6. **Question:** Which Firestore feature would be most useful for real-time collaboration between authors and editors in a CMS?  
   a) Offline support  
   b) Real-time listeners  
   c) Batch writes  
   d) Data validation  
   **Answer:** b) Real-time listeners

7. **Question:** What is the primary purpose of using Firestore in a CMS for user registration and login?  
   a) To store images  
   b) To manage user sessions  
   c) To store user data and permissions  
   d) To create user interfaces  
   **Answer:** c) To store user data and permissions

8. **Question:** If a user tries to delete a scheduled post in a CMS, which of the following checks should be implemented to prevent this action?  
   a) Check if the user is logged in  
   b) Check if the post is scheduled for future publication  
   c) Check if the user is an administrator  
   d) All of the above  
   **Answer:** b) Check if the post is scheduled for future publication

9. **Question:** In a CMS, which of the following is a common method to ensure that user passwords are stored securely?  
   a) Storing passwords in plain text  
   b) Using a hashing algorithm  
   c) Encrypting passwords with a simple cipher  
   d) Storing passwords in a separate database  
   **Answer:** b) Using a hashing algorithm

10. **Question:** What is the main challenge of allowing users to edit posts that are already scheduled for future publication?  
    a) Ensuring the post is saved correctly  
    b) Preventing conflicts with the scheduled time  
    c) Allowing users to see the post  
    d) None of the above  
    **Answer:** b) Preventing conflicts with the scheduled time

---

# Social Media Integration

## Questions

### Question 1:
What is a primary benefit of using Cloud Firestore for a social media application?
a) It requires a complex server setup  
b) It allows for easy retrieval and updates of user data and posts  
c) It does not support real-time updates  
d) It is limited to storing only text data  

**Answer:** b) It allows for easy retrieval and updates of user data and posts

---

### Question 2:
In the context of the tricky example, what potential issue arises from storing the cart as an array within the user document?
a) Increased storage costs  
b) Difficulty in retrieving user profiles  
c) Data loss or inconsistencies due to concurrent updates  
d) Inability to store multiple user accounts  

**Answer:** c) Data loss or inconsistencies due to concurrent updates

---

### Question 3:
Which of the following fields would NOT typically be found in a user document in a social media application using Cloud Firestore?
a) Username  
b) Profile picture URL  
c) Post content  
d) Array of post IDs  

**Answer:** c) Post content

---

### Question 4:
Consider the following code snippet for adding a post in a social media application using Cloud Firestore:

```javascript
const addPost = async (userId, content) => {
    const postRef = firestore.collection('posts').doc();
    await postRef.set({
        content: content,
        timestamp: firebase.firestore.FieldValue.serverTimestamp(),
        userId: userId
    });
};
```
What does the `firebase.firestore.FieldValue.serverTimestamp()` function do in this context?
a) It sets the timestamp to the current local time of the user  
b) It generates a unique ID for the post  
c) It sets the timestamp to the server's current time  
d) It retrieves the timestamp of the last post  

**Answer:** c) It sets the timestamp to the server's current time

---

### Question 5:
When implementing transaction handling for cart updates in a Cloud Firestore application, what is the primary goal?
a) To allow multiple users to edit the cart simultaneously  
b) To ensure that cart updates are atomic and consistent  
c) To reduce the number of reads and writes to the database  
d) To simplify the data structure of the user document  

**Answer:** b) To ensure that cart updates are atomic and consistent

---

# Access Control

## Questions

### Question 1:
What does the following code snippet do in a Cloud Firestore database?

```javascript
const db = firebase.firestore();

db.collection('users').get().then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
        console.log(`${doc.id} => ${JSON.stringify(doc.data())}`);
    });
});
```

a) It retrieves all documents in the 'users' collection and logs their IDs and data.  
b) It deletes all documents in the 'users' collection.  
c) It updates all documents in the 'users' collection.  
d) It retrieves only the first document in the 'users' collection.  

**Answer:** a) It retrieves all documents in the 'users' collection and logs their IDs and data.

---

### Question 2:
In the following code snippet, what is the purpose of the `where` clause?

```javascript
const db = firebase.firestore();

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

a) It retrieves all documents in the 'users' collection regardless of their email.  
b) It filters the documents to only retrieve those where the 'email' field matches the specified email address.  
c) It updates the email field of all documents in the 'users' collection.  
d) It deletes documents from the 'users' collection based on the email address.  

**Answer:** b) It filters the documents to only retrieve those where the 'email' field matches the specified email address.

---

### Question 3:
What will happen if the `emailToFind` variable does not match any documents in the 'users' collection in the following code snippet?

```javascript
const db = firebase.firestore();

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

a) The code will throw an error.  
b) The code will log 'No matching documents.' to the console.  
c) The code will log all documents in the 'users' collection.  
d) The code will update the email field of all documents.  

**Answer:** b) The code will log 'No matching documents.' to the console.

---

### Question 4:
Which of the following statements is true regarding the efficiency of the second code snippet with the `where` clause?

a) It is less efficient because it retrieves all documents and filters them afterward.  
b) It is more efficient because it only retrieves documents that match the specified email address.  
c) It is equally efficient as retrieving all documents.  
d) It is inefficient because it requires a network call for each document.  

**Answer:** b) It is more efficient because it only retrieves documents that match the specified email address.

---

