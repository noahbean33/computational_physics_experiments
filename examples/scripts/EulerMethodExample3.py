from matplotlib import pyplot as plt


def f(g, l, x, b, v):
    return (-g / l) * x - b * v


def euler_method(x=0, v=1, g=9.8, b=0.01, l=1, dt=0.001):
    x_values = []
    t_values = []
    t = 0

    while t < 100:
        x_values.append(x)
        t_values.append(t)
        v = v + dt * f(g, l, x, b, v)
        x = x + v * dt
        t = t + dt

    plt.plot(t_values, x_values)
    plt.show()


if __name__ == '__main__':
    euler_method()