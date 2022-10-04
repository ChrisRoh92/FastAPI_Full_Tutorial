# FastAPI_Full_Tutorial

## **Summary**

**German/Deutsch** 

- Hallo und Herzlich Willkommen zu Branch 2 **End Point Creation**. Im Vergleich zum letzten Branch haben wir alle wichtigen Endpunkte in main.py definiert, ohne die dazugehörige Funktionalität zu implementieren. 

- Das Abrufen, Hinzufügen, Aktualisieren und Entfernen von Daten ist den jeweiligen Methoden enthalten:

> **GET** HTTP Methode *Read*
>
>``` python
>@app.get("/user_by_mail", tags=["user"])
>def get_user_by_mail():
>    pass
>```

> **POST** HTTP Methode *Create*
>
>``` python
>@app.post("/register", tags=["user"])
>def register_user():
>    pass
>```

> **PUT** HTTP Methode *Update/Modify*
>
>``` python
>@app.put("/user/change_email", tags=["user"])
>def update_email():
>    pass
>```

> **DELETE** HTTP Methode *Delete*
>
>``` python
>@app.delete("/user", tags=["user"])
>def delete_current_user():
>    pass
>```

- Auch wenn die Endpunkte noch keine Funktionalitäten besitzen, kannst du über das Start Skript (startOnLinux.sh / startOnWindows.cmd) über deinen Browser bereits einen Blick auf die APIs in der Swagger Dokumentation auf das Design der API Schnittstelle werfen

**English**

- Hello and welcome to Branch 2 **End Point Creation**. Compared to the last branch, we have defined all the important end points in main.py without implementing the associated functionality. 

- Retrieving, adding, updating and removing data is included in the respective methods:

> **GET** HTTP Methode *Read*
>
>``` python
>@app.get("/user_by_mail", tags=["user"])
>def get_user_by_mail():
>    pass
>```

> **POST** HTTP Methode *Create*
>
>``` python
>@app.post("/register", tags=["user"])
>def register_user():
>    pass
>```

> **PUT** HTTP Methode *Update/Modify*
>
>``` python
>@app.put("/user/change_email", tags=["user"])
>def update_email():
>    pass
>```

> **DELETE** HTTP Methode *Delete*
>
>``` python
>@app.delete("/user", tags=["user"])
>def delete_current_user():
>    pass
>```

- Even if the endpoints don't have any functionality yet, you can already take a look at the APIs in the Swagger documentation via the start script (startOnLinux.sh / startOnWindows.cmd) through your browser on the design of the API interface

## **Tasks**

**German/Deutsch** 

Bevor wir mit der Implementierung der End Punkte unserer Schnittstelle anfangen, möchte ich dir zunächst zeigen, wie man bestimmte End Punkte nur benutzen kann, wenn man ein Authentifizierungs Token mitgibt. Dazu nutze ich das OAuth2 Framework, das von FastAPI als Vorschlag zum Schutz von Schnittstellen genutzt wird. Die Anwendung ist an sich nicht schwer, erfordert allerdings, die nachfolgenden Aufgaben zu durchlaufen.

- **[ ] Erstelle einen neuen Ordner in *src* mit dem Namen *auth***

- **[ ] Erstelle in dem neuen Ordner ein neues Python File mit dem Namen *auth_handler.py*** 

- **[ ] Importiere *OAuth2PasswordBearer* von *fastapi.security*** 
    - Erstelle ein Objekt von *OAuth2PasswordBearer* und übergeben für das "tokenURL" Argument "login". 
    
    - Mit "login" sagen wir OAuth2PasswordBearer, in welchem Endpunkt ein Token erzeugt und zurückgegeben wird

- **[ ] Lege die folgenden drei Konstanten an**
    - Einen Secret Key (SECRET_KEY) Wie du diesen erzeugst, habe ich im Video vorgestellt.
    
    - ALGORITHM = "HS256"

    - Eine Konstante, die angibt, wann ein Token ungültig wird: *ACCESS_TOKEN_EXPIRE_MINUTES*

- **[ ] Erstelle die folgenden drei Methoden:**
    
    ``` python
    def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    ```

    ``` python
    def is_token_valid(token: str = Depends(oauth2_scheme)):
    ```

    ``` python
    def extract_email_from_token(token: str = Depends(oauth2_scheme)):
    ```
    

- **[ ] Implementiere die Methode zur Erstellung eines Tokens**

    - In 'data' wird in der Form eines Dictionary die Email, als auch die Zeit, wann das Token abläuft mitgegeben. Kopiere diese Daten in eine neue Variable *to_encode*.

    - Sofern zusätzlich noch ein 'expires_delta' hinzugefügt wurde, erstelle eine neue Variable 'expire' in welche du die aktuelle Zeit mit *datetime.utcnow()* plus dem übergebenen Wert erstellst.

    - Sofern kein *expires_delta* hinzugefügt wurde, erstelle trotzdem eine *expire* Variable in der du wieder die aktuelle Zeit plus dem *ACCESS_TOKEN_EXPIRE_MINUTES* mit *timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)* erstellst.

    - Füge *to_encode* ein neues Feld mit dem Namen "exp" und der Variable "expire" hinzu.

    - Erstelle anschließend mit folgendem Befehl den Zugriffs Token. Importiere hierfür *jwt* von *jose*

    ``` python
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    ```

    - Gebe zum Schluss *encoded_jwt* zurück

