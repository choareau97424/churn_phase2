FROM python:3.9
WORKDIR /src
COPY /src .
RUN pip3 install -r requirements.txt
RUN mkdir -p /data
VOLUME /data
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]