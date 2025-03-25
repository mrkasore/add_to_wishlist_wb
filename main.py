import requests
from data_from_local_storage import token_data, device_id

def get_chrt_id(article):
    url = f"https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1255987&spp=30&ab_testing=false&lang=ru&nm={article}"
    res = requests.get(url)
    data = res.json()

    try:
        product = data['data']['products'][0]
        option_id = product['sizes'][0]['optionId']
        print(f"optionId: {option_id}")
        return option_id
    except (KeyError, IndexError):
        print("Не удалось найти optionId.")

def add_to_favorites(article):
    url = f"https://favs-storage-api.wildberries.ru/api/favs/sync?ts=1742890720246&device_id={device_id}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token_data}",
    }
    chrt_id = get_chrt_id(article)
    payload = [
        {
            "chrt_id":chrt_id,
            "cod_1s":int(article),
            "client_ts":None,
            "op_type":1,
            "type":2
        }
    ]

    response = requests.post(url, headers=headers, json=payload)

    print(f"Status code: {response.status_code}")
    print("Response:", response.text)

def main():
    print('Введите артикль товара: ')
    add_to_favorites(int(input()))

if __name__ == "__main__":
    main()





