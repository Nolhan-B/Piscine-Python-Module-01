def ft_garden_security():
    class SecurePlant:
        def __init__(self, name, height=0, age=0):
            self.name = name
            self.__height = height
            self.__age = age

        errmsg = "\nInvalid operation attempted:"

        def set_height(self, height):
            if height < 0:
                print(f"{self.errmsg} height {height}cm [REJECTED]")
                print("Security: Negative height rejected")
            else:
                self.__height = height
                print(f"Height updated: {height}cm [OK]")

        def set_age(self, age):
            if age < 0:
                print(f"{self.errmsg} age {age} days [REJECTED]")
                print("Security: Negative age rejected\n")
            else:
                self.__age = age
                print(f"Age updated: {age} days [OK]")

        def get_height(self):
            return self.__height

        def get_age(self):
            return self.__age

        def get_info(self):
            return f"{self.name} ({self.get_height()}cm, {self.get_age()}days)"

    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print(f"Current plant: {rose.get_info()}")


def main():
    ft_garden_security()


if __name__ == "__main__":
    main()
