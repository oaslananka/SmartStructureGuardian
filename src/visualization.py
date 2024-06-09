import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from PIL import Image
import os


def generate_bending_gif(data, filename):
    """
    Generates a GIF file showing the bending and deformation of the bridge.

    Parameters:
        data (pd.DataFrame): The sensor data with stress values.
        filename (str): The name of the GIF file to save.
    """
    # Setup the figure and 3D axis
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Extracting data
    x = data['position_x']
    y = data['position_y']
    stress = data['stress']

    # Generate the bending effect based on stress values
    z = stress * 0.1  # Scale the stress to show bending (adjust as needed)

    # Interpolation to create a smooth bending effect
    xi = np.linspace(x.min(), x.max(), 100)
    yi = np.linspace(y.min(), y.max(), 100)
    xi, yi = np.meshgrid(xi, yi)
    zi = np.interp(xi, x, z)

    def update(num):
        """
        Update function for the animation.
        """
        ax.clear()
        ax.plot_surface(xi, yi, zi * np.sin(num * np.pi / 180), cmap='viridis')
        ax.set_xlabel('Bridge Length (m)')
        ax.set_ylabel('Bridge Width (m)')
        ax.set_zlabel('Bending (scaled)')
        ax.set_title('Bridge Deformation Over Time')
        ax.set_zlim(-10, 10)  # Adjust the z-axis limit for better visualization

    ani = animation.FuncAnimation(fig, update, frames=360, interval=20, blit=False)

    # Save each frame as a separate image
    images = []
    for i in range(360):
        update(i)
        plt.draw()
        image_path = f"frame_{i}.png"
        plt.savefig(image_path)
        images.append(Image.open(image_path))

    # Save as GIF
    images[0].save(filename, save_all=True, append_images=images[1:], duration=20, loop=0)

    # Remove the individual frame images
    for image in images:
        image.close()
        os.remove(image.filename)

    plt.close()


if __name__ == "__main__":
    # File path to the preprocessed sensor data
    file_path = 'data/processed/preprocessed_sensor_data.csv'

    # Load the data
    sensor_data = pd.read_csv(file_path)

    # Generate the GIF showing bridge bending
    generate_bending_gif(sensor_data, 'outputs/figures/bridge_bending_animation.gif')
    print("GIF animation saved to 'outputs/figures/bridge_bending_animation.gif'")