- **[ ] Implementiere die Methode zur Prüfung ob ein Token noch valide ist**

    - Erhalte mit 'jwt.decode' die *payload* die in dem übergebenen Token String steckt

    - Extrahiere aus der payload das Feld 'exp', das für die Expiration steht

    - Sofern du etwas zurückbekommen hast, prüfe ob der gespeicherte Zeitstempel kleiner als der aktuelle Zeitstempel ist und gebe dann *False* zurück

    - Wenn das nicht der Fall sein sollte, kannst du *True* zurückgeben

    - Bitte Kapsele diesen Vorgang mit einem *Try-Catch* Block

    - Sofern es eine Exception gibt, implementiere folgenden Code. Importiere hierfür bitte die HTTPException von fastapi

        ```python
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        ```

- **[ ] Implementiere die Methode, mit der sich die im Token enthaltene Email Adresse extrahieren lässt**

    - Ähnlich wie in der Methode zur Validierung des Tokens, kannst du in dieser Methode wieder die Payload aus dem übergebenen Token String extrahieren

    - Extrahiere dieses mal das Feld 'email' und weise den Inhalt einer Variable *email* zu

    - Prüfe ob email einen Wert enthält und falls nicht löse eine Exception mit dem status_code 404 aus und einer Aussagekräftigen Botschaft in *detail*

    - Sofern *email* aber einen Wert enthält, gebe diesen zurück

    - Wie *is_token_valid* kapsele diesen Code in einem *Try-catch* Block

- **[ ] Importiere in *main.py* die erstellten Methoden und das *oauth2_scheme***

- **[ ] Füge jedem Endpunkt, bis auf *login* und *register* die Dependency Injection hinzu**

- **[ ] Starte jetzt den Server mit dem für dein System geeignet StartSkript (Siehe Branch 01) und versuche die Endpunkte mit der Dependency Injection abzurufen**

- **[ ] In der Swagger Docu (127.0.0.1:8000/docs) befindet sich nun oben rechts ein *Login* Button, in dem sich eine Maske öffnet, in der du aktuell noch alles eintragen kannst was du möchtest, da dies noch nicht geprüft wird. Du erhälst nach dem Anmelden ein Token, der dich aktuell schon in die Lage versetzt, die "geschützten" Methoden zu benutzen.**

**English** 

Before we start implementing the end points of our interface, I first want to show you how to use certain end points only if you provide an authentication token. To do this, I use the OAuth2 framework, which is used by FastAPI as a proposal for protecting interfaces. The application is not difficult in itself, but requires to go through the following tasks.

- **[ ] Create a new folder in *src* with the name *auth***.

- **[ ] Create a new Python file in the new folder with the name *auth_handler.py***. 

- **[ ] Import *OAuth2PasswordBearer* from *fastapi.security*** 

    - Create an object of *OAuth2PasswordBearer* and pass for the "tokenURL" argument "login". 
    
    - With "login" we tell OAuth2PasswordBearer in which endpoint a token is generated and returned

- **[ ] Create the following three constants**.
    - A Secret Key (SECRET_KEY) How you create this, I presented in the video.
    
    - ALGORITHM = "HS256"

    - A constant that indicates when a token becomes invalid: *ACCESS_TOKEN_EXPIRE_MINUTES*.

- **[ ] Create the following three methods:**
    
    ``` python
    def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    ```

    ``` python
    def is_token_valid(token: str = Depends(oauth2_scheme)):
    ```

    ``` python
    def extract_email_from_token(token: str = Depends(oauth2_scheme)):
    ```

- **[ ] Implement the method to create a token**.

    - In 'data' the email and the time when the token expires is given in the form of a dictionary. Copy this data into a new variable *to_encode*.

    - If an 'expires_delta' was added, create a new variable 'expire' in which you create the current time with *datetime.utcnow()* plus the passed value.

    - If no *expires_delta* was added, create an *expire* variable in which you again create the current time plus the *ACCESS_TOKEN_EXPIRE_MINUTES* with *timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)*.

    - Add *to_encode* a new field with the name "exp" and the variable "expire".

    - Then create the access token with the following command. Import *jwt* from *jose* for this purpose.

    ``` python
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    ```

    - Return *encoded_jwt* at the end

- **[ ] Implement the method to check if a token is still valid**.

    - Get with 'jwt.decode' the *payload* which is in the passed token string

    - Extract the field 'exp' from the payload which stands for the expiration

    - If you got something back, check if the stored timestamp is smaller than the current timestamp and return *False*.

    - If this is not the case, you can return *True*.

    - Please encapsulate this process with a *Try-Catch* block

    - If there is an exception, implement the following code. Please import the HTTPException from fastapi

        ```python
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        ```

- **[ ] Implement the method to extract the email address contained in the token**.

    - Similar to the method for validating the token, you can extract the payload from the passed token string again in this method

    - This time extract the field 'email' and assign the content to a variable *email*.

    - Check if email contains a value and if not throw an exception with the status_code 404 and a meaningful message in *detail*.

    - But if *email* contains a value, return this value

    - As *is_token_valid* encapsulate this code in a *try-catch* block

- **[ ] Import in *main.py* the created methods and the *oauth2_scheme***.

- **[ ] Add dependency injection to every endpoint except *login* and *register***.

- **[ ] Now start the server with the StartScript suitable for your system (see Branch 01) and try to retrieve the endpoints with the Dependency Injection**.

- **[ ] In the Swagger Docu (127.0.0.1:8000/docs) there is a *Login* button in the upper right corner, in which a mask opens, where you can enter everything you want, because this is not checked yet. After logging in you will get a token, which enables you to use the "protected" methods.**



