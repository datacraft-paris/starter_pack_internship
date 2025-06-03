import typing as t
from typing import Optional
from IPython import embed
from functools import cache

@cache
def square(x):
    return x**2

class Datacrafter:
    def __init__(self, first_name: str, last_name: str, company: str, interests: Optional[t.List[str]] = None, email: Optional[str] = None) -> "Datacrafter":
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.company = company
        self.interests = interests if interests is not None else []

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def _get_email(self) -> Optional[str]:
        if self.company == "datacraft":
            return f"{self.first_name.lower()}.{self.last_name.lower()}@datacraft.paris"
        return None

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def greet() -> str:
        return "Welcome"


class DatacraftManager(Datacrafter):
    def __init__(self, first_name: str, last_name: str, company: str, interests: Optional[t.List[str]] = None, email: Optional[str] = None, interns: Optional[t.List[Datacrafter]] = None):
        super().__init__(first_name=first_name, last_name=last_name, email=email, company=company, interests=interests)
        self.interns = {intern.first_name: intern for intern in interns} if interns else None

    def __repr__(self) -> str:
        intern_list = " - ".join(list(self.interns.keys())) if self.interns else "No intern"
        return f"{super().__repr__()} - Interns: {intern_list}"

    def print_interns(self):
        if self.interns:
            for _, intern in self.interns.items():
                print(intern)
        else:
            print("No intern")


class Member:
    def __init__(self, first_name: str, last_name: str, company: str, position: str, phone: str, email: str) -> "Member":
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.phone = phone
        self.email = email

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.position} at {self.company}"

    @property
    def contact_details(self) -> str:
        return f"Email: {self.email}, Phone: {self.phone}"


class Freelancer(Member):
    def __init__(self, first_name: str, last_name: str, phone: str, profession: str, email: str, specialty: str, client: str):
        super().__init__(first_name=first_name, last_name=last_name, company=client, position=profession, phone=phone, email=email)
        self.specialty = specialty

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.position}, Specialty: {self.specialty}, Client: {self.company}"


def main():
    remy = Datacrafter(first_name="Remy", last_name="Gasmi", company="datacraft")
    thais = Datacrafter(first_name="Thais", last_name="Denoyelle", company="datacraft")
    raphael = DatacraftManager(first_name="Raph", last_name="Vienne", company="datacraft", interns=[remy, thais])

    alex = Freelancer(first_name="Alex", last_name="Martin", phone="0601020304", profession="Developer", email="alex.martin@mail.com", specialty="Python", client="TechCorp")
    julie = Member(first_name="Julie", last_name="Dupont", company="TechCorp", position="CTO", phone="0605060708", email="julie.dupont@techcorp.com")

    embed()
    return remy, thais, raphael, alex, julie

if __name__ == '__main__':
    main()
