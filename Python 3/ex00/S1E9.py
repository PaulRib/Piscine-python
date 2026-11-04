from abc import ABC, abstractmethod


class Character(ABC):
    """Character class contain a first_name and a is_alive variables.
    Contain a init and a die function."""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Init the class by initializing his first_name and his is_alive
        variables"""
        self.first_name = name
        self.is_alive = is_alive

    def die(self):
        """Make the Character die by putting his variable is_alive to False."""
        self.is_alive = False


class Stark(Character):
    """Represent a Stark character."""
    def __init__(self, name, is_alive=True):
        """Init the class by calling the constructor of the parent."""
        super().__init__(name, is_alive)


def main():
    """Run the program and handle errors."""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    hodor = Character("hodor")
    hodor.die()


if __name__ == "__main__":
    main()
