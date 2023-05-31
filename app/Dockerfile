FROM python:3.11.3-slim-bullseye

RUN apt update && apt upgrade -y && \
    apt install -y fortune cowsay curl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python -

ENV PATH=$PATH:/usr/games:/etc/poetry/bin

WORKDIR app

COPY . .

RUN poetry install

# CMD ["tail","-f", "/dev/null"]

CMD ["poetry", "run", "server"]
