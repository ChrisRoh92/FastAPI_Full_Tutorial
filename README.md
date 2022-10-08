# FastAPI_Full_Tutorial

## **Summary**

**German/Deutsch** 

Hallo und Herzlich Willkommen zu Branch 3 **end_points_with_authentification**. Seit dem letzten Branch haben wir die notwendingen Methoden und Objekte erstellt, mit denen wir den Zugriff auf bestimmte Endpunkte beschränknen können. Wir haben das erste mal mit *Dependency Injection* gearbeitet und damit den Methoden den Token bereitzustellen, sofern dieser bei der Anfrage überhaupt mitgegeben wurde. Was aktuell fehlt, ist das tatsächliche Erstellen von Token mit User Daten. Hierzu müssen wir bis zum nächsten Branch 4 uns mit der Erstellung von einer Datenbank, der Modellierung dieser und der Bereitstellung in den End Punkten kümmern.

**English**

Hello and welcome to Branch 3 **end_points_with_authentification**. Since the last branch we have created the necessary methods and objects to restrict access to certain endpoints. We have worked with *Dependency Injection* for the first time, providing the token to the methods if it was provided at all during the request. What is currently missing is the actual creation of tokens with user data. For this we have to take care of the creation of a database, the modeling of this and the provision in the end points until the next Branch 4.

## **Tasks**

**German/Deutsch** 

Wie im Video bereits angesprochen, soll die Software in diesem Projekt, als Bibliotheks Verwaltungssoftware genutzt werden. Das Bedeutet, dass wir natürlich eine Datenbank anlegen müssen, in dem wir sowohl neue Nutzer, Bücher und Ausleihvorgänge bzw. Reservierungen speichern müssen. Dabei kann jedem Buch ein Reservierungsvorgang, in diesem Beispiel Booking genannt, zugeordnet werden. Wir müssen also in einer Reservierung eine Referenz auf das Buch und auf den Nutzer, der es gebucht hat halten. Nebem dem Anlegen der SQL Tabellen werden bis zum nächsten Branch auch die Methoden zur Interaktion mit der Datenbank, den dazugehörigen Eingabedaten Strukturen und dem Anlegen der Datenbank selbst Aufgabe sein. In den Folgenden Schritten, werden die einzelnen Task wie immer aufgelistet. Viel Spaß!

- **[ ] Erstelle einen neuen Ordner in *src* mit dem Namen *database* und erstelle folgende Dateien in diesem Ordner:**
    - crud.py
    - database.py
    - models.py
    - schemas.py

- **[ ] Implementiere alle notwendigen Schritte für das Betreiben einer Datenbank mit SQLAlchemy in *database.py***
    - Erstelle eine Variable *SQLALCHEMY_DAZABASE_URL* in der du die Adresse zur Datenbank angibst
    - Erstelle ein Objekt mit der Methode *create_engine*
    - Erstelle eine neues *Session* Objekt mit der Methode *sessionmaker* in der du das erstellte engine Objekt nutzt
    - Erstelle mit *declarative_base()* ein Objekt mit dem Namen *Base*, von dem die Klassen zur Definition einer Datenbank Tabelle erben 
    - Erstelle eine Funktion *get_db()* die wir später in den Endpunkten als Depedency Injection nutzen werden

- **[ ] Implementiere drei Klassen in models.py zur Definition von den Datenbank Tabellen**
    - Erstelle eine Klasse für User mit folgenden Feldern
        - 'id' von Typ Integer, als *primary_key*
        - 'email' von Typ String, der nur einmal vorkommen darf
        - 'hashed_password' von Typ String
        - 'is_employee' von Typ Boolean (optional)
        - 'bookings' als *relationship* zur Klasse *Bookings*

    - Erstelle eine Klasse für Bücher mit folgenden Feldern
        - 'id' von Typ Integer, als *primary_key*
        - 'isbn' von Typ String, der nur einmal vorkommen darf
        - 'title' von Typ String
        - 'author' von Typ String
        - 'bookings' als *relationship* zur Klasse *Bookings*
    
    - Erstelle eine Klasse für Bookings mit folgenden Feldern
        - 'id' von Typ Integer, als *primary_key*
        - 'from_timestamp' vom Typ Integer
        - 'to_timestamp' vom Typ Integer
        - 'description' vom Typ String (Optional)

        - 'book_id' als *ForeignKey* von einem Buch
        - 'booked_book' als *relationship* zur Klasse Book
        
        - 'user_id' als *ForeignKey* von einem User
        - 'user' als *relationship* zur Klasse User

