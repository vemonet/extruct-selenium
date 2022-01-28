FROM selenium/standalone-firefox:4.1.1-20220121

USER root
RUN apt-get update && \
    apt-get install -y python3-pip

USER seluser
WORKDIR /home/seluser
ENV PATH=$PATH:/home/seluser/.local/bin

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "extruct_react.py" ]
