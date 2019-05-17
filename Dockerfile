FROM python:3.6
LABEL maintainer="David Arroyo Menéndez <davidam@gnu.org>"

RUN mkdir -p /damegender
WORKDIR /damegender

COPY ./ /damegender/

RUN pip3 install -r requirements.txt
RUN pip3 install nose

RUN echo "import nltk" > nltk_prerequisites.py
RUN echo "nltk.download('names')" >> nltk_prerequisites.py
RUN echo "nltk.download('punkt')" >> nltk_prerequisites.py
RUN python3 nltk_prerequisites.py

WORKDIR /damegender/src/damegender

ENTRYPOINT ["python3"]

CMD ["main.py", "David"]