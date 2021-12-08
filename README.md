# 실시간 비상구 안내 시스템

- 실시간으로 가능한 비상구까지의 경로를 안내하기
<img src="https://user-images.githubusercontent.com/90401282/145148578-18326d5e-ce4a-423f-9b9f-602e972bc68b.jpg" width="900" height="500">



## 핵심내용

- 화재감지 센서로 화재 여부 및 위치 파악
- 바닥 led 화살표를 이용한 대피 경로 안내
- 재난 문자를 이용한 대피 경로 안내



## 프로젝트 sw 구조도

<img src="https://user-images.githubusercontent.com/90401282/145147840-3a91098a-17ca-440e-8eda-2438e4a236ee.png" width="900" height="350">



## 구현방법

* 화재감지 노드 및 대피경로 안내 노드 
  - ESP8266기반의 NodeMCU를 이용하여, UDP 통신으로 서버와 데이터 송수신
  - NodeMCU의 동작을 위한 프로그램 개발은 OpenSource인 MicroPython 이용
  - 화재감지는 시중 화재경보기의 Trigger 신호 이용 또는 화재감지 센서(불꽃, 연기 센서 등)을 이용
  - 대피 방향 안내를 위한 LED는 Dot Matrix 또는 WS2812를 이용

* 방재 서버
  - UDP 통신으로 노드와의 데이터 송수신
  - A* 알고리즘을 이용하여, 화재 여부에 따른 가중치 탐색 기법으로 대피 경로를 생성

* 실내측위 서버
  - 실내 측위 관련 OpenSource Project 인 FIND3를 이용한 실내 지도 생성 및 정보 제공
  - 주변 WIFI / BLE 신호 및 지자기 세기 변화를 이용한 실내 위치 예측


## 시연 영상
- 화재 위치를 감지 후, 바닥 led의 색깔 변화와 재난문자를 확인 할 수 있다.

#### 아래 사진의 경우 화재 감지 센서로 화재의 위치를 파악하고 A*알고지즘으로 대피 경로를 계산하고 이를 TURTLE라이버리로 시각화 한 것이다.
(각각의 과정의 데이터는 MCU를 이용하여 UDP 통신으로 서버와 데이터를 송수신 했다.)

- 화재 발생이 없는 경우- 
<https://user-images.githubusercontent.com/90401282/145150501-f25df5ba-b748-4d69-8c7a-74f9fbed200f.jpg" width="900" height="350">
- 화재 발생 케이스 1- 
<img src="https://user-images.githubusercontent.com/90401282/145149809-762afc8d-4b66-4bae-b199-0136a2c35dc8.jpg" width="900" height="350">
- 화재 발생 케이스 2- 
<img src="https://user-images.githubusercontent.com/90401282/145149812-673fa1be-4235-4964-b281-959246626526.jpg" width="900" height="350">


* [시연영상 유튜브 링크]
: https://youtu.be/7NG18pvbotk
- 화재 발생시 바닥 led의 변화를 확인 할 수 있다.

