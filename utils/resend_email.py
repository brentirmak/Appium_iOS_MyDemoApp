
import os
import base64
import html
import resend

from datetime import datetime
from pathlib import Path


def send_failure_email(
    test_name,
    test_script,
    error_message,
    screenshot_path=None
):
    """
    Send a single test failure notification through Resend.
    """

    api_key = os.getenv("RESEND_API_KEY")
    sender = os.getenv("ALERT_FROM")
    recipients = os.getenv("ALERT_TO")
    label = os.getenv("ALERT_LABEL", "Appium iOS MyDemoApp")

    if not all([api_key, sender, recipients]):
        raise ValueError(
            "Missing required Resend configuration. "
            "Check RESEND_API_KEY, ALERT_FROM and ALERT_TO."
        )

    resend.api_key = api_key

    recipient_list = [
        address.strip()
        for address in recipients.split(",")
        if address.strip()
    ]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    job_name = os.getenv("JOB_NAME", "Local Execution")
    build_number = os.getenv("BUILD_NUMBER", "N/A")
    build_url = os.getenv("BUILD_URL", "")

    safe_test = html.escape(test_name)
    safe_script = html.escape(test_script)
    safe_error = html.escape(str(error_message))
    safe_label = html.escape(label)

    build_info = f"{job_name} / Build #{build_number}"

    attachment_list = []

    if screenshot_path:
        screenshot = Path(screenshot_path)

        if screenshot.exists():
            with screenshot.open("rb") as file:
                encoded_image = base64.b64encode(
                    file.read()
                ).decode("utf-8")

            attachment_list.append({
                "filename": screenshot.name,
                "content": encoded_image,
            })

    screenshot_status = (
        "Screenshot attached."
        if attachment_list
        else "Screenshot unavailable. See Jenkins build artifacts/logs."
    )

    html_body = f"""
    <html>
      <body>
        <h2>{safe_label} - Test Failure</h2>

        <p>The first test failure has been detected.</p>

        <table cellpadding="6">
          <tr>
            <td><b>Test</b></td>
            <td>{safe_test}</td>
          </tr>
          <tr>
            <td><b>Python Script</b></td>
            <td>{safe_script}</td>
          </tr>
          <tr>
            <td><b>Execution</b></td>
            <td>{html.escape(build_info)}</td>
          </tr>
          <tr>
            <td><b>Timestamp</b></td>
            <td>{timestamp}</td>
          </tr>
        </table>

        <h3>Failure Details</h3>

        <pre>{safe_error}</pre>

        <p>{screenshot_status}</p>

        {f'<p><a href="{html.escape(build_url, quote=True)}">View Jenkins Build</a></p>' if build_url else ''}
      </body>
    </html>
    """

    params = {
        "from": sender,
        "to": recipient_list,
        "subject": f"{label} - First Test Failure",
        "html": html_body,
    }

    if attachment_list:
        params["attachments"] = attachment_list

    response = resend.Emails.send(params)

    print("[Resend] Failure notification submitted successfully.")
    print(f"[Resend] Response: {response}")

    return response
