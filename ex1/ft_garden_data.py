def ft_garden_data() -> None:
    """Gère et affiche les données des plantes du jardin."""

    class Plant:
        """Représente une plante du jardin."""

        def __init__(self, name, height, age) -> None:
            """Initialise une plante avec un nom, une taille et un âge."""
            self.name = name
            self.height = height
            self.age = age

        def present(self) -> None:
            """Affiche les informations de la plante."""
            print(f"{self.name}: {self.height}cm, {self.age} years old")

    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.present()
    sunflower.present()
    cactus.present()


def main():
    """Point d'entrée du programme."""
    ft_garden_data()


if __name__ == "__main__":
    main()
