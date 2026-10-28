class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def set_width(self, width):
        self.width = width

    def set_heigth(self, heigth):
        self.heigth = heigth

    def get_area(self):
        return self.width * self.heigth

    def get_perimeter(self):
        return 2 * (self.width + self.heigth)

    def get_diagonal(self):
        return (self.width ** 2 + self.heigth ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.heigth > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.heigth):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.heigth // shape.heigth)

    def __str__(self):
        return f"Rectangle(width={self.width}, heigth={self.heigth})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.heigth = side

    def set_width(self, side):
        self.width = side
        self.heigth = side

    def set_heigth(self, side):
        self.width = side
        self.heigth = side

    def __str__(self):
        return f"Square(side={self.width})"