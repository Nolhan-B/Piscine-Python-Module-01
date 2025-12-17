def ft_plant_growth():
    class Plant:
        def __init__(self, name, height, age_in_days):
            self.name = name
            self.height = height
            self.age_in_days = age_in_days
            self.grow_sc = 0

        def grow(self):
            self.height += 1
            self.grow_sc += 1

        def age(self):
            self.age_in_days += 1

        def pass_week(self):
            i = 1
            while i < 7:
                self.grow()
                self.age()
                i += 1

        def get_info(self):
            print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")
            if self.grow_sc > 0:
                print(f"Growth this week: +{self.grow_sc}cm")

    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 63, 60)

    rose.get_info()
    oak.get_info()
    print("=== Day 7 ===")
    rose.pass_week()
    oak.pass_week()

    oak.get_info()
    rose.get_info()


def main():
    ft_plant_growth()


if __name__ == "__main__":
    main()
