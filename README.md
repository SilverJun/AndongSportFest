# AndongSportFest

2020 안동 학생스포츠 대축전 노션 페이지 프로젝트

https://sportfest.oopy.io

* oopy.io를 사용해 노션 페이지에 custom url 적용
* 스마트폰 홈화면에 바로가기 아이콘 추가
    * 각 기기별로 내장기능 사용하도록 안내
    * 아이콘은 oopy.io에서 제공하는 script injection을 사용해 header영역에 소스코드 추가
* 구글 폼에 영상을 올리면 notion에 자동으로 등록되도록 프로그래밍
    * 구글 폼이 제출되었을 때 google script를 사용해 파이썬 웹서버에 post request
    * 파이썬 웹서버에서 post 받으면 notion-py로 만든 collection view 업로드 스크립트 실행
