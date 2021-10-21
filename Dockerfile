FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENV FLASK_APP="src"
ENTRYPOINT [ "python" ]
CMD [ "waitress-serve --call 'src:create_app'" ]