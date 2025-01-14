FROM python:3.7.9 

EXPOSE 8501

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD streamlit run app.py