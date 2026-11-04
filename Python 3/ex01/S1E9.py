from abc import ABC, abstractmethod


class Character(ABC):
    """Character class contain a first_name and an is_alive variables.
    Contain an init and a die function."""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Init the class by initializing his first_name and his is_alive
        variables."""
        self.first_name = name
        self.is_alive = is_alive

    def die(self):
        """Make the Character die by putting his variable is_alive to False."""
        self.is_alive = False


class Stark(Character):
    """Representing a Stark character."""
    def __init__(self, name, is_alive=True):
        """Init a Stark character by calling the constructor of the parent."""
        super().__init__(name, is_alive)
