from stoq.data_classes import Payload, Request, WorkerResponse
from stoq.plugins import WorkerPlugin
import asyncio
import time
class w3(WorkerPlugin):
    async def scan(self, payload: Payload, request: Request) -> WorkerResponse:
        if payload.content == b'asyncio':
            await asyncio.sleep(3)
        else:
            time.sleep(3)
        return WorkerResponse()
