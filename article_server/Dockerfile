FROM python:3.7
#WORKDIR /root
#COPY ./root .
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
COPY . .
EXPOSE 55002
CMD ["python", "app.py","--port=55002"]