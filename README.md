Der "DS ListMailer" ist eine grafische Benutzeroberfläche (GUI)-Anwendung in Python, die entwickelt wurde, um Massen-E-Mails an Empfänger aus einer CSV-Datei zu senden.
Das Programm bietet eine benutzerfreundliche Umgebung für das Einrichten von SMTP-Verbindungsinformationen, die Auswahl einer Empfängerliste aus einer CSV-Datei und das Verfassen sowie den Versand von personalisierten E-Mails.

Hauptfunktionen:

CSV-Datei auswählen:

Der Benutzer kann eine CSV-Datei auswählen, die die E-Mail-Adressen der Empfänger enthält.

SMTP-Daten eingeben:

Die Anwendung erlaubt dem Benutzer die Eingabe von SMTP-Server, -Port, -Benutzername und -Passwort für den E-Mail-Versand.

E-Mail-Betreff und -Inhalt eingeben:

Benutzer können den Betreff und den Inhalt der E-Mail eingeben, wobei der Inhalt personalisiert werden kann.

E-Mails senden:

Durch Betätigen des "E-Mails senden"-Buttons werden die E-Mails an die in der CSV-Datei aufgeführten Empfänger gesendet.

Fortschrittsanzeige:

Die GUI informiert den Benutzer über den Fortschritt des Versands, einschließlich der Gesamtanzahl der E-Mails und der Anzahl der erfolgreich gesendeten E-Mails.

Ungültige E-Mail-Adressen speichern:

Ungültige E-Mail-Adressen, die nicht dem E-Mail-Format entsprechen, werden in einer separaten CSV-Datei ("keine-nachricht-erhalten.csv") gespeichert.

Erfolgsmeldung anzeigen:

Nach erfolgreichem Versand aller E-Mails wird dem Benutzer eine Erfolgsmeldung angezeigt, die Details wie die Anzahl der versendeten und nicht versendeten E-Mails enthält.

Hinweis:

Das Programm stellt eine einfach zu bedienende Schnittstelle bereit, jedoch sollten Sicherheitsüberlegungen, insbesondere im Umgang mit SMTP-Passwörtern, in einer Produktionsumgebung sorgfältig berücksichtigt werden.
