#!/bin/bash
# マイグレーションファイルの作成
python manage.py migrate

# 初期データの投入
python manage.py loaddata labels
python manage.py loaddata posts

echo "マイグレーションとデータ投入が完了しました"

