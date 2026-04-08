# ShopNest

ShopNest is a Django-based project. The primary goal of this repository is to learn how to set up and use **Docker** for containerizing a full-stack web application.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to build and run the project using Docker:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Joel-Fah/shopnest.git
   cd shopnest
   ```

2. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```
   *This command will build the Docker image, install dependencies from `requirements.txt`, and start the Django development server.*

3. **Access the application:**
   Open your web browser and navigate to `http://localhost:8000`.

4. **Stop the containers:**
   To stop the running containers, press `Ctrl+C` in the terminal, or run the following command in another terminal window:
   ```bash
   docker-compose down
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