- **[ ] Erstelle *Schemas* für die Bedienung der verschiedenen Schnittstelle in *schemas.py***
    
    - Erstelle eine Klasse *UserBaseSchema* das von *BaseModel* erbt und die Felder 'email' vom Typ *EmailStr* und 'password' vom Typ *str* enthält
    
    - Erstelle eine Klasse *UserLoginSchema* das von *UserBaseSchema* erbt. Das ist optional, da wir keine extra Felder brauchen.
    
    - Erstelle eine Klasse *UserRegisterSchema* das von *UserBaseSchema* erbt. Hier wird zusätzlich das Feld 'fullname' vom Typ *str* benötigt. Zusätzlich kannst du darin eine Klasse 'Config' erstellen in der du ein Dictionary mit dem namen 'schemas'extra' erstellt, das beim Testen der Schnittstelle in der Swagger Doku bereits Musterdaten als Eingabe anbietet. Das kann wie folgt aussehen:
    ```python
    class Config:
        schema_extra = {
            "user" : {
                "fullname": "Max Mustermann",
                "email": "Max@Mustermann.de",
                "password": "password
            }
        }
    ```
    - Erstelle eine Klasse *BookingBaseSchema* das von *BaseModel* erbt und die die Felder 'isbn', 'description' vom Typ *str* und die Felder 'from_date' und 'to_date' vom Typ *datetime.date* enthält. Importiere hierzu *datetime*

    - Erstelle eine Klasse *BookBaseSchema* das von *BaseModel* erbt und die Felder 'isbn', 'title' und 'author' vom Typ *str* enthält. Überlebe dir auch hier, wie du eine Config Klasse mit einem Eingabevorschlag aussehen kann

    - Um nicht immer nur einzelne Bücher in die Datenbank laden zu können, sollen auch Listen von Büchern übergeben werden. Erstelle Hierzu eine Klasse *BookBaseListSchema* das von *BaseModel* erbt und ein Feld 'books' vom Typ *List[BookBaseSchema] = []* enthält. Überlege die auch hier, wie eine geschickte Config Klasse aussehen kann.

- **[ ] Erstelle alle notwendigen Methoden zur Interaktion mit der Datenbank in *crud.py***

    - Erstelle alle User spezifischen Methoden:
        - Rufe alle User ab
        - Erhalte einen User über die Email
        - Registriere neue User | Noch nicht Implementieren!
        - Update das Password von einem User | Noch nicht Implementieren!
        - Update die Email von einem User
        - Entferne einen User

    - Erstelle alle Bücher spezifischen Methoden:
        - Rufe alle Bücher ab
        - Rufe ein Buch über die ISBN ab
        - Rufe alle Bücher von einem Author ab
        - Entferne ein Buch über die ISBN
        - Erstelle ein neues Buch    


- **[ ] Verbinde die Endpunkte in *main.py* und rufe die in *crud.py* erstellten Methoden um mit der Datenbank zu interagieren**
    - Importiere dazu aus dem *database* ordner die wesentlichen Files

    - Füge der Parameter Liste der Endpunkt Methoden folgendes hinzu *db = Depends(get_db)* um Zugriff auf die Session und damit auf die Datenbank zu erhalten

    - Nutze die in *crud.py* implementierten Methoden in den Endpunkten

**English** 

As already mentioned in the video, the software in this project is to be used as library management software. This means, of course, that we have to create a database, in which we have to store new users, books and lending transactions or reservations. Each book can be assigned to a reservation, in this example called Booking. So we need to keep in a reservation a reference to the book and to the user who booked it. Besides creating the SQL tables, until the next branch, we will also have to create the methods for interacting with the database, the corresponding input data structures and the creation of the database itself. In the following steps, the individual tasks will be listed as usual. Have fun!

