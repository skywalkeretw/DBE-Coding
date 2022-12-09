import functools
import os

from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from uuid import uuid4
from flask import Flask, render_template, request

app=Flask(__name__)
# @title Define image loading and visualization functions  { display-mode: "form" }

def crop_center(image):
  """Returns a cropped square image."""
  shape = image.shape
  new_shape = min(shape[1], shape[2])
  offset_y = max(shape[1] - shape[2], 0) // 2
  offset_x = max(shape[2] - shape[1], 0) // 2
  image = tf.image.crop_to_bounding_box(
      image, offset_y, offset_x, new_shape, new_shape)
  return image

@functools.lru_cache(maxsize=None)
def load_image(image_url, image_size=(256, 256), preserve_aspect_ratio=True):
    """Loads and preprocesses images."""
    # Cache image file locally.
    image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:], image_url)
    # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
    img = tf.io.decode_image(
        tf.io.read_file(image_path),
        channels=3, dtype=tf.float32)[tf.newaxis, ...]
    img = crop_center(img)
    img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
    return img

def show_n(images, titles=('',)):
    n = len(images)
    image_sizes = [image.shape[1] for image in images]
    w = (image_sizes[0] * 6) // 320
    plt.figure(figsize=(w * n, w))
    gs = gridspec.GridSpec(1, n, width_ratios=image_sizes)
    for i in range(n):
        plt.subplot(gs[i])
        plt.imshow(images[i][0], aspect='equal')
        plt.axis('off')
        plt.title(titles[i] if len(titles) > i else '')
    plt.savefig('/static/funny.png')
    

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():

    if request.method == 'POST':
        content_image_url = request.form['content_image_url']
        style_image_url = request.form['style_image_url']
        output_image_size = 384  # @param {type:"integer"}

        # The content image size can be arbitrary.
        content_img_size = (output_image_size, output_image_size)
        # The style prediction model was trained with image size 256 and it's the 
        # recommended image size for the style image (though, other sizes work as 
        # well but will lead to different results).
        style_img_size = (256, 256)  # Recommended to keep it at 256.

        content_image = load_image(content_image_url, content_img_size)
        style_image = load_image(style_image_url, style_img_size)
        style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')
        # Stylize content image with given style image.
        # This is pretty fast within a few milliseconds on a GPU.

        outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
        stylized_image = outputs[0]

        # Visualize input images and the generated stylized image.

        show_n([content_image, style_image, stylized_image], titles=['Original content image', 'Style image', 'Stylized image'])
        return render_template('index.html', img=True,)
    else:
        return render_template('index.html', img=False,)


if __name__ == '__main__':
    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    global hub_module
    hub_module = hub.load(hub_handle)

    app.run(debug=False, host='0.0.0.0', port=8080)