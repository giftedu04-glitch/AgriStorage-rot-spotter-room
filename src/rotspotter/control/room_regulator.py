from typing import Dict, Any

class RoomRegulator:
    def __init__(self):
        # Tomatoes-only targets
        self.T_MIN=12.0; self.T_MAX=15.0
        self.RH_MIN=85.0; self.RH_MAX=90.0
    def regulate(self, env:Dict[str,Any])->Dict[str,Any]:
        t,rh=env.get('temp_c'), env.get('humidity_rh')
        actions=[]
        if t is not None:
            if t>self.T_MAX: actions.append('exhaust_on')
            if t<self.T_MIN: actions.append('heater_off_or_vent_mgmt')
        if rh is not None:
            if rh>self.RH_MAX: actions.append('dehumidify_or_vent')
            if rh<self.RH_MIN: actions.append('humidify')
        return {'tomatoes_only':True, 'targets':{'t_c':[12,15],'rh':[85,90]}, 'actions':actions}
