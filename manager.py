from rectangle_creator import RectangleCreator
from logic import Logic
from view import View


def main():
    size = 1
    ls = RectangleCreator.get_rectangle(size)
    total_square = Logic.calculate_total_square(ls)
    total_perimetr = Logic.calculate_total_perimetr(ls)

    msg = (f"Total square = {total_square}\n"
           f"Total perimetr = {total_perimetr}")

    print(View.convert(ls))
    print(msg)


if __name__ == "__main__":
    main()
