from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional
from datetime import datetime

from app.modules.conversations.models import Role

class MessageCreate(BaseModel):
    role: Role
    content: str

class MessageRead(MessageCreate):
    id: UUID
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class ConversationCreateRequest(BaseModel):
    document_id: int
    title: str | None = None

class ConversationResponse(BaseModel):
    id: UUID
    title: str | None
    created_at: datetime
    user_id: int
    document_id: Optional[int] = None
    document_owner_id: Optional[int] = None

    model_config = {
        "from_attributes": True
    }

class ConversationDetail(ConversationResponse):
    messages: List[MessageRead]

    model_config = {
        "from_attributes": True
    }
