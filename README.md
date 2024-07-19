# GAN Image Generator

This is a Flask-based web application that uses a Generative Adversarial Network (GAN) to generate images. The application allows users to generate images with a trained GAN model and view them in their browser.

## Project Structure

```
my-flask-app/
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── static/
│   └── generated_image.png
└── templates/
    └── index.html
```

## Requirements

-   Python 3.9 or later
-   Flask
-   NumPy
-   TensorFlow
-   Matplotlib
-   Gunicorn
-   Waitress

## Installation

### Clone the Repository

```sh
git clone https://github.com/Narasimha9271/GAN-Image-Generator
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

## Running the Application

### Method-1: Using Flask Development Server

1. Run the application
    ```sh
    python app.py
    ```

### Method-2: Using Virtual Environment

1. Create a virtual environment

    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment

    For Windows:

    ```sh
    venv\Scripts\activate
    ```

    For Unix or MacOS:

    ```sh
    source venv/bin/activate
    ```

3. Run the application using Gunicorn

    ```sh
    gunicorn app:app
    ```

4. Alternatively, run the application using Waitress

    ```sh
    waitress-serve --port=8000 app:app
    ```

    The application will be available at `http://localhost:8000`.

## Application Features

-   **Generate Images**: Users can generate images using a pre-trained GAN model.
-   **View Images**: Generated images are displayed in the browser.
-   **Save Images**: Generated images are saved in the `static/` directory.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!
