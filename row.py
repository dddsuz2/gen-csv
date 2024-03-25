class Rows:
    name: str
    age: int
    ip_addr: str
    address: str
    phone_number: str

    def toList(self):
        return [self.name, self.age, self.ip_addr, self.address, self.phone_number]

    def toHeader(self):
        return [
            "name",
            "age",
            "ip_addr",
            "address",
            "phone_number",
        ]