- **[ ] Create a new folder in *src* named *database* and create the following files in this folder:**
    - crud.py
    - database.py
    - models.py
    - schemas.py

- **[ ] Implement all necessary steps for running a database with SQLAlchemy in *database.py***.
    - create a variable *SQLALCHEMY_DAZABASE_URL* in which you specify the address to the database
    - Create an object with the *create_engine* method
    - Create a new *session* object with the method *sessionmaker* in which you use the created engine object
    - Create with *declarative_base()* an object with the name *base*, from which the classes for defining a database table inherit 
    - Create a function *get_db()* which we will use later in the endpoints as depedency injection

- **[ ] Implement three classes in models.py to define the database tables**.
    - Create a class for user with the following fields
        - 'id' of type integer, as *primary_key*.
        - 'email' of type string, which may occur only once
        - 'hashed_password' of type String
        - 'is_employee' of type Boolean (optional)
        - 'bookings' as *relationship* to class *Bookings*.

    - Create a class for books with the following fields
        - 'id' of type Integer, as *primary_key*.
        - 'isbn' of type String, which must occur only once
        - 'title' of type String
        - 'author' of type String
        - 'bookings' as *relationship* to class *Bookings*.
    
    - Create a class for bookings with the following fields
        - 'id' of type Integer, as *primary_key*.
        - 'from_timestamp' of type Integer
        - to_timestamp' of type integer
        - 'description' of type String (Optional)

        - 'book_id' as *ForeignKey* of a book
        - 'booked_book' as *relationship* to the class Book
        
        - 'user_id' as *ForeignKey* of a user
        - 'user' as *relationship* to the class User

- **[ ] Create *schemas* for the operation of the different interface in *schemas.py***.
    
    - Create a class *UserBaseSchema* that inherits from *BaseModel* and contains the fields 'email' of type *EmailStr* and 'password' of type *str*.
    
    - Create a class *UserLoginSchema* that inherits from *UserBaseSchema*. This is optional, since we don't need extra fields.
    
    - Create a class *UserRegisterSchema* that inherits from *UserBaseSchema*. Here you also need the field 'fullname' of type *str*. Additionally, you can create a class 'Config' in it in which you create a dictionary named 'schemas'extra' that already offers sample data as input when testing the interface in the Swagger doc. This can look like this:
    ```python
    class Config:
        schema_extra = {
            "user" : {
                "fullname": "maxampleman",
                "email": { "Max@Mustermann.de",
                "password" : { "password
            }
        }
    ```
    - Create a class *BookingBaseSchema* that inherits from *BaseModel* and contains the fields 'isbn', 'description' of type *str* and the fields 'from_date' and 'to_date' of type *datetime.date*. Import *datetime* for this purpose

    - Create a class *BookBaseSchema* that inherits from *BaseModel* and contains the fields 'isbn', 'title' and 'author' of type *str*. See also here how you can create a config class with an input proposal

    - In order to be able to load not always only single books into the database, also lists of books are to be transferred. Create a class *BookBaseListSchema* that inherits from *BaseModel* and contains a field 'books' of type *List[BookBaseSchema] = []*. Think about what a clever config class could look like here as well.

- **[ ] Create all necessary methods to interact with the database in *crud.py***.

    - Create all user specific methods:
        - Retrieve all users
        - Get a user via email
        - Register new users | Do not implement yet!
        - Update the password of a user | Not yet implemented!
        - Update the email of a user
        - Remove a user

    - Create all books specific methods:
        - Retrieve all books
        - Retrieve a book by ISBN
        - Retrieve all books from an author
        - Remove a book by ISBN
        - Create a new book    


- **[ ] Connect the endpoints in *main.py* and call the methods created in *crud.py* to interact with the database**.
    - import the essential files from the *database* folder

    - Add the following to the parameter list of the endpoint methods *db = Depends(get_db)* to get access to the session and thus to the database

    - Use the methods implemented in *crud.py* in the endpoints