FROM python:3.7
#WORKDIR /usr/local/lib/python3.7/site-packages
#COPY ./lib .
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
COPY . .
EXPOSE 55002
CMD ["python", "app.py"]