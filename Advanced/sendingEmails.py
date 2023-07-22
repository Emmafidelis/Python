from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from string import Template
from pathlib import Path
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Mosh hamedani"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body", "plain"))
body = template.substitute({ "name": "John" })
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("movies.json").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
  smtp.send_message(message)
  print("Sent...")