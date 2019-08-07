From python:3.7-alpine
ADD . /
WORKDIR /
RUN pip install -r requirements.txt
ENV PYTHONPATH /
COPY get_company_name.py /
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

