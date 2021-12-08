from socket import *
import json
import path_algorithm
import navigation


LED_NODE_IP = "**"
LED_NODE_PORT = 9999

map = [[0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 0]]

curr_loc = (0, 4)
led_loc = (2, 3)
exit_list = [(0, 0), (0, 6), (2, 0)]

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(10)

while True:
    fireNode_sock, addr = sock.accept()

    rawData = fireNode_sock.recv(1024).decode()
    # jsonData = {'detect': 1, 'id': 0, 'location': [0, 2]}
    jsonData = json.loads(rawData)

    print(jsonData)

    updated_map = path_algorithm.map_update(map, jsonData["location"])

    path_list = path_algorithm.find_path(updated_map, curr_loc, exit_list)

    shortest_path = path_algorithm.find_shortest_path(path_list)

    print(path_list)
    print(shortest_path)
    print("Recommend Exit::", exit_list[path_list.index(shortest_path)])

    direction = path_algorithm.get_direction(led_loc, path_list)

    dictData = {"id": 0, "location": led_loc, "direction": direction}
    print(dictData)
    jsonData = json.dumps(dictData)
    ledSock = socket(AF_INET, SOCK_STREAM)
    ledSock.connect((LED_NODE_IP, LED_NODE_PORT))
    ledSock.send(jsonData.encode())

    navigation.show(path_list)