def prepare_documents():
    print("准备资料：只执行一次")
    chunks = [
        "退货：收到商品后7天内可以申请。",
        "保修：商品保修期为一年。",
        "配送：付款后两天内发货。",
    ]
    return chunks


def search_documents(chunks, keyword):
    print("本次查找：", keyword)
    for chunk in chunks:
        if keyword in chunk:
            print("找到资料：", chunk)


chunks = prepare_documents()

for keyword in ["退货", "保修", "配送"]:
    search_documents(chunks, keyword)