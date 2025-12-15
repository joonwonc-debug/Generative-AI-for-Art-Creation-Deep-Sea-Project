import streamlit as st
import os
from PIL import Image
import base64

# --- 1. 페이지 설정 (반드시 코드 최상단에 위치) ---
st.set_page_config(
    page_title="ABYSS: The Deep Sea Archive",
    page_icon="🦈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. 커스텀 CSS (디자인 핵심: 다크모드, 네온 효과, 폰트) ---
def local_css():
    st.markdown("""
    <style>
        /* 전체 배경을 심해색(매우 어두운 남색)으로 변경 */
        .stApp {
            background-color: #050510;
            background-image: linear-gradient(to bottom, #020205, #0a1128);
            color: #E0E0E0;
        }
        
        /* 제목 스타일링 (네온 효과) */
        h1 {
            font-family: 'Courier New', Courier, monospace;
            color: #00FFFF;
            text-shadow: 0 0 10px #00FFFF, 0 0 20px #00AAAA;
            text-align: center;
            padding-bottom: 20px;
        }
        
        h3 {
            color: #00e5ff;
            border-bottom: 1px solid #00e5ff;
            padding-bottom: 10px;
        }

        /* 이미지 컨테이너 스타일 (박물관 액자 느낌) */
        div[data-testid="stImage"] {
            border: 1px solid #333;
            border-radius: 10px;
            padding: 5px;
            background-color: #111;
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }
        
        div[data-testid="stImage"]:hover {
            transform: scale(1.02);
            border: 1px solid #00FFFF;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
        }

        /* 사이드바 스타일 */
        [data-testid="stSidebar"] {
            background-color: #020205;
            border-right: 1px solid #333;
        }
        
        /* 캡션 텍스트 스타일 */
        .caption-text {
            color: #aaaaaa;
            font-size: 0.9em;
            text-align: center;
            margin-top: -10px;
            margin-bottom: 20px;
            font-family: 'Helvetica', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- 3. 사이드바 (탐사 로그 컨셉) ---
with st.sidebar:
    st.title("⚓ MISSION CONTROL")
    st.markdown("---")
    st.write("**Current Depth:** 8,400m")
    st.write("**Pressure:** 850 atm")
    st.write("**Status:** Online")
    
    st.markdown("---")
    st.info("""
    **[ARCHIVE INFO]**
    이곳에 전시된 생명체들은
    인류가 도달하지 못한
    심해의 미확인 생물체(Unidentified)들입니다.
    """)
    st.warning("⚠️ WARNING: 일부 생물체는 정신 착란을 유발할 수 있습니다.")

# --- 4. 메인 헤더 ---
st.title("THE ABYSS ARCHIVE")
st.markdown("<p style='text-align: center; color: #888;'>CLASSIFIED DEEP SEA SPECIMENS COLLECTED BY AI</p>", unsafe_allow_html=True)
st.divider()

# --- 5. 이미지 갤러리 로직 ---
image_folder = "images"

if not os.path.exists(image_folder):
    st.error("❌ 'images' 폴더를 찾을 수 없습니다. 프로젝트 폴더 안에 images 폴더를 생성하고 사진을 넣어주세요.")
else:
    # 이미지 파일 불러오기
    files = os.listdir(image_folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    if not image_files:
        st.write("📂 저장된 표본이 없습니다. images 폴더에 사진을 추가하세요.")
    else:
        # 3열 그리드 레이아웃
        cols = st.columns(3)
        
        for idx, file_name in enumerate(image_files):
            file_path = os.path.join(image_folder, file_name)
            img = Image.open(file_path)
            
            # 파일명 가공 (예: "deep_fish.jpg" -> "Deep Fish")
            display_name = file_name.split('.')[0].replace("Gemini_Generated_Image_", "").replace("_", " ").upper()
            
            # 짧은 이름으로 자르기 (너무 길면 디자인 깨짐 방지)
            if len(display_name) > 20:
                display_name = display_name[:15] + "..."

            # 열 순서대로 배치
            with cols[idx % 3]:
                st.image(img, use_container_width=True)
                st.markdown(f"<div class='caption-text'>SPECIMEN: {display_name}</div>", unsafe_allow_html=True)
                
                # 상세 정보 (Expander) - 박물관 도슨트 설명 느낌
                with st.expander("🔬 표본 데이터 분석"):
                    st.write(f"""
                    - **학명:** *Abyssal {display_name.split()[-1]}*
                    - **발견 심도:** {3000 + (idx * 520)}m
                    - **위험 등급:** {'🔴 Extreme' if idx % 2 == 0 else '🟡 Moderate'}
                    - **특이 사항:** 생체 발광 기관 보유. 고압 환경 적응 진화.
                    """)

# --- 6. 푸터 ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #444; font-size: 0.8em;'>© 2024 DEEP SEA RESEARCH LAB. ACCESS RESTRICTED.</p>", unsafe_allow_html=True)
