import dataclasses

@dataclasses.dataclass
class Rows:
    name: str = None
    age: int = None
    ip_addr: str = None
    address: str = None
    phone_number: str = None

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
