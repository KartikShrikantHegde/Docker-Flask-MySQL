# Flask-Docker Sample Template

This project can be used to run a basic "Hello World" flask app using docker-compose.

## Getting Started

**Step 1:** Make sure git is installed on your os. I will be using macOS for the project.

On macOS, you can install the git using Homebrew using ```brew install git```

**Step 2:** Clone the project into your local machine using below command.

```git clone https://github.com/KartikShrikantHegde/Docker-Flask-Sample.git```

### Prerequisites

**1. Docker**

Make sure you have Docker installed. Please follow the below link for official documentation from Docker to install latest version of docker on your os. For this project I am using Docker CE (18.09).

```https://docs.docker.com/docker-for-mac/install/```

### Installing

**Step 1:** Change to the directory where the project was cloned in previous step.

```
cd Docker-Flask-Sample
```

**Step 2:** Make sure Docker is up and running. You can start the docker engine from desktop icon on Mac.

**Step 3:** Run

```
docker-compose up --build
```

**Step 4:** Open up the browser and paste the below url

```
http://localhost:8000/
```

The browser should display "Hello World" message. The app is up and running inside a docker container using docker-compose.

## Running the tests

## Deployment

## Built With

* [Docker](http://www.dropwizard.io/1.0.2/docs/) -  Deployment model
* [Flask](https://maven.apache.org/) - The web framework
* [Python](https://rometools.github.io/rome/) - programming language
* [pip](https://rometools.github.io/rome/) - Package and dependency manager

## Contributing

## Versioning

## Authors

## License

## Acknowledgments