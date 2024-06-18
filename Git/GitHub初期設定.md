# GitHub初期設定
### 事象No.1
- ```git push origin HEAD```実行時に403エラー
### 対策No.1
- "developer settings"から"Personal access tokens"に行き"Select scopes"の"repo"をONに
- "Select scopes"ではパーソナルトークンでアクセスできるスコープを定義している

### 事象No.2
- ```git push origin main```が機能しない
### 対策No.2
- ```git remote add <エイリアス名> <リポジトリのURL>```
- リモートリポジトリのURLが ```https://github.com/username/repository.git``` である場合、次のようにエイリアスを origin として追加する
  - ```git remote add origin https://github.com/username/repository.git```
- これにより、origin というエイリアスが ```https://github.com/username/repository.git``` というリモートリポジトリを指すようになる
- 以降は、リモートリポジトリに対する操作を origin を使って行うことができる

