import matplotlib.pyplot as plt


def plot_training_curves(train_history, plot_title):
    plt.plot(train_history["loss"])
    plt.plot(train_history["val_loss"])
    plt.title(plot_title)
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.grid()
    plt.legend(["Train", "Val"], loc="upper left")
    plt.show()
