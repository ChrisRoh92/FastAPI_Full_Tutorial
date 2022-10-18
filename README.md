# FastAPI_Full_Tutorial

## **Summary**

**German/Deutsch**

Herzlich Willkommen zum Branch 5 *end_point_bookings*. Seit dem letzten Branch haben wir alle Endpunkte zu dem Erstellen und Abrufen von Buchungen bzw. Bookings implementiert. Dabei haben wir über das Vergleichen von Zeitstempeln aus den angefragten Zeiträumen eine Konfliktsuche implementiert, sodass nur dann Buchungen erstellt werden können, wenn ein Buch in einem Zeitraum nicht bereits gebucht ist. Bis zum nächsten Branch werden wir uns mit dem systematischen Testen unserer API Schnittstelle beschäftigen und Unit-Tests erstellen. Auch wenn es auf den ersten Blick nicht als der wichtigste Punkt ist, empfehle ich sehr, euch mit diesem Thema zu beschäftigen. Es hilft euch bei der Weiterentwicklung eurer Schnittstelle, bestehende Funktionen abzusichern und hilft euch auch nachzuweisen, dass eure Funktionen genau das erledigen, wofür ihr diese geschrieben habt. Ich wünsche euch wie immer viel Spaß bei diesem Tutorial :)

**English**

Welcome to Branch 5 *end_point_bookings*. Since the last branch, we have implemented all endpoints for creating and retrieving bookings. We have implemented a conflict search by comparing timestamps from the requested time periods, so that bookings can only be created if a book in a time period is not already booked. Until the next branch, we will be busy systematically testing our API interface and creating unit tests. Even though it may not seem like the most important point at first glance, I highly recommend you to deal with this topic. It will help you in the further development of your interface, secure existing functions and also help you to prove that your functions do exactly what you wrote them for. As always, I hope you enjoy this tutorial :)

## Task for this Branch

**German/Deutsch**

Wie bereits in der Zusammenfassung beschrieben, werden bis zum nächsten Branch Unit-Tests zum Testen der Schnittstelle implementiert. Hierzu erstellen wir uns einen neuen Ordner neben dem eigentlichen Source-Code und erstellen uns hierfür auch Start-Skripte, ähnlich den Skripten zum Starten von dem Uvicorn Server.

- **[ ] Benenne den Ordner *src* in *app* und erstelle daneben einen Ordner *test* mit einem "__init__" File**

- **[ ] Je nachdem auf welchem System du arbeitest, erstelle dir ein Skript zum Starten von den Tests**
    - Für Linux *startTestingOnLinux.sh*
        ```bash
        #!/bin/bash

        # Try to remove SQLlite Database
        rm sql_app.db

        # Start Testing with pytest
        pytest -vv
        ```
        *Hinweis* Bitte mache dieses Skript Ausführbar mit folgendem Befehl:
        ```bash
        sudo chmod +x startTestingOnLinux.sh
        ```
    - Für Windows *startTestingOnWindows*
        ```bat
        del sql_app.db

        pytest -vv
        ```

- **[ ] Erstelle die Datei *prep.py* in dem wir alle Vorbereitungen für das Testing implementieren**
    - In diesem musst du den **TestClient**, der als Schnittstelle zu den Endpunkten in *main.py* dient, vo *fastapi.testclient* importieren
    - Anschließend musst du das Package *sys* importieren und mit folgender Anweisung, das importieren aus dem *app* Ordner ermöglichen:
    ```python
    sys.path.append("..")
    ```
    - Importiere anschließend von *app.main* das Objekt **app**
    - Erstelle eine Objekt vom Typ *TestClient* dem du das eben importierte *app* übergibst
    - Setze drei Variablen für eine *Email-Adresse*, *Passwort* und einen *Namen*, die wir für die initiale Registrierung und dem Abrufen von einem Token zur Nutzung der geschützten Endpunkte benötigen
    - Erstelle dir anschließend eine Methode, die als Parameter eine *Email-Adresse*, ein *Namen* und ein *Passwort* erwarten
        - Erstelle ein Dictionary mit den Feldern *email*, *password* und *fullname*
        - Führe die Registrierung mit dem TestClient Objekt wie folgt aus:
        ```python
        response = client.post("/register", json=data)
        ```
        - Wobei *data* das erstellte Dictionary ist
        - Extrahiere aus *response* den *access_token* mit
        ```python
        auth_token = response.json()["access_token"]
        ```
        - Gebe diesen Token wie folgt als Funktionsrückgabewert an
        ```python
        return {"Authorization": f"Bearer {auth_token}"}
        ```
    - Erstelle eine weitere Methode *update_access_token_header*, der einen neuen Token in Form eines Strings entgegennimmt und wie oben einen Authorization Header zurück gibt
    - Rufe am Ende von *prep.py* die Methode zur Registrierung auf und speichere den Authorization Header in einer Variable *access_token_header*


