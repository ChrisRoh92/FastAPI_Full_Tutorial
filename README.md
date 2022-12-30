# FastAPI_Full_Tutorial

## **Summary**

**German/Deutsch**

Hallo und Herzlich Willkommen zu Branch 4 *database_with_sqlalchemy*. Seit dem letzten Branch, haben wir alle notwendigen Implementierungen durchgeführt um eine Datenbank mit dem *SQLAlchemy* Package zu erstellen. Wie bereits in der Einführung zu diesem Projekt erwähnt, soll in diesem Tutorial eine einfache Bibliotheksverwaltung geschrieben werden, in der es Nutzer, Bücher und Reservierungen, oder auch Bookings gibt. Für jedes dieser drei Elemente wurde ein Model bzw. eine Tabellenstruktur erstellt. Außerdem wurden die ersten CRUD (https://de.wikipedia.org/wiki/CRUD) Methoden zur Interaktion mit der Datenbank erstellt und die zum Zugriff auf die Datenbank notwendigen Methoden für die 'Dependency Injection' erstellt. Außerdem wurden so genannte 'schemas' erstellt, die als Eingabestruktur für die Endpunkte dienen. Diese müssen beim Abrufen der jeweiligen Endpunkte zur Verfügung gestellt werden, damit der jeweilige Endpunkt die Anfrage auch akzeptiert. Was wir in zwischen diesem und dem nächsten Branch zu tun haben, erfährst du in der unteren Sektion. Ich wünsche dir, wie immer, viel Spaß bei diesem Tutorial und freue mich immer über Vorschläge und Kommentare :)

**English**

Hello and welcome to Branch 4 *database_with_sqlalchemy*. Since the last branch, we have done all the necessary implementations to create a database with the *SQLAlchemy* package. As already mentioned in the introduction to this project, in this tutorial we want to write a simple library management where there are users, books and reservations, or bookings. For each of these three elements a model or table structure was created. In addition, the first CRUD (https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) methods for interaction with the database were created and the methods necessary to access the database for 'Dependency Injection' were created. So-called 'schemas' were also created, which serve as the input structure for the endpoints. These must be provided when the respective endpoints are retrieved, so that the respective endpoint also accepts the request. You can find out what we have to do in between this and the next branch in the section below. As always, I hope you enjoy this tutorial and I'm always happy to receive suggestions and comments :)

## Task for this Branch

**German/Deutsch**

Bis zum nächsten Branch ist es deine Aufgabe, Methoden bereitzustellen, mit denen man aus einem Klartext, das dem vom User übermittelten Passwort sein wird, ein gehashted, also nicht wieder auf die originale Eingabe zurückzuführenden Text, zu machen. Daneben wird eine Methode benötigt, die überprüft, ob ein Klartext Passwort, mit dem später in der Datenbank gehashten Password übereinstimmt oder nicht.

Mit diesen neuen Methoden können wir dann auch die fehlenden Methoden in der *crud.py*, als auch in *main.py* implementieren, da wir nun in der Lage sind, die Passwörter der User sicher zu speichern. Nachfolgend habe ich dir erneut eine Liste mit den zu erledigenden Aufgaben erstellt. Ich empfehle dir jedoch stark, das YT Video von mir nebenher zu gucken. Viel Spaß damit :)

- **[ ] Erstelle ein neues File im *auth* Ordner mit dem Namen *password_handler.py***
    - Importiere von *passlib.context* den *CryptoContext*
    - Erstelle ein Objekt vom Typ *CryptoContext* und den namen *pwd_context* und übergebe foldene Argumente an:
        - 'schemes=["bcrypt"]'
        - 'deprecated="auto"'
    - Erstelle die folgenden zwei Methoden:
        - *verifiy_password*, die zwei Strings als Parameter besitzt
        - *get_password_hash*, die einen String für das Passwort als Klartext als Parameter besitzt
    - Um ein ein Klartext Passwort in Hash String zu verwandeln, musst du vom Objekt *pwd_context* die Methode *hash(...)* mit dem übergebenen Klartext aufrufen. Diese Methode gibt dir dann das aus dem Passwort erstellt Hash zurück, das du anschließend als Rückgabewert definierst
    - Um zu prüfen, ob ein Klartext Passwort mit dem Hash des Passworts übereinstimmt, musst du vom Objekt *pwd_context* die Methode *verifiy(...)* aufrufen und dabei zuerst das Passwort als Klartext und anschließend das Password als Hash übergeben. Die Methode gibt dann ein Bool zurück, das ebenfalls als Rückgabewert für diese Methode dienen soll

