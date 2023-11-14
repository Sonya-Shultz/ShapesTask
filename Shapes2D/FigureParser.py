from Shapes2D.Figures.Rectangle import Rectangle
from Shapes2D.Figures.Circle import Circle
from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.Square import Square


class FigureParser:
    """
    Main class for parsing users input.
    Contains one (last) figure from user's input and ask user input in loop until exit.

    Consts:
    - FIGURES_NAMES (array of strings): Names of all avalible shapes.
    Var:
    - input_str (string): User inpt in string format.
    - figure (Figure obj): None in start, after parsing - object of Figure or its' child classes.
    - status (bool): True until loop is runing.
    """
    input_str = ""
    figure = None
    FIGURES_NAMES = ["Square", "Rectangle", "Circle"]
    status = True

    def start(self):
        """
           The main loop where users can enter theirs shapes util pressed "x".

           Args:
           - none

           Returns:
           - none.
        """
        while self.status:
            try:
                self.set_from_input()
                self.show_result()
                self.is_end()
            except Exception as e:
                print("Something went wrong:")
                print(str(e), "\n")
                self.is_end()


    def is_end(self):
        """
           A function that asks if user wants to stop the program.

           Args:
           - none

           Returns:
           - none.
        """
        str_val = input("For exit enter 'x', to keep going - any other symbol\n")
        if len(str_val) > 0 and str_val in "xXчЧ":
            self.status = False

    def set_from_input(self):
        """
           Rerads users input and parses it to some of the shapes.
           Saves this shape to self.figure and user input to self.input_str

           Args:
           - none

           Returns:
           - none.
        """
        str_val = input("Enter your figure: ")
        self.input_str = str_val
        self.figure = self.get_data()

    def set_from_str(self, data_str):
        """
            Sets users string and parses it to some of the shapes.
            Saves this shape to self.figure and data_str to self.input_str

            Args:
            - data_str (string): string with information about shape for parsing

            Returns:
            - none.
        """
        self.input_str = data_str
        self.figure = self.get_data()

    def get_data(self):
        """
            Checks first keyword of input and create corresponding 2d-shape

            Args:
            - none

            Returns:
            - Figure obj: if input data in right format - returns child class obj of Figure.
        """
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
        return f"{self.figure.NAME} Perimeter {self.figure.perimeter()} Area {self.figure.area()}"

    def show_result(self):
        print(self.res_to_str())
