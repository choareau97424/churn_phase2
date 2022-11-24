FROM ubuntu
WORKDIR /Backend/Model/src
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests-file
RUN mkdir -p /Backend/Model/src
COPY /src /Backend/Model/src
RUN pip3 install -r /Backend/Model/src/requirements.txt
RUN mkdir -p /Backend/Model/src/data
VOLUME /Backend/Model/src/data
CMD ["/Backend/Model/src/modelAPI.py"]
EXPOSE 8000
CMD ["uvicorn", "modelAPI:api", "--app-dir", "/Backend/Model/src/", "--host", "0.0.0.0", "--port", "8000"]