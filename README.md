Booklist is an API built with Django REST Framework.  It will allow the user to maintain a list of books that they have read, are wanting to read, or are in the process of reading.

Djoser is used to allow users to register and authenticate.

Users only have access to their own Booklist

All books will have a title, zero or more authors, and a status ("to read," "read," or "reading").

Users can update and delete their books, including changing the status.

Users can access their books in a complete list, or sorted by status.

Users can also add notes to books.  Notes will have a datetime and will include the body of the note and an optional page number for reference.
