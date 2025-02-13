# Clothing Store Project

This is a simple clothing store application built using FastAPI. The application provides endpoints to manage and retrieve product information.

## Project Structure

```
clothing-store
├── src
│   ├── main.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── product_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   └── product.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── product_routes.py
│   ├── services
│   │   ├── __init__.py
│   │   └── product_service.py
│   └── types
│       └── __init__.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd clothing-store
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
uvicorn src.main:app --reload
```

You can then access the API at `http://127.0.0.1:8000`.

## API Endpoints

- **GET /products**: Retrieve a list of all products.
- **GET /products/{id}**: Retrieve a product by its ID.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.