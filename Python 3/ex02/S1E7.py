from S1E9 import Character


class Baratheon(Character):
    """Representing a Baratheon character."""
    def __init__(self, name, is_alive=True, eyes="brown", hairs="dark"):
        """Init a Baratheon character by calling the constructor of the parent
        and adding family_name, eyes and hairs variables."""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """Overload str method to return a string of his characteristics."""
        return repr(self)

    def __repr__(self):
        """Overload repr method to return a string of his characteristics."""
        values = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {values}"


class Lannister(Character):
    """Representing a Lannister character."""
    def __init__(self, name, is_alive=True, eyes="blue", hairs="light"):
        """Init a Lannister character by calling the constructor of the parent
            and adding family_name, eyes and hairs variables."""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """Overload str method to return a string of his characteristics."""
        return repr(self)

    def __repr__(self):
        """Overload repr method to return a string of his characteristics."""
        values = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {values}"

    @classmethod
    def create_lannister(cls, name: str, is_alive=True):
        """Return a new Lannister class."""
        return cls(name, is_alive)
