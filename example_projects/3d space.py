from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def create_circle(length):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    zline = np.linspace(0, length, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'black')
    zdata = length * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
    plt.show()


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


def create_3d_lines(x, y):
    x = np.linspace(-x, x, 30)
    y = np.linspace(-y, y, 30)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.contour3D(X, Y, Z, 50)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


def main():
    length = int(input("Enter length of the circle graph: "))
    x = int(input("Enter x:  "))
    y = int(input("Enter y:  "))
    create_circle(length)
    create_3d_lines(x, y)


if __name__ == "__main__":
    main()
