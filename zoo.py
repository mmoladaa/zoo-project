class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            return None  # or raise an error
        elif 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        else:  # age > 60
            return 100