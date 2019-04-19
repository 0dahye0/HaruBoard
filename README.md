# HaruBoard
익명 게시판 서비스를 위한 프로젝트 HaruBoard

### 개발 환경 및 기술 스택

Python 3.6 - Django 2.2<br/>
psycopg2<br/>
Virtualenv<br/>
HTML · CSS · Javascript · UIKit · jQuery(AJAX)<br/>
PostgreSQL 9.6<br/>
Visual Studio Code<br/>

### 배포 환경

진행 중인 프로젝트 이며 현재 local 테스트 서버로 구동 중입니다.<br/>
아래 배포 환경은 '예정' 입니다.<br/>
<br/>
Google Cloud Platform ( GCP )<br/>
Compute Engine vCPU 1 / 1.7 GB Mem / HDD / Osaka(asia-northeast2)<br/>
SQL PostgreSQL 9.6 / vCPU 1 / 1.7 GB Mem / HDD / Tokyo(asia-northeast1-a)<br/>
Debian 9 (stretch) Python 3.6 | NGINX · Gunicorn<br/>
https://board.haruhuey.kr --> Cloudflare SSL · DNS<br/>

### HaruBoard 기타 사항

가장 최근에 진행하고 있는 프로젝트입니다.
익명 게시판이라는 주제로 시작 된 본 프로젝트는 인스타그램 디자인을 모티브로 하며<br/>
AJAX를 통한 로딩과 POST(게시물) 상호작용 기능, 댓글 처리 기능 등에 대해 배우며<br/>
공개 배포(외부)를 통해 로그 정보를 수집하며 운영 경험을 쌓기 위해 개발을 진행하고<br/>
있습니다.<br/>
<br/>
현재는 UIKit 을 통해 메인 페이지의 간단한 구조만 나온 형태이며 Django 연동과<br/>
URL Routing, AJAX 구현 등 아직은 부족한 프로젝트 입니다.<br/>
<br/>
HTML과 CSS(Django 정적 load 제거 후 CSS 링크)<br/>
Django URL과 Views(HTML Render) / 간단한 라우팅 및 렌더<br/>
