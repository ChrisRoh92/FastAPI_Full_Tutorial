# FastAPI_Full_Tutorial

## **Summary**

**German/Deutsch**

Herzlich Willkommen zu Branch 5 *user_password_hashing*. Seit dem letzten Branch haben wir nun auch Logik implementiert, um User in unsere Datenbank aufzunehmen und vor allem auch das Passwort sicher speichern zu können. Hierzu haben wir zwei Methoden implementiert. Die Eine erzeugt aus einem Klartext Passwort ein Hash, der in der Datenbank hinterlegt wird. Die andere Methode prüft, ob eine Klartext Passwort mit einem übergebenen Hash übereinstimmt. Damit konnten wir nun endlich alle Endpunkte implementieren, in der das Handling mit Passwörter notwendig war. Wir sind schon fast am Ende von diesem Projekt. Bis zum nächsten Branch müssen alle Methoden zu den Reservierungen, auch Bookings in diesem Projekt genannt, implementiert werden. Ich wünsche dir, wie immer, viel Spaß beim Bearbeiten der Aufgaben :)

**English**

Welcome to Branch 5 *user_password_hashing*. Since the last branch, we have now implemented logic to add users to our database and, above all, to be able to store the password securely. We have implemented two methods for this. One creates a hash from a plaintext password, which is stored in the database. The other method checks whether a plaintext password matches a passed hash. With this we could implement all endpoints where the handling of passwords was necessary. We are almost at the end of this project. Until the next branch, all methods for reservations, also called bookings in this project, have to be implemented. As always, have fun working on the tasks :)

## Task for this Branch

**German/Deutsch**

Bis zum nächsten Branch, sollen alle Methoden rund um das Buchen von Büchern implementiert werden. Hierzu gehört insbesondere das Hinzufügen von Buchungen und dem Anzeigen von Buchungen, die einem Buch und einem User zugeordnet sind. Beim Hinzufügen von Buchungen für ein Buch ist dabei zu beachten, dass nur dann eine Buchung akzeptiert werden kann, wenn es zu keinem Konflikt in der Zeitlichen Belegung gibt. Hierzu muss eine geeignete Zeitkollisionsprüfung implementiert werden. Wenn du dir die Klasse **Booking** in *models.py* bereits angesehen hast, siehst du, dass ich nicht ein Datum speichere sondern 'timestamps'. Das Vergleichen von Zahlenwerten ist recht gut geeignet um Konflikte zu finden. Nachfolgend siehst du wie immer alle Aufgaben als Liste aufgeschlüsselt. Viel Spaß beim Bearbeiten :)

- **[ ] Erstelle eine neue Datei mit dem Namen *utils.py* in dem Unterordner *database***
    - Importiere von *datetime* die Klasse *datetime* 
    - Erstelle eine Methode *create_timestamp* in der aus einem *Date* Objekt ein Zeitstempel generiert wird. 

- **[ ] Füge weitere Methoden zu *crud.py* für das Verwalten von Buchungen hinzu**
    - Gebe alle im System angelegte Buchungen zurück
    - Gebe alle Buchungen, die einem User zugeordnet sind zurück
    - Gebe alle Buchungen, die einem Buch zugeordnet sind zurück
    - Eine Methode zum Anlegen von Buchungen, bei dem das *BookingBasseSchema* übergeben wird
    - Eine Hilfsmethode *book_has_booking_in_timerange*, in der geprüft wird, ob ein Buch in einem angefragten Zeitraum bereits gebucht ist
        - Die Methode erwartet ein *BookingBaseSchema* und die ID von dem angefragten Buch in der Datenbank
        - Erstelle aus den angefragten Tagen Zeitstemptel mit der *create_timestamp* Methode
        - Prüfe direkt, ob der *Bis* Tag nicht vor dem *Ab* Tag befindet. Sofern das doch der Fall sein sollte, werfe eine geeignete *HTTPException*
        - Importiere von *sqlalchemy*, *or_* und *and_*
        - Überlege dir, wie die Bedingungen aussehen müssen, damit ein Buch in dem angefragten Zeitraum bereits eine Buchung hat.
        - Fasse diese (zwei) Bedingungen mit einer Verundung in Variablen zusammen, nachfolgend dazu ein Beispiel.
        ```python
        cond1 = and_(to_timestamp >= Booking.from_timestamp, to_timestamp < Booking.to_timestamp)
        ```

        - Frage die Datenbank nach Buchungen ab, bei dem die *book_id* der übergebenen Buch ID entspricht und filtere diese mit den beiden Conditions, die Verodert auftreten können
        ```python
        bookings = db.query(Booking).filter_by(book_id = book_id).filter(or_(cond1, cond2)).all()
        ```
        - Sofern Bookings gefunden wurden, gebe *True* zurück, andernfalls *False*
    - Erstelle eine weitere Methode *add_new_booking*, das ein *BookingBaseSchema*, die Buch ID und die User ID als Parameter hat.
        - Erstelle zunächst ein Objekt vom Typ Booking, mit den übergebenen Argumenten. Vergesse nicht die jeweilis angefragten Tage in Zeitstempel umzuwandeln.
        - Füge dann diese Objekt der Datenbank hinzu und nutze dieses Objekt als Rückgabewert

