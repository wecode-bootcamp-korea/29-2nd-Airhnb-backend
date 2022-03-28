# Air HnB 2차 프로젝트

## 🎆 기획

Air bnb를 모티브로한 흉가 예약 시스템

<br><br>

## ⭐️ 구성원

### 백엔드

- 강종범&nbsp; [GITHUB](https://github.com/jxngbxxm)

- 주다희 &nbsp;[GITHUB](https://github.com/newdana01)

- 최형택 &nbsp;[GITHUB](https://github.com/knuckles6974)


### 프론트 엔드

- 이화종 &nbsp;[GITHUB](https://github.com/hjlee1811)

- 정지민 &nbsp;[GITHUB](https://github.com/rindalica)

- 신수녕&nbsp; [GITHUB](https://github.com/cozynye)

- 한신웅&nbsp; [GITHUB](https://github.com/hsuj86)


<br><br>

## 📆 기간

- 2022/2/14 ~ 2022/2/26

<br><br>

## 💾 데모 영상

- [Demo Video Link](https://www.youtube.com/watch?v=PZlc97VmxNs)

<br><br>

## 💻 적용 기술

- Python, Django, MySQL, AWS(EC2, RDS, S3), Docker, Git

<br><br>


## 🔒 필수 구현 목표

- 소셜 로그인

- 흉가 리스트 페이지 

- 흉가 상세 페이지�

- 흉가 검색 기능

- 호스트 되기

<br><br>

## 🗒ERD

<img width="868" alt="스크린샷 2022-03-25 오후 4 12 58" src="https://user-images.githubusercontent.com/94527515/160072612-c7db6893-45f6-4fc3-8f28-d7f108b64cc1.png">

<br><br>

## 📌 구현 파트
> ## 주다희  
### 카카오 API를 활용한 소셜 로그인
- ### 카카오 서버 토큰 받기
    - 인가코드 전달받아 request 라이브러리를 통해 카카오 서버에 post 요청
    - 상태코드가 401인 경우 에러발생

- ### 사용자 정보 요청
    - 요청 헤더에 토큰 담에 post로 사용자 정보 요청
    - 상태코드가 200이 아닌 경우 에러 발생

- ### 회원 조회
    - 카카오 서버로부터 받은 사용자 정보를 통해(id) 데이터 베이스 등록 여부 조회
    - 서비스에 처음 로그인을 시도한 회원인 경우 DB에 회원 등록 후 jwt 토큰 발행
    - 로그인 이력이 있는 회원인 경우 jwt발행

- ### jwt 토큰 인증 데코레이터
    - 서버에서 발행한 jwt인지 확인하고 로그인 여부 판단
    - 요청에 user 객체를 담아 반환

<br>

### 전체 숙소 리스트 조회 및 필터링
- 사용자가 선택한 옵션에 해당되는 데이터만 filtering하여 반환
- 사용자가 체크인/체크아웃 날짜 등 예약 조건을 선택한 경우 exclude() 를 이용하여 예약 가능한 숙소만 반환
- Pagination: 쿼리스트링으로 offset, limit 값을 받아 원하는 데이터 개수만큼만 반환
- Annotate를 이용하여 숙소의 리뷰 총 개수 및 평점 계산

<br>

>## 최형택

<br>

>## 강종범
### 호스트 되기 API 구현
- API 호출 시 request로 파일들을 받아 개수가 기획에서 의도한 2개 미만일 때 해당 에러메세지 반환
- 등록 될 숙소의 국가 정보나, 도시 정보가 프로젝트 DB에 없을 시 생성하여 저장하고 있을 시 불러오는 로직 작성
- transaction을 사용하여 모든 입력 정보가 한번에 처리 되게끔 작성

<br>

### AWS S3를 이용한 이미지 업로드 구현
- boto3를 사용하여 s3에 이미지 업로드하는 기능을 클래스화 하여 구현


<br><br>

## Reference

이 프로젝트는 에어비앤비 사이트를 참조하여 학습목적으로 만들었습니다.

실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.

이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
