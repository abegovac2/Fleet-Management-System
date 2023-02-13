# Fleet Management System

***IMPORTANT!***  `.env` file left in repo for demo purposes

## Description

Project consists of three systems:

1. Fleet management system - CRUD api manages data for vehicles, drivers and trips
2. GPS simulator - simulator service of a GPS tracker on a vehicle that generates data of the current driver, location and speed
3. Vehicle monitoring service - consumes data created by the GPS simulator service and assigns infraction points accordingly

## Diagram

![img](https://github.com/abegovac2/Fleet-Management-System/blob/main/fms_v1.drawio.png)

## Tools used

* [FastApi](https://fastapi.tiangolo.com/) - a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
* [PostgreSQL](https://www.postgresql.org/) - a powerful, open-source, object-relational database management system with a strong emphasis on reliability, data integrity, and performance.
* [RabbitMQ](https://www.rabbitmq.com/) - an open-source message-broker software that implements the Advanced Message Queuing Protocol (AMQP), allowing applications to communicate and exchange messages in a flexible and efficient manner.
* [Docker](https://www.docker.com/) - a platform that enables developers to easily create, deploy, and run applications in containers, making it easier to manage application dependencies and improve resource utilization.

## Start the app

Inside the root folder of the solution run the following command:

```
docker-compose up -d
```

Once all containers are up and running, verify the instalation with any request from the provided [postman collection](https://github.com/abegovac2/Fleet-Management-System/blob/main/TRG%20task.postman_collection.json).
