import smtplib
from email.message import EmailMessage

from token_guard.exceptions.common_exceptions import email_missing_field_exception
from token_guard.schemas import EmailSendDTO


class EmailService:
    def __init__(self, gmail_username: str, gmail_app_password: str) -> None:
        self._gmail_username = gmail_username
        self._gmail_app_password = gmail_app_password

    def send_verification_email(self, send_dto: EmailSendDTO) -> None:
        if (
            not send_dto.subject
            or not send_dto.email_from
            or not send_dto.email_to
            or not send_dto.content
        ):
            raise email_missing_field_exception

        msg = EmailMessage()
        msg["Subject"] = send_dto.subject
        msg["From"] = send_dto.email_from
        msg["To"] = send_dto.email_to
        msg.set_content(send_dto.content)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self._gmail_username, self._gmail_app_password)
            smtp.send_message(msg)

        return
