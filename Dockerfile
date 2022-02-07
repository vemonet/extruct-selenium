ARG SELENIUM_TAG=4.1.1-20220121
FROM selenium/standalone-firefox:$SELENIUM_TAG

USER root
RUN apt-get update && \
    apt-get install -y python3-pip

USER seluser
WORKDIR /home/seluser
ENV PATH=$PATH:/home/seluser/.local/bin

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "extruct_url.py" ]
CMD [ "--help" ]