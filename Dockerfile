FROM mlspec/mlspeclib-action-dockersha256:2a982d37c379dd3953c456449fa0a8aab328b2b788280f3b3a05b695b5295d43

RUN apt-get -y update && apt-get -y install python3-all python3-pip

ARG FIRSTCACHEBUST=1

COPY requirements.txt /requirements.txt

RUN python3 -m pip install -U pip
RUN python3 -m pip install --no-cache-dir -r /requirements.txt

WORKDIR /src
COPY .parameters/schemas /src/parameters
COPY integration/.parameters/schemas /src/parameters/test_schemas
COPY step_execution.py /src
COPY integration/container_debugging.sh /src
COPY utils/utils.py /src/utils/utils.py
RUN touch /src/utils/__init__.py

ENTRYPOINT ["/src/entrypoint.sh"]
