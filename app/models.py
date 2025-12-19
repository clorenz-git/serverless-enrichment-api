from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class EnrichedUser(BaseModel):
    full_name: str
    email_domain: str
    email_is_free_provider: bool
    normalized_first_name: str
    normalized_last_name: str
    initials: str
    timestamp_utc: str
