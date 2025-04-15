# Network Traffic Report Emailer

## Overview

This Python script automates sending daily network traffic reports via email with PDF attachments. It dynamically generates file names based on the current date and supports multiple attachments.

**Key Features**:

- Automatically attaches daily network traffic reports in PDF format.
- Sends emails via an SMTP server (configured for internal use without a password).
- Includes basic error handling (e.g., for missing files).

## Prerequisites

- Python 3.6 or higher.

- Required Python packages:

  ```
  pip install python-dotenv
  ```

- Access to an SMTP server (internal server without authentication in this setup).

- Network traffic reports in PDF format, stored in a specified directory.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd network-traffic-report-emailer
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   (If no `requirements.txt` exists, install `python-dotenv` directly.)

## Configuration

1. Ensure the following are set up:

   - **Email addresses**: Sender and recipient email addresses (hardcoded in the script or via environment variables).
   - **SMTP server**: Your SMTP server address and port (defaults to 465 with SSL).
   - **Report path**: Directory containing PDF reports (e.g., a local folder like `reports/`).

2. (Optional) If using environment variables, create a `.env` file with the following structure:

   ```
   SENDER_EMAIL=your-email@example.com
   RECEIVER_EMAIL=target-email@example.com
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=465
   ```

**Note**: The `.env` file is included in `.gitignore` to prevent uploading sensitive data to GitHub.

## Usage

1. Ensure PDF reports are available in the specified path (e.g., `Network Traffic for Network1 2025-04-15.pdf`).

2. Run the script:

   ```bash
   python send_report.py
   ```

3. The script will:

   - Attach the specified PDF files.
   - Send the email via the configured SMTP server.
   - Display "Email sent successfully!" or an error message if something goes wrong.

## Project Structure

```
├── send_report.py       # Main script
├── .gitignore           # Ignores sensitive files
├── README.md            # Project documentation
├── requirements.txt     # (Optional) Dependency list
```

## Notes

- Ensure PDF files exist in the specified path, or the script will report a "File not found" error.
- The script uses SSL with port 465 by default. Modify `send_report.py` if your SMTP server uses a different configuration.
- This script assumes an internal SMTP server without authentication. For password-protected servers, add `server.login()` logic as needed.

## Contributing

Suggestions for improvements are welcome! Please open an issue or submit a pull request.

## License

MIT License (or as per your organization's policy)

## Contact

For questions, contact your IT support team.
