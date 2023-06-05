import numpy
import matplotlib.pyplot


def main():
    x = numpy.arange(0, 3.5 * 3.14, 0.1)
    x_cos = numpy.arange(0, 3.5 * 3.14, 0.1)
    y = numpy.sin(x)
    z = numpy.cos(x_cos)
    matplotlib.pyplot.plot(x, y, x_cos, z)
    matplotlib.pyplot.xlabel("X values from 0 to 5 pi.")
    matplotlib.pyplot.ylabel("sin(x) and cos(x)")
    matplotlib.pyplot.title("sin and cos from 0 to 5 pi")
    matplotlib.pyplot.legend(["sin(x)", "cos(x)"])
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
