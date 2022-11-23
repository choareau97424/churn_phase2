FROM ubuntu
WORKDIR /src
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests-file
COPY /src .
RUN pip3 install -r requirements.txt
RUN mkdir -p /data
VOLUME /data
CMD ["/src/dataAPI.py"]
EXPOSE 8000
CMD ["uvicorn", "dataAPI:api", "--host", "172.50.0.4", "--port", "8002"]