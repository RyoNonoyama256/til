
### 1. CodeSandboxにサインアップ/ログイン
まず、[CodeSandbox](https://codesandbox.io/)にアクセスしてアカウントを作成するか、既存のアカウントでログインします。

### 2. 新しいSandboxを作成
1. ダッシュボードで「Create Sandbox」ボタンをクリックします。
2. 使用したいテンプレート（例: Python）を選択します。

### 3. サンプルAPIのコードを書く
以下のようなシンプルなFlaskアプリを作成します。

**app.py**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### 4. パッケージのインストール
CodeSandboxのターミナルで以下のコマンドを実行して、必要なパッケージをインストールします。
```bash
pip install flask
```

### 5. サーバーの設定
CodeSandboxの設定で、サーバーの開始スクリプトを指定します。

1. 左側のメニューで「Server Control Panel」を開きます。
2. 「Start Command」に `python app.py` を入力し、サーバーを開始します。

### 6. 公開URLの取得
サーバーが起動すると、CodeSandboxは自動的に公開URLを生成します。このURLを使って外部からAPIにアクセスできます。

### 例
ブラウザで以下のようにアクセスします:
```
https://your-sandbox-id.sse.codesandbox.io/
```
このURLにアクセスすると、"Hello, World!"というメッセージが表示されます。

### まとめ
1. CodeSandboxにログイン
2. 新しいSandboxを作成
3. Flaskアプリを作成
4. 必要なパッケージをインストール
5. サーバーの開始スクリプトを設定
6. 公開URLを取得

