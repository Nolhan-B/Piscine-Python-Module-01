class Plant:
    """Classe de base représentant une plante."""

    def __init__(self, name, height, age) -> None:
        """Initialise une plante générique."""
        self.name = name
        self.height = height
        self.age = age
        self.type = "Plant"

    def get_info(self) -> None:
        """Retourne les informations de la plante."""
        intro = f"{self.name} ({self.type}):"
        height_info = f"{self.height}cm"
        age_info = f"{self.age} days"
        return f"{intro} {height_info}, {age_info}"


class Flower(Plant):
    """Représente une fleur."""

    def __init__(self, name, height, age, color) -> None:
        """Initialise une fleur."""
        super().__init__(name, height, age)
        self.color = color
        self.type = "Flower"

    def bloom(self) -> None:
        """Fait éclore la fleur."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """Affiche les informations de la fleur."""
        parent_info = super().get_info()
        print(f"{parent_info}, {self.color} color")


class Tree(Plant):
    """Représente un arbre."""

    def __init__(self, name, height, age, trunk_diameter) -> None:
        """Initialise un arbre."""
        super().__init__(name, height, age)
        self.type = "Tree"
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        """Affiche les informations de l'arbre."""
        parent_info = super().get_info()
        print(f"{parent_info}, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Calcule et affiche l'ombre produite."""
        shade = (2 * 3.14 * (self.trunk_diameter / 2) * self.height) / 1000
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    """Représente un légume."""

    def __init__(self,
                 name,
                 height,
                 age,
                 harvest_season,
                 nutritional_value) -> None:
        """Initialise un légume."""
        super().__init__(name, height, age)
        self.type = "Vegetable"
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        """Affiche les informations du légume."""
        parent_info = super().get_info()
        print(f"{parent_info}, {self.harvest_season} harvest")

    def get_nutritional(self) -> None:
        """Affiche la valeur nutritionnelle."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    """Gère différents types de plantes."""

    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()

    print()

    oak = Tree("Oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()

    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    tomato.get_info()
    tomato.get_nutritional()

    # print()

    # tulip = Flower("Tulip", 35, 45, "yellow")
    # tulip.get_info()
    # tulip.bloom()

    # print()

    # pine = Tree("Pine", 800, 3650, 60)
    # pine.get_info()
    # pine.produce_shade()

    # print()

    # tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    # tomato.get_info()
    # tomato.get_nutritional()

    # print()

    # carrot = Vegetable("Carrot", 40, 75, "autumn", "beta-carotene")
    # carrot.get_info()
    # carrot.get_nutritional()
##########


def main():
    ft_plant_types()


if __name__ == "__main__":
    main()
