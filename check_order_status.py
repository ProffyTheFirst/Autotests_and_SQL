# Шарифуллин Владислав, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def get_new_order_tracker():
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    order_body = data.order_body.copy()
    # В переменную order_response сохраняется результат запроса на создание заказа
    order_response = sender_stand_request.post_new_order(order_body)
    # возвращается словарь с нужным значением track
    tracker = order_response.json()["track"]
    return tracker


# проверка запроса на получения заказа по треку заказа
def test_tracker():
    # получаем ответ от сервера при запросе заказа по номеру трека
    response = sender_stand_request.get_order_by_track(get_new_order_tracker())
    # проверяем, что код ответа 200
    assert response.status_code == 200
