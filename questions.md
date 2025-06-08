<h1>Cloud Data Management</h1>
<h2>Questions</h2>
<p>Question 1: What is the primary purpose of using Amazon S3 for data backups?<br />
a) To increase data redundancy<br />
b) To ensure data is securely stored and easily accessible<br />
c) To improve data processing speed<br />
d) To eliminate the need for local storage<br />
<strong>Answer:</strong> b) To ensure data is securely stored and easily accessible  </p>
<p>Question 2: Which of the following is a benefit of implementing lifecycle policies in Amazon S3?<br />
a) It increases the speed of data retrieval<br />
b) It automatically deletes all data older than a specified date<br />
c) It transitions older backups to cheaper storage classes<br />
d) It prevents data from being accessed<br />
<strong>Answer:</strong> c) It transitions older backups to cheaper storage classes  </p>
<p>Question 3: In the context of cloud data management, what does the term "data availability" refer to?<br />
a) The speed at which data can be processed<br />
b) The ability to access data whenever needed<br />
c) The amount of data that can be stored<br />
d) The security measures in place to protect data<br />
<strong>Answer:</strong> b) The ability to access data whenever needed  </p>
<p>Question 4: Consider the following code snippet for uploading a file to Amazon S3. What does the <code>putObject</code> method do?<br />
```python
import boto3</p>
<p>s3 = boto3.client('s3')
s3.put_object(Bucket='my-bucket', Key='my-file.txt', Body='Hello, World!')
```
a) It retrieves a file from the S3 bucket<br />
b) It deletes a file from the S3 bucket<br />
c) It uploads a file to the specified S3 bucket<br />
d) It lists all files in the S3 bucket<br />
<strong>Answer:</strong> c) It uploads a file to the specified S3 bucket  </p>
<p>Question 5: What is a potential drawback of not implementing lifecycle policies for data stored in Amazon S3?<br />
a) Increased data retrieval times<br />
b) Higher storage costs due to retaining data in expensive storage classes<br />
c) Loss of data integrity<br />
d) Inability to access data from multiple locations<br />
<strong>Answer:</strong> b) Higher storage costs due to retaining data in expensive storage classes  </p>
<hr />
<h1>Mobile Application Development</h1>
<h2>Questions</h2>
<h3>Multiple Choice Questions on Mobile Application Development</h3>
<p><strong>Question 1:</strong> What is a common risk associated with improperly configured cloud database access controls?<br />
a) Increased application performance<br />
b) Exposure of sensitive customer data<br />
c) Enhanced user experience<br />
d) Reduced server costs<br />
<strong>Answer:</strong> b) Exposure of sensitive customer data</p>
<hr />
<p><strong>Question 2:</strong> Which of the following is a best practice for managing access to cloud databases?<br />
a) Allowing all users full access<br />
b) Regularly reviewing and updating access permissions<br />
c) Using the same password for all database users<br />
d) Ignoring access logs<br />
<strong>Answer:</strong> b) Regularly reviewing and updating access permissions</p>
<hr />
<p><strong>Question 3:</strong> In a mobile application, which of the following methods can be used to secure sensitive data before sending it to a cloud database?<br />
a) Sending data in plain text<br />
b) Encrypting the data before transmission<br />
c) Using a public Wi-Fi network<br />
d) Storing data in local storage without encryption<br />
<strong>Answer:</strong> b) Encrypting the data before transmission</p>
<hr />
<p><strong>Question 4:</strong> Consider the following code snippet for accessing a cloud database. What is the potential security issue in this code?</p>
<p>```python
import cloud_database</p>
<p>db = cloud_database.connect(user='admin', password='password123')
```</p>
<p>a) The database connection is not encrypted<br />
b) The username and password are hardcoded<br />
c) The database is not specified<br />
d) There is no error handling<br />
<strong>Answer:</strong> b) The username and password are hardcoded</p>
<hr />
<p><strong>Question 5:</strong> What is the primary purpose of implementing access controls in a cloud database?<br />
a) To improve application speed<br />
b) To ensure only authorized users can access sensitive data<br />
c) To reduce the cost of cloud services<br />
d) To simplify database queries<br />
<strong>Answer:</strong> b) To ensure only authorized users can access sensitive data</p>
<hr />
<p><strong>Question 6:</strong> Which of the following tools can help monitor access to a cloud database for security purposes?<br />
a) Cloud storage<br />
b) Access logs and monitoring tools<br />
c) Basic text editors<br />
d) Image editing software<br />
<strong>Answer:</strong> b) Access logs and monitoring tools</p>
<hr />
<p><strong>Question 7:</strong> What is a potential consequence of failing to manage access controls effectively in a mobile application?<br />
a) Increased user engagement<br />
b) Data breaches and loss of customer trust<br />
c) Improved application scalability<br />
d) Enhanced data analytics<br />
<strong>Answer:</strong> b) Data breaches and loss of customer trust</p>
<hr />
<p>These questions are designed to test understanding of key concepts related to mobile application development, particularly focusing on security and access management in cloud databases.</p>
<hr />
<h1>Lecture 6</h1>
<h2>Questions</h2>
<p>Based on the provided concept and examples, here are some multiple choice questions:</p>
<h3>Question 1:</h3>
<p>What programming language is primarily used for developing iOS applications in the fitness tracking app example?
a) Java<br />
b) Swift<br />
c) Kotlin<br />
d) C#<br />
<strong>Answer:</strong> b) Swift</p>
<h3>Question 2:</h3>
<p>Which programming language is used for Android development in the fitness tracking app?
a) Swift<br />
b) Kotlin<br />
c) Objective-C<br />
d) Python<br />
<strong>Answer:</strong> b) Kotlin</p>
<h3>Question 3:</h3>
<p>What is the primary purpose of the fitness tracking app described in the typical example?
a) To play music<br />
b) To log workouts and track progress<br />
c) To send messages<br />
d) To browse the internet<br />
<strong>Answer:</strong> b) To log workouts and track progress</p>
<h3>Question 4:</h3>
<p>If a developer wants to create a cross-platform app that works on both iOS and Android, which of the following approaches could they take?
a) Use only Swift<br />
b) Use only Kotlin<br />
c) Use a framework like React Native<br />
d) Use HTML and CSS only<br />
<strong>Answer:</strong> c) Use a framework like React Native</p>
<h3>Question 5:</h3>
<p>In the context of mobile app development, what does "native development tools" refer to?
a) Tools that are used for web development<br />
b) Tools specifically designed for a particular platform (iOS or Android)<br />
c) Tools that can be used for any operating system<br />
d) Tools that require internet access to function<br />
<strong>Answer:</strong> b) Tools specifically designed for a particular platform (iOS or Android)</p>
<hr />
<h1>Edward Szeto</h1>
<h2>Questions</h2>
<p>Based on the provided concept and example, here are some multiple-choice questions that test understanding of the challenges faced when integrating with third-party APIs:</p>
<h3>Question 1:</h3>
<p>What is a common challenge when integrating with multiple third-party APIs?
a) Consistent API responses<br />
b) Uniform data formats<br />
c) Inconsistent API responses<br />
d) Simplified user experience  </p>
<p><strong>Answer:</strong> c) Inconsistent API responses</p>
<h3>Question 2:</h3>
<p>When dealing with varying data formats from different APIs, what is a recommended approach to ensure smooth integration?
a) Ignore the data formats<br />
b) Use a middleware to standardize data<br />
c) Only use APIs from the same provider<br />
d) Manually convert data each time  </p>
<p><strong>Answer:</strong> b) Use a middleware to standardize data</p>
<h3>Question 3:</h3>
<p>Given the following code snippet, what is the purpose of the <code>fetchWeatherData</code> function?</p>
<p><code>javascript
async function fetchWeatherData(apiUrl) {
    const response = await fetch(apiUrl);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}</code>
