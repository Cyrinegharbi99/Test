FROM python:3
ADD main.py
RUN pip install typefit[api,dates], pip install fastapi uvicorn requests beautifulsoup4, pip install facebook-scraper
CMD [ "python3 ", "./main.py" ]