- **[ ] Erstelle ein File zum Testen der Beschränkung von Endpunkten**
    - Um nicht authorizierten Zugriff auf unsere implementierten Endpunkte zu erlauben prüfen wir zunächst ob alle Endpunkte zuverlässig einen *Authorization Error* werfen, wenn kein valider Token mitgegeben wird
    - Erstelle daher ein neues File mit den Namen **test_not_auth.py**
    - Importiere hier von *.prep* den erstellten TestClienten **client**
    - Erstelle für jeden Endpunkt eine Methode, wie die folgende:
    ```python
    def test_get_all_users_no_auth():
        response = client.get("/users")
        assert response.status_code == 401
        assert response.json() == {"detail": "Not authenticated"}
    ```
    - Wir verwenden den *client* um eine *GET* Anfrage an den Endpunkt */user* durchzuführen
    - Da wir alle Endpunkte nur für authorisierte User zulassen möchten, erwarten wir hier
        - Den Status Code *401*
        - Als Empfange Antwort das oben beschriebene JSON


- **[ ] Erstelle Files zum Testen der beschränkten Endpunkte**
    - Anders als in den vorherigen Tests, soll nun getestet werden, ob die Funktionen auch tatsächlich das tun, für das sie ursprünglich implementiert wurden
    - Für eine bessere Übersichtlichkeit erstelle jeweils Files für das Testen von den Endpunkten für User-, Book- und Booking-Endpunkte
        - *"test_user_endpoints.py"*
        - *"test_book_endpoints.py"*
        - *"test_booking_endpoints.py"*
    - Damit du auch Zugriff auf die Methoden hast, muss bei jeder Anfrage, ein valider Token mitgeben werden. Importiere dazu in jedem der Files, den *client* und den *access_token_header*
    - Mache dir nun Gedanken, wie du jeden Endpunkt sinnvoll testen kannst. Wichtig ist natürlich die Grundfunktionalität, aber auch das Prüfen, ob die Funktion mit allen möglichen Input Kombination immernoch so funktioniert wie ursprünglich gedacht. Ein wichtigtes Stichwort dafür, sind die so genannten *Äquivalenzklassen*. Siehe dazu diesen Link: https://de.wikipedia.org/wiki/%C3%84quivalenzklassentest
    - Nachfolgend siehst du zwei Tests für den gleichen Endpunkt. Der eine prüft, ob das Buch korrekt angelegt wurde und der Zweite, ob wir eine Fehlermeldung erhalten, wenn wir probieren, das gleiche Buche nochmals anzulegen:
    ```python
    ## Add Books at first:
    def test_add_books():
        input_data = {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}
        response = client.post("/book/add_single", json=input_data, headers=access_token_header)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['title'] == "Book Title"
        assert response_data['author'] == "Test Author"
        assert response_data['isbn'] == "123456789"

    ## Try to add the same book again:
    def test_add_same_book_again():
        input_data = {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}
        response = client.post("/book/add_single", json=input_data, headers=access_token_header)
        assert response.status_code == 404
        response_data = response.json()
        assert response_data == {"detail": "Book with ISBN {} already exist".format("123456789")}
    ```
    - Da es sich bei dem *'/book/add_single'* Endpunkt um eine Post Methode handelt und Daten erwartet werden, erstellen wir zunächst das Dict 'input_data', mit den Feldern, die von der jeweiligen Methode erwartet wird.
    - Diese wird über den 'client' innerhalb einer *POST* Methode zusammen mit dem *access_token_header* übergegeben.
    - Anschließend wird über das *'assert'* Keyword die wichtigen Abfragen durchgeführt, wie ob der übergebene Titel auch dem vom Input entspricht etc.
    - Im zweiten Test wird exakt der gleiche Datensatz übergeben. Nur wird dieses Mal ein Fehler erwartet, der aber eben auch abgeprüft wird.

**English**

As already described in the summary, unit tests for testing the interface are implemented until the next branch. To do this, we create a new folder next to the actual source code and also create start scripts for this, similar to the scripts for starting the Uvicorn server.

- **[ ] Rename the folder *src* to *app* and create a folder *test* next to it with a "__init__" file**.

