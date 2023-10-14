FROM python:3.8

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD main.py .
CMD ["python", "./main.py"]
