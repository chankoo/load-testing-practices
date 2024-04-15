# 시스템 디자인 연습

## 목적
서비스 부하가 증가할 때 시스템에 발생하는 다양한 문제들을 직접 경험하고 해결하기

## 방식
부하 테스트 툴 활용해 가상의 트래픽 생성. 시스템 반응을 관찰하며 점진적으로 개선

## 서비스 종류
- 피드(sample_feed): 사용자들이 게시물을 업로드하고, 이 게시물이 다른 사용자들의 피드에 실시간으로 반영되는 시나리오를 구현한다.
- 채팅(sample_chat): 실시간으로 메시지를 주고받는 채팅 서비스를 구현한다. 웹소켓과 발행/구독 모델 등으로 시스템을 구성하고, 부하를 늘린다.
- 숏 링크(short_link): 단축 url을 제공하는 서비스를 구현하고, 동시성 문제를 경험한다.

## 기술 스택
- python, django, gunicorn
- python, fastapi, uvicorn
- sqlite, mysql, postgressql, redis
- docker, AWS ECS
- k6, grafana, influxdb

자세히 보기 👉👉 https://chankoo.github.io/series/%EC%8B%9C%EC%8A%A4%ED%85%9C-%EB%94%94%EC%9E%90%EC%9D%B8-%EC%97%B0%EC%8A%B5/