- **[ ] Depending on the system you are working on, create a script to start the tests**.
    - For Linux *startTestingOnLinux.sh*
        ``bash
        #!/bin/bash

        # Try to remove SQLlite Database
        rm sql_app.db

        # Start Testing with pytest
        pytest -vv
        ```
        *Note* Please make this script executable with the following command:
        ``bash
        sudo chmod +x startTestingOnLinux.sh
        ```
    - For Windows *startTestingOnWindows* ```bat
        ``bat
        del sql_app.db

        pytest -vv
        ```

- **[ ] Create the file *prep.py* in which we implement all the preparations for testing**.
    - In this file you have to import the **TestClient**, which serves as an interface to the endpoints in *main.py*, vo *fastapi.testclient*.
    - Then you have to import the package *sys* and enable the import from the *app* folder with the following statement:
    ``python
    sys.path.append("..")
    ```
    - Then import from *app.main* the object **app**.
    - Create an object of type *TestClient* to which you pass the just imported *app*.
    - Set three variables for an *email address*, *password* and a *name*, which we need for initial registration and to retrieve a token to use the protected endpoints.
    - Then create a method that expects an *email address*, a *name* and a *password* as parameters.
        - Create a dictionary with the fields *email*, *password* and *fullname*.
        - Execute the registration with the TestClient object as follows:
        ``python
        response = client.post("/register", json=data)
        ```
        - Where *data* is the dictionary created.
        - Extract the *access_token* from *response* with
        python
        auth_token = response.json()["access_token"]
        ```
        - Specify this token as a function return value as follows
        ``python
        return {"Authorisation": f "Bearer {auth_token}"}
        ```
    - Create another method *update_access_token_header* that takes a new token in the form of a string and returns an Authorization header as above.
    - At the end of *prep.py*, call the method to register and store the Authorization Header in a variable *access_token_header*.


- **[ ] Create a file to test the restriction of endpoints**.
    - To allow unauthorised access to our implemented endpoints, we first check that all endpoints will reliably throw an *Authorisation Error* if a valid token is not provided.
    - Therefore create a new file with the name **test_not_auth.py**.
    - Import the created test client **client** from *.prep*.
    - Create a method for each endpoint, like the following:
    ``python
    def test_get_all_users_no_auth():
        response = client.get("/users")
        assert response.status_code == 401
        assert response.json() == {"detail": "Not authenticated"}
    ```
    - We use the *client* to make a *GET* request to the endpoint */user*.
    - Since we want to allow all endpoints only for authorised users, we expect here
        - The status code *401*
        - Receive the JSON described above as a response.

- **[ ] Create files to test the restricted endpoints**.
    - In contrast to the previous tests, we now want to test whether the functions actually do what they were originally implemented to do.
    - For a better overview, create files for testing the endpoints for user, book and booking endpoints
        - *"test_user_endpoints.py "*
        - *"test_book_endpoints.py "*
        - *"test_booking_endpoints.py "*
    - In order to have access to the methods, a valid token must be provided with each request. To do this, import the *client* and the *access_token_header* in each of the files.
    - Now think about how you can test each endpoint in a meaningful way. Of course, the basic functionality is important, but also checking whether the function still works as originally intended with all possible input combinations. An important keyword for this are the so-called *equivalence classes*. See this link: https://de.https://en.wikipedia.org/wiki/Equivalence_partitioning
    - Below you see two tests for the same endpoint. One checks if the book was created correctly and the second if we get an error message when we try to create the same book again:
    ``python

    ## Add Books at first:
    def test_add_books():
        input_data = {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}
        response = client.post("/book/add_single", json=input_data, headers=access_token_header)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['title'] == "Book Title".
        assert response_data['author'] == "Test Author"
        assert response_data['isbn'] == "123456789"

    
    ## Try to add the same book again:
    def test_add_same_book_again():
        input_data = {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}
        response = client.post("/book/add_single", json=input_data, headers=access_token_header)
        assert response.status_code == 404
        response_data = response.json()
        assert response_data == {"detail": "Book with ISBN {} already exist".format("123456789")}
    ```
    - Since the *'/book/add_single'* endpoint is a post method and data is expected, we first create the dict 'input_data', with the fields expected by the respective method.
    - This is passed via the 'client' within a *POST* method along with the *access_token_header*.
    - Afterwards, the important queries are carried out via the *'assert'* keyword, such as whether the title passed also corresponds to that of the input, etc. The second test is carried out with exactly the same data.
    - In the second test, exactly the same data set is passed. Only this time an error is expected, which is also checked.