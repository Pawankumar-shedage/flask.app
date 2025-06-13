FROM python
WORKDIR /src
COPY . .
RUN pip install flask
EXPOSE 4000
CMD python server.py
