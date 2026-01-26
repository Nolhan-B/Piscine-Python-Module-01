class Plant:
    """Représente une plante."""

    def __init__(self, name, height, age_in_days) -> None:
        """Initialise une plante avec ses données de départ."""
        self.name = name
        self.height = height
        self.age_in_days = age_in_days
        self.grow_sc = 0

    def grow(self) -> None:
        """Augmente la taille et l'age de la plante."""
        self.height += 1
        self.grow_sc += 1

    def age(self) -> None:
        """Vieillit la plante d'un jour."""
        self.age_in_days += 1

    def pass_week(self) -> None:
        """Fait évoluer la plante sur une semaine."""
        i = 1
        while i < 7:
            self.grow()
            self.age()
            i += 1

        def get_info(self) -> None:
            """Affiche les informations de la plante."""
            print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")
            if self.grow_sc > 0:
                print(f"Growth this week: +{self.grow_sc}cm")


def ft_plant_growth():
    """Simule la croissance des plantes sur une semaine."""

    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)

    rose.get_info()
    print("=== Day 7 ===")
    rose.pass_week()

    rose.get_info()


def main():
    """Point d'entrée du programme."""
    ft_plant_growth()


if __name__ == "__main__":
    main()
