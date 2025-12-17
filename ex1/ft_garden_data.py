def ft_garden_data():
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def present(self):
            print(f"{self.name}: {self.height}cm, {self.age} years old")

    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.present()
    sunflower.present()
    cactus.present()


def main():
    ft_garden_data()


if __name__ == "__main__":
    main()
