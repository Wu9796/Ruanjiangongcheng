import json
import os

# 文件路径
DATA_FILE = "transactions.json"

# 初始化交易记录
def init_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

# 加载交易记录
def load_transactions():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# 保存交易记录
def save_transactions(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

# 记录收入
def record_income(amount, description):
    transactions = load_transactions()
    transactions.append({
        "type": "income",
        "amount": amount,
        "description": description
    })
    save_transactions(transactions)
    print(f"收入记录成功: +{amount} 元 ({description})")

# 记录支出
def record_expense(amount, description):
    transactions = load_transactions()
    transactions.append({
        "type": "expense",
        "amount": amount,
        "description": description
    })
    save_transactions(transactions)
    print(f"支出记录成功: -{amount} 元 ({description})")

# 计算余额
def calculate_balance():
    transactions = load_transactions()
    balance = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        elif transaction["type"] == "expense":
            balance -= transaction["amount"]
    return balance

# 查看交易历史
def view_transactions():
    transactions = load_transactions()
    if not transactions:
        print("暂无交易记录。")
        return
    for transaction in transactions:
        type_str = "收入" if transaction["type"] == "income" else "支出"
        amount = transaction["amount"]
        description = transaction["description"]
        print(f"{type_str}: {amount} 元 ({description})")

# 主菜单
def main_menu():
    print("\n个人记账系统")
    print("1. 记录收入")
    print("2. 记录支出")
    print("3. 查看余额")
    print("4. 查看交易历史")
    print("5. 退出")

# 主程序
def main():
    init_data()
    while True:
        main_menu()
        choice = input("请选择操作 (1-5): ")
        if choice == "1":
            amount = float(input("请输入收入金额: "))
            description = input("请输入收入描述: ")
            record_income(amount, description)
        elif choice == "2":
            amount = float(input("请输入支出金额: "))
            description = input("请输入支出描述: ")
            record_expense(amount, description)
        elif choice == "3":
            balance = calculate_balance()
            print(f"当前余额: {balance} 元")
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            print("退出系统。")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()
