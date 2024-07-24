FROM python:3.12

WORKDIR /app

COPY . /app

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "bot.py"]

CMD ["python", "bot.py"]