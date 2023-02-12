FROM python:3.10-slim
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
COPY . ./app
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
ENTRYPOINT [ "./entrypoint.sh" ]