a) To fetch data from a local database<br />
b) To handle errors in API responses<br />
c) To retrieve weather data from a specified API URL<br />
d) To convert weather data into a different format  </p>
<p><strong>Answer:</strong> c) To retrieve weather data from a specified API URL</p>
<h3>Question 4:</h3>
<p>What could be a potential consequence of inconsistent API responses when developing a mobile app?
a) Improved performance<br />
b) Enhanced user experience<br />
c) Increased development time and complexity<br />
d) Simplified code structure  </p>
<p><strong>Answer:</strong> c) Increased development time and complexity</p>
<h3>Question 5:</h3>
<p>Which of the following strategies can help mitigate issues with varying data formats from third-party APIs?
a) Using a single API for all functionalities<br />
b) Implementing data validation and transformation layers<br />
c) Avoiding API integration altogether<br />
d) Relying solely on user input for data  </p>
<p><strong>Answer:</strong> b) Implementing data validation and transformation layers</p>
<hr />
<h1>Firebase Introduction</h1>
<h2>Questions</h2>
<p>Question 1: What is a key advantage of using cloud databases over traditional databases?<br />
a) Higher cost<br />
b) Limited scalability<br />
c) Global accessibility<br />
d) Manual data backup<br />
<strong>Answer:</strong> c) Global accessibility  </p>
<p>Question 2: In the context of Firebase, which of the following is NOT a feature of its real-time database?<br />
a) Offline support<br />
b) Real-time synchronization<br />
c) SQL query support<br />
d) Data storage in JSON format<br />
<strong>Answer:</strong> c) SQL query support  </p>
<p>Question 3: Which of the following services is part of Amazon Web Services (AWS) for managing databases?<br />
a) Google Cloud Storage<br />
b) Amazon RDS<br />
c) Microsoft Azure SQL<br />
d) Firebase Firestore<br />
<strong>Answer:</strong> b) Amazon RDS  </p>
<p>Question 4: In Firebase, which of the following code snippets correctly initializes the Firebase app?<br />
<code>javascript
const firebase = require('firebase/app');
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT_ID.firebaseio.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};</code>
a) firebase.initializeApp(firebaseConfig);<br />
b) firebase.startApp(firebaseConfig);<br />
c) firebase.createApp(firebaseConfig);<br />
d) firebase.setupApp(firebaseConfig);<br />
<strong>Answer:</strong> a) firebase.initializeApp(firebaseConfig);  </p>
<p>Question 5: What is the primary purpose of using cloud data management systems like AWS?<br />
a) To store data locally<br />
b) To ensure data availability and durability<br />
c) To eliminate the need for data security<br />
d) To reduce internet usage<br />
<strong>Answer:</strong> b) To ensure data availability and durability  </p>
<hr />
<h1>Realtime Database</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What does the "A" in the CAP theorem stand for?<br />
a) Accessibility<br />
b) Availability<br />
c) Accuracy<br />
d) Affordability<br />
<strong>Answer:</strong> b) Availability</p>
<h3>Question 2:</h3>
<p>In a scenario where a user updates their profile information in a real-time database, which of the following outcomes could occur if the update fails to propagate to another region?<br />
a) The user sees their updated profile in all regions immediately.<br />
b) The user sees outdated information in some regions while others show the updated profile.<br />
c) The update is rolled back in all regions.<br />
d) The update is ignored entirely.<br />
<strong>Answer:</strong> b) The user sees outdated information in some regions while others show the updated profile.</p>
<h3>Question 3:</h3>
<p>Which of the following statements best describes a trade-off in the CAP theorem?<br />
a) You can achieve consistency and partition tolerance but not availability.<br />
b) You can achieve availability and partition tolerance but not consistency.<br />
c) You can achieve consistency and availability but not partition tolerance.<br />
d) All of the above are possible simultaneously.<br />
<strong>Answer:</strong> d) All of the above are possible simultaneously.</p>
<h3>Question 4:</h3>
<p>Consider the following code snippet that updates a user's profile in a real-time database. What will happen if the network connection is lost during the update process?</p>
<p><code>javascript
database.ref('users/' + userId).update({
    name: 'John Doe',
    email: 'john.doe@example.com'
});</code>
a) The update will be completed successfully in all regions.<br />
b) The update will fail silently, and the user will not be notified.<br />
c) The update will be queued and executed once the connection is restored.<br />
d) The update will cause an error and stop the application.<br />
<strong>Answer:</strong> b) The update will fail silently, and the user will not be notified.</p>
<h3>Question 5:</h3>
<p>If a cloud service prioritizes availability over consistency, which of the following scenarios is most likely to occur?<br />
a) Users will always see the most recent data.<br />
b) Users may see stale or outdated data temporarily.<br />
c) Data will be lost if a failure occurs.<br />
d) All regions will be updated simultaneously.<br />
<strong>Answer:</strong> b) Users may see stale or outdated data temporarily.</p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<p>Based on the concept of Cloud Firestore, here are some multiple choice questions:</p>
<hr />
<p><strong>Question 1:</strong> What is Cloud Firestore primarily used for?<br />
a) Image processing<br />
b) Real-time database storage<br />
c) Video streaming<br />
d) Machine learning model training<br />
<strong>Answer:</strong> b) Real-time database storage</p>
<hr />
<p><strong>Question 2:</strong> Which of the following is a feature of Cloud Firestore?<br />
a) It only supports SQL queries.<br />
b) It provides offline data access.<br />
c) It requires a dedicated server.<br />
d) It does not support real-time updates.<br />
<strong>Answer:</strong> b) It provides offline data access.</p>
<hr />
<p><strong>Question 3:</strong> In Cloud Firestore, what is a "document"?<br />
a) A collection of images<br />
b) A single record in a database<br />
c) A type of query<br />
d) A user authentication method<br />
<strong>Answer:</strong> b) A single record in a database</p>
<hr />
<p><strong>Question 4:</strong> Given the following code snippet, what does it do?</p>
<p><code>javascript
const db = firebase.firestore();
db.collection("users").add({
    name: "John Doe",
    age: 30
});</code></p>
<p>a) It updates an existing user document.<br />
b) It deletes a user document.<br />
c) It adds a new user document to the "users" collection.<br />
d) It retrieves user documents from the "users" collection.<br />
<strong>Answer:</strong> c) It adds a new user document to the "users" collection.</p>
<hr />
<p><strong>Question 5:</strong> Which of the following is NOT a valid way to query data in Cloud Firestore?<br />
a) Using the <code>where</code> clause<br />
b) Using the <code>orderBy</code> clause<br />
c) Using the <code>join</code> clause<br />
d) Using the <code>limit</code> clause<br />
<strong>Answer:</strong> c) Using the <code>join</code> clause</p>
<hr />
<p><strong>Question 6:</strong> What is the maximum size of a document in Cloud Firestore?<br />
a) 1 MB<br />
b) 2 MB<br />
c) 10 MB<br />
d) 5 MB<br />
<strong>Answer:</strong> a) 1 MB</p>
<hr />
<p><strong>Question 7:</strong> Which of the following statements about Cloud Firestore security rules is true?<br />
a) Security rules can only be applied to collections.<br />
b) Security rules are written in JavaScript.<br />
c) Security rules can restrict access based on user authentication.<br />
d) Security rules are not necessary for data protection.<br />
<strong>Answer:</strong> c) Security rules can restrict access based on user authentication.</p>
<hr />
<p>Feel free to ask for more questions or any specific topics related to Cloud Firestore!</p>
<hr />
<h1>Firebase Authentication</h1>
<h2>Questions</h2>
<p>Based on the concept of Firebase Authentication, here are some multiple choice questions:</p>
<hr />
<p><strong>Question 1:</strong> What is Firebase Authentication primarily used for?<br />
a) Storing data in the cloud<br />
b) Managing user authentication and identity<br />
c) Hosting web applications<br />
d) Sending push notifications<br />
<strong>Answer:</strong> b) Managing user authentication and identity</p>
<hr />
<p><strong>Question 2:</strong> Which of the following methods can be used to sign in a user with Firebase Authentication?<br />
a) Email and password<br />
b) Phone number<br />
c) Google Sign-In<br />
d) All of the above<br />
<strong>Answer:</strong> d) All of the above</p>
<hr />
<p><strong>Question 3:</strong> In Firebase Authentication, which of the following code snippets correctly initializes Firebase?<br />
```javascript
import firebase from 'firebase/app';
import 'firebase/auth';</p>
<p>const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
};</p>
<p>firebase.initializeApp(firebaseConfig);
```
a) The code is incorrect because it does not import Firebase correctly.<br />
b) The code is correct and initializes Firebase with the provided configuration.<br />
c) The code is missing the Firebase database import.<br />
d) The code will throw an error due to missing API keys.<br />
<strong>Answer:</strong> b) The code is correct and initializes Firebase with the provided configuration.</p>
<hr />
<p><strong>Question 4:</strong> What is the purpose of the <code>signInWithEmailAndPassword</code> method in Firebase Authentication?<br />
a) To create a new user account<br />
b) To sign in an existing user with email and password<br />
c) To send a password reset email<br />
d) To log out the current user<br />
<strong>Answer:</strong> b) To sign in an existing user with email and password</p>
<hr />
<p><strong>Question 5:</strong> Which of the following Firebase Authentication features allows users to reset their passwords?<br />
a) signInWithEmailAndPassword<br />
b) sendPasswordResetEmail<br />
c) createUserWithEmailAndPassword<br />
d) signOut<br />
<strong>Answer:</strong> b) sendPasswordResetEmail</p>
<hr />
<p>These questions cover various aspects of Firebase Authentication, including its purpose, methods, and code usage.</p>
<hr />
<h1>Firebase Cloud Storage</h1>
<h2>Questions</h2>
<p>Question 1: What is the primary purpose of Firebase Cloud Storage?<br />
a) To store user authentication data<br />
b) To store and serve user-generated content such as images and videos<br />
c) To manage real-time database transactions<br />
d) To host web applications<br />
<strong>Answer:</strong> b) To store and serve user-generated content such as images and videos  </p>
<p>Question 2: Which of the following Firebase services is typically used in conjunction with Firebase Cloud Storage for user authentication?<br />
a) Firebase Realtime Database<br />
b) Firebase Hosting<br />
c) Firebase Authentication<br />
d) Firebase Functions<br />
<strong>Answer:</strong> c) Firebase Authentication  </p>
<p>Question 3: Given the following code snippet, what is the purpose of the <code>uploadBytes</code> function?<br />
```javascript
const storageRef = firebase.storage().ref();
const fileRef = storageRef.child('images/myImage.png');
const file = document.getElementById('fileInput').files[0];</p>
<p>uploadBytes(fileRef, file).then((snapshot) =&gt; {
  console.log('Uploaded a blob or file!');
});
```
a) To download a file from Firebase Cloud Storage<br />
b) To upload a file to Firebase Cloud Storage<br />
c) To delete a file from Firebase Cloud Storage<br />
d) To list files in a Firebase Cloud Storage bucket<br />
<strong>Answer:</strong> b) To upload a file to Firebase Cloud Storage  </p>
<p>Question 4: What is the maximum file size limit for a single file upload to Firebase Cloud Storage?<br />
a) 1 MB<br />
b) 5 MB<br />
c) 10 MB<br />
d) 5 TB<br />
<strong>Answer:</strong> d) 5 TB  </p>
<p>Question 5: Which of the following is NOT a feature of Firebase Cloud Storage?<br />
a) Automatic scaling<br />
b) Real-time database synchronization<br />
c) Secure file uploads and downloads<br />
d) File versioning<br />
<strong>Answer:</strong> b) Real-time database synchronization  </p>
<hr />
<h1>Firebase</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Firebase Realtime Database?
a) To store large binary files<br />
b) To manage structured data in real-time<br />
c) To host static websites<br />
d) To perform complex SQL queries  </p>
<p><strong>Answer:</strong> b) To manage structured data in real-time</p>
<hr />
<h3>Question 2:</h3>
<p>Which of the following is a potential issue when using Firebase Realtime Database for large binary file storage?
a) It automatically compresses files<br />
b) It is optimized for structured data<br />
c) It provides unlimited storage<br />
d) It supports SQL queries  </p>
<p><strong>Answer:</strong> b) It is optimized for structured data</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following code snippet, what will happen if the developer tries to store a large binary file in the Firebase Realtime Database?</p>
<p><code>javascript
const database = firebase.database();
const largeFile = new Blob([/* large binary data */]);
database.ref('files/largeFile').set(largeFile);</code></p>
<p>a) The file will be stored successfully without any issues<br />
b) The file will be stored, but performance will degrade<br />
c) An error will occur due to file size limitations<br />
d) The file will be automatically converted to a string  </p>
<p><strong>Answer:</strong> b) The file will be stored, but performance will degrade</p>
<hr />
<h3>Question 4:</h3>
<p>Which Firebase service is recommended for storing large binary files instead of Firebase Realtime Database?
a) Firebase Hosting<br />
b) Firebase Cloud Functions<br />
c) Firebase Cloud Storage<br />
d) Firebase Authentication  </p>
<p><strong>Answer:</strong> c) Firebase Cloud Storage</p>
<hr />
<h3>Question 5:</h3>
<p>What is a key feature of Firebase Realtime Database?
a) It allows for SQL-like queries<br />
b) It provides real-time synchronization of data<br />
c) It is designed for file storage<br />
d) It requires a server to run  </p>
<p><strong>Answer:</strong> b) It provides real-time synchronization of data</p>
<hr />
<h1>Firebase</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What feature of Firebase allows for real-time data synchronization across clients in a chat application?
a) Firestore<br />
b) Realtime Database<br />
c) Cloud Functions<br />
d) Firebase Hosting<br />
<strong>Answer:</strong> b) Realtime Database</p>
<h3>Question 2:</h3>
<p>In a Firebase Realtime Database, which of the following data structures is commonly used to store chat messages?
a) Array<br />
b) Object<br />
c) String<br />
d) Number<br />
<strong>Answer:</strong> b) Object</p>
<h3>Question 3:</h3>
<p>Given the following code snippet, what will be the output when a new message is added to the <code>messages</code> node in the Firebase Realtime Database?</p>
<p><code>javascript
const dbRef = firebase.database().ref('messages');
dbRef.on('child_added', (data) =&gt; {
    console.log(data.val());
});</code>
a) It will log the entire <code>messages</code> node.<br />
b) It will log the first message only.<br />
c) It will log each new message as it is added.<br />
d) It will log an error.<br />
<strong>Answer:</strong> c) It will log each new message as it is added.</p>
<h3>Question 4:</h3>
<p>Which Firebase service would you use to implement user authentication in a chat application?
a) Firebase Storage<br />
b) Firebase Hosting<br />
c) Firebase Authentication<br />
d) Firebase Cloud Messaging<br />
<strong>Answer:</strong> c) Firebase Authentication</p>
<h3>Question 5:</h3>
<p>If you want to ensure that only authenticated users can send messages in your chat application, which Firebase feature should you implement?
a) Firestore Security Rules<br />
b) Realtime Database Rules<br />
c) Firebase Functions<br />
d) Firebase Analytics<br />
<strong>Answer:</strong> b) Realtime Database Rules</p>
<h3>Question 6:</h3>
<p>What is the primary benefit of using Firebase for a chat application compared to traditional server-client architectures?
a) It requires less coding.<br />
b) It provides built-in user authentication.<br />
c) It allows for real-time data updates without manual refresh.<br />
d) It is free to use.<br />
<strong>Answer:</strong> c) It allows for real-time data updates without manual refresh.</p>
<hr />
<h1>Firebase</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Firebase Realtime Database?
a) To store static files<br />
b) To provide real-time data synchronization<br />
c) To host websites<br />
d) To manage user authentication  </p>
<p><strong>Answer:</strong> b) To provide real-time data synchronization</p>
<h3>Question 2:</h3>
<p>In a collaborative document editor using Firebase, what happens when two users make conflicting changes to the same document?
a) The first user's changes are saved, and the second user's changes are discarded<br />
b) Both users' changes are saved, and the document is updated in real-time<br />
c) The document is locked until one user finishes editing<br />
d) An error message is displayed, and no changes are saved  </p>
<p><strong>Answer:</strong> b) Both users' changes are saved, and the document is updated in real-time</p>
<h3>Question 3:</h3>
<p>Which Firebase feature would you use to ensure that all users see the most up-to-date version of a document?
a) Firebase Hosting<br />
b) Firebase Cloud Functions<br />
c) Firebase Realtime Database<br />
d) Firebase Authentication  </p>
<p><strong>Answer:</strong> c) Firebase Realtime Database</p>
<h3>Question 4:</h3>
<p>Consider the following code snippet that updates a document in Firebase Realtime Database:</p>
<p><code>javascript
firebase.database().ref('documents/doc1').update({
  content: 'New content added by user.'
});</code>
What does this code do?
a) It deletes the document with ID 'doc1'<br />
b) It retrieves the document with ID 'doc1'<br />
c) It updates the 'content' field of the document with ID 'doc1'<br />
d) It creates a new document with ID 'doc1'  </p>
<p><strong>Answer:</strong> c) It updates the 'content' field of the document with ID 'doc1'</p>
<h3>Question 5:</h3>
<p>When using Firebase Realtime Database, which of the following is a key benefit of its data structure?
a) Data is stored in a flat file<br />
b) Data is stored in a relational database format<br />
c) Data is stored as a JSON tree, allowing for easy access and updates<br />
d) Data is stored in a binary format  </p>
<p><strong>Answer:</strong> c) Data is stored as a JSON tree, allowing for easy access and updates</p>
<hr />
<h1>Firebase Services</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What Firebase service is primarily used for real-time data synchronization in mobile applications?</p>
<p>a) Firebase Authentication<br />
b) Cloud Firestore<br />
c) Firebase Hosting<br />
d) Firebase Cloud Messaging  </p>
<p><strong>Answer:</strong> b) Cloud Firestore</p>
<hr />
<h3>Question 2:</h3>
<p>In a social media app using Cloud Firestore, which of the following operations allows a user to update their profile information?</p>
<p>a) Create<br />
b) Read<br />
c) Update<br />
d) Delete  </p>
<p><strong>Answer:</strong> c) Update</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following code snippet, what does the <code>set()</code> method do in the context of Cloud Firestore?</p>
<p><code>javascript
const db = firebase.firestore();
db.collection("users").doc("user1").set({
    name: "John Doe",
    age: 30
});</code></p>
<p>a) It retrieves the user data from the database.<br />
b) It deletes the user data from the database.<br />
c) It creates or updates the user data in the database.<br />
d) It listens for changes in the user data.  </p>
<p><strong>Answer:</strong> c) It creates or updates the user data in the database.</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following is NOT a feature of Cloud Firestore?</p>
<p>a) Real-time updates<br />
b) Offline support<br />
c) Built-in user authentication<br />
d) Querying capabilities  </p>
<p><strong>Answer:</strong> c) Built-in user authentication</p>
<hr />
<h3>Question 5:</h3>
<p>If a user posts an update in a social media app using Cloud Firestore, which Firebase feature ensures that all users see the update in real-time?</p>
<p>a) Firebase Storage<br />
b) Cloud Functions<br />
c) Cloud Firestore<br />
d) Firebase Hosting  </p>
<p><strong>Answer:</strong> c) Cloud Firestore</p>
<hr />
<h3>Question 6:</h3>
<p>What is the primary benefit of using Cloud Firestore for a mobile application?</p>
<p>a) It provides a static website hosting service.<br />
b) It allows for real-time data synchronization across multiple clients.<br />
c) It offers server-side processing capabilities.<br />
d) It is primarily used for sending push notifications.  </p>
<p><strong>Answer:</strong> b) It allows for real-time data synchronization across multiple clients.</p>
<hr />
<h1>Realtime Database</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>In a real-time database, what is the primary benefit of using Cloud Firestore for managing inventory in an e-commerce application?<br />
a) It allows for offline data access<br />
b) It provides automatic scaling<br />
c) It ensures real-time updates for multiple users<br />
d) It requires no authentication  </p>
<p><strong>Answer:</strong> c) It ensures real-time updates for multiple users</p>
<hr />
<h3>Question 2:</h3>
<p>Consider the following code snippet for updating stock levels in a Cloud Firestore database:</p>
<p>```javascript
const db = firebase.firestore();
const productRef = db.collection('products').doc('productId');</p>
<p>productRef.update({
    stock: firebase.firestore.FieldValue.increment(-1)
});
```</p>
<p>What does the <code>FieldValue.increment(-1)</code> method do in this context?<br />
a) It sets the stock level to -1<br />
b) It decreases the stock level by 1<br />
c) It increases the stock level by 1<br />
d) It resets the stock level to 0  </p>
<p><strong>Answer:</strong> b) It decreases the stock level by 1</p>
<hr />
<h3>Question 3:</h3>
<p>When multiple users are trying to purchase the same item in an e-commerce application using a real-time database, what is a potential issue that could arise?<br />
a) Users may see outdated stock levels<br />
b) Users will always receive the correct stock level<br />
c) The database will automatically handle all conflicts<br />
d) Users will be unable to purchase items  </p>
<p><strong>Answer:</strong> a) Users may see outdated stock levels</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following strategies can help prevent overselling in a real-time database when multiple users are purchasing the same item?<br />
a) Allow only one user to purchase at a time<br />
b) Use transactions to update stock levels atomically<br />
c) Disable real-time updates<br />
d) Increase the stock level after each purchase  </p>
<p><strong>Answer:</strong> b) Use transactions to update stock levels atomically</p>
<hr />
<h3>Question 5:</h3>
<p>In the context of a real-time database, what is the purpose of using transactions when updating stock levels?<br />
a) To ensure that updates are applied in a non-blocking manner<br />
b) To allow multiple updates to occur simultaneously<br />
c) To guarantee that the stock level is updated correctly even if multiple users are making changes at the same time<br />
d) To improve the performance of read operations  </p>
<p><strong>Answer:</strong> c) To guarantee that the stock level is updated correctly even if multiple users are making changes at the same time</p>
<hr />
<h1>Realtime Database</h1>
<h2>Questions</h2>
<h3>Questions on Realtime Database and Firebase Authentication</h3>
<p><strong>Question 1:</strong> What is the primary purpose of Firebase Authentication in a mobile application?<br />
a) To store user data<br />
b) To handle user sign-in and authentication<br />
c) To manage database transactions<br />
d) To create user interfaces<br />
<strong>Answer:</strong> b) To handle user sign-in and authentication</p>
<hr />
<p><strong>Question 2:</strong> In the context of Firebase Authentication, what does redirecting the user to a Google sign-in page accomplish?<br />
a) It allows the user to create a new Firebase project<br />
b) It enables the user to authenticate using their Google account<br />
c) It retrieves user data from the Firebase Realtime Database<br />
d) It updates the user's profile information<br />
<strong>Answer:</strong> b) It enables the user to authenticate using their Google account</p>
<hr />
<p><strong>Question 3:</strong> Consider the following code snippet for Firebase Authentication:</p>
<p><code>javascript
firebase.auth().signInWithEmailAndPassword(email, password)
  .then((userCredential) =&gt; {
    // Signed in 
    var user = userCredential.user;
  })
  .catch((error) =&gt; {
    var errorCode = error.code;
    var errorMessage = error.message;
  });</code></p>
