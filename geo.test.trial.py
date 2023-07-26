import matplotlib.pyplot as plt
import numpy as np

def plot_circle(radius):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    plt.plot(x, y)
    plt.axis('equal')
    plt.title("Circle with radius {}".format(radius))
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def plot_triangle(vertices):
    x = [vertices[0][0], vertices[1][0], vertices[2][0], vertices[0][0]]
    y = [vertices[0][1], vertices[1][1], vertices[2][1], vertices[0][1]]
    plt.plot(x, y)
    plt.axis('equal')
    plt.title("Triangle")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def plot_rectangle(length, width):
    x = [0, length, length, 0, 0]
    y = [0, 0, width, width, 0]
    plt.plot(x, y)
    plt.axis('equal')
    plt.title("Rectangle with length {} and width {}".format(length, width))
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def plot_square(side):
    x = [0, side, side, 0, 0]
    y = [0, 0, side, side, 0]
    plt.plot(x, y)
    plt.axis('equal')
    plt.title("Square with side length {}".format(side))
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def plot_parallelogram(base, height):
    x = [0, base, base + height, height, 0]
    y = [0, 0, height, height, 0]
    plt.plot(x, y)
    plt.axis('equal')
    plt.title("Parallelogram with base {} and height {}".format(base, height))
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def plot_trapezoid(base1, base2, height):
    x = [0, base1, base2, 0, 0]
    y = [0, 0, height, height, 0]
    plt.plot(x, y)
    plt.axis('equal')
    plt.title("Trapezoid with base1 {}, base2 {}, and height {}".format(base1, base2, height))
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def calc_circle():
    measure = input("Do you want to calculate the circumference or the area of the circle? ")
    if measure.lower() == 'circumference':
        radius = float(input("Enter the radius: "))
        circumference = 2 * np.pi * radius
        print("The circumference of the circle is:", circumference)
        plot_circle(radius)
    elif measure.lower() == 'area':
        radius = float(input("Enter the radius: "))
        area = np.pi * radius ** 2
        print("The area of the circle is:", area)
        plot_circle(radius)
    else:
        print("Invalid measure choice. Please try again.")

def calc_triangle():
    measure = input("Do you want to calculate the perimeter or the area of the triangle? ")
    if measure.lower() == 'perimeter':
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
        perimeter = side1 + side2 + side3
        print("The perimeter of the triangle is:", perimeter)
        vertices = [(0, 0), (side1, 0), (side2, side3)]
        plot_triangle(vertices)
    elif measure.lower() == 'area':
        base = float(input("Enter the length of the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print("The area of the triangle is:", area)
        vertices = [(0, 0), (base, 0), (base / 2, height)]
        plot_triangle(vertices)
    else:
        print("Invalid measure choice. Please try again.")

def calc_rectangle():
    measure = input("Do you want to calculate the perimeter or the area of the rectangle? ")
    if measure.lower() == 'perimeter':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        perimeter = 2 * (length + width)
        print("The perimeter of the rectangle is:", perimeter)
        plot_rectangle(length, width)
    elif measure.lower() == 'area':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print("The area of the rectangle is:", area)
        plot_rectangle(length, width)
    else:
        print("Invalid measure choice. Please try again.")

def calc_square():
    measure = input("Do you want to calculate the perimeter or the area of the square? ")
    if measure.lower() == 'perimeter':
        side = float(input("Enter the side length: "))
        perimeter = 4 * side
        print("The perimeter of the square is:", perimeter)
        plot_square(side)
    elif measure.lower() == 'area':
        side = float(input("Enter the side length: "))
        area = side ** 2
        print("The area of the square is:", area)
        plot_square(side)
    else:
        print("Invalid measure choice. Please try again.")

def calc_parallelogram():
    measure = input("Do you want to calculate the perimeter or the area of the parallelogram? ")
    if measure.lower() == 'perimeter':
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))
        perimeter = 2 * (base + height)
        print("The perimeter of the parallelogram is:", perimeter)
        plot_parallelogram(base, height)
    elif measure.lower() == 'area':
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))
        area = base * height
        print("The area of the parallelogram is:", area)
        plot_parallelogram(base, height)
    else:
        print("Invalid measure choice. Please try again.")

def calc_trapezoid():
    measure = input("Do you want to calculate the perimeter or the area of the trapezoid? ")
    if measure.lower() == 'perimeter':
        base1 = float(input("Enter the length of base 1: "))
        base2 = float(input("Enter the length of base 2: "))
        height = float(input("Enter the height: "))
        perimeter = base1 + base2 + 2 * height
        print("The perimeter of the trapezoid is:", perimeter)
        plot_trapezoid(base1, base2, height)
    elif measure.lower() == 'area':
        base1 = float(input("Enter the length of base 1: "))
        base2 = float(input("Enter the length of base 2: "))
        height = float(input("Enter the height: "))
        area = 0.5 * (base1 + base2) * height
        print("The area of the trapezoid is:", area)
        plot_trapezoid(base1, base2, height)
    else:
        print("Invalid measure choice. Please try again.")

def show_available_shapes():
    print("Available shapes:")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Parallelogram")
    print("6. Trapezoid")

def main():
    while True:
        show_available_shapes()
        choice = input("Enter the number of the shape you desire for me to calculate (or press Enter to exit): ")
        if choice == "":
            print("Maybe next time")
            break
        elif choice == "1":
            calc_circle()
            plt.close()  # Close the plot window after displaying the graph
        elif choice == "2":
            calc_triangle()
            plt.close()  # Close the plot window after displaying the graph
        elif choice == "3":
            calc_rectangle()
            plt.close()  # Close the plot window after displaying the graph
        elif choice == "4":
            calc_square()
            plt.close()  # Close the plot window after displaying the graph
        elif choice == "5":
            calc_parallelogram()
            plt.close()  # Close the plot window after displaying the graph
        elif choice == "6":
            calc_trapezoid()
            plt.close()  # Close the plot window after displaying the graph
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

