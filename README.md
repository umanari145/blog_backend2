# blog_backend2


## 初期db作成

```
docker exec -it dja_mongo_node sh
node createDB.js
```

## プロジェクト起動
```
#django-admin startproject <プロジェクト名> <作成するディレクトリ>
# 最初は設定ファイルのディレクトリが独立してさくせいされるため、プロジェクト名と違う名称をつける
django-admin startproject config .
```

## 開発サーバー起動
```
python manage.py runserver 0.0.0.0:8000
```
下記のようにエラーが出ても無視。

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 01, 2025 - 10:57:55
Django version 4.2.18, using settings 'blogs.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
無事に起動したら、ブラウザでhttp://localhost:8000/にアクセスできればOK

## プロジェクトのテンプレート作成

```
python manage.py startapp blogs
```

## migrations

```
# migrationファイルの作成
python manage.py makemigrations blogs

# migrationファイルの適用
python manage.py migrate

# 開発サーバー起動
python manage.py runserver 0.0.0.0:8000
```



## 参考
APIサーバーの作成方法<br>
https://zenn.dev/whitecat_22/articles/f826daf43155cd<br>
djangoとmongodbの連携方法<br>
https://qiita.com/Edim/items/90ee83a5d385807f67a6