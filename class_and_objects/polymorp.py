class India:

    def language(self):
        print("telugu is most spoken language")

    def capital(self):
        print("Delhi is capital city of india")

    def currency(self):
        print("rupee is the currency")

class USA:

    def language(self):
        print("english is most spoken language")

    def capital(self):
        print("new yark is capital")

    def currency(self):
        print("Dollor is the currency")

obj1 = India()
obj2 = USA()

for country in (obj1, obj2):
    country.language()
    country.capital()
    country.currency()

