# 디렉터리 구조
```
42gg.match.server/
├── app/                         # 주요 애플리케이션 코드가 위치하는 루트 디렉터리
│   ├── api/                     # API 엔드포인트 관련 파일들이 위치
│   │   ├── v1/                  
│   │   │   ├── endpoints/       # 각 도메인별 API 엔드포인트 파일들
│   │   │   │   ├── __init__.py  
│   │   │   │   ├── auth.py      # OAuth와 JWT 기반 인증 및 인가를 처리하는 엔드포인트
│   │   │   │   ├── evaluation.py# 평가 기능을 처리하는 엔드포인트
│   │   │   │   └── user.py      # 사용자 관련 엔드포인트
│   │   │   ├── __init__.py      
│   │   │   └── deps.py          # 의존성 주입을 위한 파일
│   ├── core/                    # 애플리케이션의 핵심 설정 및 보안 관련 파일들
│   │   ├── __init__.py          # 패키지 초기화 파일
│   │   ├── config.py            # 애플리케이션 설정을 관리
│   │   ├── security.py          # 보안 관련 유틸리티와 설정을 관리
│   │   └── logging.py           # 로깅 설정 및 유틸리티를 관리
│   ├── services/                # 비즈니스 로직을 처리하는 서비스 레이어
│   │   ├── __init__.py          # 패키지 초기화 파일
│   │   ├── auth_service.py      # 인증 및 인가 서비스 로직
│   │   ├── evaluation_service.py# 평가 서비스 로직
│   │   └── user_service.py      # 사용자 서비스 로직
│   ├── utils/                   # 재사용 가능한 유틸리티 함수들이 위치
│   │   ├── __init__.py          # 패키지 초기화 파일
│   │   ├── redis.py             # Redis와 관련된 유틸리티 함수들
│   │   └── common.py            # 공통으로 사용되는 유틸리티 함수들
│   ├── main.py                  # FastAPI 애플리케이션의 진입점
│   ├── dependencies.py          # 의존성 주입을 위한 공통 모듈
│   └── schemas/                 # Pydantic 스키마 정의 파일들이 위치
│       ├── __init__.py          # 패키지 초기화 파일
│       ├── auth.py              # 인증 관련 스키마 (dto)
│       ├── evaluation.py        # 평가 관련 스키마 (dto)
│       └── user.py              # 사용자 관련 스키마 (dto)
├── tests/                       # 테스트 관련 파일들이 위치
│   ├── __init__.py              # 패키지 초기화 파일
│   ├── test_auth.py             # 인증 및 인가 관련 테스트
│   ├── test_evaluation.py       # 평가 기능 관련 테스트
│   └── test_user.py             # 사용자 기능 관련 테스트
├── .env                         # 환경 변수 설정 파일
├── .gitignore                   # Git에서 추적하지 않을 파일들을 지정
├── poetry.lock                  # Poetry 종속성 잠금 파일
├── pyproject.toml               # 프로젝트의 종속성 및 설정을 정의
└── README.md                    # 프로젝트 설명서
```

* 디렉터리 구조 한번 읽어보고 숙지 부탁드립니다.
* Exception은 관련한 도메인별로 상속받아서 더 작성하셔도 됩니다.