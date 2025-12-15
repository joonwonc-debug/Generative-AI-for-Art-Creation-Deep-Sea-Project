import streamlit as st
import os
from PIL import Image
import base64

# --- 1. 페이지 설정 (반드시 최상단) ---
st.set_page_config(
    page_title="THE ABYSS: ARCHIVE",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed" # 사이드바를 숨겨서 더 넓고 깔끔하게
)

# --- 2. 고급스러운 박물관 스타일 CSS ---
def local_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400&display=swap');

        /* 전체 배경: 완전한 칠흑색 (고급스러움 강조) */
        .stApp {
            background-color: #050505;
            color: #E0E0E0;
            font-family: 'Lato', sans-serif;
        }

        /* 타이틀 폰트: 우아한 명조체 (Serif) */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            font-weight: 600;
            letter-spacing: 2px;
        }

        /* 메인 타이틀 스타일: 금빛 그라데이션 텍스트 */
        .main-title {
            font-size: 3.5em;
            text-align: center;
            background: -webkit-linear-gradient(#eee, #999);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: 50px;
            margin-bottom: 10px;
        }

        .sub-title {
            text-align: center;
            font-family: 'Lato', sans-serif;
            font-weight: 300;
            color: #888;
            font-size: 1.0em;
            letter-spacing: 5px;
            margin-bottom: 60px;
            text-transform: uppercase;
        }

        /* 이미지 카드 스타일: 미니멀한 액자 느낌 */
        div[data-testid="stImage"] {
            border: 1px solid #222;
            padding: 15px;
            background-color: #0f0f0f;
            transition: all 0.4s ease;
        }
        
        div[data-testid="stImage"]:hover {
            border-color: #C5A059; /* 앤티크 골드색 */
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }

        /* 캡션 스타일: 도록 설명처럼 작고 깔끔하게 */
        .caption-style {
            font-family: 'Playfair Display', serif;
            color: #C5A059; /* 골드 포인트 */
            font-size: 1.1em;
            margin-top: 10px;
            text-align: left;
            border-bottom: 1px solid #333;
            padding-bottom: 5px;
        }

        .desc-style {
            font-family: 'Lato', sans-serif;
            font-size: 0.85em;
            color: #888;
            margin-top: 5px;
            line-height: 1.6;
            text-align: justify;
        }

        /* 구분선 스타일 */
        hr {
            border-top: 1px solid #222;
            margin: 50px 0;
        }
        
        /* Expander 스타일 커스텀 (상세보기 버튼) */
        .streamlit-expanderHeader {
            font-family: 'Lato', sans-serif;
            font-size: 0.9em;
            color: #666;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- 3. 오디오 가이드 (배경 음악) ---
# audio/deep_sea_ambient.mp3 파일이 있어야 재생됩니다.
audio_path = "audio/deep_sea_ambient.mp3"

if os.path.exists(audio_path):
    # 화면에 플레이어를 작게 숨기거나 하단에 배치
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
        # autoplay=True로 자동 재생
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        # 플레이어를 시각적으로 숨기고 싶으면 아래 주석 해제 (CSS로 숨김 처리)
        # st.markdown("<style>audio {display:none;}</style>", unsafe_allow_html=True) 
else:
    # 파일이 없으면 조용히 넘어감 (에러 메시지로 디자인 망치지 않음)
    pass

# --- 4. 메인 전시 공간 ---

# 헤더 섹션
st.markdown("<h1 class='main-title'>THE ABYSS</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Unknown Specimens Exhibition</div>", unsafe_allow_html=True)

st.write("") # 여백
st.write("") 

# 인트로 텍스트 (박물관 벽면 텍스트 느낌)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown("""
    <div style='text-align: center; color: #aaa; font-style: italic; font-family: "Playfair Display", serif;'>
    "Generative AI for Art Creation, <br>
    Undiscovered Creatures Generated Image Under Deep Sea."
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 5. 갤러리 로직 ---
image_folder = "images"

if not os.path.exists(image_folder):
    st.error("System Error: Image archive not found.")
else:
    files = sorted(os.listdir(image_folder)) # 파일 이름순 정렬
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    if not image_files:
        st.write("No specimens available.")
    else:
        # 3열 그리드 (여백을 넉넉하게)
        cols = st.columns(3)
        
        for idx, file_name in enumerate(image_files):
            file_path = os.path.join(image_folder, file_name)
            img = Image.open(file_path)
            
            # 이름 가공
            raw_name = file_name.split('.')[0].replace("Gemini_Generated_Image_", "").replace("_", " ")
            
            with cols[idx % 3]:
                # 이미지 출력
                st.image(img, use_container_width=True)
                
                # 작품 설명 (박물관 캡션 스타일)
                st.markdown(f"<div class='caption-style'>Specimen No. {idx+1 :03d}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='desc-style'>**Designation:** {raw_name.upper()}</div>", unsafe_allow_html=True)
                
                # 미니멀한 상세보기
                with st.expander("View Details"):
                    st.markdown(f"""
                    <div style='font-size: 0.8em; color: #bbb;'>
                    • <b>Estimated Depth:</b> {4000 + (idx * 350)}m<br>
                    • <b>Environment:</b> High Pressure / Zero Light<br>
                    • <b>Status:</b> Cataloged by AI
                    </div>
                    """, unsafe_allow_html=True)
                
                st.write("") # 카드 간 간격 조절
                st.write("")

# --- 6. 푸터 ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 0.7em; color: #444; letter-spacing: 2px;'>
MUSEUM OF GENERATIVE BIOLOGY &copy; 2024
</div>
""", unsafe_allow_html=True)
