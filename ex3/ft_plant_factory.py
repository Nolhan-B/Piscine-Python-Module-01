class Plant:
    """Représente une plante simple."""

    def __init__(self, name, height, age) -> None:
        """Initialise une plante avec ses attributs."""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    """Crée et affiche une collection de plantes."""

    plant_data = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]

    plant_collection = []

    for data in plant_data:
        new_plant = Plant(data[0], data[1], data[2])
        plant_collection.append(new_plant)

    print("=== Plant Factory Output ===")
    i = 0
    for e in plant_collection:
        print(f"Created: {e.name} ({e.height}cm, {e.age} days)")
        i += 1
    print(f"\nTotal plants created: {i}")


def main():
    """Point d'entrée du programme."""
    ft_plant_factory()


if __name__ == "__main__":
    main()
