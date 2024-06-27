### Glitchの概要

[Glitch](https://glitch.com/)は、ブラウザ上でコードを記述し、即座にホスティングとデプロイができるオンラインの開発環境  
特に初心者や迅速なプロトタイプ作成に適しており、簡単なWebアプリケーションやAPIの開発が可能

### プロジェクトの手順

#### 1. Glitchにアクセス

- [Glitch](https://glitch.com/)にアクセスし、アカウントを作成
- ダッシュボードから「New Project」をクリックし、「Create a Node App」を選択

#### 2. プロジェクトの編集

1. **`package.json`の編集**

   プロジェクトに必要な依存関係を追加するために、`package.json`ファイルを編集

   ```json
   {
     "name": "my-express-api",
     "version": "1.0.0",
     "description": "A simple Express API hosted on Glitch",
     "main": "server.js",
     "scripts": {
       "start": "node server.js"
     },
     "dependencies": {
       "express": "^4.17.1",
       "body-parser": "^1.19.0"
     },
     "engines": {
       "node": "14.x"
     }
   }
   ```

2. **`server.js`の作成**

   `server.js`ファイルを作成し、以下の内容を追加

   ```javascript
   const express = require('express');
   const bodyParser = require('body-parser');
   const app = express();
   const port = process.env.PORT || 3000;

   // Middleware to parse JSON
   app.use(bodyParser.json());

   // GET endpoint for basic check
   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   // POST endpoint to receive and modify data
   app.post('/data', (req, res) => {
     let receivedData = req.body;

     // Modify the received data
     let modifiedData = {
       ...receivedData,
       modified: true,
       timestamp: new Date().toISOString()
     };

     // Send back the modified data
     res.json(modifiedData);
   });

   app.listen(port, () => {
     console.log(`Server is running on port ${port}`);
   });
   ```

#### 3. プロジェクトの実行

- Glitchは自動的に依存関係をインストールし、アプリケーションを起動
- 左下の「Show」ボタンをクリックして、提供されるURLを使用してAPIが動作しているか確認

#### 4. APIのテスト

**GETリクエストのテスト**

- ブラウザで `https://<your-glitch-project-name>.glitch.me/` にアクセスして、「Hello, World!」と表示されることを確認

**POSTリクエストのテスト**

- [Postman](https://www.postman.com/) や [curl](https://curl.se/) などのツールを使用して、APIに対してPOSTリクエストを送信

**curlの使用方法**

ターミナルで以下のコマンドを実行

```bash
curl -X POST https://<your-glitch-project-name>.glitch.me/data -H "Content-Type: application/json" -d '{"name":"John Doe","message":"Hello, this is a test!"}'
```

**返されるデータ例**

```json
{
  "name": "John Doe",
  "message": "Hello, this is a test!",
  "modified": true,
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```
