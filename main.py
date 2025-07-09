import asyncio
import logging 
from logging import logger
import os
from typing import Dict, Any, Optional 
from dataclasses import dataclass 
from datetime import datetime 

#configure logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s = %(name)s - %(levelname)s = %(message)s'
)

@dataclass
class QueryContext:
    #Contetext for a single query processing workflow
    query: str
    user_id: str
    chanel_id: str
    timestamp: datetime 
    triange_result: Optional[Dict[str, Any]] = None
    retried_info: Optional[Dict[str, Any]] = None
    synthesized_answer: Optional[Dict[str]] = None
    slack_response: Optional[Dict[str, Any]] = None

class QueryReceiver: 
    #Handles receiving queries from various sources

    def _init_(self):
        self.supported_sources = ['slack', 'api', 'webhook']

    async def receive_query(self, source: str, **kwargs) -> QueryContext:
        #Receive a query from the specified csource
        logger.info(f"Receiving query from source: {source}")

        if source == 'slack':
            return await self._receive_from_slack(**kwargs)
        elif source == 'api':
            return await self._receive_from_api(**kwargs)
        elif source == 'webhook':
            return await self._receive_from_webhook(**kwargs)
        else:
            raise ValueError(f"Unsupported source: {source}")
        
        