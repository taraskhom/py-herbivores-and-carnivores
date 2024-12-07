from __future__ import annotations


class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            Animal.alive.append(self)

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
        )

    def __repr__(self) -> str:

        return f"{{{self}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Herbivore | Carnivore) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
