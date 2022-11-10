# Universal Image Generator:

### [app.py contains Universal Prompt Formula](https://github.com/tboie/universal_image_generator/blob/master/app.py)

### Install:

- `pip install -r requirements.txt` (python 3.8+ required)
- run server with `flask run`

### Info:

- `app.py` is the server file and calls `demo.py` with prompt string as argument
- `/templates/home.html` is the web file
- image file saved to `/output/output.png`

- EXTRA: image color pallete generation with imgColors.js (port to python?)

### [uses Stable Diffusion CPU (I don't have GPU)](https://github.com/bes-dev/stable_diffusion.openvino)

![example 1](https://github.com/tboie/universal_image_generator/tree/master/examples/1.png)
![example 2](https://github.com/tboie/universal_image_generator/tree/master/examples/2.png)
![example 2](https://github.com/tboie/universal_image_generator/tree/master/examples/3.png)
![example 2](https://github.com/tboie/universal_image_generator/tree/master/examples/4.png)
![example 2](https://github.com/tboie/universal_image_generator/tree/master/examples/5.png)
![example 2](https://github.com/tboie/universal_image_generator/tree/master/examples/6.png)
