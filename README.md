
# FastAPI & Redis QR Code Generator (Dockerized)

A lightning-fast, containerized microservice API that generates QR codes
from URLs and uses Redis caching for performance optimization.

This project demonstrates a real-world multi-container architecture
using Docker Compose.

------------------------------------------------------------------------

##  Architecture & Features

-   **Web Service (FastAPI)**\
    Handles incoming HTTP requests and generates PNG QR codes.

-   **Cache Service (Redis)**\
    Stores previously generated QR codes. If a user requests the same
    URL again, the QR code is served instantly from memory.

-   **Fully Containerized**\
    Isolated environments using Docker and Docker Compose --- zero local
    dependency conflicts.

------------------------------------------------------------------------

##  Tech Stack

-   **Backend:** Python 3.11, FastAPI, Uvicorn\
-   **Caching:** Redis\
-   **Image Processing:** `qrcode` library\
-   **DevOps / Containerization:** Docker, Docker Compose

------------------------------------------------------------------------

## Prerequisites

Make sure you have:

-   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    installed and running

------------------------------------------------------------------------

## How to Run

1.  Clone this repository:

``` bash
git clone <your-repo-url>
cd <project-folder>
```

2.  Build and start the containers:

``` bash
docker compose up --build
```

3.  The API will automatically start on:

```{=html}
<!-- -->
```
    http://localhost:8000

------------------------------------------------------------------------

## Usage / Endpoints

###  Generate a QR Code

Send a `GET` request to the `/generate` endpoint with a URL as a query
parameter.

#### Example (Browser):

    http://localhost:8000/generate?url=https://www.linkedin.com/in/your-profile

The API will return a PNG image containing the QR code.

------------------------------------------------------------------------

##  Testing the Cache (Performance Optimization)

1.  Open the endpoint above in your browser.\
    The API will generate the QR code and store it in Redis.

2.  Refresh the page quickly.

3.  Check your terminal logs --- you should see a cache hit message
    like:

```{=html}
<!-- -->
```
    Gasit in Redis! Returnam rapid.

This proves the image was served instantly from memory without
regenerating it.

------------------------------------------------------------------------

##  Cleanup

To stop the containers and remove the created network:

1.  Press:

```{=html}
<!-- -->
```
    Ctrl + C

2.  Then run:

``` bash
docker compose down
```

------------------------------------------------------------------------

## 📌 Possible Improvements

-   Add request rate limiting
-   Add QR code customization (size, color, logo)
-   Add expiration time for Redis cache
-   Deploy to a cloud provider (Railway, Render, AWS)
