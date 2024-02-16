class Email:
    def __init__(self, user, domain):
        self.user = user
        self.domain = domain

    def __eq__(self, other):
        return self.user == other.user and \
            self.domain == self.domain

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"Email address: {self.user}@{self.domain}"


email_one = Email('vasil_a_g', 'hotmail.com')
email_two = Email('vasil_a_g', 'hotmail.com')

print(email_one)
print(email_one == email_two)

