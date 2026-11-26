# ELECTRIC NEWS LAB ⚡

학생을 위한 전기·에너지 뉴스 자동 수집 사이트.

- GitHub Pages 정적 사이트
- 매주 Google News RSS 기반 기사 수집 (최근 7일 검색)
- 전력, 신재생에너지, 배터리, 전기차, 전기 안전, 전기 기술 분류
- 검색 및 분야 필터
- GitHub Actions 자동 실행 및 수동 실행

## 배포
GitHub 저장소 Settings > Pages에서 Deploy from a branch를 선택하고 main / root를 지정합니다.

## 자동 수집
GitHub Actions의 Weekly Electric News Crawl은 매주 일요일 UTC 21시 (한국 시간 월요일 오전 6시)에 실행됩니다. Actions 탭에서 수동 실행도 가능합니다.

뉴스 RSS 수집은 기사 제목, 출처, 날짜, 링크만 저장합니다. 요약 문구는 학습 안내용이며 기사의 AI 요약은 아닙니다.
