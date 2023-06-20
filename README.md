## Summary
+ This project is a Python application that utilizes MongoDB for data storage and Flask for backend web framework. This README provides instructions on how to set up the MongoDB database and run the application using Docker and Docker Compose.

## Prerequisites
+ Python: [Python](https://www.python.org/downloads/)
+ Docker: [Install Docker](https://docs.docker.com/get-docker/).
+ Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/).

## Build/Run Application 
+ Navigate to directory where docker-compose.yml file locates.
+ Open command terminal in the same directory
+ Build and run containers using Docker Compose:
```bash
docker-compose up
```
This command starts both MongoDB container and API container using the provided Docker Compose configuration.

## Test Application 
+ Navigate to "testcase" directory
+ Open command terminal in the same directory 
+ Make sure that docker-compose is up and running
+ Run test
```bash
python test.py
```

## Stop Application
+ To stop the application and the MongoDB container, run the following command:
```bash
docker-compose down 
```
This will stop and remove the Docker containers associated with the application.

## Addtional Configuration 
+ To make the necessary changes in the appropriate files. The changes will be reflected when you rebuild and run the Docker container.
```bash
docker-compose build
```
This command rebuilds API container
+ Customize the MongoDB configuration by modifying the docker-compose.yml file. Adjust the environment variables, volumes, or any other configuration as needed.
