import math
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw


def plot_scheme(angle_pred, angle_true=None):
    image_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../static_files', "vehicle_scheme.jpg"))
    with Image.open(image_path) as img:
        w, h = img.size

        img1 = ImageDraw.Draw(img)

        angle_pred *= -1
        coords_pred = [
            w // 2,
            h // 2,
            w // 2 + math.cos(angle_pred / 180 * math.pi) * max(w, h),
            h // 2 + math.sin(angle_pred / 180 * math.pi) * max(w, h),
        ]
        img1.line(coords_pred, fill="red", width=2)

        if angle_true is not None:
            angle_true *= -1
            coords_true = [
                w // 2,
                h // 2,
                w // 2 + math.cos(angle_true / 180 * math.pi) * max(w, h),
                h // 2 + math.sin(angle_true / 180 * math.pi) * max(w, h),
            ]

            img1.line(coords_true, fill=(0, 200, 0), width=2)

        return img


# plot_scheme(-170, -0).show()


def plot_image_from_tensor(image_tensor, y_pred_angle, y_true_angle=None, resize_to=(480, 480)):
    if not isinstance(image_tensor, np.ndarray):
        image_tensor = image_tensor.numpy()
    data = image_tensor.astype(int)

    orig_image = Image.fromarray(data.astype("uint8"), "RGB")
    # Resize keeping the aspect ratio
    resize_to = (min(resize_to[0], orig_image.size[0]), min(resize_to[1], orig_image.size[1]))
    orig_image.thumbnail(resize_to, Image.LANCZOS)

    scheme = plot_scheme(y_pred_angle, y_true_angle)
    scheme.thumbnail(
        (orig_image.size[0] * 0.4, orig_image.size[1] * 0.4), Image.LANCZOS
    )

    orig_image.paste(
        scheme,
        (orig_image.size[0] - scheme.size[0], 0, orig_image.size[0], scheme.size[1]),
    )

    plt.imshow(orig_image)
    title = f"Predicted: {round(y_pred_angle, 2)}"
    if y_true_angle is not None:
        title += f", GT: {round(y_true_angle, 2)}"
    plt.title(title)
    plt.axis("off")


def plot_image_from_path(image_path, y_pred, y_true=None):
    data = Image.open(image_path)
    data = np.array(data)

    return plot_image_from_tensor(data, y_pred, y_true)
