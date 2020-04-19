from stoq.data_classes import Payload, Request, WorkerResponse
from stoq.plugins import WorkerPlugin
import asyncio
import time
class w1(WorkerPlugin):
    async def scan(self, payload: Payload, request: Request) -> WorkerResponse:
        if payload.content == b'asyncio':
            await asyncio.sleep(1)
        else:
            time.sleep(1)
        return WorkerResponse()
