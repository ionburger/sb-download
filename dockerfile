FROM python:3.12

RUN pip install -U yt-dlp
RUN pip install -U sponsorblock

ADD downloader.py .

CMD ["python", "./downloader.py"]