## Storage V1
I am planning on making a simple web-based storage system.

Notes below were thoughts along the way.
  * To create a user-storage system, I would need an easy way to sort all of them instead of just putting them in one source folder.
  * I should create a two-layered folder system stored in a root directory. The first layer taking the first character of the username, and then the first two characters for the second layer.
  * I should now create metadata for each user. This system requires "user" to exist in the dictionary or else it won't work.
  * I should add a way to add other types of meta data dynamically.
  * When new meta data is added dynamically, we should update all the other users meta data.
  * I will sort the meta data alphabetically in a .txt file.
  * The password should be encrypted.
  * Now to create a sign-up system. I first need to check if the user already exists.
  * If not, then we need to take the user and password meta data, and the core metadata and store it into a file.
  * The filename is named after the username.
  * For the login, we need to check if the user does exist.
  * If so, check if password matches with metadata.
  * If password matches, login successful.
  * Now I should make a way to give username and password from client to server.


