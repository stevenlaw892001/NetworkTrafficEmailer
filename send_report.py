import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email configuration
SMTP_PORT = 465  # SSL port for secure email transmission
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "sender@example.com")  # Sender email from .env or default
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "receiver@example.com")  # Recipient email from .env or default
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")  # SMTP server from .env or default

# Email content
SUBJECT = "Daily Network Traffic Reports"  # Email subject
BODY = """\
Dear Team,

Attached are the daily network traffic reports.

Regards,
Network Admin
"""

# Generate current date for dynamic file naming
TODAY_DATE = datetime.datetime.now().strftime("%Y-%m-%d")

# Paths to report files (placeholders, configure actual paths in production)
REPORTS_DIR = os.getenv("REPORTS_DIR", "path/to/reports")  # Report directory from .env or default
ATTACHMENTS = [
    os.path.join(REPORTS_DIR, f"Network_Traffic_Report1_{TODAY_DATE}.pdf"),
    os.path.join(REPORTS_DIR, f"Network_Traffic_Report2_{TODAY_DATE}.pdf"),
]

# Create MIME email object
message = MIMEMultipart()
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL
message["Subject"] = SUBJECT

# Attach plain text body
message.attach(MIMEText(BODY, "plain"))

# Attach report files
for file_path in ATTACHMENTS:
    try:
        with open(file_path, "rb") as attachment:
            # Create MIMEBase object for attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)  # Encode attachment in base64

            # Set attachment headers
            file_name = os.path.basename(file_path)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={file_name}"
            )

            # Attach file to email
            message.attach(part)
    except FileNotFoundError:
        print(f"Error: Report file not found - {file_path}")
    except Exception as e:
        print(f"Error attaching file {file_path}: {e}")

# Send email
try:
    # Establish secure SSL connection to SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL], message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")