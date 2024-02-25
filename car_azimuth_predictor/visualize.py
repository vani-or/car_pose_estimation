import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from car_azimuth_predictor.utils.training_tools import np_get_angle_from_double_sigmoids
from car_azimuth_predictor.utils.visualization_tools import plot_image_from_tensor


def visualize_single_predictions(model, test_dataset, save_path=None):
    matplotlib.use('Agg')
    img_counter = 0
    for i, (x_batch, y_true_batch) in enumerate(test_dataset):
        y_pred_batch = model.predict(x_batch)
        for j, x, y_true, y_pred in zip(
            range(len(x_batch)), x_batch, y_true_batch, y_pred_batch
        ):
            y_true_degrees = (
                np_get_angle_from_double_sigmoids(np.expand_dims(y_true, axis=0))
                / np.pi
                * 180
            )
            y_pred_degrees = (
                np_get_angle_from_double_sigmoids(np.expand_dims(y_pred, axis=0))
                / np.pi
                * 180
            )

            plot_image_from_tensor(x, float(y_pred_degrees[0]), y_true_degrees[0])
            filepath = os.path.join(save_path, f"prediction_{img_counter:03d}.png")
            plt.tight_layout()
            plt.savefig(filepath)
            img_counter += 1


def visualize_grid_predictions(model, test_dataset, save_path=None):
    plt.figure(figsize=(24, 24))
    y_true_all = []
    y_pred_all = []

    y_true_angle_all = []
    y_pred_angle_all = []

    for i, (x_batch, y_true_batch) in enumerate(test_dataset):
        y_pred_batch = model.predict(x_batch)
        for i, x, y_true, y_pred in zip(
            range(len(x_batch)), x_batch, y_true_batch, y_pred_batch
        ):

            y_true_all.append(y_true)
            y_pred_all.append(y_pred)

            y_true_degrees = (
                np_get_angle_from_double_sigmoids(np.expand_dims(y_true, axis=0))
                / np.pi
                * 180
            )
            y_pred_degrees = (
                np_get_angle_from_double_sigmoids(np.expand_dims(y_pred, axis=0))
                / np.pi
                * 180
            )

            y_true_angle_all.append(y_true_degrees)
            y_pred_angle_all.append(y_pred_degrees)

            plt.subplot(6, 6, i + 1)
            plot_image_from_tensor(x, float(y_pred_degrees[0]), y_true_degrees[0])
            plt.show()
        if i == 1:
            break
