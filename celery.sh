#!/bin/bash
cd /var/www/html/EARL-Pixel-Tracker
source bin/activate
celery -A pfpt.main.celery worker --loglevel=INFO --concurrency=1