- **[ ] Implementiere die Endpunkte zu den Bookings in *main.py***
    - Erstelle einen Endpunkt über den man alle im System gespeicherten Buchungen abrufen kann
    - Erstelle einen Endpunkt, über den man alle Buchungen, die dem aktuellen User zugeordnet sind abrufen kann
    - Erstelle einen Endpunkt, über den man alle Buchungen von einem Buch, über dessen ISBN abrufen kann 
    - Erstelle eine Methode in der man eine Buchung hinzufügen kann.
        - Die Methode erwartet dabei ein BookingBaseSchema als Übergabeparameter
        - Prüfe zunächst ob der User und das angefragte Buch in der Datenbank hinterlegt ist.
        - Prüfe anschließend, ob das Buch in dem angefragten Zeitraum bereits gebucht ist.
        - Sofern das nicht der Fall ist, rufe die *add_new_booking* Methode in *crud.py* und erstelle damit eine neue Buchung
        - Fange mögliche Fehlerfehler an jeder geeignet Stelle mit dem Werfen einer geeigneten *HTTPException* ab


**English**

Until the next branch, all methods around the booking of books are to be implemented. This includes, in particular, adding book bookings and displaying bookings that are assigned to a book and a user. When adding book bookings, it must be noted that a booking can only be accepted if there is no conflict in the time allocation. For this, a suitable time collision check must be implemented. If you have already looked at the class **Booking** in *models.py*, you will see that I do not store a date but timestamps. Comparing numerical values is quite good for finding conflicts. Below you can see all the tasks as a list. Have fun :)

- **[ ] Create a new file with the name *utils.py* in the subfolder *database***.
    - Import from *datetime* the class *datetime*. 
    - Create a method *create_timestamp* in which a timestamp is generated from a *date* object. 

- **[ ] Add more methods to *crud.py* for managing bookings**.
    - Return all bookings created in the system.
    - Return all bookings that are assigned to a user.
    - Return all bookings assigned to a book
    - A method for creating bookings, passing the *BookingBasseSchema*.
    - A helper method *book_has_booking_in_timerange*, which checks whether a book is already booked in a requested time period.
        - The method expects a *BookingBaseSchema* and the ID of the requested book in the database.
        - Create timestamps from the requested days with the *create_timestamp* method.
        - Check directly if the *To* day is not before the *From* day. If it is, throw an appropriate *HTTPException*.
        - Import from *sqlalchemy*, *or_* and *and_*.
        - Consider what the conditions must be so that a book already has a booking in the requested period.
        - Summarise these (two) conditions with a compound in variables, below is an example.
        ```python
        cond1 = and_(to_timestamp >= Booking.from_timestamp, to_timestamp < Booking.to_timestamp)
        ```
        - Query the database for bookings where the *book_id* matches the given book ID and filter them with the two conditions that can occur in order
        ```python
        bookings = db.query(Booking).filter_by(book_id = book_id).filter(or_(cond1, cond2)).all()
        ```
        - If bookings were found, return *True*, otherwise *False*.
    - Create another method *add_new_booking* that has a *BookingBaseSchema*, the book ID and the user ID as parameters.
        - First create an object of the type Booking, with the passed arguments. Don't forget to convert the requested days into timestamps.
        - Then add this object to the database and use this object as return value.

- **[ ] Implement the endpoints to the bookings in *main.py***.
    - Create an endpoint to retrieve all bookings stored in the system.
    - Create an endpoint that can be used to retrieve all bookings assigned to the current user.
    - Create an endpoint to retrieve all bookings of a book by its ISBN. 
    - Create a method in which you can add a booking.
        - The method expects a BookingBaseSchema as a transfer parameter.
        - First check whether the user and the requested book are stored in the database.
        - Then check whether the book is already booked in the requested period.
        - If this is not the case, call the *add_new_booking* method in *crud.py* and create a new booking.
        - Catch possible errors at any suitable point by throwing a suitable *HTTPException*.