from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a King character."""
    def __init__(self, name, is_alive=True, eyes="brown", hairs="dark"):
        """Init a King character by calling the constructor of the parent
        and adding family_name, eyes and hairs variables."""
        super().__init__(name, is_alive)

    @property
    def eyes(self):
        """Return the eye color."""
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        """Change the eye color."""
        self._eyes = value

    @property
    def hairs(self):
        """Return the hair color."""
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        """Change the hair color."""
        self._hairs = value

    def get_eyes(self):
        """Get the eyes color using the property."""
        return self.eyes

    def get_hairs(self):
        """Get the hair color using the property."""
        return self.hairs

    def set_eyes(self, value):
        """Set the eyes color using the property."""
        self.eyes = value

    def set_hairs(self, value):
        """Set the hairs color using the property."""
        self.hairs = value


def main():
    """Run the program and handle errors."""
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
        print(f"Order in which python search for parent's method \
    and attribute: {King.__mro__}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
