import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(path):
    image = cv2.imread(path)
    return image


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def apply_filter(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred


def detect_edges(image):
    edges = cv2.Canny(image, 100, 200)
    return edges


def run_pipeline(image_path):
    image = load_image(image_path)
    gray = preprocess_image(image)
    filtered = apply_filter(gray)
    edges = detect_edges(filtered)
    return image, edges

  if __name__ == "__main__":
    original, edges = run_pipeline("sample_image.jpg")

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Edges")
    plt.imshow(edges, cmap="gray")
    plt.axis("off")

    plt.show()