<p>What does the <code>signInWithEmailAndPassword</code> method do?<br />
a) It creates a new user account<br />
b) It signs in an existing user with their email and password<br />
c) It retrieves user data from the database<br />
d) It logs out the current user<br />
<strong>Answer:</strong> b) It signs in an existing user with their email and password</p>
<hr />
<p><strong>Question 4:</strong> What is a potential security risk when exposing the Firebase API key in client-side code?<br />
a) It can lead to unauthorized access to the Firebase project<br />
b) It can slow down the application<br />
c) It can cause data loss in the database<br />
d) It can prevent users from signing in<br />
<strong>Answer:</strong> a) It can lead to unauthorized access to the Firebase project</p>
<hr />
<p><strong>Question 5:</strong> Which of the following is a best practice for securing Firebase Authentication in a web application?<br />
a) Use the Firebase API key in the client-side code without restrictions<br />
b) Implement server-side validation of user credentials<br />
c) Allow any user to access the Firebase project<br />
d) Disable authentication methods<br />
<strong>Answer:</strong> b) Implement server-side validation of user credentials</p>
<hr />
<p><strong>Question 6:</strong> In a mobile application using Firebase Authentication, what happens after a user successfully signs in with their Google account?<br />
a) The user is logged out automatically<br />
b) The app retrieves user data from the Firebase Realtime Database<br />
c) The user is redirected to the app with an authenticated session<br />
d) The app crashes<br />
<strong>Answer:</strong> c) The user is redirected to the app with an authenticated session</p>
<hr />
<p>These questions assess the understanding of Firebase Authentication and its implications in application security and functionality.</p>
<hr />
<h1>Features</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Firebase Cloud Storage in a mobile application?
a) To store user preferences<br />
b) To store images and videos<br />
c) To manage user authentication<br />
d) To send push notifications<br />
<strong>Answer:</strong> b) To store images and videos</p>
<h3>Question 2:</h3>
<p>In the context of uploading a profile picture to Firebase Cloud Storage, which of the following is a typical step in the process?
a) Compress the image before uploading<br />
b) Convert the image to a text file<br />
c) Encrypt the image using a password<br />
d) Delete the image from the device after uploading<br />
<strong>Answer:</strong> a) Compress the image before uploading</p>
<h3>Question 3:</h3>
<p>Given the following code snippet, what will happen if the image upload fails due to a network error?</p>
<p><code>javascript
firebase.storage().ref('profile_pictures/user123.jpg').put(file)
  .then(() =&gt; {
    console.log('Upload successful');
  })
  .catch((error) =&gt; {
    console.error('Upload failed:', error);
  });</code></p>
<p>a) The console will log 'Upload successful'<br />
b) The console will log 'Upload failed:' followed by the error message<br />
c) The image will be uploaded successfully regardless of the error<br />
d) The application will crash<br />
<strong>Answer:</strong> b) The console will log 'Upload failed:' followed by the error message</p>
<h3>Question 4:</h3>
<p>What could be a potential issue when a social media app attempts to upload videos longer than the maximum allowed size for Firebase Cloud Storage?
a) The video will be uploaded successfully<br />
b) The app will automatically resize the video<br />
c) The upload will fail, and the video may become corrupted<br />
d) The video will be stored in a different format<br />
<strong>Answer:</strong> c) The upload will fail, and the video may become corrupted</p>
<h3>Question 5:</h3>
<p>Which of the following best describes a "chunked upload" in the context of Firebase Cloud Storage?
a) Uploading multiple files simultaneously<br />
b) Dividing a large file into smaller parts for upload<br />
c) Uploading files in a compressed format<br />
d) Uploading files directly from a URL<br />
<strong>Answer:</strong> b) Dividing a large file into smaller parts for upload</p>
<hr />
<h1>Use cases</h1>
<h2>Questions</h2>
<p>Question 1: What is a primary use case for Firebase Authentication in mobile applications?<br />
a) To store user data<br />
b) To allow users to sign up and log in using social media accounts<br />
c) To manage app performance<br />
d) To create user interfaces<br />
<strong>Answer:</strong> b) To allow users to sign up and log in using social media accounts  </p>
<p>Question 2: Which of the following is NOT a benefit of using Firebase Authentication?<br />
a) Simplified user experience<br />
b) Enhanced security<br />
c) Automatic data backup<br />
d) Support for multiple authentication providers<br />
<strong>Answer:</strong> c) Automatic data backup  </p>
<p>Question 3: In the context of Firebase Authentication, which of the following code snippets correctly initializes Firebase?<br />
```javascript
import firebase from 'firebase/app';
import 'firebase/auth';</p>
<p>const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
};</p>
<p>firebase.initializeApp(firebaseConfig);
```<br />
a) The code initializes Firebase with the provided configuration.<br />
b) The code is missing the Firebase database initialization.<br />
c) The code will throw an error due to missing imports.<br />
d) The code initializes Firebase without any configuration.<br />
<strong>Answer:</strong> a) The code initializes Firebase with the provided configuration.  </p>
<p>Question 4: Which of the following authentication methods is supported by Firebase Authentication?<br />
a) Email and password<br />
b) Phone number<br />
c) Google sign-in<br />
d) All of the above<br />
<strong>Answer:</strong> d) All of the above  </p>
<p>Question 5: What is the primary purpose of Firebase Authentication in a mobile app?<br />
a) To manage app analytics<br />
b) To authenticate users and manage their sessions<br />
c) To store user-generated content<br />
d) To enhance app performance<br />
<strong>Answer:</strong> b) To authenticate users and manage their sessions  </p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Firebase Cloud Functions in relation to Cloud Firestore?</p>
<p>a) To store large files<br />
b) To handle background tasks and respond to Firestore events<br />
c) To manage user authentication<br />
d) To create user interfaces  </p>
<p><strong>Answer:</strong> b) To handle background tasks and respond to Firestore events</p>
<hr />
<h3>Question 2:</h3>
<p>In the context of Firestore, what could be a consequence of triggering a Cloud Function on every document change in a collection?</p>
<p>a) Improved performance<br />
b) Increased billing due to excessive invocations<br />
c) Enhanced security<br />
d) Automatic data backup  </p>
<p><strong>Answer:</strong> b) Increased billing due to excessive invocations</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following code snippet, what will happen when a document in the "users" collection is created or updated?</p>
<p><code>javascript
exports.onUserChange = functions.firestore
    .document('users/{userId}')
    .onWrite((change, context) =&gt; {
        console.log('User document changed:', context.params.userId);
    });</code></p>
<p>a) The function will only trigger on document creation<br />
b) The function will trigger on document deletion only<br />
c) The function will trigger on both document creation and deletion<br />
d) The function will not trigger at all  </p>
<p><strong>Answer:</strong> c) The function will trigger on both document creation and deletion</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following best describes a potential issue when using Firestore triggers without proper filtering?</p>
<p>a) They can lead to data inconsistency<br />
b) They can cause functions to run unnecessarily, leading to higher costs<br />
c) They can improve the speed of data retrieval<br />
d) They can enhance user experience  </p>
<p><strong>Answer:</strong> b) They can cause functions to run unnecessarily, leading to higher costs</p>
<hr />
<h3>Question 5:</h3>
<p>If a developer wants to limit the invocation of a Cloud Function to only when a document is created, which of the following code snippets would be correct?</p>
<p>a) 
<code>javascript
exports.onUserCreate = functions.firestore
    .document('users/{userId}')
    .onUpdate((change, context) =&gt; {
        console.log('User document updated:', context.params.userId);
    });</code></p>
<p>b) 
<code>javascript
exports.onUserCreate = functions.firestore
    .document('users/{userId}')
    .onCreate((snap, context) =&gt; {
        console.log('User document created:', context.params.userId);
    });</code></p>
<p>c) 
<code>javascript
exports.onUserCreate = functions.firestore
    .document('users/{userId}')
    .onDelete((snap, context) =&gt; {
        console.log('User document deleted:', context.params.userId);
    });</code></p>
<p>d) 
<code>javascript
exports.onUserCreate = functions.firestore
    .document('users/{userId}')
    .onWrite((change, context) =&gt; {
        console.log('User document changed:', context.params.userId);
    });</code></p>
<p><strong>Answer:</strong> b) 
<code>javascript
exports.onUserCreate = functions.firestore
    .document('users/{userId}')
    .onCreate((snap, context) =&gt; {
        console.log('User document created:', context.params.userId);
    });</code></p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<p>Question 1: What is the primary purpose of Firebase Authentication in a mobile app?<br />
a) To store user data<br />
b) To allow users to sign in using third-party accounts<br />
c) To manage app performance<br />
d) To host the app  </p>
<p>Answer: b) To allow users to sign in using third-party accounts  </p>
<p>Question 2: Which of the following is NOT a supported authentication method in Firebase Authentication?<br />
a) Email and password<br />
b) Phone number<br />
c) OAuth with GitHub<br />
d) LDAP  </p>
<p>Answer: d) LDAP  </p>
<p>Question 3: In the context of Firebase Authentication, which of the following code snippets correctly initializes Firebase?<br />
<code>javascript
firebase.initializeApp({
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
});</code>
a) Correct<br />
b) Incorrect  </p>
<p>Answer: a) Correct  </p>
<p>Question 4: What feature does Firebase Authentication provide to enhance user experience?<br />
a) Automatic data backup<br />
b) User sign-in with social media accounts<br />
c) Real-time database updates<br />
d) Cloud storage for images  </p>
<p>Answer: b) User sign-in with social media accounts  </p>
<p>Question 5: Which of the following Firebase Authentication methods would you use to allow users to sign in with their Google accounts?<br />
a) Email and password<br />
b) Anonymous authentication<br />
c) Google Sign-In<br />
d) Phone authentication  </p>
<p>Answer: c) Google Sign-In  </p>
<hr />
<h1>Use cases of Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is a primary use case for Firebase Cloud Firestore?
a) Storing large binary files<br />
b) Real-time data synchronization<br />
c) Hosting static websites<br />
d) Running server-side scripts  </p>
<p><strong>Answer:</strong> b) Real-time data synchronization</p>
<hr />
<h3>Question 2:</h3>
<p>In the context of Firebase Cloud Firestore, what could be a consequence of misconfigured security rules?
a) Improved application performance<br />
b) Unauthorized access to data<br />
c) Increased data storage costs<br />
d) Enhanced user experience  </p>
<p><strong>Answer:</strong> b) Unauthorized access to data</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following Firestore security rule, what does it allow?</p>
<p><code>plaintext
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}</code></p>
<p>a) Only authenticated users can read and write data<br />
b) Only users with specific roles can read and write data<br />
c) Anyone can read and write data<br />
d) No one can read or write data  </p>
<p><strong>Answer:</strong> c) Anyone can read and write data</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following scenarios best illustrates a potential risk when using Firebase Cloud Firestore?
a) A developer uses Firestore for a simple to-do list application.<br />
b) A developer uses Firestore for a chat application but does not restrict access to user messages.<br />
c) A developer uses Firestore to store images for a photo gallery.<br />
d) A developer uses Firestore to log application errors.  </p>
<p><strong>Answer:</strong> b) A developer uses Firestore for a chat application but does not restrict access to user messages.</p>
<hr />
<h3>Question 5:</h3>
<p>What is a recommended practice when configuring Firestore security rules?
a) Allow all users to read and write data for ease of development<br />
b) Regularly review and update security rules based on application needs<br />
c) Use the same security rules for all applications<br />
d) Disable security rules during development  </p>
<p><strong>Answer:</strong> b) Regularly review and update security rules based on application needs</p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<p>Question 1: What is the primary purpose of Firebase Authentication in a mobile app?<br />
a) To store user data<br />
b) To allow users to sign in using various methods<br />
c) To manage database queries<br />
d) To host the mobile app<br />
<strong>Answer:</strong> b) To allow users to sign in using various methods  </p>
<p>Question 2: Which of the following authentication methods is NOT supported by Firebase Authentication?<br />
a) Email and password<br />
b) Phone number<br />
c) Social media accounts<br />
d) Biometric authentication<br />
<strong>Answer:</strong> d) Biometric authentication  </p>
<p>Question 3: In the context of Firebase Authentication, which of the following code snippets correctly initializes Firebase?<br />
```javascript
import firebase from 'firebase/app';
import 'firebase/auth';</p>
<p>const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
};</p>
<p>firebase.initializeApp(firebaseConfig);
```
a) The code is incorrect because it does not import Firebase correctly.<br />
b) The code is correct and initializes Firebase with the provided configuration.<br />
c) The code is missing the Firestore initialization.<br />
d) The code will throw an error due to missing API keys.<br />
<strong>Answer:</strong> b) The code is correct and initializes Firebase with the provided configuration.  </p>
<p>Question 4: What is the benefit of using Firebase Authentication in a mobile app?<br />
a) It allows for real-time database updates.<br />
b) It simplifies the user login process and enhances security.<br />
c) It provides cloud storage for user files.<br />
d) It automatically scales the app's backend.<br />
<strong>Answer:</strong> b) It simplifies the user login process and enhances security.  </p>
<p>Question 5: Which Firebase Authentication method would you use to allow users to sign in with their Google accounts?<br />
a) Email and password<br />
b) Anonymous authentication<br />
c) OAuth provider<br />
d) Phone authentication<br />
<strong>Answer:</strong> c) OAuth provider  </p>
<hr />
<h1>Data Structure - Collections and Documents</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Firebase Realtime Database?<br />
a) To store large binary files<br />
b) To store structured data in real-time<br />
c) To host static websites<br />
d) To manage user authentication  </p>
<p><strong>Answer:</strong> b) To store structured data in real-time</p>
<h3>Question 2:</h3>
<p>Which Firebase service is recommended for storing large binary files?<br />
a) Firebase Realtime Database<br />
b) Firebase Cloud Firestore<br />
c) Firebase Storage<br />
d) Firebase Hosting  </p>
<p><strong>Answer:</strong> c) Firebase Storage</p>
<h3>Question 3:</h3>
<p>Consider the following code snippet that attempts to store a large image in Firebase Realtime Database:</p>
<p><code>javascript
const database = firebase.database();
const largeImage = fetch('path/to/large/image.jpg');
database.ref('images/largeImage').set(largeImage);</code>
What is the main issue with this code?<br />
a) The image is not being fetched correctly<br />
b) Firebase Realtime Database is not designed for storing large binary files<br />
c) The database reference is incorrect<br />
d) The image will be stored successfully  </p>
<p><strong>Answer:</strong> b) Firebase Realtime Database is not designed for storing large binary files</p>
<h3>Question 4:</h3>
<p>Which of the following statements is true regarding Firebase Realtime Database?<br />
a) It can handle any type of data without limitations.<br />
b) It is optimized for structured data and real-time synchronization.<br />
c) It is the best choice for storing large video files.<br />
d) It does not support offline capabilities.  </p>
<p><strong>Answer:</strong> b) It is optimized for structured data and real-time synchronization.</p>
<h3>Question 5:</h3>
<p>If a developer needs to store user-generated content such as images and videos, which Firebase service should they primarily use?<br />
a) Firebase Realtime Database<br />
b) Firebase Cloud Firestore<br />
c) Firebase Storage<br />
d) Firebase Functions  </p>
<p><strong>Answer:</strong> c) Firebase Storage</p>
<hr />
<h1>Collections</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Firebase Authentication in an app?
a) To store user data<br />
b) To allow users to sign in using various methods<br />
c) To send push notifications<br />
d) To manage app performance  </p>
<p><strong>Answer:</strong> b) To allow users to sign in using various methods</p>
<hr />
<h3>Question 2:</h3>
<p>Which of the following is NOT a method provided by Firebase Authentication for user sign-in?
a) Email and password<br />
b) Phone number<br />
c) Google account<br />
d) Local storage  </p>
<p><strong>Answer:</strong> d) Local storage</p>
<hr />
<h3>Question 3:</h3>
<p>Consider the following code snippet for Firebase Authentication:</p>
<p><code>javascript
firebase.auth().signInWithPopup(new firebase.auth.GoogleAuthProvider())
  .then((result) =&gt; {
    // User signed in
  })
  .catch((error) =&gt; {
    // Handle Errors here.
  });</code>
