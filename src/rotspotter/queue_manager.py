from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Dict, Any, Optional
import json, os

@dataclass
class Crate:
    id:str; timestamp:str; status:str; rot_score:float; notes:str=''

class QueueManager:
    def __init__(self, store_path='data/queue.json'):
        self.store_path=store_path; os.makedirs(os.path.dirname(store_path), exist_ok=True)
        self.crates=[]
        self._load()
    def _load(self):
        if os.path.exists(self.store_path):
            try:
                with open(self.store_path) as f: self.crates=[Crate(**c) for c in json.load(f)]
            except Exception: self.crates=[]
    def _save(self):
        with open(self.store_path,'w') as f: json.dump([asdict(c) for c in self.crates], f, indent=2)
    def add_crate(self, cid:str, rot_score:float, notes:str='')->Crate:
        status='healthy' if rot_score<0.25 else 'warning' if rot_score<0.6 else 'spoiling'
        c=Crate(cid, datetime.utcnow().isoformat()+'Z', status, rot_score, notes)
        self.crates.append(c); self._save(); return c
    def rotate(self)->Optional[Crate]:
        if not self.crates: return None
        c=self.crates.pop(0); self._save(); return c
    def list(self)->List[Dict[str,Any]]:
        return [asdict(c) for c in self.crates]
