import asyncio
import logging 
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