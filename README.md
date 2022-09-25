# 프로젝트 소개

![리뷰맛집](https://user-images.githubusercontent.com/75832544/186341537-be7f66ae-113e-47cc-8006-8539e74a69d7.png)

컬리 해커톤 [이커머스에서 해결하고자 하는 과제 구현 팀 프로젝트]

유저 작성 후기와 함께 구매한 상품 목록을 기반으로 연관 상품 및 카테고리 추천 서비스를 개발하였습니다. <br>
기존의 리뷰 및 신규 리뷰 데이터를 활용한 키워드 분석을 통해 연관 카테고리를 도출하고, 함께 구매한 상품을 기반으로 유저에게 직접 피드백을 받는 연관 상품 도출 방식을 구현하고 배포하였습니다.

## 초기기획 & ERD

## 과제 계획서
[작성자 : <a href="https://github.com/DevSeulgi">Seulgi Park</a>]

![리뷰맛집 과제 계획서_1](https://blog.kakaocdn.net/dn/5arvi/btrMUTtXYms/Xwoh9fRQ1Lf5cqikdUgKj1/img.jpg)

![리뷰맛집 과제 계획서_2](https://blog.kakaocdn.net/dn/wZYm3/btrMUFpcdLx/yjUYj7SpmyKVJGpfE5Yqr0/img.jpg)

![리뷰맛집 과제 계획서_3](https://blog.kakaocdn.net/dn/mo2iS/btrMYqEdF7N/VqqtRsAKzrvvzCzrhAxlo1/img.jpg)

![리뷰맛집 과제 계획서_4](https://blog.kakaocdn.net/dn/rmiqm/btrMUGhl6kO/OjSylKVtAmthcXt8FaXmHk/img.jpg)

![리뷰맛집 과제 계획서_5](https://blog.kakaocdn.net/dn/bc8SXX/btrMUM9Aj3T/R50EbKXx1KhIow7iDhsjY0/img.jpg)

### Main Service Flow
로그인 > 메인페이지 > 금주의 베스트 리뷰 페이지 > 카테고리별 리뷰 순위 > 제품 상세페이지 > 리뷰 작성
  
## 개발기간 및 팀원

### 개발기간
2022.08. ~ 2022.08. (1주간)

### 팀명
리뷰왕 킹컬리(ReviewKing KingKurly)

### 팀원 소개
| 개발 분야 | 팀원 명 |
| ------- | ------- |
| 프론트엔드 | 박슬기, 장수연 |
| 백엔드 | 최혜인, 황재승 |

## 기술 스택 및 구현 기능
### 적용 기술
Python, Django, MySQL, AWS EC2 / RDS / S3 활용 배포

### 백엔드 업무 담당
최혜인 - DB 모델링, 리뷰 API <br>
황재승 - DB 모델링, 제품 API, 고객 API <br>

### 구현 기능
<p>
- products : 연관 카테고리 및 연관 상품 추출 기능 구현 <br>
- reviews : 리뷰를 작성하고 S3로 해당 리뷰의 이미지 저장 및 리뷰 기반의 키워드 추출 기능 구현 <br>
- users : 기본적인 사용자 관련 기능 구현 <br>
- core : 리뷰에서 상품명을 추출하도록 함수 선언, jwt 및 로그인 데코레이터 
</p>

### 과제 발표자료

![리뷰맛집 과제 발표자료_1](https://blog.kakaocdn.net/dn/cj9GKn/btrM0nHdVCU/PBk5dMAmbG2whmidWRkOOK/img.jpg)

![리뷰맛집 과제 발표자료_2](https://blog.kakaocdn.net/dn/qwpNG/btrMUTHBN9q/rHEfBrSlfvBEKEkfkf9H10/img.jpg)

![리뷰맛집 과제 발표자료_3](https://blog.kakaocdn.net/dn/zlHpG/btrMYS1LePj/AC9SEWiiLWYbKSXmv8H7uK/img.jpg)

![리뷰맛집 과제 발표자료_4](https://blog.kakaocdn.net/dn/tzGde/btrM2qcBW1W/D0KxE28xtOlizKgt3EzuQk/img.jpg)

![리뷰맛집 과제 발표자료_5](https://blog.kakaocdn.net/dn/AKIlq/btrM0nNZpfy/8kTGx4mmHkXd50PpkzdTVK/img.jpg)

![리뷰맛집 과제 발표자료_6](https://blog.kakaocdn.net/dn/cDIXy3/btrMUMhvkI7/l3rvDqNp39En4hNMBSRpz0/img.jpg)

![리뷰맛집 과제 발표자료_7](https://blog.kakaocdn.net/dn/bpjZGm/btrMWd6zuma/EDeExcTlJbfbSZkUdYzjLK/img.jpg)

![리뷰맛집 과제 발표자료_8](https://blog.kakaocdn.net/dn/bzGTDM/btrMXjSZP3d/TjE7b52CbOWk1K0JSSzlKk/img.jpg)

![리뷰맛집 과제 발표자료_9](https://blog.kakaocdn.net/dn/GKOnn/btrMYTGmHLB/1zbuFNyveq5gd6CMDSDn00/img.jpg)

![리뷰맛집 과제 발표자료_10](https://blog.kakaocdn.net/dn/LoPCc/btrMWdyJ2Ic/1e7y4huM7w57EN346BjXyk/img.jpg)

### API DOC
<a href="https://hyein-resume.notion.site/API-7d57f051fcb44ba3a2ccc208d448b260">노션</a> 을 이용해 엔드포인트 정의 및 공유

## Frontend Repository
[프론트엔드 레포지토리 바로가기](https://github.com/reviewking-kingkurly/review_king_front)

## 시연영상
![시연영상](https://im3.ezgif.com/tmp/ezgif-3-d84c387f06.gif)