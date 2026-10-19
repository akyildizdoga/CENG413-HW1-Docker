# CENG413 HW1 - Answers

## 1. Dockerfile Instruction Order

I used Python 3.12.12 as the base image. First, I copied requirements.txt and installed the packages. After that, I copied app.py into the image. I did it in this order because Docker can use the cached packages when I only change my code. If I changed this order, the build could take longer.

## 2. Container Data and Persistence

When I remove a container, the data saved inside its writable layer is lost. But if I only stop the container, the data stays there. I can use Docker volumes to save data even if the container is removed. Important application data should be stored in a volume or a database.

## 3. Risks of the Latest Tag

Using the latest tag can be risky because the image version can change over time. This means the same Dockerfile might give different results later. I used python:3.12.12-slim-bookworm instead of latest. This helps me use a more consistent version when building my image.

## AI Assistant Usage

I used ChatGPT to help me write and understand the code, Dockerfile, and documentation. I also used it to solve errors, and I tested the application myself.
