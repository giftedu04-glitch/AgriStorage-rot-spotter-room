from typing import Dict, Any
class EnvSensor:
    def read(self)->Dict[str,Any]: return {'temp_c':None,'humidity_rh':None,'source':'manual'}
