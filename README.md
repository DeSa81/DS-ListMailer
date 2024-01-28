Programmbeschreibung:

Der "DS ListMailer" ist eine grafische Benutzeroberfläche (GUI)-Anwendung in Python, entwickelt für den Versand von Massen-E-Mails an Empfänger anhand einer CSV-Datei.
Die Anwendung ermöglicht die einfache Konfiguration von SMTP-Verbindungsinformationen, die Auswahl einer Empfängerliste aus einer CSV-Datei und die Verwaltung des E-Mail-Inhalts sowie dessen Versand.

Hauptfunktionen:

CSV-Datei auswählen:

Der Benutzer wählt eine CSV-Datei aus, die die E-Mail-Adressen der Empfänger enthält. Es ist wichtig sicherzustellen, dass die CSV-Datei die erwartete Struktur aufweist. Die erste Zeile der CSV-Datei sollte einen Header mit der Bezeichnung "Email" enthalten, um dem Programm die korrekte Identifikation der E-Mail-Adressen zu ermöglichen.

SMTP-Daten eingeben:

Benutzer können SMTP-Server, -Port, -Benutzername und -Passwort eingeben, um die Verbindung für den E-Mail-Versand herzustellen.

E-Mail-Betreff und -Inhalt eingeben:

Benutzer können den Betreff und den Inhalt der E-Mail eingeben. Der Inhalt kann dabei personalisiert werden, um individuelle Nachrichten zu erstellen.

E-Mails senden:

Durch Betätigen des "E-Mails senden"-Buttons werden die E-Mails an die in der CSV-Datei aufgeführten Empfänger versendet.

Fortschrittsanzeige:

Die GUI informiert über den Fortschritt des Versands, einschließlich Gesamtanzahl der E-Mails und Anzahl der erfolgreich versendeten E-Mails.

Ungültige E-Mail-Adressen speichern:

Ungültige E-Mail-Adressen, die nicht dem E-Mail-Format entsprechen, werden in einer separaten CSV-Datei ("keine-nachricht-erhalten.csv") gespeichert.

Erfolgsmeldung anzeigen:

Nach erfolgreichem Versand aller E-Mails erhält der Benutzer eine Meldung mit Details wie Anzahl der versendeten und nicht versendeten E-Mails.

Hinweis:

Es handelt sich um ein Projekt, das im Rahmen des Lernens von Programmierung entstanden ist.
Bei der Entwicklung wurden keine Sicherheitsaspekte für einen produktiven Einsatz berücksichtigt.
Es ist besonders wichtig, Sicherheitsüberlegungen zu beachten, insbesondere im Umgang mit SMTP-Passwörtern, wenn das Projekt in einer Produktionsumgebung verwendet werden soll.
