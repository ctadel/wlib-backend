from typing import List
from fastapi import APIRouter, Depends
from uuid import UUID
from app.modules.conversations.service import ConversationService
from app.modules.conversations.schemas import ConversationCreateRequest, MessageCreate, ConversationDetail, \
        MessageRead, ConversationResponse

class ConversationRoutes:
    def __init__(self, prefix: str = "/conversations"):
        self.router = APIRouter(
                prefix=prefix, tags=["Conversations"])

        self.router.get(    ''                              )(self.list_user_conversations)
        self.router.post(   ''                              )(self.start_new_conversation)
        self.router.get(    '/{convo_id}'                   )(self.get_conversation)
        self.router.post(   '/{convo_id}'                   )(self.add_message)
        self.router.delete( '/{convo_id}'                   )(self.delete_conversation)
        self.router.post(   '/{convo_id}/archive'           )(self.archive_conversation)


    async def list_user_conversations(
            self, service: ConversationService = Depends(ConversationService)
            ) -> List[ConversationResponse]:
        return await service.list_conversations()

    async def start_new_conversation(
            self, data: ConversationCreateRequest,
            service: ConversationService = Depends(ConversationService)
            ) -> ConversationResponse:
        return await service.create_conversation(data)

    async def add_message(
            self, convo_id: UUID, data: MessageCreate,
            service: ConversationService = Depends(ConversationService)
            ) -> MessageRead:
        return await service.post_message(convo_id, data)

    async def get_conversation(
            self, convo_id: UUID,
            service: ConversationService = Depends(ConversationService)
            ) -> list[MessageRead]:
        return await service.get_messages(convo_id)

    async def delete_conversation(
            self, convo_id: UUID,
            service: ConversationService = Depends(ConversationService)):
        return await service.delete_conversation(convo_id)

    async def archive_conversation(
            self, convo_id: UUID,
            service: ConversationService = Depends(ConversationService)):
        return await service.archive_conversation(convo_id)
