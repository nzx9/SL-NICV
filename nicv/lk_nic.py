import re
from months import DaysPerMonth

class LK_NIC:
    origin = "LK"
    nic = None
    re_10_dig = "[0-9]{9}[vxVX]{1}"
    re_12_dig = "[0-9]{12}"
    nic_type = None
    year =  None,
    month = None,
    day = None
    gender = None

    def __init__(self, nic: str):
        self.nic = nic
        if self.valid():
            ttl_passed = 0
            if self.nic_type == "10digit":
                self.year = "19{}".format(self.nic[0:2])
                g_clc = int(nic[2:5])
            elif(len(nic) == 12):
                self.year  = self.nic[0:4]
                g_clc = int(nic[4: 7])

            if(g_clc > 500):
                self.gender = "female"
                g_clc = g_clc - 500
            else:
                self.gender = "male"

            dpm = DaysPerMonth()
            for month in dpm.all(): 
                ttl_passed = ttl_passed + dpm.get_str(month)
                if(g_clc <= ttl_passed):
                    self.month = month
                    self.day = g_clc - ttl_passed + dpm.get_str(month)
                    break
        else:
            raise ValueError("Not a valid NIC. \nLength of the `{} NIC` need to be in between 10 and 12 characters. \n10 character NICs need to be in XXXXXXXXXc format where Xs are digits and c is v or x. \n12 character NICs need to be in XXXXXXXXXXXX format where Xs are digits.".format(self.origin))
    
    def valid(self):
        if len(self.nic) == 10 and re.match(self.re_10_dig, self.nic):
            self.nic_type = "10digit"
            return True
        elif len(self.nic) == 12 and re.match(self.re_12_dig, self.nic):
            self.nic_type = "12digit"
            return True
        else:
            return False       

    def origin(self):
        return self.origin

    def dob(self):
        return {
            "year" : self.year,
            "month" : self.month,
            "day" : self.day
            }