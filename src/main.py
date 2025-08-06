import datetime
from db.database import insert_record
from models.record import Record

def add_record(date, category, amount, memo=""):
    record = Record(date, category, amount, memo)
    insert_record(record)

def show_records():
    # ここではデータベースからレコードを取得して表示する処理を追加する予定
    pass

def main():
    print("activate HOUSE HOLD ACCOUNT BOOK SYSTEM")
    # サンプルデータ追加
    add_record(datetime.date.today(), "食費", -1200, "ランチ")
    add_record(datetime.date.today(), "給料", 200000, "7月分")
    show_records()

if __name__ == "__main__":
    main()