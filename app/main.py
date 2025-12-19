from fastapi import FastAPI
from datetime import datetime, timezone
from mangum import Mangum

from app.models import UserRequest, EnrichedUser
## adding version end point
import os
from datetime import datetime, timezone

app = FastAPI(
    title="User Enrichment API",
    version="1.0.0",
)

### adding versioning end point

@app.get("/version")
def version():
    return {
        "service": os.getenv("SERVICE_NAME", "serverless-enrichment-api"),
        "version": os.getenv("APP_VERSION", "dev"),
        "git_sha": os.getenv("GIT_SHA", "unknown"),
        "deployed_utc": os.getenv("DEPLOYED_UTC", "unknown"),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/enrich-user", response_model=EnrichedUser)
def enrich_user(body: UserRequest):
    domain = body.email.split("@")[-1].lower()
    free_providers = {
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "live.com",
    }

    first = body.first_name.strip()
    last = body.last_name.strip()

    return EnrichedUser(
        full_name=f"{first} {last}",
        email_domain=domain,
        email_is_free_provider=domain in free_providers,
        normalized_first_name=first.lower(),
        normalized_last_name=last.lower(),
        initials=f"{first[0].upper()}{last[0].upper()}",
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
    )

handler = Mangum(app)
