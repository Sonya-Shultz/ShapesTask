from Shapes2D.Figures.Rectangle import Rectangle
from Shapes2D.Figures.Circle import Circle
from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.Square import Square


class FigureParser:
    input_str = ""
    figure = None
    FIGURES_NAMES = ["Square", "Rectangle", "Circle"]
    status = True

    def start(self):
        while self.status:
            try:
                self.set_from_input()
                self.show_result()
                self.is_end()
            except Exception as e:
                print("Something went wrong:")
                print(str(e), "\n")

    def is_end(self):
        str_val = input("For exit enter 'x', to keep going - any other symbol\n")
        if len(str_val) > 0 and str_val in "xXчЧ":
            self.status = False

    def set_from_input(self):
        str_val = input("Enter your figure: ")
        self.input_str = str_val
        self.figure = self.get_data()

    def set_from_str(self, data_str):
        self.input_str = data_str
        self.figure = self.get_data()

    def get_data(self):
        fig = None
        if self.FIGURES_NAMES[0]+" " in self.input_str:
            fig = Square(self.input_str)
        elif self.FIGURES_NAMES[1]+" " in self.input_str:
            fig = Rectangle(self.input_str)
        elif self.FIGURES_NAMES[2]+" " in self.input_str:
            fig = Circle(self.input_str)
        else:
            fig = Figure(self.input_str)
        return fig

    def res_to_str(self):
        return f"{self.figure.name} Perimeter {self.figure.perimeter()} Area {self.figure.area()}"

    def show_result(self):
        print(self.res_to_str())
