FROM redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask 

COPY test.py /test.py

CMD ["python3" , "/test.py"]

