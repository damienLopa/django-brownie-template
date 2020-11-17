FROM python:3.8-alpine

RUN apk add --update --no-cache build-base postgresql-dev curl pcre-dev linux-headers libffi-dev

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

ENV PATH "/root/.poetry/bin:$PATH"



WORKDIR /app

COPY bin ./bin
COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip pipenv && \
    pipenv install --system

COPY src ./src
WORKDIR /app/src

COPY pytest.ini .pylintrc ./

EXPOSE 5000

CMD /app/bin/start