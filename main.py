import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys

csv_file_path = None
total_emails = 0
sent_emails = 0
invalid_emails = []

def choose_file():
    global csv_file_path, total_emails, sent_emails
    csv_file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    if csv_file_path:
        file_label.config(text=csv_file_path)
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            total_emails = sum(1 for row in reader)
        update_status_label()
    else:
        file_label.config(text="Bitte wählen Sie eine .csv Datei aus")

def is_valid_email(email):
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    return bool(re.match(email_regex, email))

def send_emails():
    global csv_file_path, total_emails, sent_emails, invalid_emails

    errors = []

    if not csv_file_path:
        errors.append("Bitte wählen Sie eine gültige CSV-Datei.")

    if email_text.get("1.0", "end-1c") == "":
        errors.append("Bitte geben Sie eine Nachricht ein.")

    if not email_subject_entry.get():
        errors.append("Bitte geben Sie einen Betreff ein.")

    smtp_server = smtp_server_entry.get()
    smtp_port = smtp_port_entry.get()
    smtp_username = smtp_username_entry.get()
    smtp_password = smtp_password_entry.get()

    if not smtp_server or not smtp_port or not smtp_username or not smtp_password:
        errors.append("Bitte geben Sie alle SMTP-Daten ein.")

    if errors:
        error_message = "\n".join(errors)
        messagebox.showerror("Fehler", error_message)
        return

    email_subject = email_subject_entry.get()

    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            email_content = email_text.get("1.0", "end-1c")

            for row in reader:
                to_email = row.get('Email', '').strip()
                if not to_email or not to_email.strip():
                    continue

                if not is_valid_email(to_email):
                    invalid_emails.append(to_email)
                    continue

                if send_email(to_email, email_content, smtp_server, smtp_port, smtp_username, smtp_password, email_subject):
                    sent_emails += 1
                    update_status_label()

    except FileNotFoundError:
        errors.append("Die ausgewählte Datei wurde nicht gefunden.")
    except Exception as e:
        errors.append(f"Ein Fehler ist aufgetreten: {e}")

    if invalid_emails:
        save_invalid_emails()

    if errors:
        error_message = "\n".join(errors)
        messagebox.showerror("Fehler", error_message)

    root.after(100, show_success_message)

def save_invalid_emails():
    app_directory = os.path.dirname(sys.argv[0])
    invalid_emails_file_path = os.path.join(app_directory, "keine-nachricht-erhalten.csv")

    with open(invalid_emails_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for email in invalid_emails:
            writer.writerow({'Email': email})

def send_email(to_email, content, smtp_server, smtp_port, smtp_username, smtp_password, email_subject):
    if not to_email:
        return False

    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = email_subject

    body = content
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, message.as_string())
    except Exception as e:
        return False

    return True

def update_status_label():
    global sent_emails, total_emails, invalid_emails
    status_label.config(text=f"Fortschritt: {sent_emails}/{total_emails}")
    progress_value = int((sent_emails / total_emails) * 100)
    progress_bar['value'] = progress_value
    root.update_idletasks()

def show_success_message():
    global sent_emails, total_emails, invalid_emails
    success_message = f"Alle E-Mail-Adressen wurden verarbeitet!\n\n" \
                      f"Versendete E-Mails: {sent_emails}\n" \
                      f"Nicht versendete E-Mails: {total_emails - sent_emails}\n\n" \
                      f"Details finden Sie in der Datei 'keine-nachricht-erhalten.csv'."
    messagebox.showinfo("Erfolg", success_message)

root = tk.Tk()
root.title("DS ListMailer")
root.geometry("500x800")
root.resizable(False, False)
root.padding_x = 10
root.padding_y = 10

smtp_group = ttk.LabelFrame(root, text="SMTP Daten", padding=(10, 10))
smtp_group.pack(fill="both", expand=True, pady=root.padding_y, padx=root.padding_x)

smtp_server_label = tk.Label(smtp_group, text="SMTP Server:")
smtp_server_label.grid(row=0, column=0, pady=root.padding_y, padx=root.padding_x, sticky=tk.W)

smtp_server_entry = tk.Entry(smtp_group, width=40)
smtp_server_entry.grid(row=0, column=1, pady=root.padding_y, padx=root.padding_x)

smtp_port_label = tk.Label(smtp_group, text="SMTP Port:")
smtp_port_label.grid(row=1, column=0, pady=root.padding_y, padx=root.padding_x, sticky=tk.W)

smtp_port_entry = tk.Entry(smtp_group, width=40)
smtp_port_entry.grid(row=1, column=1, pady=root.padding_y, padx=root.padding_x)

smtp_username_label = tk.Label(smtp_group, text="SMTP Username:")
smtp_username_label.grid(row=2, column=0, pady=root.padding_y, padx=root.padding_x, sticky=tk.W)

smtp_username_entry = tk.Entry(smtp_group, width=40)
smtp_username_entry.grid(row=2, column=1, pady=root.padding_y, padx=root.padding_x)

smtp_password_label = tk.Label(smtp_group, text="SMTP Password:")
smtp_password_label.grid(row=3, column=0, pady=root.padding_y, padx=root.padding_x, sticky=tk.W)

smtp_password_entry = tk.Entry(smtp_group, width=40, show="*")
smtp_password_entry.grid(row=3, column=1, pady=root.padding_y, padx=root.padding_x)

receiver_group = ttk.LabelFrame(root, text="Empfängerliste", padding=(10, 10))
receiver_group.pack(fill="both", expand=True, pady=root.padding_y, padx=root.padding_x)

file_label = tk.Label(receiver_group, text="Bitte wählen Sie eine .csv Datei aus")
file_label.pack(fill="both", expand=True, pady=(0, root.padding_y), padx=root.padding_x)

choose_button = tk.Button(receiver_group, text="Datei auswählen", command=choose_file)
choose_button.pack(fill="both", expand=True, pady=(0, root.padding_y), padx=root.padding_x)

email_text_group = ttk.LabelFrame(root, text="E-Mail", padding=(10, 10))
email_text_group.pack(fill="both", expand=True, pady=root.padding_y, padx=root.padding_x)

email_subject_label = tk.Label(email_text_group, text="E-Mail Betreff:")
email_subject_label.grid(row=0, column=0, pady=root.padding_y, padx=root.padding_x, sticky=tk.W)

email_subject_entry = tk.Entry(email_text_group, width=55)
email_subject_entry.grid(row=0, column=1, pady=root.padding_y, padx=root.padding_x, sticky=tk.W)

email_text = tk.Text(email_text_group, height=5, width=54)  # Ändere die Breite nach Bedarf
email_text.grid(row=1, column=0, pady=root.padding_y, padx=root.padding_x, sticky="nsew", columnspan=2)

status_label = tk.Label(root, text="Fortschritt:")
status_label.pack(fill="both", expand=True, pady=root.padding_y, padx=root.padding_x)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=480, mode="determinate")
progress_bar.pack(fill="both", expand=True, pady=root.padding_y, padx=root.padding_x)

start_button = tk.Button(root, text="E-Mails senden", command=send_emails, width=60)
start_button.pack(fill="both", expand=True, pady=(0, root.padding_y), padx=root.padding_x)

root.mainloop()