- **[ ] Vervollständigen der Methoden in crud.py**
    - Erstelle eine Methode, in der geprüft wird, ob ein Nutzer bereits registriert ist.
    - Erstelle eine Methode, in der ein User mit seiner Email und seinem Password authentifiziert wird. Gebe je nachdem entweder *True* oder *False* zurück.
    - Erweitere die Methode *register_new_user*:
        - Die Vorprüfung soll in den Endpunkten stattfinden (z.B. ob die übergebene Email-Adresse bereits registriert ist)
        - Generiere mit *get_password_hash* ein Hash aus dem übergebenen Passwort
        - Erstelle ein Objekt *db_user* vom Typ *User*, und übergebe die Daten für die *Email-Adresse* und dem *Password Hash*
        - Füge dieses Objekt der Datenbank hinzu und gebe es auch wieder als Funktionsrückgabe Wert an
    - Erweitere die Methode *update_password*:
        - Erstelle dir aus dem neuem Passwort, der als Klartext übergeben wird, ein Hash mit der Methode *get_password_hash*
        - Aktualisiere das Feld *hashed_password* von dem übergebenen User Objekt *db_user*
        - Füge das aktualisierte *User* Objekt der Datenbank hinzu und nutze dieses Objekt ebenfalls als Funktionsrückgabe Wert
    - Erweitere die Methode *remove_current_user*
        - Da wir den Nutzer wirklich nur dann entfernen möchten, wenn wir uns das per erneuter Passwort Eingabe bestätigen lassen, implementierst du diese Methode erst jetzt.
        - Nutze folgende Anweisung um das übergebene *User* Objekt aus der Datenbank zu entfernen: *db.query(User).filter_by(id = db_user.id).delete()*
        - Speichere dir den Rückgabewert der Lösch-Operation in einer lokalen Variable. Sofern die Löschung erfolgreich war, wird in dieser Variable True stehen. Nur wenn das der Fall ist, möchten wir diese Operationen commiten und True zurückgeben, andernfalls geben wir False zurück

    - **[ ] Vervollständigen die User spezifischen Endpunkte in main.py**
        - Nutze die Methode *get_user_by_email* aus *crud.py* um im Endpunkt den User über die Email zurückzugeben. Achte dabei darauf, dass im Falle, dass ein User nicht existiert, eine *HTTPException* geworfen wird
        - Implementiere den Endpunkt zur Registrierung von einem Nutzer *register_user*:
            - Prüfe zunächst, ob die übergebene Email Adresse bereits registriert ist. Sollte das der Fall sein, werfe eine *HTTPExcetion*
            - Sofern das nicht der Fall ist, übergebe das übermittelte *UserRegisterSchema* und die Datenbank Session der Methode *register_new_user* in *crud.py* um einen neuen User zu erstellen. 
            - Damit der User direkt nach der Registrierung Zugriff auf die geschützten Methoden hat, soll hier nun auch direkt ein Token aus der Email-Adresse des neuen Users erstellt und zurückgegeben werden.
            - Erstelle dir hierzu zunächst eine lokale Variable *access_token_expires* das ein *timedelta* mit dem Wert der Konstante *ACCESS_TOKEN_EXPIRE_MINUTES* erstellt.
            - Erstelle anschließend ein Token mit der Methode *create_access_token*, bei dem für den Parameter *data* ein Dictionary mit dem Schlüssel "email" und der User Email-Adresse als Wert übergeben wird. Außerdem wird das *access_token_expires* für den Parameter *expires_delta* der gleichen Methode übergeben.
            - Gebe anschließend folgendes Dictionary als Rückgabe Wert für diesen Endpunkt zurück:
                ```python
                return {"access_token": token, "token_type":"bearer"} 
                ``` 
        - Implementiere den Endpunkt zum Login von einem User *login_user*
            - Als Übergabeparameter wird Nachfolgendes benötigt:
                - *form_data* vom Typ *OAuth2PasswordRequestForm*, das du von *fastapi.security* ggfs. noch importieren musst
                - Eine Datenbank Session *db* als Dependency Injection von *get_db*
            - Prüfe mit der Methode *authenticate_user* aus *crud.py*, ob die Eingaben aus *form_data* stimmen. Nutze Dazu die Felder *username* für die Email-Adresse und *password* für das Passwort
            - Sofern der User sich mit den Eingaben authentifizieren konnte, erstellst du, ähnlich wie in *register_user* ein Token. 
        - Implementiere die Methode zum Aktualisieren von der Email-Adresse *update_email*
            - Extrahiere aus dem übergebenen Token die Email-Adresse
            - Gebe dir für die Email Adresse das zugehörige User Objekt mit der Methode *get_user_by_mail* aus der *crud.py*
            - Sofern es diesen User gibt, rufe die Methode zum Aktualisieren der Email-Adresse aus der *crud.py* auf
            - Sofern es den User nicht gibt, werfe eine *HTTPException*
        - Implementiere die Methode zum Aktualisieren des User Passwords *update_password*
            - Führe die Schritte zum Ändern des Passwords, analog zu den Schritten beim Ändern der Email-Adresse, durch.
        - Implementiere die Methode zum Löschen des aktuellen Nutzers' *delete_current_user*
            - Prüfe im Vorfeld, ob das übergebene Passwort zu dem User gehört. Extrahiere hierfür davor die Email-Adresse aus dem übergebenen Token
            - Sofern sich der User authentifizieren konnte, rufe das User Objekt mit der übergebenen Email-Adresse auf und prüfe zur Sicherheit nochmal, ob dieser User auch existiert. 
            - Sofern der User existiert, rufe die in *crud.py* implementierte Methode *remove_current_user* auf, um den User aus der Datenbank zu entfernen.
            - Prüfe anhand des Rückgabewertes von *remove_current_user* ob das Entfernen des Users' erfolgreich war
            - Füge an allen Stellen eine Werfen von einer *HTTPException*, die dir sinnvoll erscheinen.

