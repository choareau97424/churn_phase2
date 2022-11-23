#!/bin/bash
cd Streamlit/
docker build --tag streamlit-api-docker .
cd ..
docker run -d -p 8501:8501 -v backend_churn-shared-volume:/data --name streamlit1 streamlit-api-docker
docker network connect backend_my_network streamlit1