import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. КОНФІГУРАЦІЯ СТОРІНКИ ТА КІБЕРПАНК СТИЛІЗАЦІЯ
st.set_page_config(
    page_title="Патрік OS v6.0",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

cyberpunk_css = """
<style>
    .stApp { background-color: #0b031a; color: #e0d5f5; }
    .sidebar .sidebar-content { background-color: #14072d; }
    h1, h2, h3 { color: #b388ff !important; text-shadow: 0 0 10px #7c4dff; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #7c4dff !important; color: white !important; border: 1px solid #b388ff !important; box-shadow: 0 0 8px #7c4dff; transition: 0.3s; }
    .stButton>button:hover { background-color: #b388ff !important; box-shadow: 0 0 15px #b388ff; }
</style>
"""
st.markdown(cyberpunk_css, unsafe_allow_html=True)

# 2. ІНІЦІАЛІЗАЦІЯ GEMINI API
API_KEY = "GEMINI_KEY"
genai.configure(api_key=API_KEY)

system_instruction = (
    "Ти — Патрік OS v6.0, досвідчений інженер-напарник, ШІ-бро. "
    "Спілкуєшся просто, з дружнім гумором, без зайвої офіціози та води. "
    "Коротко, по ділу, підтримуєш розробника. Використовуй технічний сленг, де це доречно."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

# 3. ІНТЕРФЕЙС ТА НАВІГАЦІЯ
st.title("🤖 ПАТРІК OS v6.0 // СИСТЕМА ЗАПУЩЕНА")

module = st.sidebar.radio(
    "🤖 ОВЕРЛЕЙ МОДУЛІВ:",
    ["Кібер-Strategist", "Візуальний Аудит", "SMM Автопілот", "Кухня Коду"]
)

st.sidebar.markdown("---")
st.sidebar.success("Мізки: Gemini 1.5 Flash")
st.sidebar.info("Статус: Ланцюжок GitHub -> Streamlit Cloud")

# 4. ЛОГІКА РОБОТИ МОДУЛІВ
if module == "Кібер-Strategist":
    st.subheader("🎯 Модуль: Кібер-Strategist")
    mode = st.checkbox("🔥 Увімкнути режим Devil's Advocate (Жорстка критика)")
    
    user_input = st.text_area("Яку бізнес-ідею або фічу аналізуємо, бро?")
    if st.button("Запустити аналіз"):
        if user_input:
            prompt = user_input
            if mode:
                prompt += " (Розкритикуй цю ідею в пух і прах як Devil's Advocate, знайди всі слабкі місця)."
            
            with st.spinner("🤖 Патрік думає..."):
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.warning("Введи щось, бро, немає контексту для аналізу.")

elif module == "Візуальний Аудит":
    st.subheader("🖼️ Модуль: Візуальний Аудит")
    st.write("Завантажуй сюди скріншот сайту, додатка чи інтерфейсу, і я розберу його по поличках.")
    
    uploaded_file = st.file_uploader("Завантаж зображення (PNG, JPG, JPEG):", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Твій скріншот завантажено, бро", use_column_width=True)
        
        audit_prompt = st.text_input("На що звернути особливу увагу? (Або залиш порожнім для загального аудиту):")
        
        if st.button("Просканувати візуал"):
            with st.spinner("🤖 Патрік сканує пікселі..."):
                final_prompt = [
                    "Зроби повний технічний та UX/UI аудит цього зображення. Знайди косяки, баги верстки, проблеми з юзабіліті та дай чіткі інженерні поради, як це покращити.",
                    image
                ]
                if audit_prompt:
                    final_prompt.append(f"Особливий фокус користувача на це: {audit_prompt}")
                
                response = model.generate_content(final_prompt)
                st.write(response.text)

elif module == "SMM Автопілот":
    st.subheader("📱 Модуль: SMM Автопілот")
    st.info("Тут буде генерація контент-планів та вірусних постів.")

elif module == "Кухня Коду":
    st.subheader("⚡ Модуль: Кухня Коду")
    st.info("Тут буде рев'ю твого коду та пошук багів.")
