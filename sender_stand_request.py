import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=body,  # тело
                         headers=data.headers)  # заголовок


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,  # подставляем полный url
                        params={"t": track},  # параметр
                        headers=data.headers)  # заголовок
