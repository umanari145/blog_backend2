# blog_backend2


## プロジェクト起動
```
#django-admin startproject <プロジェクト名> <作成するディレクトリ>
django-admin startproject blogs .
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
