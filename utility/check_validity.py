class Validity:

    def check_phone(self, phone):
        results = False
        number = phone
        count = len(str(number))
        if count == 12:
            valid = int(str(number)[:4])
            if valid == 2547 or valid == 2541:
                results = True
        return results
