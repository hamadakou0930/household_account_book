# 家計簿システム

このプロジェクトは、家計簿を管理するためのアプリケーションです。ユーザーは収入や支出を記録し、簡単に管理することができます。

## 構成ファイル

- `src/main.py`: アプリケーションのエントリーポイント。サンプルデータを追加し、記録を表示します。
- `src/db/database.py`: PostgreSQLデータベースへの接続を管理します。接続設定やレコードを挿入するための関数を含みます。
- `src/models/record.py`: レコードモデルを定義します。日付、カテゴリ、金額、メモなどの属性を持つクラスを含みます。
- `requirements.txt`: プロジェクトに必要なPythonパッケージをリストします。`psycopg2`や`SQLAlchemy`などが含まれます。

## セットアップ手順

1. リポジトリをクローンします。
   ```
   git clone <repository-url>
   cd household_account_book
   ```

2. 必要なパッケージをインストールします。
   ```
   pip install -r requirements.txt
   ```

3. PostgreSQLデータベースを設定します。接続情報を`src/db/database.py`に追加してください。

## 使用方法

アプリケーションを起動するには、以下のコマンドを実行します。
```
python src/main.py
```

これにより、サンプルデータが追加され、記録が表示されます。