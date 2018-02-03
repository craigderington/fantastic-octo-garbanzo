#!/bin/bash
cd /var/www/html/flask-pixel-tracker
source bin/activate
celery -A pfpt.main.celery worker --loglevel=INFO --concurrency=1