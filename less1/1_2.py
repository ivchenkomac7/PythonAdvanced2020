# Создать словарь Страна:Столица. Создать список стран. Не все
# страны со списка должны сходиться с названиями стран со словаря. С
# помощою оператора in проверить на вхождение элемента страны в
# словарь, и если такой ключ действительно существует вывести
# столицу.

country = {
    "Ukraine": "Kyiv",
    "Belarus": "Minsk",
    "Poland": "Warsaw"
    }

country_extended = ["Ukraine", "Slovakia", "Hungary", "Poland"]

for i in country_extended:
    if i in country:
        print(country[i])
