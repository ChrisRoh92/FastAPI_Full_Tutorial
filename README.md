# FastAPI_Full_Tutorial

## **Introduction**

**German/Deutsch** 

- Hallo und Herzlich Willkommen zu diesem FastAPI Tutorial. Dieses Repo ist begleitend zu dem Video auf meinem Channel *CodingWithChris*. Das Repo ist so
aufgebaut, das es dich von den wichtigsten Momenten aus dem Video führt. Jeder Branch ist nummeriert und im so benannt, dass sich ergibt, was seit dem letzten Branch durchgeführt wurde. 

- Du findest in jedem nummerierten Branch eine Zusammenfassung, von dem implementieren Features im Vergleich zum Vorherigen Branch. Gleichzeitig findest du in diesem File in dem nächsten Abschnitt, die Aufgaben bzw. Tasks, die du für den nächsten Stand zu tun sind. Du musst sicherlich nicht wortwörtlich den gleichen Code haben, und bestimmt auch nicht alles gleich haben. Vielleicht findest du andere Methoden und andere Funktionalitäten wichtiger und möchtest 
diese gerne sehen. Es soll dir vor allem eine Hilfe sein, dieses Thema genauer zu verstehen und dir die Möglichkeit geben, genau zu erkennen, was durch welches Implementierungsdetail erreicht wurde.

- Du befindest dich im ersten Branch, dem 'Start' Branch, wie ich ihn genannt habe. Hier sind alle wichtigen Files, die für dieses Projekt brauchst enthalten, sowie einer grundlegenden Struktur, die sich vielleicht sogar noch ändern kann, wer weiß :)

*Nun wünsche ich dir viel Spaß beim Durchgehen dieses Tutorials. Ich freue mich sehr über dein Feedback!*

**English**

- Hello and welcome to this FastAPI tutorial. This repo is accompanying the video on my channel *CodingWithChris*. The repo is structured
that it takes you from the most important moments in the video. Each branch is numbered and named to indicate what has been done since the last branch. 

- You will find in each numbered branch a summary of the implemented features compared to the previous branch. At the same time you will find in this file in the next section, the tasks that you have to do for the next state. You certainly don't have to have literally the same code, and you certainly don't have to have everything the same. Maybe you find other methods and other functionalities more important and would like to see them. 
and would like to see them. It should mainly be a help for you to understand this topic in more detail and give you the possibility to see exactly what was achieved by which implementation detail.

- You are in the first branch, the 'Start' branch as I called it. Here you will find all the important files you need for this project, as well as a basic structure, which may even change, who knows :)

*Now I wish you a lot of fun while going through this tutorial. I am very happy about your feedback!*

## **Tasks**

**German/Deutsch** 

Deine Aufgabe in diesem Abschnitt ist es, alles zum Einrichten von FastAPI durchzuführen. Ich habe dir im Video hierzu 
eine Einführung gegeben. Bitte mache die damit vertraut und probiere, wie du das Projekt startest und wie du damit interagieren kannst.

- **[ ] Installiere alle notwendigen Libraries mit** 
    
    > `pip install -r requirements.txt`

- **[ ] Starte den Server für die API mit**

    > Wenn du auf Linux arbeitest:      
    >
    > `./startOnLinux.sh`
    
    > Wenn du mit Windows arbeitest:    
    >
    > `startOnWindows.cmd`

- **[ ] Rufe in deinem Browser deiner Wahl folgende Adresse und versuche den ersten implementierten API Endpunkt zu erreichen**

    > [127.0.0.1:8000/docs](127.0.0.1:8000/docs)

- **[ ] Nun kannst du anfangen in der main.py in in dem *src* Ordner weitere Endpunkt einzufügen**

    > Füge nur die Methoden, ohne Logiken ein. Als Methoden Körper kannst du `pass` eingeben, so wie nachfolgend dargestellt:
    >
    > ``` python
    > @app.get("/")
    > def get_root(): 
    >   pass 
    >  ```

    > **User Endpunkte**
    >
    > - Rufe alle User ab
    > - Rufe einen User über die Email ab
    > - Registriere einen User
    > - Logge einen User ein
    > - Update das Password 
    > - Update die Email Adresse
    > - Lösche den Nutzer

    > **Bücher Endpunkte**
    >
    > - Rufe alle Bücher ab
    > - Rufe ein Buch über die ISBN ab
    > - Rufe alle Bücher von eine Author ab
    > - Füge ein neues Buch hinzu
    > - Füge eine Liste von neuen Büchern hinzu
    > - Update den Titel von einem Buch über die ISBN

    > **Booking Endpunkte**
    >
    > - Rufe alle Bookings auf
    > - Rufe alle Bookings von dem aktuellen Nutzer auf
    > - Rufe alle Bookings die zu einem Buch gehören auf
    > - Füge ein neues Booking hinzu


**English** 

Your task in this section is to do everything to set up FastAPI. I have given you an introduction to this. Please familiarise yourself with it and try out how to start the project and interact with it.

- **[ ] Install all necessary libraries with** 
    
    > `pip install -r requirements.txt`

- **[ ] Start the server for the API with**

    > If you work on Linux:      
    >
    > `./startOnLinux.sh`
    
    > If you work with Windows:    
    >
    > `startOnWindows.cmd`

- **[ ] Call the following address in your browser of choice and try to reach the first implemented API endpoint**

    > [127.0.0.1:8000/docs](127.0.0.1:8000/docs)

- **[ ] Now you can start adding more endpoints in the main.py in the *src* folder**

    > Insert only the methods, without the logics. You can enter 'pass' as the method body, as shown below.:
    >
    > ``` python
    > @app.get("/")
    > def get_root(): 
    >   pass 
    >  ```

    > **User end points**
    >
    > - Retrieve all users
    > - Retrieve a user via email
    > - Register a user
    > - Log in a user
    > - Update the password 
    > - Update the email address
    > - Delete the user

    > **Book end points**
    >
    > - Retrieve all books
    > - Retrieve a book by ISBN
    > - Retrieve all books from an author
    > - Add a new book
    > - Add a list of new books
    > - Update the title of a book by ISBN

    > **Booking end points**
    >
    > - Retrieve all bookings
    > - Retrieve all bookings from the current user
    > - Retrieve all bookings that belong to a book
    > - Add a new booking