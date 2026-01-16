"""Module de gestion et d’analyse de jardins et de plantes."""


class Human:
    """Représente un être humain propriétaire d’un jardin."""

    def __init__(self, name: str, age: int) -> None:
        """Initialise un humain."""
        self.name = name
        self.age = age


class Plant:
    """Représente une plante de base."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialise une plante."""
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        self.type = "Plant"

    def grow(self) -> None:
        """Fait grandir la plante."""
        self.height += 1
        self.growth += 1
        self.age += 1
        print(f"{self.name} grew 1cm")

    def print_description(self) -> None:
        """Affiche une description simple de la plante."""
        b_desc = f"- {self.name}: {self.height}cm"
        print(f"{b_desc}")


class FloweringPlant(Plant):
    """Représente une plante à fleurs."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialise une plante à fleurs."""
        super().__init__(name, height, age)
        self.color = color
        self.type = "FloweringPlant"

    def print_description(self) -> None:
        """Affiche la description de la plante à fleurs."""
        b_desc = f"- {self.name}: {self.height}cm"
        print(f"{b_desc}, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Représente une fleur pouvant rapporter des points."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialise une fleur à points."""
        super().__init__(name, height, age, color)
        self.prize_points = height // 5
        self.type = "PrizeFlower"

    def print_description(self) -> None:
        """Affiche la description détaillée de la fleur à points."""
        b_desc = f"- {self.name}: {self.height}cm"
        pp = f"Prize points {self.prize_points}"
        print(f"{b_desc}, {self.color} flowers (blooming), {pp}")


class Garden:
    """Représente un jardin contenant des plantes."""

    def __init__(self, owner: Human) -> None:
        """Initialise un jardin."""
        self.owner = owner
        self.name = f"{owner.name}'s garden"
        self.plant_collection = []

    def print_info(self) -> None:
        """Affiche les informations du jardin."""
        print(f"{self.name}, owned by {self.owner.name}")

    def get_plants_count(self) -> int:
        """Retourne le nombre de plantes."""
        total = 0
        for plant in self.plant_collection:
            total += 1
        return total

    def get_plants_growth(self) -> int:
        """Retourne la croissance totale des plantes."""
        total = 0
        for plant in self.plant_collection:
            total += plant.growth
        return total

    def add_plant(self, plant: Plant) -> None:
        """Ajoute une plante au jardin."""
        self.plant_collection.append(plant)

    def update_prizeflowers_pp(self) -> None:
        """Met à jour les points des fleurs à prix."""
        for plant in self.plant_collection:
            if plant.type == "PrizeFlower":
                plant.prize_points = plant.height // 5

    def print_plants_info(self) -> None:
        """Affiche les informations de toutes les plantes."""
        for plant in self.plant_collection:
            plant.print_description()

    def print_plants_evolution(self) -> None:
        """Affiche l’évolution globale des plantes."""
        pcount = self.get_plants_count()
        gcount = self.get_plants_growth()
        print(f"\nPlants Added: {pcount}, Total growth : {gcount}cm")

    def print_plants_type_count(self) -> None:
        """Affiche le nombre de plantes par type."""
        n_regular = 0
        n_flowering = 0
        n_pf = 0
        for plant in self.plant_collection:
            match plant.type:
                case "Plant":
                    n_regular += 1
                case "FloweringPlant":
                    n_flowering += 1
                case "PrizeFlower":
                    n_pf += 1
        regular = f"{n_regular} regular"
        flowering = f"{n_flowering} flowering"
        pf = f"{n_pf} prize flowers"
        print(f"Plant types: {regular}, {flowering}, {pf}")


class GardenNetwork:
    """Représente un réseau de jardins."""

    def __init__(self, name: str) -> None:
        """Initialise un réseau de jardins."""
        self.name = name
        self.garden_collection = []

    def add_garden(self, garden: Garden) -> None:
        """Ajoute un jardin au réseau."""
        self.garden_collection.append(garden)


class GardenManager:
    """Gère la création et la gestion des jardins."""

    network_collection = []

    @staticmethod
    def create_garden(owner: Human) -> Garden:
        """Crée un jardin."""
        return Garden(owner)

    @staticmethod
    def create_garden_network(name: str) -> GardenNetwork:
        """Crée un réseau de jardins."""
        return GardenNetwork(name)

    @staticmethod
    def add_garden_to_network(garden: Garden, network: GardenNetwork) -> None:
        """Ajoute un jardin à un réseau."""
        network.add_garden(garden)

    @staticmethod
    def add_plants_to_garden(garden: Garden, plants: list[Plant]) -> None:
        """Ajoute plusieurs plantes à un jardin."""
        for plant in plants:
            garden.add_plant(plant)
            print(f"Added {plant.name} to {garden.name}")

    @staticmethod
    def make_all_plants_grow_from_garden(garden: Garden) -> None:
        """Fait grandir toutes les plantes du jardin."""
        for plant in garden.plant_collection:
            plant.grow()

    class GardenStats:
        """Fournit des statistiques sur les jardins."""

        @staticmethod
        def print_garden_report(garden: Garden) -> None:
            """Affiche l’en-tête du rapport du jardin."""
            print(f"\n=== {garden.owner.name}'s Garden Report ===")

        @staticmethod
        def get_pp_from_garden(garden: Garden) -> int:
            """Calcule le score total du jardin."""
            garden_pp = 0
            for plant in garden.plant_collection:
                garden_pp += 2
                if plant.type == "PrizeFlower":
                    garden_pp += plant.prize_points
                garden_pp += plant.height
            return garden_pp

        @staticmethod
        def print_garden_managed_in_network(network: GardenNetwork) -> None:
            """Affiche le nombre de jardins du réseau."""
            count = 0
            for garden in network.garden_collection:
                count += 1
            print(f"Total gardens managed: {count}")

        @staticmethod
        def print_all_stats_from_garden(garden: Garden) -> None:
            """Affiche toutes les statistiques d’un jardin."""
            garden.update_prizeflowers_pp()
            garden.print_plants_info()
            garden.print_plants_evolution()
            garden.print_plants_type_count()

        @staticmethod
        def print_gardens_score_from_network(network: GardenNetwork) -> None:
            """Affiche les scores de tous les jardins du réseau."""
            last = 0
            i = 0
            string = "Garden scores - "
            for garden in network.garden_collection:
                last += 1
            for garden in network.garden_collection:
                i += 1
                g_pp = GardenManager.GardenStats.get_pp_from_garden(garden)
                if i == last:
                    string += f"{garden.owner.name}: {g_pp}"
                else:
                    string += f"{garden.owner.name}: {g_pp}, "
            print(f"{string}")


def ft_garden_analytics() -> None:
    """Fonction de démonstration du système de gestion de jardin."""

    nbilyj = Human("nbilyj", 20)
    print("=== Garden Management System Demo ===\n")
    MyGardenNetwork = GardenManager.create_garden_network("Network 1")

    my_garden = GardenManager.create_garden(nbilyj)
    GardenManager.add_garden_to_network(my_garden, MyGardenNetwork)

    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 35, "yellow")
    oak = Plant("Oak Tree", 100, 1825)
    GardenManager.add_plants_to_garden(my_garden, [oak, rose, sunflower])

    print()

    GardenManager.make_all_plants_grow_from_garden(my_garden)

    GardenManager.GardenStats.print_garden_report(my_garden)
    GardenManager.GardenStats.print_all_stats_from_garden(my_garden)

    GardenManager.GardenStats.print_gardens_score_from_network(MyGardenNetwork)
    GardenManager.GardenStats.print_garden_managed_in_network(MyGardenNetwork)

    print()


def main():
    """Point d’entrée principal du programme."""
    ft_garden_analytics()


if __name__ == "__main__":
    main()