What does the <code>signInWithPopup</code> method do?
a) It signs in the user silently without any UI.<br />
b) It opens a popup for the user to sign in with their Google account.<br />
c) It sends a verification email to the user.<br />
d) It retrieves the user's profile information.  </p>
<p><strong>Answer:</strong> b) It opens a popup for the user to sign in with their Google account.</p>
<hr />
<h3>Question 4:</h3>
<p>What could be a consequence of not handling the case where a user has disabled notifications when implementing Firebase Cloud Messaging (FCM)?
a) The app will crash.<br />
b) Users will not receive any notifications, leading to a poor user experience.<br />
c) Notifications will be sent to all users regardless of their settings.<br />
d) The app will automatically enable notifications for the user.  </p>
<p><strong>Answer:</strong> b) Users will not receive any notifications, leading to a poor user experience.</p>
<hr />
<h3>Question 5:</h3>
<p>In Firebase Cloud Messaging, which of the following is a necessary step to send a push notification to a user?
a) The user must be logged in.<br />
b) The app must be installed on the user's device.<br />
c) The user must have a valid email address.<br />
d) The user must have a Google account.  </p>
<p><strong>Answer:</strong> b) The app must be installed on the user's device.</p>
<hr />
<h1>Documents</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is a common use case for Cloud Storage in a mobile application?
a) Storing user-generated content like images and videos<br />
b) Managing user authentication<br />
c) Performing real-time data synchronization<br />
d) Hosting static web pages<br />
<strong>Answer:</strong> a) Storing user-generated content like images and videos</p>
<h3>Question 2:</h3>
<p>Which of the following is a potential issue when using Cloud Firestore for a large-scale application?
a) Automatic scaling of resources<br />
b) Slow queries due to improper data structuring<br />
c) High availability of data<br />
d) Built-in security rules<br />
<strong>Answer:</strong> b) Slow queries due to improper data structuring</p>
<h3>Question 3:</h3>
<p>Given the following code snippet, what is the purpose of the <code>set()</code> method in the context of Firestore?</p>
<p><code>javascript
const db = firebase.firestore();
db.collection("users").doc("user1").set({
    name: "John Doe",
    age: 30
});</code>
a) It retrieves the document from the Firestore collection.<br />
b) It updates the document if it exists or creates a new one if it doesn't.<br />
c) It deletes the document from the Firestore collection.<br />
d) It listens for real-time updates to the document.<br />
<strong>Answer:</strong> b) It updates the document if it exists or creates a new one if it doesn't.</p>
<h3>Question 4:</h3>
<p>What could be a consequence of excessive reads in Cloud Firestore?
a) Reduced latency in data retrieval<br />
b) Increased costs associated with data usage<br />
c) Improved performance of queries<br />
d) Automatic data backup<br />
<strong>Answer:</strong> b) Increased costs associated with data usage</p>
<h3>Question 5:</h3>
<p>When linking user-generated content stored in Cloud Storage to user profiles in the Realtime Database, which of the following is a best practice?
a) Store the entire image file in the Realtime Database.<br />
b) Store only the URL of the image in the Realtime Database.<br />
c) Use a single database for both user profiles and images.<br />
d) Avoid using Cloud Storage altogether.<br />
<strong>Answer:</strong> b) Store only the URL of the image in the Realtime Database.</p>
<hr />
<h1>Example of Data Structure</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of using Firebase Analytics in an application?
a) To store user data securely<br />
b) To track user engagement and behavior<br />
c) To host web applications<br />
d) To manage user authentication  </p>
<p><strong>Answer:</strong> b) To track user engagement and behavior</p>
<hr />
<h3>Question 2:</h3>
<p>Which of the following is a potential drawback of relying solely on Firebase Hosting for a complex web application?
a) It provides excellent performance<br />
b) It supports server-side rendering<br />
c) It may lead to performance issues<br />
d) It is free for all users  </p>
<p><strong>Answer:</strong> c) It may lead to performance issues</p>
<hr />
<h3>Question 3:</h3>
<p>Consider the following code snippet that initializes Firebase Analytics. What is the purpose of the <code>logEvent</code> method?</p>
<p><code>javascript
firebase.analytics().logEvent('select_content', {
  content_type: 'image',
  item_id: 'P12453'
});</code></p>
<p>a) To log user sign-in events<br />
b) To track user interactions with specific content<br />
c) To initialize Firebase Hosting<br />
d) To manage user authentication  </p>
<p><strong>Answer:</strong> b) To track user interactions with specific content</p>
<hr />
<h3>Question 4:</h3>
<p>When using Firebase Analytics, which of the following data can be tracked to make data-driven decisions?
a) User location<br />
b) User engagement metrics<br />
c) App crashes<br />
d) All of the above  </p>
<p><strong>Answer:</strong> d) All of the above</p>
<hr />
<h3>Question 5:</h3>
<p>In the context of Firebase, what does the term "server-side rendering" refer to?
a) Rendering web pages on the client-side<br />
b) Generating HTML on the server before sending it to the client<br />
c) Storing data in Firebase Firestore<br />
d) Hosting static files on Firebase Hosting  </p>
<p><strong>Answer:</strong> b) Generating HTML on the server before sending it to the client</p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Cloud Firestore in a chat application?</p>
<p>a) To store images<br />
b) To manage user authentication<br />
c) To provide a real-time database for message updates<br />
d) To host the application  </p>
<p><strong>Answer:</strong> c) To provide a real-time database for message updates</p>
<hr />
<h3>Question 2:</h3>
<p>Which of the following is a potential security vulnerability when using Firebase Authentication without proper input validation?</p>
<p>a) Data redundancy<br />
b) SQL injection<br />
c) Slow performance<br />
d) High latency  </p>
<p><strong>Answer:</strong> b) SQL injection</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following code snippet, what will happen when a new message is added to the Firestore collection "messages"?</p>
<p><code>javascript
const db = firebase.firestore();
db.collection("messages").add({
    user: "John",
    text: "Hello, world!",
    timestamp: firebase.firestore.FieldValue.serverTimestamp()
});</code></p>
<p>a) The message will be stored locally only<br />
b) The message will be sent to all users in real-time<br />
c) The message will be ignored<br />
d) The message will be stored but not sent to other users  </p>
<p><strong>Answer:</strong> b) The message will be sent to all users in real-time</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following best describes a feature of Cloud Firestore?</p>
<p>a) It only supports SQL queries<br />
b) It allows for offline data access and synchronization<br />
c) It requires a dedicated server<br />
d) It does not support real-time updates  </p>
<p><strong>Answer:</strong> b) It allows for offline data access and synchronization</p>
<hr />
<h3>Question 5:</h3>
<p>In the context of a chat application, what is the consequence of not validating user input properly?</p>
<p>a) Users will receive messages faster<br />
b) The application will crash<br />
c) It may lead to unauthorized access or data breaches<br />
d) The application will use more storage  </p>
<p><strong>Answer:</strong> c) It may lead to unauthorized access or data breaches</p>
<hr />
<h3>Question 6:</h3>
<p>What is the correct way to listen for real-time updates in a Firestore collection called "messages"?</p>
<p>a) 
<code>javascript
db.collection("messages").get().then(snapshot =&gt; {
    snapshot.forEach(doc =&gt; {
        console.log(doc.data());
    });
});</code></p>
<p>b) 
<code>javascript
db.collection("messages").onSnapshot(snapshot =&gt; {
    snapshot.forEach(doc =&gt; {
        console.log(doc.data());
    });
});</code></p>
<p>c) 
<code>javascript
db.collection("messages").addListener(snapshot =&gt; {
    snapshot.forEach(doc =&gt; {
        console.log(doc.data());
    });
});</code></p>
<p>d) 
<code>javascript
db.collection("messages").listen(snapshot =&gt; {
    snapshot.forEach(doc =&gt; {
        console.log(doc.data());
    });
});</code></p>
<p><strong>Answer:</strong> b) 
<code>javascript
db.collection("messages").onSnapshot(snapshot =&gt; {
    snapshot.forEach(doc =&gt; {
        console.log(doc.data());
    });
});</code></p>
<hr />
<h1>CRUD Operations - Create Data</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What does CRUD stand for in the context of database operations?<br />
a) Create, Read, Update, Delete<br />
b) Create, Retrieve, Upload, Download<br />
c) Create, Read, Upload, Delete<br />
d) Create, Read, Update, Deploy<br />
<strong>Answer:</strong> a) Create, Read, Update, Delete</p>
<h3>Question 2:</h3>
<p>Which Firebase service is primarily used for deploying static websites?<br />
a) Firebase Realtime Database<br />
b) Firebase Cloud Functions<br />
c) Firebase Hosting<br />
d) Firebase Authentication<br />
<strong>Answer:</strong> c) Firebase Hosting</p>
<h3>Question 3:</h3>
<p>In the context of Firebase Cloud Functions, what could happen if you do not manage the function's memory and timeout settings?<br />
a) The function will always execute successfully.<br />
b) The function may fail unexpectedly during high traffic.<br />
c) The function will run indefinitely without any issues.<br />
d) The function will automatically scale to handle traffic.<br />
<strong>Answer:</strong> b) The function may fail unexpectedly during high traffic.</p>
<h3>Question 4:</h3>
<p>Which of the following is NOT a typical operation in CRUD?<br />
a) Create<br />
b) Read<br />
c) Update<br />
d) Execute<br />
<strong>Answer:</strong> d) Execute</p>
<h3>Question 5:</h3>
<p>Consider the following code snippet for creating a new document in Firestore:</p>
<p><code>javascript
const db = firebase.firestore();
db.collection("users").add({
    name: "John Doe",
    email: "john@example.com"
});</code>
What operation is being performed in this code?<br />
a) Read<br />
b) Update<br />
c) Create<br />
d) Delete<br />
<strong>Answer:</strong> c) Create</p>
<h3>Question 6:</h3>
<p>When deploying a static website using Firebase Hosting, which of the following commands is used to initialize the project?<br />
a) firebase deploy<br />
b) firebase init<br />
c) firebase start<br />
d) firebase setup<br />
<strong>Answer:</strong> b) firebase init</p>
<h3>Question 7:</h3>
<p>What is a potential consequence of not using a global CDN when deploying a static website?<br />
a) Increased loading speed<br />
b) Decreased loading speed for users far from the server<br />
c) Automatic scaling of resources<br />
d) Enhanced security features<br />
<strong>Answer:</strong> b) Decreased loading speed for users far from the server</p>
<hr />
<h1>Adding a Document Example</h1>
<h2>Questions</h2>
<p><strong>Question 1:</strong> In a chat application using a real-time database, what is the primary benefit of using such a database for message handling?<br />
a) Messages are stored permanently<br />
b) Messages are sent via email<br />
c) Messages appear instantly on all users' screens<br />
d) Messages can only be viewed by the sender<br />
<strong>Answer:</strong> c) Messages appear instantly on all users' screens  </p>
<hr />
<p><strong>Question 2:</strong> Which of the following is a common technology used for implementing real-time databases in chat applications?<br />
a) SQL<br />
b) Firebase Realtime Database<br />
c) MongoDB<br />
d) SQLite<br />
<strong>Answer:</strong> b) Firebase Realtime Database  </p>
<hr />
<p><strong>Question 3:</strong> Consider the following code snippet for adding a message to a real-time database in a chat application:</p>
<p><code>javascript
const messageRef = database.ref('messages');
messageRef.push({
    username: 'user1',
    message: 'Hello, everyone!'
});</code></p>
<p>What does the <code>push()</code> method do in this context?<br />
a) It updates an existing message<br />
b) It deletes a message<br />
c) It adds a new message to the database<br />
d) It retrieves messages from the database<br />
<strong>Answer:</strong> c) It adds a new message to the database  </p>
<hr />
<p><strong>Question 4:</strong> In a real-time chat application, which of the following would NOT be a typical feature of the real-time database?<br />
a) Automatic synchronization of messages<br />
b) Offline message storage<br />
c) Manual refresh of the message list<br />
d) Real-time updates for all connected users<br />
<strong>Answer:</strong> c) Manual refresh of the message list  </p>
<hr />
<p><strong>Question 5:</strong> When implementing a chat application, which of the following data structures is most commonly used to store messages in a real-time database?<br />
a) Array<br />
b) Object<br />
c) Queue<br />
d) Stack<br />
<strong>Answer:</strong> b) Object  </p>
<hr />
<h1>Success and Failure Listeners</h1>
<h2>Questions</h2>
<p><strong>Question 1:</strong> In a stock trading application that uses a real-time database, what could be a potential consequence of network latency?<br />
a) All users see the same stock prices<br />
b) Users may see outdated prices leading to poor trading decisions<br />
c) The application will crash<br />
d) Prices will update instantly for all users<br />
<strong>Answer:</strong> b) Users may see outdated prices leading to poor trading decisions  </p>
<p><strong>Question 2:</strong> Which of the following best describes a "success listener" in the context of a real-time database?<br />
a) A listener that triggers when data is successfully written to the database<br />
b) A listener that handles errors during data retrieval<br />
c) A listener that updates the user interface with outdated data<br />
d) A listener that logs all database transactions<br />
<strong>Answer:</strong> a) A listener that triggers when data is successfully written to the database  </p>
<p><strong>Question 3:</strong> In a scenario where a stock trading application has both success and failure listeners, what would a failure listener typically handle?<br />
a) Successful updates to stock prices<br />
b) Network errors or issues retrieving data<br />
c) User interface updates<br />
d) Data validation before writing to the database<br />
<strong>Answer:</strong> b) Network errors or issues retrieving data  </p>
<p><strong>Question 4:</strong> Consider the following code snippet for a stock trading application. What will happen if the <code>onFailure</code> listener is triggered?</p>
<p><code>javascript
database.ref('stocks').on('value', function(snapshot) {
    // Success listener
    updateStockPrices(snapshot.val());
}, function(error) {
    // Failure listener
    console.error("Error retrieving stock prices: ", error);
});</code>
a) The stock prices will be updated successfully<br />
b) An error message will be logged to the console<br />
c) The application will stop functioning<br />
d) The stock prices will be cached<br />
<strong>Answer:</strong> b) An error message will be logged to the console  </p>
<p><strong>Question 5:</strong> What is a common strategy to mitigate the effects of network latency in a real-time stock trading application?<br />
a) Disable all listeners<br />
b) Implement a caching mechanism for stock prices<br />
c) Use a single listener for all data<br />
d) Increase the frequency of database updates<br />
<strong>Answer:</strong> b) Implement a caching mechanism for stock prices  </p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Questions on Cloud Firestore</h3>
<p><strong>Question 1:</strong> What type of database is Cloud Firestore?<br />
a) Relational Database<br />
b) Document Database<br />
c) Key-Value Store<br />
d) Graph Database<br />
<strong>Answer:</strong> b) Document Database</p>
<hr />
<p><strong>Question 2:</strong> In Cloud Firestore, what is the primary data structure used to store data?<br />
a) Tables<br />
b) Collections<br />
c) Rows<br />
d) Objects<br />
<strong>Answer:</strong> b) Collections</p>
<hr />
<p><strong>Question 3:</strong> Given the following code snippet, what will the <code>addMessage</code> function do?</p>
<p><code>javascript
function addMessage(message) {
    const db = firebase.firestore();
    db.collection("messages").add({
        text: message,
        timestamp: firebase.firestore.FieldValue.serverTimestamp()
    });
}</code></p>
<p>a) It will update an existing message in the "messages" collection.<br />
b) It will delete a message from the "messages" collection.<br />
c) It will add a new message to the "messages" collection with a timestamp.<br />
d) It will retrieve messages from the "messages" collection.<br />
<strong>Answer:</strong> c) It will add a new message to the "messages" collection with a timestamp.</p>
<hr />
<p><strong>Question 4:</strong> Which of the following is NOT a feature of Cloud Firestore?<br />
a) Real-time synchronization<br />
b) Offline support<br />
c) SQL query support<br />
d) Automatic scaling<br />
<strong>Answer:</strong> c) SQL query support</p>
<hr />
<p><strong>Question 5:</strong> What is the maximum size of a document in Cloud Firestore?<br />
a) 1 MB<br />
b) 2 MB<br />
c) 10 MB<br />
d) 5 MB<br />
<strong>Answer:</strong> a) 1 MB</p>
<hr />
<p><strong>Question 6:</strong> In Cloud Firestore, how can you listen for real-time updates to a collection?<br />
a) Using <code>db.collection("collectionName").get()</code><br />
b) Using <code>db.collection("collectionName").onSnapshot()</code><br />
c) Using <code>db.collection("collectionName").fetch()</code><br />
d) Using <code>db.collection("collectionName").subscribe()</code><br />
<strong>Answer:</strong> b) Using <code>db.collection("collectionName").onSnapshot()</code></p>
<hr />
<p><strong>Question 7:</strong> What is the purpose of Firestore security rules?<br />
a) To improve database performance<br />
b) To manage data storage<br />
c) To control access to data<br />
d) To format data<br />
<strong>Answer:</strong> c) To control access to data</p>
<hr />
<p><strong>Question 8:</strong> Which of the following statements about Cloud Firestore is true?<br />
a) It requires a fixed schema.<br />
b) It supports complex queries with multiple conditions.<br />
c) It can only store text data.<br />
d) It does not support offline access.<br />
<strong>Answer:</strong> b) It supports complex queries with multiple conditions.</p>
<hr />
<h1>CRUD Operations - Read Data</h1>
<h2>Questions</h2>
<h3>Questions on CRUD Operations</h3>
<p><strong>Question 1:</strong> In a collaborative document editor, what does the "R" in CRUD stand for?<br />
a) Remove<br />
b) Read<br />
c) Replace<br />
d) Render<br />
<strong>Answer:</strong> b) Read</p>
<hr />
<p><strong>Question 2:</strong> Which of the following strategies can be used to handle conflicts when multiple users edit the same line in a document?<br />
a) Last-write-wins<br />
b) First-write-wins<br />
c) Ignore changes<br />
d) Random selection<br />
<strong>Answer:</strong> a) Last-write-wins</p>
<hr />
<p><strong>Question 3:</strong> In a JSON structure for a collaborative document, which of the following represents a new paragraph added by a user?<br />
<code>json
{
  "document": {
    "content": [
      "This is the first line.",
      "This is the second line.",
      "This is a new paragraph."
    ]
  }
}</code>
a) "This is the first line."<br />
b) "This is a new paragraph."<br />
c) "This is the second line."<br />
d) None of the above<br />
<strong>Answer:</strong> b) "This is a new paragraph."</p>
<hr />
<p><strong>Question 4:</strong> If two users edit the same line simultaneously, which of the following is NOT a potential outcome?<br />
a) One user's changes overwrite the other's<br />
b) Both users' changes are merged<br />
c) The application crashes<br />
d) The document remains unchanged<br />
<strong>Answer:</strong> d) The document remains unchanged</p>
<hr />
<p><strong>Question 5:</strong> In a collaborative editing application, which of the following is a common method to ensure data integrity during concurrent edits?<br />
<code>javascript
function updateDocument(userId, newContent) {
    // Pseudocode for updating document
    if (checkForConflicts(userId)) {
        resolveConflict(userId);
    }
    saveToDatabase(newContent);
}</code>
What does the <code>checkForConflicts</code> function likely do?<br />
a) It saves the new content to the database.<br />
b) It checks if another user is editing the same line.<br />
c) It logs the changes made by the user.<br />
d) It sends a notification to all users.<br />
<strong>Answer:</strong> b) It checks if another user is editing the same line.</p>
<hr />
<p><strong>Question 6:</strong> In a real-time collaborative document editor, which of the following data structures is commonly used to store the document content?<br />
a) Array<br />
b) String<br />
c) JSON<br />
d) XML<br />
<strong>Answer:</strong> c) JSON</p>
<hr />
<p><strong>Question 7:</strong> What is a potential drawback of using a "last-write-wins" strategy in a collaborative editing application?<br />
a) It guarantees data integrity.<br />
b) It may lead to loss of important changes made by users.<br />
c) It is easy to implement.<br />
d) It allows for real-time collaboration.<br />
<strong>Answer:</strong> b) It may lead to loss of important changes made by users.</p>
<hr />
<h1>Retrieving Documents</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>In the context of a web application for managing personal notes, which of the following actions corresponds to the "Create" operation?</p>
<p>a) Viewing a list of all notes<br />
b) Editing an existing note<br />
c) Adding a new note<br />
d) Deleting a note  </p>
<p><strong>Answer:</strong> c) Adding a new note</p>
<hr />
<h3>Question 2:</h3>
<p>In an e-commerce platform, what happens when a user attempts to delete an item from their shopping cart that is out of stock?</p>
<p>a) The item is deleted without any warning<br />
b) The system allows the deletion and updates the cart<br />
c) The system prompts the user with a warning instead of allowing the deletion<br />
d) The user is redirected to the homepage  </p>
<p><strong>Answer:</strong> c) The system prompts the user with a warning instead of allowing the deletion</p>
<hr />
<h3>Question 3:</h3>
<p>Which of the following operations is NOT part of the CRUD (Create, Read, Update, Delete) functionality?</p>
<p>a) Create<br />
b) Retrieve<br />
c) Update<br />
d) Archive  </p>
<p><strong>Answer:</strong> d) Archive</p>
<hr />
<h3>Question 4:</h3>
<p>Consider the following code snippet for adding a note in a web application:</p>
<p><code>python
def add_note(note_content):
    notes.append(note_content)
    return "Note added successfully!"</code></p>
