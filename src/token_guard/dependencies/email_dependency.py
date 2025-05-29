from typing import Annotated

from fastapi import Depends

from token_guard.core import config
from token_guard.services.email_service import EmailService


def _get_email_service() -> EmailService:
    service = EmailService(config.GMAIL_USERNAME, config.GMAIL_APP_PASSWORD)
    return service


EmailServiceDep = Annotated[EmailService, Depends(_get_email_service)]
