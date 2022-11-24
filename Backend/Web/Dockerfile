FROM ubuntu
WORKDIR /Backend/Web/src
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests-file
RUN mkdir -p /Backend/Web/src
COPY /src /Backend/Web/src
RUN pip3 install -r requirements.txt
RUN mkdir -p /Backend/Web/src/data
VOLUME /Backend/Web/src/data
CMD ["/Backend/Web/src/webAPI.py"]
EXPOSE 8000
CMD ["uvicorn", "webAPI:api", "--app-dir", "/Backend/Web/src/", "--host", "172.50.0.3", "--port", "8001"]