import streamlit as st
import os
from PIL import Image
import base64

# --- 1. 페이지 설정 ---
st.set_page_config(
    page_title="ABYSS: Deep Sea Wonders Exhibition",
    page_icon="🐙", # 더 적절한 아이콘으로 변경
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. 커스텀 CSS (심해 박물관 테마) ---
def local_css():
    st.markdown("""
    <style>
        /* 전체 배경: 깊은 바다 그라데이션 */
        .stApp {
            background-color: #020510;
            background-image: linear-gradient(to bottom, #000005, #000a20, #000d30);
            color: #E0E0E0;
            font-family: 'Georgia', serif; /* 전시회 느낌 폰트 */
        }
        
        /* 헤더 및 타이틀: 웅장하고 빛나는 느낌 */
        h1 {
            font-family: 'Times New Roman', serif;
            color: #BBDEFB; /* 밝은 푸른색 */
            text-shadow: 0 0 15px rgba(187, 222, 251, 0.7), 0 0 30px rgba(187, 222, 251, 0.4);
            text-align: center;
            padding: 30px 0;
            border-bottom: 2px solid rgba(187, 222, 251, 0.3);
            margin-bottom: 40px;
        }
        
        h2 {
            color: #81D4FA; /* 약간 더 어두운 푸른색 */
            font-family: 'Georgia', serif;
            margin-top: 30px;
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(129, 212, 250, 0.2);
            padding-bottom: 10px;
        }

        /* 서브 헤더 */
        h3 {
            color: #90CAF9;
            font-family: 'Georgia', serif;
            border-bottom: 1px solid rgba(144, 202, 249, 0.2);
            padding-bottom: 8px;
            margin-top: 25px;
        }

        /* 일반 텍스트 */
        p {
            font-size: 1.05em;
            line-height: 1.6;
        }

        /* 구분선 */
        hr {
            border-top: 1px solid rgba(187, 222, 251, 0.1);
            margin: 30px 0;
        }

        /* 사이드바 */
        [data-testid="stSidebar"] {
            background-color: #010308;
            border-right: 1px solid #1a237e;
            padding: 20px;
        }
        [data-testid="stSidebar"] .stButton {
            width: 100%;
            background-color: #1A237E;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px;
        }
        [data-testid="stSidebar"] .stButton:hover {
            background-color: #283593;
        }
        
        /* 이미지 컨테이너 (전시 패널 느낌) */
        div[data-testid="stImage"] {
            border: 2px solid #1A237E; /* 깊은 남색 테두리 */
            border-radius: 12px;
            padding: 8px;
            background-color: #080C1A; /* 이미지 배경 */
            box-shadow: 0 6px 15px rgba(0,0,0,0.7), 0 0 10px rgba(26, 35, 126, 0.4); /* 그림자 및 발광 */
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            margin-bottom: 25px;
        }
        
        div[data-testid="stImage"]:hover {
            transform: translateY(-5px) scale(1.02);
            border: 2px solid #00FFFF; /* 호버 시 네온 테두리 */
            box-shadow: 0 8px 20px rgba(0,0,0,0.8), 0 0 25px rgba(0, 255, 255, 0.6);
        }

        /* 캡션 텍스트 (표본 정보) */
        .specimen-caption {
            color: #B0BEC5; /* 은은한 회색 */
            font-size: 0.9em;
            text-align: center;
            margin-top: -15px; /* 이미지와 가깝게 */
            margin-bottom: 20px;
            font-family: 'Roboto', sans-serif;
            font-style: italic;
        }

        /* 인포 박스 (전시 설명 패널) */
        .stAlert {
            background-color: rgba(26, 35, 126, 0.3);
            border-left: 5px solid #00B0FF;
            color: #E0E0E0;
        }

        /* 코드 블록 (데이터 표시용) */
        .stCodeBlock {
            background-color: #000510;
            border: 1px solid #1A237E;
            padding: 15px;
            border-radius: 8px;
        }
        
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- 3. 배경 음악 추가 (자동 재생) ---
audio_file_path = "audio/deep_sea_ambient.mp3"
if os.path.exists(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0, loop=True, autoplay=True)
else:
    st.sidebar.warning("🔊 배경 음악 파일(deep_sea_ambient.mp3)을 찾을 수 없습니다. 'audio' 폴더에 넣어주세요.")

# --- 4. 사이드바 (큐레이터 노트) ---
with st.sidebar:
    st.header("🌌 심해 박물관: 큐레이터 노트")
    st.markdown("---")
    st.markdown("""
    **전시 주제: ABYSSAL WONDERS**
    <p style='font-size:0.9em;'>인류가 미처 도달하지 못한 심해의 신비로운 영역에서, AI가 상상으로 빚어낸 미지의 생명체들을 소개합니다. 이 디지털 전시는 빛 한 줄기 없는 심연 속에서 진화한 생명체의 경이로움을 탐구합니다.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("탐사 기록")
    st.write(f"**현재 관측 수심:** {st.slider('시뮬레이션 수심', 0, 10000, 7500, 500)}m")
    st.write("**수압:** 약 750 기압")
    st.markdown("---")
    
    st.markdown("---")
    st.info("""
    **[전시 안내]**
    본 전시에 소개된 생물들은 생성형 AI에 의해 구현된 가상의 존재입니다.
    이들은 심해 생태계의 다양성과 미지에 대한 인간의 상상력을 자극합니다.
    """)
    st.markdown("---")
    st.button("전시 해설 듣기 (준비중)", help="클릭 시 전시 해설 음성 재생")

# --- 5. 메인 헤더 (전시회 메인 간판) ---
st.title("DEEP SEA WONDERS: The Abyssal Archive")
st.markdown("<p style='text-align: center; color: #BBDEFB;'>AI가 밝혀낸 심연 속 미지의 경이로운 생명체들</p>", unsafe_allow_html=True)
st.divider()

st.header("✨ 심연의 조각들: 컬렉션")
st.markdown("""
<p style='font-size:1.1em; line-height:1.7;'>
수많은 탐사선이 침묵한 심해의 어둠 속에서, 우리는 AI의 눈을 통해 전에 없던 생명체들을 조우합니다. 
각각의 표본은 고유한 빛과 형태, 그리고 심연에 적응한 생존 전략을 보여주며, 우리에게 
'생명'의 한계를 다시 생각하게 합니다.
</p>
""", unsafe_allow_html=True)
st.divider()

# --- 6. 이미지 갤러리 로직 ---
image_folder = "images"

if not os.path.exists(image_folder):
    st.error("❌ 'images' 폴더를 찾을 수 없습니다. 프로젝트 폴더 안에 images 폴더를 생성하고 사진을 넣어주세요.")
else:
    files = os.listdir(image_folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    if not image_files:
        st.warning("📂 전시할 표본이 없습니다. 'images' 폴더에 AI 생성 사진을 추가하세요!")
    else:
        cols = st.columns(3) # 3열 그리드
        
        for idx, file_name in enumerate(image_files):
            file_path = os.path.join(image_folder, file_name)
            img = Image.open(file_path)
            
            # 파일명에서 확장자와 'Gemini_Generated_Image_' 제거 후 가공
            display_name = file_name.split('.')[0].replace("Gemini_Generated_Image_", "").replace("_", " ").title()
            
            # 열 순서대로 배치
            with cols[idx % 3]:
                st.image(img, use_container_width=True)
                st.markdown(f"<div class='specimen-caption'>SPECIMEN ID: <span style='color:#00B0FF;'>{display_name}</span></div>", unsafe_allow_html=True)
                
                # 상세 정보 - '전시 해설' 느낌
                with st.expander(f"👁️‍🗨️ [{display_name}] 표본 상세 분석"):
                    st.markdown(f"**학명:** *Abyssalis {display_name.replace(' ', '_').lower()}*")
                    st.markdown(f"**발견 심도:** 약 {3000 + (idx * 450)}m - {4000 + (idx * 550)}m")
                    st.markdown(f"**생존 전략:** {'강력한 생체 발광 유인체' if idx % 2 == 0 else '위장 및 고압 적응 단단한 외피'}")
                    st.markdown(f"**위험 등급:** {'🔴 위험 (Extremely Hazardous)' if idx % 3 == 0 else '🟡 주의 (Potentially Dangerous)' if idx % 3 == 1 else '🟢 무해 (Harmless)'}")
                    st.markdown(f"**큐레이터 코멘트:** <p style='font-size:0.9em; font-style:italic;'>\"이 {display_name}은/는 심해의 극한 환경 속에서 빛과 어둠을 이용해 생존하는 놀라운 사례를 보여줍니다.\"</p>", unsafe_allow_html=True)
                    st.code(f"데이터 로그: pH 6.8, 수온 2.1°C, 염도 35‰", language="markdown")

# --- 7. 푸터 (저작권 및 정보) ---
st.divider()
st.markdown("<p style='text-align: center; color: #444; font-size: 0.8em;'>© 2024 ABYSSAL RESEARCH INITIATIVE. ALL RIGHTS RESERVED. Unauthorized access is strictly prohibited.</p>", unsafe_allow_html=True)
```http://googleusercontent.com/image_generation_content/2
