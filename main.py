import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


WIDTH = 400
HEIGHT = 400

def create_matrix_1(values):

    X = np.zeros((HEIGHT, WIDTH))

    for i in range(HEIGHT):
        for j in range(WIDTH):

            if (i < int(HEIGHT*0.1)) or (i > HEIGHT-int(HEIGHT*0.1)):
                X[i, j] = 0

            elif np.abs(i - j) < len(values):
                X[i, j] = values[np.abs(i-j)]

            else:
                X[i, j] = 0

    return X


def create_matrix_2(values):

    X = np.zeros((HEIGHT, WIDTH))
    T1 = int((WIDTH-len(values)) / 2)
    T2 = WIDTH - T1

    k = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):

            if (i < int(HEIGHT*0.1)) or (i > HEIGHT-int(HEIGHT*0.1)):
                X[i, j] = 0

            elif j > T1 and j < T2:
                value = values[k]
                X[i, j] = values[value]
                k = (k + 1) % len(values)

            else:
                X[i, j] = 0

    return X




def print_matrix(X):
    print("\n\n")
    for row in X:
        print("\t", end="")
        for value in row:
            print(str(value) + "   ", end="")
        print("\n")
    print("\n\n")


def plot_image(grid_1, grid_2, grid_combos):

    x = np.array([i for i in range(WIDTH)])
    y = np.array([i for i in range(HEIGHT)])

    fig = plt.figure()

    base_grids = [grid_1, grid_2]

    for i in range(1, 3):
        a = fig.add_subplot(3, 2, i)
        a.set_title("RF{}".format(i))
        imgplot = plt.imshow(base_grids[i-1], extent=(x.min(), x.max(), y.max(), y.min()),
                   interpolation='nearest', cmap=cm.afmhot)

    labels = ["a*RF1 + b*RF2; a > b", "a*RF1 + b*RF2; a < b", "a*RF1 + b*RF2; a == b"]
    k = 3
    for i in range(len(grid_combos)):
        a = fig.add_subplot(3, 2, k)
        a.set_title(labels[i])
        imgplot = plt.imshow(grid_combos[i], extent=(x.min(), x.max(), y.max(), y.min()),
                   interpolation='nearest', cmap=cm.afmhot)
        k += 1


    plt.show()




def main():

    values_1_positive = [x for x in range(100, 50, -1)]
    values_1_negative = [-50 for x in range(len(values_1_positive))]

    values_1 = values_1_positive + values_1_negative


    values_reversed = values_1[::-1][:-1]
    values_2 = values_reversed + values_1


    A = 40
    B = 10

    grid_1 = create_matrix_1(values_1)
    grid_2 = create_matrix_2(values_2)
    grid_combo_1 = A*grid_1 + B*grid_2
    grid_combo_2 = B*grid_1 + A*grid_2
    grid_combo_3 = B*grid_1 + B*grid_2

    grid_combos = [grid_combo_1, grid_combo_2, grid_combo_3]

    # print_matrix(grid)

    plot_image(grid_1, grid_2, grid_combos)




if __name__ == '__main__':
    main()