<p>What does this function primarily perform?</p>
<p>a) It retrieves a note from the list<br />
b) It updates an existing note<br />
c) It creates a new note<br />
d) It deletes a note  </p>
<p><strong>Answer:</strong> c) It creates a new note</p>
<hr />
<h3>Question 5:</h3>
<p>In a CRUD application, which operation would you use to change the content of an existing note?</p>
<p>a) Create<br />
b) Read<br />
c) Update<br />
d) Delete  </p>
<p><strong>Answer:</strong> c) Update</p>
<hr />
<h3>Question 6:</h3>
<p>If a user wants to view all their notes in a web application, which CRUD operation are they performing?</p>
<p>a) Create<br />
b) Read<br />
c) Update<br />
d) Delete  </p>
<p><strong>Answer:</strong> b) Read</p>
<hr />
<h3>Question 7:</h3>
<p>In the context of an e-commerce platform, which of the following actions would be classified as an "Update"?</p>
<p>a) Adding a new item to the cart<br />
b) Viewing the cart contents<br />
c) Changing the quantity of an item in the cart<br />
d) Removing an item from the cart  </p>
<p><strong>Answer:</strong> c) Changing the quantity of an item in the cart</p>
<hr />
<h3>Question 8:</h3>
<p>Which of the following best describes the "Delete" operation in a CRUD application?</p>
<p>a) It allows users to view their data.<br />
b) It enables users to remove data they no longer need.<br />
c) It allows users to modify existing data.<br />
d) It creates new data entries.  </p>
<p><strong>Answer:</strong> b) It enables users to remove data they no longer need.</p>
<hr />
<h1>Success Listener</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>In a chat application, what is the primary purpose of a success listener?<br />
a) To log all messages sent by users<br />
b) To notify users when a message has been successfully delivered<br />
c) To delete messages after a certain time<br />
d) To change the theme of the chat application<br />
<strong>Answer:</strong> b) To notify users when a message has been successfully delivered</p>
<h3>Question 2:</h3>
<p>Which of the following scenarios best illustrates a typical use of a success listener in a chat application?<br />
a) A user receives a notification when a file is uploaded successfully.<br />
b) A user is informed when their message fails to send due to a network issue.<br />
c) A user can change their profile picture.<br />
d) A user is prompted to log out after a period of inactivity.<br />
<strong>Answer:</strong> a) A user receives a notification when a file is uploaded successfully.</p>
<h3>Question 3:</h3>
<p>Consider the following code snippet for a chat application. What does the <code>onMessageSent</code> function represent?<br />
```javascript
function sendMessage(message) {
    // Code to send the message
    onMessageSent(message);
}</p>
<p>function onMessageSent(message) {
    console.log("Message sent successfully: " + message);
}
```
a) It is a function that sends the message to the server.<br />
b) It is a callback function that executes after a message is sent successfully.<br />
c) It is a function that logs errors when sending a message fails.<br />
d) It is a function that formats the message before sending.<br />
<strong>Answer:</strong> b) It is a callback function that executes after a message is sent successfully.</p>
<h3>Question 4:</h3>
<p>In a chat application, what could be a potential issue if a user sends a message to the wrong channel?<br />
a) The message will be deleted automatically.<br />
b) The user will receive a success notification.<br />
c) Team members may be confused about the intended audience for the message.<br />
d) The application will crash.<br />
<strong>Answer:</strong> c) Team members may be confused about the intended audience for the message.</p>
<h3>Question 5:</h3>
<p>What feature could enhance productivity in a chat application like Slack?<br />
a) Allowing users to send messages only during working hours.<br />
b) Integrating with other tools such as calendars and task managers.<br />
c) Limiting the number of messages a user can send per day.<br />
d) Disabling notifications for all messages.<br />
<strong>Answer:</strong> b) Integrating with other tools such as calendars and task managers.</p>
<hr />
<h1>Failure Listener</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is a common feature of collaborative tools like Google Docs that helps users track changes made to a document?
a) Spell check<br />
b) Version history<br />
c) Text formatting<br />
d) Page layout  </p>
<p><strong>Answer:</strong> b) Version history</p>
<hr />
<h3>Question 2:</h3>
<p>In a collaborative editing scenario, what could lead to a user accidentally overwriting another user's changes?
a) Clear communication<br />
b) Lack of version history<br />
c) Real-time editing<br />
d) User permissions  </p>
<p><strong>Answer:</strong> b) Lack of version history</p>
<hr />
<h3>Question 3:</h3>
<p>Which of the following statements best describes a failure listener in collaborative tools?
a) It prevents users from editing simultaneously.<br />
b) It notifies users when someone else is editing the same document.<br />
c) It allows users to edit documents without any restrictions.<br />
d) It automatically saves changes made by users.  </p>
<p><strong>Answer:</strong> b) It notifies users when someone else is editing the same document.</p>
<hr />
<h3>Question 4:</h3>
<p>Consider the following code snippet that simulates a collaborative document editing environment. What will happen if two users try to edit the same section without proper communication?</p>
<p>```python
class Document:
    def <strong>init</strong>(self):
        self.content = ""</p>
<pre><code>def edit(self, user, new_content):
    self.content = new_content
    print(f"{user} edited the document.")
</code></pre>
<p>doc = Document()
doc.edit("User1", "Hello World!")
doc.edit("User2", "Goodbye World!")
```</p>
<p>a) User1's changes will be saved.<br />
b) User2's changes will overwrite User1's changes.<br />
c) Both changes will be saved in the document.<br />
d) The document will not allow any edits.  </p>
<p><strong>Answer:</strong> b) User2's changes will overwrite User1's changes.</p>
<hr />
<h3>Question 5:</h3>
<p>What is a potential consequence of not having a failure listener in a collaborative tool?
a) Increased productivity<br />
b) Reduced chances of data loss<br />
c) Confusion and loss of important edits<br />
d) Enhanced user experience  </p>
<p><strong>Answer:</strong> c) Confusion and loss of important edits</p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is a primary use case for Cloud Firestore in application development?<br />
a) Storing images<br />
b) Real-time data synchronization<br />
c) Video streaming<br />
d) File storage<br />
<strong>Answer:</strong> b) Real-time data synchronization</p>
<h3>Question 2:</h3>
<p>Which of the following statements about Cloud Firestore is true?<br />
a) It only supports SQL queries.<br />
b) It is a NoSQL database that allows for flexible data structures.<br />
c) It requires a fixed schema for data storage.<br />
d) It does not support offline data access.<br />
<strong>Answer:</strong> b) It is a NoSQL database that allows for flexible data structures.</p>
<h3>Question 3:</h3>
<p>Consider the following code snippet for adding a document to a Firestore collection:</p>
<p><code>javascript
const db = firebase.firestore();
db.collection("users").add({
    name: "John Doe",
    age: 30,
    city: "New York"
});</code>
What will happen if the "users" collection does not exist?<br />
a) An error will be thrown.<br />
b) The document will be added, and the collection will be created automatically.<br />
c) The document will be ignored.<br />
d) The database will crash.<br />
<strong>Answer:</strong> b) The document will be added, and the collection will be created automatically.</p>
<h3>Question 4:</h3>
<p>What is a potential issue when using a live dashboard that relies on Cloud Firestore?<br />
a) It can only display data from one collection.<br />
b) Data may be outdated due to synchronization delays.<br />
c) It cannot handle real-time updates.<br />
d) It requires a constant internet connection.<br />
<strong>Answer:</strong> b) Data may be outdated due to synchronization delays.</p>
<h3>Question 5:</h3>
<p>In Cloud Firestore, what is the purpose of a "listener"?<br />
a) To delete documents from a collection.<br />
b) To listen for changes in data and update the UI in real-time.<br />
c) To create new collections.<br />
d) To perform batch writes.<br />
<strong>Answer:</strong> b) To listen for changes in data and update the UI in real-time.</p>
<hr />
<h1>CRUD Operations - Update Data</h1>
<h2>Questions</h2>
<h3>Questions on CRUD Operations - Update Data</h3>
<p><strong>Question 1:</strong> In a mobile application using Cloud Firestore, which operation allows a user to change their profile picture?<br />
a) Create<br />
b) Read<br />
c) Update<br />
d) Delete<br />
<strong>Answer:</strong> c) Update</p>
<hr />
<p><strong>Question 2:</strong> Which of the following statements about Cloud Firestore's real-time synchronization is true?<br />
a) Changes made by one user are only visible to that user.<br />
b) Changes are reflected across all devices instantly.<br />
c) Real-time synchronization is only available for read operations.<br />
d) Users must refresh the app to see updates made by others.<br />
<strong>Answer:</strong> b) Changes are reflected across all devices instantly.</p>
<hr />
<p><strong>Question 3:</strong> Given the following code snippet, what operation is being performed when the <code>updateProfilePicture</code> function is called?</p>
<p><code>javascript
function updateProfilePicture(userId, newPictureUrl) {
    const userRef = firestore.collection('users').doc(userId);
    return userRef.update({
        profilePicture: newPictureUrl
    });
}</code>
a) Creating a new user<br />
b) Reading user data<br />
c) Updating the user's profile picture<br />
d) Deleting the user's profile<br />
<strong>Answer:</strong> c) Updating the user's profile picture</p>
<hr />
<p><strong>Question 4:</strong> Which of the following is NOT a typical use case for the Update operation in a CRUD application?<br />
a) Changing a user's email address<br />
b) Modifying the content of a blog post<br />
c) Retrieving a list of all users<br />
d) Updating a user's subscription status<br />
<strong>Answer:</strong> c) Retrieving a list of all users</p>
<hr />
<p><strong>Question 5:</strong> What will happen if the <code>update</code> method is called on a document that does not exist in Cloud Firestore?<br />
a) It will create a new document.<br />
b) It will throw an error.<br />
c) It will update the document with default values.<br />
d) It will do nothing.<br />
<strong>Answer:</strong> b) It will throw an error.</p>
<hr />
<h1>Updating a Document Example</h1>
<h2>Questions</h2>
<p><strong>Question 1:</strong> In a web application using Cloud Firestore for a chat feature, what is a potential issue when multiple users send messages simultaneously?<br />
a) Messages are always stored correctly<br />
b) Messages could be lost or duplicated<br />
c) Messages are automatically encrypted<br />
d) Messages are stored in alphabetical order<br />
<strong>Answer:</strong> b) Messages could be lost or duplicated  </p>
<hr />
<p><strong>Question 2:</strong> Which of the following strategies can be used to handle race conditions in a chat application using Cloud Firestore?<br />
a) Ignoring the issue<br />
b) Implementing proper transaction handling<br />
c) Using a single-threaded approach<br />
d) Storing messages in a local database only<br />
<strong>Answer:</strong> b) Implementing proper transaction handling  </p>
<hr />
<p><strong>Question 3:</strong> Consider the following code snippet for sending a message in a chat application. What is the purpose of the <code>transaction</code> method in this context?</p>
<p>```javascript
const sendMessage = async (message) =&gt; {
  const db = firebase.firestore();
  const messageRef = db.collection('messages').doc();</p>
<p>await db.runTransaction(async (transaction) =&gt; {
    transaction.set(messageRef, {
      text: message,
      timestamp: firebase.firestore.FieldValue.serverTimestamp(),
    });
  });
};
```</p>
<p>a) To ensure that the message is sent only once<br />
b) To automatically delete old messages<br />
c) To retrieve messages from the database<br />
d) To update the user's profile<br />
<strong>Answer:</strong> a) To ensure that the message is sent only once  </p>
<hr />
<p><strong>Question 4:</strong> What is a potential consequence of not implementing conflict resolution strategies in a chat application?<br />
a) Users will receive notifications for every message<br />
b) Messages may appear out of order or be duplicated<br />
c) The application will run faster<br />
d) Users will be able to edit their messages<br />
<strong>Answer:</strong> b) Messages may appear out of order or be duplicated  </p>
<hr />
<p><strong>Question 5:</strong> In the context of Cloud Firestore, what does the term "transaction" refer to?<br />
a) A single read operation<br />
b) A batch of write operations that are executed atomically<br />
c) A method to delete documents<br />
d) A way to create indexes<br />
<strong>Answer:</strong> b) A batch of write operations that are executed atomically  </p>
<hr />
<h1>Success and Failure Listeners</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>In a mobile application for a bookstore, which of the following fields would NOT typically be found in a document within the 'books' collection?</p>
<p>a) title<br />
b) author<br />
c) ISBN<br />
d) user reviews  </p>
<p><strong>Answer:</strong> d) user reviews</p>
<hr />
<h3>Question 2:</h3>
<p>In a social media application, if you want to retrieve all posts made by users with a specific interest, what is a potential challenge you might face?</p>
<p>a) The posts are not stored in a collection.<br />
b) You can only query one collection at a time.<br />
c) Users cannot have multiple interests.<br />
d) Posts are automatically deleted after a week.  </p>
<p><strong>Answer:</strong> b) You can only query one collection at a time.</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following code snippet, what will be the output if the 'books' collection contains a book with the title "The Great Gatsby"?</p>
<p><code>javascript
const bookTitle = "The Great Gatsby";
const query = db.collection('books').where('title', '==', bookTitle);
query.get().then(snapshot =&gt; {
    if (snapshot.empty) {
        console.log('No matching documents.');
    } else {
        snapshot.forEach(doc =&gt; {
            console.log(doc.id, '=&gt;', doc.data());
        });
    }
});</code></p>
<p>a) No matching documents.<br />
b) The Great Gatsby =&gt; { ... }<br />
c) An error will occur.<br />
d) The query will return all books.  </p>
<p><strong>Answer:</strong> b) The Great Gatsby =&gt; { ... }</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following statements is true regarding querying in Firestore?</p>
<p>a) You can perform complex queries across multiple collections without limitations.<br />
b) Firestore allows you to query documents based on multiple fields in a single collection.<br />
c) Firestore does not support indexing, making queries slow.<br />
d) You can only retrieve documents based on their document ID.  </p>
<p><strong>Answer:</strong> b) Firestore allows you to query documents based on multiple fields in a single collection.</p>
<hr />
<h3>Question 5:</h3>
<p>If you have a 'users' collection with a sub-collection 'posts', which of the following queries would be the most efficient way to find posts by users interested in "Photography"?</p>
<p>a) Query the 'posts' collection directly for the interest "Photography".<br />
b) Retrieve all users, filter them by interest, and then retrieve their posts.<br />
c) Query the 'users' collection for "Photography" and then retrieve all posts.<br />
d) Use a single query to get all posts and filter them in the application code.  </p>
<p><strong>Answer:</strong> c) Query the 'users' collection for "Photography" and then retrieve all posts.</p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is a primary benefit of using Cloud Firestore in a social media application?</p>
<p>a) It allows for real-time updates of user data and interactions.<br />
b) It requires complex SQL queries for data retrieval.<br />
c) It stores data in a flat file format.<br />
d) It does not support offline access.  </p>
<p><strong>Answer:</strong> a) It allows for real-time updates of user data and interactions.</p>
<hr />
<h3>Question 2:</h3>
<p>In the context of Cloud Firestore, what could be a consequence of not properly indexing your data?</p>
<p>a) Improved data retrieval speed.<br />
b) Increased data redundancy.<br />
c) Slow and inefficient queries, especially under high traffic.<br />
d) Automatic scaling of the database.  </p>
<p><strong>Answer:</strong> c) Slow and inefficient queries, especially under high traffic.</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following code snippet, which of the following statements is true about the Firestore document structure?</p>
<p><code>javascript
const userRef = firestore.collection('users').doc('user123');
const userProfile = {
    username: 'john_doe',
    profilePicture: 'url_to_picture',
    postIDs: ['post1', 'post2', 'post3']
};
userRef.set(userProfile);</code></p>
<p>a) The document is stored in a collection named 'posts'.<br />
b) The document contains fields for username, profile picture, and an array of post IDs.<br />
c) The document will automatically delete itself after 30 days.<br />
d) The document can only contain string values.  </p>
<p><strong>Answer:</strong> b) The document contains fields for username, profile picture, and an array of post IDs.</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following scenarios best illustrates a potential issue when using Cloud Firestore for an e-commerce platform?</p>
<p>a) Users can view products without any delay.<br />
b) A query to retrieve products based on multiple filters becomes slow and inefficient due to lack of indexing.<br />
c) The platform can easily scale to handle millions of users.<br />
d) Products are automatically categorized based on user preferences.  </p>
<p><strong>Answer:</strong> b) A query to retrieve products based on multiple filters becomes slow and inefficient due to lack of indexing.</p>
<hr />
<h3>Question 5:</h3>
<p>What type of data structure does Cloud Firestore use to store user profiles and posts in the provided social media application example?</p>
<p>a) Key-Value pairs<br />
b) Relational tables<br />
c) Document collections<br />
d) Graph nodes  </p>
<p><strong>Answer:</strong> c) Document collections</p>
<hr />
<h1>CRUD Operations - Delete Data</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>In a content management system (CMS) using Cloud Firestore, which of the following fields is NOT typically included in an article document?</p>
<p>a) Title<br />
b) Content<br />
c) Author ID<br />
d) Comment Count  </p>
<p><strong>Answer:</strong> d) Comment Count</p>
<hr />
<h3>Question 2:</h3>
<p>What is a potential downside of storing all comments in a single collection in a CMS?</p>
<p>a) It simplifies the database structure.<br />
b) It allows for faster retrieval of comments.<br />
c) It can lead to slow loading times for articles with many comments.<br />
d) It ensures that all comments are stored in one place.  </p>
<p><strong>Answer:</strong> c) It can lead to slow loading times for articles with many comments.</p>
<hr />
<h3>Question 3:</h3>
<p>Which of the following operations is NOT part of CRUD operations?</p>
<p>a) Create<br />
b) Read<br />
c) Update<br />
d) Delete<br />
e) Execute  </p>
<p><strong>Answer:</strong> e) Execute</p>
<hr />
<h3>Question 4:</h3>
<p>Given the following code snippet, what operation is being performed?</p>
<p><code>javascript
db.collection("articles").doc("articleId").delete();</code></p>
<p>a) Creating a new article<br />
b) Reading an article<br />
c) Updating an article<br />
d) Deleting an article  </p>
<p><strong>Answer:</strong> d) Deleting an article</p>
<hr />
<h3>Question 5:</h3>
<p>In a CMS, if a developer wants to efficiently retrieve comments for each article, which of the following strategies would be best?</p>
<p>a) Store all comments in a single collection regardless of the article.<br />
b) Create a separate collection for each article's comments.<br />
c) Store comments as sub-collections within each article document.<br />
d) Use a flat file to store comments.  </p>
<p><strong>Answer:</strong> c) Store comments as sub-collections within each article document.</p>
<hr />
<h1>Example of Deleting a Document</h1>
<h2>Questions</h2>
<p><strong>Question 1:</strong> In a mobile application using Cloud Firestore, which method would you use to delete a user profile document with the ID "user123"?<br />
a) <code>db.collection("profiles").remove("user123")</code><br />
b) <code>db.collection("profiles").delete("user123")</code><br />
c) <code>db.collection("profiles").doc("user123").delete()</code><br />
d) <code>db.collection("profiles").removeDocument("user123")</code><br />
<strong>Answer:</strong> c) <code>db.collection("profiles").doc("user123").delete()</code></p>
<hr />
<p><strong>Question 2:</strong> What is the primary benefit of using Cloud Firestore for managing user profiles in a mobile application?<br />
a) It requires no internet connection.<br />
b) It allows for real-time synchronization across devices.<br />
c) It only supports text data.<br />
d) It is limited to storing images.<br />
<strong>Answer:</strong> b) It allows for real-time synchronization across devices.</p>
<hr />
<p><strong>Question 3:</strong> If you want to ensure that a user profile is deleted only if it exists, which of the following code snippets would be the best approach?<br />
<code>javascript
const userRef = db.collection("profiles").doc("user123");
userRef.get().then((doc) =&gt; {
    if (doc.exists) {
        userRef.delete();
    }
});</code>
What does this code do?<br />
a) Deletes the user profile without checking if it exists.<br />
b) Checks if the user profile exists before deleting it.<br />
c) Creates a new user profile if it doesn't exist.<br />
d) Updates the user profile if it exists.<br />
<strong>Answer:</strong> b) Checks if the user profile exists before deleting it.</p>
<hr />
<p><strong>Question 4:</strong> Which of the following statements is true regarding the deletion of documents in Cloud Firestore?<br />
a) Deleted documents can be recovered easily.<br />
b) Deleting a document does not affect the data in other documents.<br />
c) You can delete multiple documents in a single operation.<br />
d) Deleting a document requires a confirmation step from the user.<br />
<strong>Answer:</strong> b) Deleting a document does not affect the data in other documents.</p>
<hr />
<p><strong>Question 5:</strong> In the context of Cloud Firestore, what happens to the data of a deleted document?<br />
a) It is archived and can be restored later.<br />
b) It is permanently removed and cannot be recovered.<br />
c) It is moved to a different collection.<br />
d) It is only hidden from view but remains in the database.<br />
<strong>Answer:</strong> b) It is permanently removed and cannot be recovered.</p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the primary purpose of Cloud Firestore in an e-commerce application?</p>
<p>a) To manage user authentication<br />
b) To store and sync data in real-time<br />
c) To handle payment processing<br />
d) To serve static files  </p>
<p><strong>Answer:</strong> b) To store and sync data in real-time</p>
<hr />
<h3>Question 2:</h3>
<p>In the context of Cloud Firestore, what is a potential issue when multiple users attempt to purchase the same item simultaneously?</p>
<p>a) Data redundancy<br />
b) Race conditions<br />
c) Data encryption<br />
d) Network latency  </p>
<p><strong>Answer:</strong> b) Race conditions</p>
<hr />
<h3>Question 3:</h3>
<p>Given the following code snippet, what will happen if two users try to execute this transaction at the same time?</p>
<p>```javascript
const db = firebase.firestore();
const productRef = db.collection('products').doc('item123');</p>
<p>db.runTransaction(async (transaction) =&gt; {
    const doc = await transaction.get(productRef);
    if (!doc.exists) {
        throw "Document does not exist!";
    }
    const newStock = doc.data().stock - 1;
    transaction.update(productRef, { stock: newStock });
});
```</p>
<p>a) Both transactions will succeed, and stock will be decremented twice.<br />
b) One transaction will succeed, and the other will fail due to a document not existing.<br />
c) Both transactions will fail due to a race condition.<br />
d) One transaction will succeed, and the stock will be decremented by 1.  </p>
<p><strong>Answer:</strong> d) One transaction will succeed, and the stock will be decremented by 1.</p>
<hr />
<h3>Question 4:</h3>
<p>Which of the following strategies can help prevent race conditions in Cloud Firestore when updating stock levels?</p>
<p>a) Using Firestore's offline capabilities<br />
b) Implementing optimistic concurrency control<br />
c) Increasing the read/write limits<br />
d) Storing stock levels in a separate database  </p>
<p><strong>Answer:</strong> b) Implementing optimistic concurrency control</p>
<hr />
<h3>Question 5:</h3>
<p>What is the maximum size of a document in Cloud Firestore?</p>
<p>a) 1 MB<br />
b) 2 MB<br />
c) 4 MB<br />
d) 10 MB  </p>
<p><strong>Answer:</strong> a) 1 MB</p>
<hr />
<h1>Realtime Update Listener</h1>
<h2>Questions</h2>
<p>Question 1: In a Cloud Firestore database, which of the following is a valid way to set up a real-time update listener for a collection named 'Users'?<br />
a) <code>db.collection('Users').onSnapshot(snapshot =&gt; { console.log(snapshot); });</code><br />
b) <code>db.collection('Users').get().then(snapshot =&gt; { console.log(snapshot); });</code><br />
c) <code>db.collection('Users').listen(snapshot =&gt; { console.log(snapshot); });</code><br />
d) <code>db.collection('Users').subscribe(snapshot =&gt; { console.log(snapshot); });</code><br />
<strong>Answer:</strong> a) <code>db.collection('Users').onSnapshot(snapshot =&gt; { console.log(snapshot); });</code></p>
<p>Question 2: What type of data structure is typically used to represent a user document in a Firestore database?<br />
a) Array<br />
b) String<br />
c) Object<br />
d) Set<br />
<strong>Answer:</strong> c) Object</p>
<p>Question 3: If you want to listen for real-time updates on a specific document in the 'Users' collection, which of the following code snippets is correct?<br />
a) <code>db.collection('Users').doc('userId').onSnapshot(doc =&gt; { console.log(doc.data()); });</code><br />
b) <code>db.collection('Users').doc('userId').get().then(doc =&gt; { console.log(doc.data()); });</code><br />
c) <code>db.collection('Users').doc('userId').listen(doc =&gt; { console.log(doc.data()); });</code><br />
d) <code>db.collection('Users').doc('userId').subscribe(doc =&gt; { console.log(doc.data()); });</code><br />
<strong>Answer:</strong> a) <code>db.collection('Users').doc('userId').onSnapshot(doc =&gt; { console.log(doc.data()); });</code></p>
<p>Question 4: Which of the following fields would NOT typically be included in a user document in a Firestore database?<br />
a) 'name'<br />
b) 'email'<br />
c) 'password'<br />
d) 'age'<br />
<strong>Answer:</strong> c) 'password' (assuming best practices for security)</p>
<p>Question 5: What will happen if you call <code>onSnapshot</code> on a Firestore collection?<br />
a) It will return a promise with the current data.<br />
b) It will set up a listener that triggers every time the data changes.<br />
c) It will delete the collection.<br />
d) It will only fetch the data once without listening for updates.<br />
<strong>Answer:</strong> b) It will set up a listener that triggers every time the data changes.</p>
<hr />
<h1>addSnapshotListener</h1>
<h2>Questions</h2>
<h3>Multiple Choice Questions on <code>addSnapshotListener</code></h3>
<p><strong>Question 1:</strong> What is the primary purpose of the <code>addSnapshotListener</code> method in Firestore?<br />
a) To add a new document to a collection<br />
b) To listen for real-time updates to a document or collection<br />
c) To delete a document from a collection<br />
d) To update a document in a collection<br />
<strong>Answer:</strong> b) To listen for real-time updates to a document or collection</p>
<hr />
<p><strong>Question 2:</strong> Given the following code snippet, what will happen when a new item is added to the 'Items' sub-collection of an order document?</p>
<p><code>javascript
const orderRef = firestore.collection('Orders').doc('12345');
orderRef.onSnapshot((doc) =&gt; {
    console.log("Current data: ", doc.data());
});</code></p>
<p>a) The console will log the current data of the order document only once.<br />
b) The console will log the current data of the order document every time it changes.<br />
c) The console will log an error if the 'Items' sub-collection is updated.<br />
d) The console will not log anything since it only listens to the 'Items' sub-collection.<br />
<strong>Answer:</strong> b) The console will log the current data of the order document every time it changes.</p>
<hr />
<p><strong>Question 3:</strong> In the context of Firestore, what is a potential issue when using <code>addSnapshotListener</code> on a document that contains a sub-collection?<br />
a) It will not listen to changes in the sub-collection.<br />
b) It may lead to performance issues due to multiple listeners.<br />
c) It will only return the data of the sub-collection and ignore the parent document.<br />
d) It will automatically delete the sub-collection when the parent document is deleted.<br />
<strong>Answer:</strong> b) It may lead to performance issues due to multiple listeners.</p>
<hr />
<p><strong>Question 4:</strong> If you want to listen for changes specifically in the 'Items' sub-collection of an order document, which of the following code snippets would you use?</p>
<p><code>javascript
const itemsRef = firestore.collection('Orders').doc('12345').collection('Items');
itemsRef.onSnapshot((snapshot) =&gt; {
    snapshot.forEach((doc) =&gt; {
        console.log(doc.id, " =&gt; ", doc.data());
    });
});</code></p>
<p>a) This code will listen for changes in the 'Orders' collection only.<br />
b) This code will listen for changes in the 'Items' sub-collection and log each item's data.<br />
c) This code will throw an error since you cannot listen to sub-collections.<br />
d) This code will only log the IDs of the documents in the 'Items' sub-collection.<br />
<strong>Answer:</strong> b) This code will listen for changes in the 'Items' sub-collection and log each item's data.</p>
<hr />
<p><strong>Question 5:</strong> When using <code>addSnapshotListener</code>, what type of updates can you expect to receive?<br />
a) Only initial data when the listener is first added<br />
b) Only updates to the document's fields, not sub-collections<br />
c) Real-time updates including additions, modifications, and deletions<br />
d) Only deletions of documents in the collection<br />
<strong>Answer:</strong> c) Real-time updates including additions, modifications, and deletions</p>
<hr />
<h1>DocumentChange Types</h1>
<h2>Questions</h2>
<p>Question 1: In Cloud Firestore, which of the following is NOT a typical field you might find in a user document within a 'Users' collection?<br />
a) name<br />
b) email<br />
c) password<br />
d) age<br />
<strong>Answer:</strong> c) password  </p>
<p>Question 2: Given the following document structure in a 'Users' collection, which field would you use to retrieve the user's age?<br />
<code>json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "age": 25
}</code><br />
a) name<br />
b) email<br />
c) age<br />
d) userAge<br />
<strong>Answer:</strong> c) age  </p>
<p>Question 3: If you wanted to update the email of a user in the 'Users' collection, which of the following Firestore methods would you use?<br />
a) set()<br />
b) update()<br />
c) delete()<br />
d) get()<br />
<strong>Answer:</strong> b) update()  </p>
<p>Question 4: In a Firestore document, which of the following data types can be used for fields?<br />
a) String<br />
b) Number<br />
c) Boolean<br />
d) All of the above<br />
<strong>Answer:</strong> d) All of the above  </p>
<p>Question 5: If you have a document in the 'Users' collection with the following data:<br />
<code>json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "age": 28
}</code><br />
What would be the correct Firestore query to retrieve this document by email?<br />
a) db.collection('Users').where('name', '==', 'Alice Johnson')<br />
b) db.collection('Users').where('email', '==', 'alice@example.com')<br />
c) db.collection('Users').get('age', '==', 28)<br />
d) db.collection('Users').find('email', 'alice@example.com')<br />
<strong>Answer:</strong> b) db.collection('Users').where('email', '==', 'alice@example.com')  </p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>In Cloud Firestore, which of the following is true about sub-collections?</p>
<p>a) Sub-collections can only be created at the root level.<br />
b) Sub-collections can exist within documents.<br />
c) Sub-collections cannot contain documents.<br />
d) Sub-collections are limited to a maximum of 5 documents.  </p>
<p><strong>Answer:</strong> b) Sub-collections can exist within documents.</p>
<hr />
<h3>Question 2:</h3>
<p>Given the following Firestore document structure for an order, which query would you use to retrieve all items from the 'Items' sub-collection of the order with <code>orderId</code> '12345'?</p>
<p><code>javascript
const orderRef = db.collection('Orders').doc('12345');</code></p>
<p>a) <code>orderRef.collection('Items').get()</code><br />
b) <code>db.collection('Items').get()</code><br />
c) <code>db.collection('Orders').doc('12345').collection('Items').get()</code><br />
d) <code>db.collection('Orders').get('Items')</code>  </p>
<p><strong>Answer:</strong> c) <code>db.collection('Orders').doc('12345').collection('Items').get()</code></p>
<hr />
<h3>Question 3:</h3>
<p>What is the primary benefit of using sub-collections in Cloud Firestore?</p>
<p>a) They reduce the overall size of the database.<br />
b) They allow for more complex data structures and relationships.<br />
c) They automatically index all fields.<br />
d) They eliminate the need for document IDs.  </p>
<p><strong>Answer:</strong> b) They allow for more complex data structures and relationships.</p>
<hr />
<h3>Question 4:</h3>
<p>If you want to query all items across multiple orders in Firestore, which of the following approaches is NOT recommended?</p>
<p>a) Use a separate collection for items and reference order IDs.<br />
b) Use Firestore's built-in querying capabilities to filter items by order ID.<br />
c) Store all items in a single document to avoid multiple reads.<br />
d) Use batched reads to fetch items from multiple orders.  </p>
<p><strong>Answer:</strong> c) Store all items in a single document to avoid multiple reads.</p>
<hr />
<h3>Question 5:</h3>
<p>Consider the following Firestore document structure for an order. What will be the output of the following code snippet?</p>
<p><code>javascript
const orderRef = db.collection('Orders').doc('12345');
orderRef.get().then(doc =&gt; {
    if (doc.exists) {
        console.log(doc.data().Items);
    } else {
        console.log("No such document!");
    }
});</code></p>
<p>a) It will log "No such document!" if the order does not exist.<br />
b) It will log the entire order document.<br />
c) It will log only the <code>Items</code> sub-collection.<br />
d) It will throw an error if the document does not exist.  </p>
<p><strong>Answer:</strong> a) It will log "No such document!" if the order does not exist.</p>
<hr />
<h1>Security Rules</h1>
<h2>Questions</h2>
<p>Question 1: In a database of customer information, which of the following fields would most likely be stored as a string?<br />
a) Phone Number<br />
b) Age<br />
c) Name<br />
d) Customer ID<br />
<strong>Answer:</strong> c) Name  </p>
<p>Question 2: If a customer record contains the following fields: name, email, phone number, and address, which field is most likely to contain an integer data type?<br />
a) Name<br />
b) Email<br />
c) Phone Number<br />
d) Address<br />
<strong>Answer:</strong> c) Phone Number  </p>
<p>Question 3: Which of the following is NOT a typical field in a customer information database?<br />
a) Name<br />
b) Email<br />
c) Purchase History<br />
d) Favorite Color<br />
<strong>Answer:</strong> d) Favorite Color  </p>
<p>Question 4: In a database schema for customer information, which of the following data types would be most appropriate for storing an email address?<br />
a) Integer<br />
b) String<br />
c) Boolean<br />
d) Date<br />
<strong>Answer:</strong> b) String  </p>
<p>Question 5: Given the following code snippet for a customer record in a database, what is the data type of the 'phoneNumber' field?<br />
<code>json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phoneNumber": "1234567890",
  "address": "123 Main St"
}</code><br />
a) Integer<br />
b) String<br />
c) Float<br />
d) Boolean<br />
<strong>Answer:</strong> b) String  </p>
<hr />
<h1>Example Security Rule</h1>
<h2>Questions</h2>
<p><strong>Question 1:</strong> In the context of a security rule for a database, which of the following best describes a document that includes an array with mixed data types?</p>
<p>a) A document that only contains strings<br />
b) A document that contains only numeric values<br />
c) A document that includes fields for product name, price, and an array of specifications with mixed data types<br />
d) A document that has no fields at all  </p>
<p><strong>Answer:</strong> c) A document that includes fields for product name, price, and an array of specifications with mixed data types</p>
<hr />
<p><strong>Question 2:</strong> Given the following code snippet, which of the following statements is true regarding the <code>specifications</code> field?</p>
<p><code>json
{
  "productName": "Smartphone",
  "price": 699,
  "specifications": [
    "Color: Black",
    200,
    {
      "dimensions": {
        "height": 6.1,
        "width": 2.8,
        "depth": 0.3
      }
    }
  ]
}</code></p>
<p>a) The <code>specifications</code> field can only contain strings.<br />
b) The <code>specifications</code> field can only contain numeric values.<br />
c) The <code>specifications</code> field can contain strings, numbers, and nested objects.<br />
d) The <code>specifications</code> field must be empty.  </p>
<p><strong>Answer:</strong> c) The <code>specifications</code> field can contain strings, numbers, and nested objects.</p>
<hr />
<p><strong>Question 3:</strong> What is a potential challenge when handling a document with an array that contains different data types?</p>
<p>a) It is easy to process since all data types are the same.<br />
b) It can lead to type errors when trying to access or manipulate the data.<br />
c) It simplifies the database structure.<br />
d) It guarantees that all data will be valid.  </p>
<p><strong>Answer:</strong> b) It can lead to type errors when trying to access or manipulate the data.</p>
<hr />
<p><strong>Question 4:</strong> If a security rule is applied to restrict access to the <code>specifications</code> field of a product document, which of the following would be a valid rule?</p>
<p>a) Allow read access to all fields in the document.<br />
b) Deny access to the <code>specifications</code> field for all users.<br />
c) Allow read access to the <code>specifications</code> field only if the user is an admin.<br />
d) Allow write access to the <code>specifications</code> field for any user.  </p>
<p><strong>Answer:</strong> c) Allow read access to the <code>specifications</code> field only if the user is an admin.</p>
<hr />
<h1>Cloud Firestore</h1>
<h2>Questions</h2>
<p>Question 1: In a Cloud Firestore database, what is the primary structure used to store data?<br />
a) Table<br />
b) Collection<br />
c) Row<br />
d) Document<br />
<strong>Answer:</strong> b) Collection  </p>
<p>Question 2: Given the following document structure in a Firestore collection named '/users', which of the following is a valid way to access the 'age' of '/user1'?<br />
<code>javascript
const userRef = firestore.collection('users').doc('user1');
const userData = await userRef.get();</code><br />
a) userData.age<br />
b) userData.data().age<br />
c) userData['age']<br />
d) userData.get('age')<br />
<strong>Answer:</strong> b) userData.data().age  </p>
<p>Question 3: If you want to add a new user document to the '/users' collection with the name 'Charlie' and age 28, which of the following code snippets is correct?<br />
a)<br />
<code>javascript
firestore.collection('users').add({name: 'Charlie', age: 28});</code><br />
b)<br />
<code>javascript
firestore.collection('users').doc('Charlie').set({age: 28});</code><br />
c)<br />
<code>javascript
firestore.collection('users').insert({name: 'Charlie', age: 28});</code><br />
d)<br />
<code>javascript
firestore.collection('users').create({name: 'Charlie', age: 28});</code><br />
<strong>Answer:</strong> a)<br />
<code>javascript
firestore.collection('users').add({name: 'Charlie', age: 28});</code>  </p>
<p>Question 4: What is the purpose of a document in a Cloud Firestore collection?<br />
a) To store metadata about the collection<br />
b) To represent a single record with fields and values<br />
c) To define the structure of the collection<br />
d) To manage user permissions<br />
<strong>Answer:</strong> b) To represent a single record with fields and values  </p>
<p>Question 5: If you want to retrieve all documents from the '/users' collection, which of the following code snippets would you use?<br />
a)<br />
<code>javascript
const users = await firestore.collection('users').get();</code><br />
b)<br />
<code>javascript
const users = firestore.collection('users').all();</code><br />
c)<br />
<code>javascript
const users = firestore.collection('users').fetch();</code><br />
d)<br />
<code>javascript
const users = firestore.collection('users').retrieve();</code><br />
<strong>Answer:</strong> a)<br />
<code>javascript
const users = await firestore.collection('users').get();</code>  </p>
<hr />
<h1>Demonstration</h1>
<h2>Questions</h2>
<p><strong>Question 1:</strong> What is a potential issue when dealing with inconsistent document structures in a data collection?<br />
a) Increased performance<br />
b) Simplified querying<br />
c) Complications in querying<br />
d) Uniform data handling<br />
<strong>Answer:</strong> c) Complications in querying  </p>
<p><strong>Question 2:</strong> Given the following two documents in a collection, which of the following statements is true?<br />
Document 1: {'name': 'Alice', 'age': 30}<br />
Document 2: {'username': 'Bob', 'birth_year': 1995}<br />
a) Both documents can be queried using the same field names.<br />
b) Both documents have the same structure.<br />
c) Different documents may require different handling due to their varying structures.<br />
d) The documents are guaranteed to return the same results in queries.<br />
<strong>Answer:</strong> c) Different documents may require different handling due to their varying structures.  </p>
<p><strong>Question 3:</strong> If you want to query the age of 'Alice' from the first document, which of the following queries would be correct?<br />
a) <code>db.collection.find({ 'username': 'Alice' })</code><br />
b) <code>db.collection.find({ 'name': 'Alice' }, { 'age': 1 })</code><br />
c) <code>db.collection.find({ 'birth_year': 30 })</code><br />
d) <code>db.collection.find({ 'name': 'Alice' }, { 'username': 1 })</code><br />
<strong>Answer:</strong> b) <code>db.collection.find({ 'name': 'Alice' }, { 'age': 1 })</code>  </p>
<p><strong>Question 4:</strong> In a scenario where you have inconsistent document structures, which of the following strategies could help manage the complexity?<br />
a) Use a single field for all data types.<br />
b) Implement a schema validation to enforce consistency.<br />
c) Ignore the inconsistencies and query as usual.<br />
d) Only store documents with the same structure.<br />
<strong>Answer:</strong> b) Implement a schema validation to enforce consistency.  </p>
<p><strong>Question 5:</strong> If you encounter a document with a field that is not present in other documents, what is the best approach to handle it in your application?<br />
a) Assume all documents will have the same fields.<br />
b) Write code that checks for the existence of the field before accessing it.<br />
c) Remove the document from the collection.<br />
d) Always return a default value for missing fields.<br />
<strong>Answer:</strong> b) Write code that checks for the existence of the field before accessing it.  </p>
<hr />
<h1>Firebase Authentication</h1>
<h2>Questions</h2>
<h3>Questions on Firebase Authentication</h3>
<p><strong>Question 1:</strong> What is the primary purpose of Firebase Authentication?<br />
a) To store user data<br />
b) To authenticate users and manage user sessions<br />
c) To provide real-time database capabilities<br />
d) To host web applications<br />
<strong>Answer:</strong> b) To authenticate users and manage user sessions</p>
<hr />
<p><strong>Question 2:</strong> Which of the following methods can be used for user authentication in Firebase?<br />
a) Email and password<br />
b) Phone number<br />
c) Social media accounts (Google, Facebook, etc.)<br />
d) All of the above<br />
<strong>Answer:</strong> d) All of the above</p>
<hr />
<p><strong>Question 3:</strong> In a Firebase application, which of the following code snippets correctly initializes Firebase Authentication?<br />
<code>javascript
firebase.initializeApp({
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
});</code>
a) This code initializes Firebase Authentication correctly.<br />
b) This code is missing the database URL.<br />
c) This code initializes Firebase Firestore, not Authentication.<br />
d) This code is incorrect because it lacks the project ID.<br />
<strong>Answer:</strong> a) This code initializes Firebase Authentication correctly.</p>
<hr />
<p><strong>Question 4:</strong> When a user signs in with their email and password using Firebase Authentication, which method is used?<br />
a) firebase.auth().signInWithEmail()<br />
b) firebase.auth().signInWithEmailAndPassword()<br />
c) firebase.auth().loginWithEmailAndPassword()<br />
d) firebase.auth().authenticateUser()<br />
<strong>Answer:</strong> b) firebase.auth().signInWithEmailAndPassword()</p>
<hr />
<p><strong>Question 5:</strong> What happens when a user updates their profile picture in a mobile application using Cloud Firestore?<br />
a) The change is only reflected on the user's device.<br />
b) The change is reflected across all devices in real-time.<br />
c) The user must refresh the app to see the change.<br />
d) The change is stored in local storage only.<br />
<strong>Answer:</strong> b) The change is reflected across all devices in real-time.</p>
<hr />
<p><strong>Question 6:</strong> Which Firebase feature allows you to manage user sessions and keep users logged in across app restarts?<br />
a) Firebase Realtime Database<br />
b) Firebase Cloud Functions<br />
c) Firebase Authentication<br />
d) Firebase Hosting<br />
<strong>Answer:</strong> c) Firebase Authentication</p>
<hr />
<p><strong>Question 7:</strong> In Firebase Authentication, which of the following is NOT a valid way to sign out a user?<br />
a) firebase.auth().signOut()<br />
b) firebase.auth().logout()<br />
c) firebase.auth().signOut()<br />
d) firebase.auth().currentUser = null;<br />
<strong>Answer:</strong> b) firebase.auth().logout()</p>
<hr />
<p><strong>Question 8:</strong> If a user wants to reset their password using Firebase Authentication, which method should be used?<br />
a) firebase.auth().resetPassword()<br />
b) firebase.auth().sendPasswordResetEmail()<br />
c) firebase.auth().changePassword()<br />
d) firebase.auth().updatePassword()<br />
<strong>Answer:</strong> b) firebase.auth().sendPasswordResetEmail()</p>
<hr />
<h1>Firebase Authentication</h1>
<h2>Questions</h2>
<h3>Questions on Firebase Authentication and Cloud Firestore</h3>
<p><strong>Question 1:</strong> What is the primary purpose of Firebase Authentication?<br />
a) To manage database transactions<br />
b) To authenticate users and manage user sessions<br />
c) To store product inventory<br />
d) To handle payment processing<br />
<strong>Answer:</strong> b) To authenticate users and manage user sessions</p>
<hr />
<p><strong>Question 2:</strong> In the context of an e-commerce application, what is a potential issue when multiple users attempt to purchase the same item simultaneously?<br />
a) Increased loading time<br />
b) Overselling of products<br />
c) User interface glitches<br />
d) Slow authentication process<br />
<strong>Answer:</strong> b) Overselling of products</p>
<hr />
<p><strong>Question 3:</strong> Which Firebase feature can be used to ensure that inventory counts are updated correctly when multiple users are purchasing the same item?<br />
a) Cloud Functions<br />
b) Firestore Transactions<br />
c) Firebase Hosting<br />
d) Firebase Storage<br />
<strong>Answer:</strong> b) Firestore Transactions</p>
<hr />
<p><strong>Question 4:</strong> Given the following code snippet, what will happen if two users execute this transaction at the same time?</p>
<p>```javascript
const db = firebase.firestore();
const itemRef = db.collection('products').doc('item123');</p>
<p>db.runTransaction(async (transaction) =&gt; {
    const doc = await transaction.get(itemRef);
    if (!doc.exists) {
        throw "Document does not exist!";
    }
    const newQuantity = doc.data().quantity - 1;
    transaction.update(itemRef, { quantity: newQuantity });
});
```</p>
<p>a) Both transactions will succeed, and the quantity will be decremented twice.<br />
b) One transaction will succeed, and the other will fail due to a document not existing.<br />
c) Both transactions will fail due to a race condition.<br />
d) One transaction will succeed, and the other will be retried automatically.<br />
<strong>Answer:</strong> d) One transaction will succeed, and the other will be retried automatically.</p>
<hr />
<p><strong>Question 5:</strong> What is a race condition in the context of database transactions?<br />
a) A situation where multiple transactions are executed in parallel without any issues.<br />
b) A scenario where two or more transactions interfere with each other, leading to inconsistent data.<br />
c) A method to speed up database queries.<br />
d) A technique to optimize user authentication.<br />
<strong>Answer:</strong> b) A scenario where two or more transactions interfere with each other, leading to inconsistent data.</p>
<hr />
<h1>Features of Firebase Authentication</h1>
<h2>Questions</h2>
<h3>Questions on Features of Firebase Authentication</h3>
<p><strong>Question 1:</strong> What is the primary purpose of Firebase Authentication?<br />
a) To store user data<br />
b) To manage user authentication and authorization<br />
c) To create real-time databases<br />
d) To host web applications<br />
<strong>Answer:</strong> b) To manage user authentication and authorization</p>
<hr />
<p><strong>Question 2:</strong> In Firebase Authentication, which of the following methods can be used to sign in a user?<br />
a) Email and password<br />
b) Phone number<br />
c) Social media accounts (like Google, Facebook)<br />
d) All of the above<br />
<strong>Answer:</strong> d) All of the above</p>
<hr />
<p><strong>Question 3:</strong> When adding a new user with Firebase Authentication, which of the following code snippets correctly creates a user with email and password?<br />
<code>javascript
firebase.auth().createUserWithEmailAndPassword(email, password)</code>
a) <code>firebase.auth().addUser(email, password)</code><br />
b) <code>firebase.auth().registerUser(email, password)</code><br />
c) <code>firebase.auth().createUserWithEmailAndPassword(email, password)</code><br />
d) <code>firebase.auth().newUser(email, password)</code><br />
<strong>Answer:</strong> c) <code>firebase.auth().createUserWithEmailAndPassword(email, password)</code></p>
<hr />
<p><strong>Question 4:</strong> What happens if you try to create a user with an email that already exists in Firebase Authentication?<br />
a) The user is created with a new ID<br />
b) An error is thrown indicating the email is already in use<br />
c) The existing user is updated with new information<br />
d) The operation is ignored silently<br />
<strong>Answer:</strong> b) An error is thrown indicating the email is already in use</p>
<hr />
<p><strong>Question 5:</strong> If you attempt to add a user with a password that is too short, what will Firebase Authentication do?<br />
a) Accept the password anyway<br />
b) Automatically generate a stronger password<br />
c) Throw an error indicating the password is too weak<br />
d) Prompt the user to enter a new password<br />
<strong>Answer:</strong> c) Throw an error indicating the password is too weak</p>
<hr />
<p><strong>Question 6:</strong> In the context of Firebase Authentication, which of the following is NOT a valid way to sign out a user?<br />
a) <code>firebase.auth().signOut()</code><br />
b) <code>firebase.auth().logout()</code><br />
c) <code>firebase.auth().signOut()</code><br />
d) <code>firebase.auth().disconnect()</code><br />
<strong>Answer:</strong> b) <code>firebase.auth().logout()</code></p>
<hr />
<p><strong>Question 7:</strong> When using Firebase Authentication, which of the following is a common way to handle user state changes?<br />
a) Using <code>onAuthStateChanged</code> listener<br />
b) Using <code>getCurrentUser</code> method<br />
c) Using <code>checkUserStatus</code> function<br />
d) Using <code>isUserLoggedIn</code> variable<br />
<strong>Answer:</strong> a) Using <code>onAuthStateChanged</code> listener</p>
<hr />
<p><strong>Question 8:</strong> If you try to use a reserved field name like 'id' when creating a user document in Firestore, what is the potential issue?<br />
a) The document will not be created<br />
b) The document will be created, but querying may lead to conflicts<br />
c) The document will be created with a different field name<br />
d) There are no issues with using reserved field names<br />
<strong>Answer:</strong> b) The document will be created, but querying may lead to conflicts</p>
<hr />
<p>These questions cover various aspects of Firebase Authentication, including its features, methods, and potential pitfalls when working with user data.</p>
<hr />
<h1>Use cases of Firebase Authentication</h1>
<h2>Questions</h2>
<h3>Question 1:</h3>
<p>What is the purpose of the <code>addUser</code> function in the provided code snippet?
a) To retrieve user data from Firestore<br />
b) To add a user document to Firestore<br />
c) To delete a user document from Firestore<br />
d) To update a user document in Firestore<br />
<strong>Answer:</strong> b) To add a user document to Firestore</p>
<h3>Question 2:</h3>
<p>In the tricky example, what will happen if the <code>addUser</code> function is called with the arguments <code>addUser('Jane Doe', -5)</code>?
a) The user will be added successfully<br />
b) An error will be logged stating "Invalid input types"<br />
c) An error will be logged stating "Age cannot be negative"<br />
d) The function will return without any output<br />
<strong>Answer:</strong> c) An error will be logged stating "Age cannot be negative"</p>
<h3>Question 3:</h3>
<p>Which of the following statements is true about the validation checks in the tricky example?
a) The function only checks if the name is a string<br />
b) The function checks if the age is a positive number<br />
c) The function does not perform any validation<br />
d) The function checks if the name is a number<br />
<strong>Answer:</strong> b) The function checks if the age is a positive number</p>
<h3>Question 4:</h3>
<p>What will be logged to the console if the <code>addUser</code> function is called with valid inputs, such as <code>addUser('John Doe', 30)</code>?
a) User added successfully<br />
b) Error adding user: [error message]<br />
c) Invalid input types<br />
d) Age cannot be negative<br />
<strong>Answer:</strong> a) User added successfully</p>
<h3>Question 5:</h3>
<p>In the context of Firebase Authentication, which of the following is a common use case?
a) Storing user preferences<br />
b) Authenticating users to access secure resources<br />
c) Displaying user profiles<br />
d) Sending notifications to users<br />
<strong>Answer:</strong> b) Authenticating users to access secure resources</p>
<hr />