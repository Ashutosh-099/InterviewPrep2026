# Docker
- Real world analogy: The Shipping Industry
Before the 1950s, global shipping was a mess. You had barrels of oil, sacks of flour & wooden crates of different sizes. Loading a ship took weeks because workers had to play a giant tetris game to fit everything.
- Then someone invented the "standardized shipping container"(big steel boxes). Suddenly, it didn't matter what was inside - a truck, a train & a ship could all handle the exact same steel boxes. It revolutionized global trade.

- The Problem docker solves "It works on my machine"
In software world, a developer writes an application on their system. It needs specific version of tools like Python 3.9, a certain database & a specific security settings.

- When they send that app to tester running on another system computer, or upload it to live server running linux, it crashes. The environment is different, files are missing & versions don't match.

Docker is the standardized shipping container for software.

Instead of just sending the code, Docker bundles the code the tools, the libraries & the exact settings into one standard package called container.

If you have Docker installed on the system, it can run that container perfectly, regardless of underlying operating system.

Docker is the platform that helps us to build container. It is lightweight and Portable.

One of the advantage is Docker container provides is that we can run two application in our one system with different versions, dependencies, libraries etc.

## Docker Image
Docker image is the executable file that contains list of information to build the container. The relation between Docker image and container is like Classes and object, where class is a blueprint to create a multiple objects.

```
Docker Image ---> Docker Container 1
             ---> Docker Container 2
             ---> Docker Container 3
```

The software installed on the computer that knows how to run these containers is called Docker Engine (Docker Desktop).

## Docker Hub
Docker hub is exactly like the app store for developers, or a massive global public library for software.
Docker hub contains docker images that we can fetch, download & build container on top of it. To fetch & download any docker image from docker hub, run this command:
```
docker pull <IMAGE_NAME>:<version>
```
Example:
```
docker pull hello-world
```

- To create a container from an image,
```
docker run IMAGE_NAME
```
This command create conatiner, if image is not available locally, it'll be downloaded from DockerHub.
Example:
```
docker run hello-world
```

## Port Binding & Running container in background
- By default, Docker containers are completely sealed off from your computer, like a sound proof room.
- Any library or server inside that room listening for visitor at door number, but because the room is sealed, nobody from outside can reach it.

- To bind a port to the library container door, we can use ```-p <HOST_PORT>:<CONTAINER_PORT>``` command.

- To run any container in background, we can use "**-d**" flag, which means **Detached mode**.
  Example: ``` docker run -d -p 8080:80 nginx ```
  - **-p** stands for port binding
  - **-d** stands for detached mode, container run in background

  ### Nginx:
  - It is webserver that is famous for being able to handle tens of thousands of request at the exact same time without breaking a sweat or using much computer memory.

- We can choose any HOST Port to connect with container door.
- **Why 80 for nginx?** Port 80 isn't an Nginx, it is global internet rule.
- 80: Standard unencrypted web pages(HTTP).
- 443: Secure web pages (HTTPS).
- 3306: MySQL Databases.
- 6379: Redis

- Every piece of software has it's own standard "door" based on specific job.

## Docker v/s Virtual Machine:
- Docker & VM achieve a similar goal(keeping apps seperated & safe) but they do it in a completely different way. Docker is much lighter than Virtual machine.
- Virtual machine are like building seperate houses. VM installs a completely brand new massive operating system for every single app you want to run. It is heavy takes up to ton of hard drive space, requires a lot of computer memory.
- Docker containers are like opening shop in a mall. Docker uses your computer's existing operating system. It doesn't install new OS for every app. It just puts up secure invisible "walls" around your app so it think it's alone.

<img width="787" height="817" alt="image" src="https://github.com/user-attachments/assets/a9a26947-5f1e-406c-a6a5-b1b6c238d5c3" />

- In our system, these is how operating system layers divided. Difference b/w Docker and VM is in these layers, Docker uses the same Host OS kernel & Virtualize application layer. But VM virtualize both OS kernel & Application layer.
