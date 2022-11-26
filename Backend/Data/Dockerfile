FROM ubuntu
WORKDIR /Backend/Data/src
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests-file
RUN mkdir -p /Backend/Data/src
COPY /src /Backend/Data/src
RUN pip3 install -r requirements.txt
RUN mkdir -p /Backend/Data/src/data
VOLUME /Backend/Data/src/data
CMD ["/Backend/Data/src/dataAPI.py"]
EXPOSE 8000
CMD ["uvicorn", "dataAPI:api", "--app-dir", "/Backend/Data/src/", "--host", "0.0.0.0", "--port", "8002"]
