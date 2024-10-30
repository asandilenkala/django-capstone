Personal Portfolio of Asandile Nkala

- Python 3.11
- Docker
- Virtualenv

## Setting Up the Project

### Using Virtualenv

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   

Running the Application with Docker

To run this application using Docker, follow these steps:

    Install Docker
        Ensure that Docker is installed on your machine. You can download and install Docker from the official Docker website.

    Build the Docker Image
        Open your terminal, navigate to the project root directory, and run the following command:

        bash

    docker build -t asandile/portfolio_image .

Run the Docker Container

    Once the image is built, you can run it with this command:

    bash

    docker run -d -p 8000:8000 asandile/portfolio_image


    This will start the application in a detached mode (-d) and map port 8000 on your local machine to port 8000 in the container.

Access the Application

    After running the container, you should be able to access the application at http://localhost:8000.

Stop the Docker Container

    To stop the application, find the container ID by running:


docker ps

Then, use the following command to stop the container:


    docker stop 4988c823c8fa

(Optional) Docker Compose Setup

    If your application requires multiple services (e.g., a database), consider using docker-compose. Create a docker-compose.yml file, then start all services by running:


        docker-compose up -d

        This command will start up all services specified in the docker-compose.yml file in detached mode.




Welcome to my personal portfolio! This repository contains the source code for my portfolio website, showcasing my projects, skills, and experiences as a software developer.

About Me

I am Asandile Nkala, a passionate software developer with a focus on software engineering. I enjoy building applications that solve real-world problems and constantly seek to improve my skills and knowledge in the field.

Website Features

- Home: An introduction to who I am and what I do.
- Projects: A showcase of my recent projects, including descriptions, technologies used, and links to live demos and GitHub repositories.
- Skills: A list of my technical skills and proficiencies.
- Contact: Information on how to get in touch with me.

Technologies Used

- HTML5 & CSS3: For structuring and styling the website.
- JavaScript: For adding interactivity.
- Bootstrap: For responsive design.
- Django: For server-side processing and dynamic content.
- GitHub Pages: For deployment.


Feel free to reach out to me via the following channels:

- Email: [asandilenkala@gmail.com](mailto:asandilenkala@gmail.com)
- LinkedIn: [https://www.linkedin.com/in/asandile-nkala-37b635256/](https://www.linkedin.com/in/asandile-nkala-37b635256/)
- GitHub: [https://github.com/asandilenkala](https://github.com/asandilenkala)

Thank you for visiting my portfolio! I look forward to connecting with you.
