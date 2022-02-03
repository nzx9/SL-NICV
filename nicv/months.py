class DaysPerMonth: 
    def all(self):
        months_dict = {
            "january": 31,
            "february": 29,
            "march": 31,
            "april": 30,
            "may": 31,
            "june": 30,
            "july": 31,
            "august": 31,
            "september": 30,
            "october": 31,
            "november": 30,
            "december": 31,
        }
        return months_dict

    def get_str(self, month:str):
        return self.all()[month.lower()]

    def get_int(self, month:int):
        months_lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month <= 0 or month > 12:
            raise ValueError("month need to be in between 1 and 12")
        else:
            return months_lst[month - 1]