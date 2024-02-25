import numpy as np

from car_azimuth_predictor.utils.training_tools import (
    np_get_angle_from_double_sigmoids,
    tf_get_angle_from_double_sigmoids,
)


def test_angle_decoding():
    np.random.seed(0)
    test_angles = (np.random.random(size=(1000,)) * 2 - 1) * np.pi
    alfa = np.abs(test_angles) / np.pi
    beta = test_angles - np.pi / 2
    beta -= (beta >= np.pi) * 2 * np.pi
    beta += (beta < -np.pi) * 2 * np.pi
    beta /= np.pi
    beta = np.abs(beta)

    sigmoids = np.stack([alfa, beta]).T
    angles_recovered_np = np_get_angle_from_double_sigmoids(y_sigmoids=sigmoids)
    assert all(np.round(angles_recovered_np, 10) == np.round(test_angles, 10))

    angles_recovered_tf = (
        tf_get_angle_from_double_sigmoids(y_output=sigmoids).numpy().astype(np.float64)
    )
    assert np.sum(np.round(test_angles - angles_recovered_tf, 6)) == 0