**English**

In this section it will be your task to provide methods to turn a plaintext password, which will be the password submitted by the user, into a hashed one, i.e. one that cannot be traced back to the original input. Besides, a method is needed to check whether a plaintext password matches the hashed password later in the database or not.

With these new methods, we can then implement the missing methods in *crud.py*, as well as in *main.py*, since we are now able to store the passwords of the users securely. Below, I have again provided you with a list of tasks to be done. Have fun with it :)

- **[ ] Create a new file in the *auth* folder with the name *password_handler.py***.
    - Import from *passlib.context* the *CryptoContext*.
    - Create an object of type *CryptoContext* and name *pwd_context* and pass the following arguments:
        - 'schemes=["bcrypt"]'
        - 'deprecated="auto"'
    - Create the following two methods:
        - *verifiy_password*, which has two strings as parameters
        - *get_password_hash*, which has one string for the password in plaintext as parameter
    - To convert a plaintext password into hash string, you have to call from object *pwd_context* the method *hash(...)* with the passed plaintext. This method will then return the hash created from the password, which you then define as a return value
    - To check if a plaintext password matches the hash of the password, you must call the *verifiy(...)* method from the *pwd_context* object, passing first the password as plaintext and then the password as hash. The method then returns a bool which should also serve as return value for this method

- **[ ] Completing the methods in crud.py**
    - Create a method that checks if a user is already registered.
    - Create a method in which a user is authenticated with his email and password. Return either *True* or *False* as appropriate.
    - Extend the method *register_new_user*:
        - The pre-check should take place in the endpoints (e.g. if the given email address is already registered).
        - Generate with *get_password_hash* a hash from the passed password
        - Create an object *db_user* of type *user*, and pass the data for the *email-address* and the *password hash
        - Add this object to the database and pass it again as function return value
    - Extend the method *update_password*:
        - Create a hash from the new password, which is passed as plaintext, with the method *get_password_hash
        - Update the field *hashed_password* from the passed user object *db_user*.
        - Add the updated *user* object to the database and use this object as function return value as well
    - Extend the method *remove_current_user*.
        - Since we really only want to remove the user if we have it confirmed by entering the password again, implement this method only now.
        - Use the following statement to remove the passed *user* object from the database: *db.query(User).filter_by(id = db_user.id).delete()*
        - Store the return value of the delete operation in a local variable. Provided the delete was successful, this variable will say True. Only if this is the case we want to commit these operations and return True, otherwise we return False

    - **[ ] Complete the user specific endpoints in main.py**.
        - Use the *get_user_by_email* method from *crud.py* to return the user by email in the endpoint. Make sure that in case a user does not exist, a *HTTPException* is thrown.
        - Implement the endpoint to register a user *register_user*:
            - First check if the given email address is already registered. If this is the case, throw a *HTTPExcetion*.
            - If not, pass the given *UserRegisterSchema* and the database session of the method *register_new_user* into *crud.py* to create a new user. 
            - So that the user has access to the protected methods directly after the registration, a token from the email address of the new user is to be created and returned here now also directly.
            - First create a local variable *access_token_expires* which creates a *timedelta* with the value of the constant *ACCESS_TOKEN_EXPIRE_MINUTES*.
            - Then create a token with the *create_access_token* method, passing for the *data* parameter a dictionary with the key "email" and the user email address as value. Also, pass the *access_token_expires* for the *expires_delta* parameter of the same method.
            - Then return the following dictionary as the return value for this endpoint:
                ```python
                return {"access_token": token, "token_type": "bearer"} 
                ``` 
        - Implement the endpoint to login from a user *login_user*.
            - The following is needed as a transfer parameter:
                - *form_data* of type *OAuth2PasswordRequestForm*, which you may have to import from *fastapi.security*.
                - A database session *db* as dependency injection of *get_db*
            - Check with the method *authenticate_user* from *crud.py* if the input from *form_data* is correct. Use the fields *username* for the email address and *password* for the password.
            - If the user could authenticate himself with the input, you create a token, similar to *register_user*. 
        - Implement the method to update the email address *update_email*.
            - Extract the email address from the passed token
            - Get the user object for the email address with the method *get_user_by_mail* from *crud.py
            - If this user exists, call the method to update the email address from *crud.py*.
            - If the user does not exist, throw a *HTTPException*.
        - Implement the method to update the user password *update_password*.
            - Perform the steps to change the password, analogous to the steps to change the email address.
        - Implement the method to delete the current user *delete_current_user*.
            - Check in advance if the given password belongs to the user. Extract the email address from the passed token beforehand.
            - If the user could authenticate, call the user object with the given email address and check again if this user exists. 
            - If the user exists, call the method *remove_current_user* implemented in *crud.py* to remove the user from the database.
            - Check the return value of *remove_current_user* to see if the user was removed successfully.
            - Add a throwing of a *HTTPException* at all places that seem to make sense to you.
