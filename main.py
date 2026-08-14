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

# 2. БЕЗПЕЧНА ІНІЦІАЛІЗАЦІЯ GEMINI API ЧЕРЕЗ НОВИЙ SECRETS ТОКЕН
try:
    API_KEY = st.secrets["PATRIK_BRAIN"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("🚨 Бро, залий новий API-ключ у Secrets додатка на Streamlit Cloud! Поле PATRIK_BRAIN порожнє.")
    st.stop()

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
    st.write("Завантажуй сюди скріншот сайту чи інтерфейсу, і я розберу його по пікселях.")
    
    uploaded_file = st.file_uploader("Завантаж зображення:", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Твій скріншот завантажено, бро", use_column_width=True)
        audit_prompt = st.text_input("На що звернути особливу увагу? (Або залиш порожнім):")
        
        if st.button("Просканувати візуал"):
            with st.spinner("🤖 Патрік сканує пікселі..."):
                final_prompt = [
                    "Зроби повний технічний та UX/UI audit цього зображення. Знайди косяки, баги верстки, проблеми з юзабіліті та дай чіткі інженерні поради розробнику.",
                    image
                ]
                if audit_prompt:
                    final_prompt.append(f"Особливий фокус користувача на це: {audit_prompt}")
                response = model.generate_content(final_prompt)
                st.write(response.text)

elif module == "SMM Автопілот":
    st.subheader("📱 Модуль: SMM Автопілот")
    st.write("Генеруємо вірусний контент та стратегію просування в один клік.")
    
    project_desc = st.text_area("Опиши свій проєкт чи товар, бро (для кого пишемо?):")
    post_type = st.selectbox("Який контент потрібен?", ["Вірусний пост для Instagram/TikTok", "Експертний лонгрід для Telegram", "Контент-план на 7 днів"])
    tone_style = st.select_slider("Тональність тексту:", options=["Максимально серйозно", "Дружній хайп", "Повний треш і гумор"])
    
    if st.button("Згенерувати контент"):
        if project_desc:
            prompt = f"Напиши контент для проєкту: '{project_desc}'. Тип контенту: {post_type}. Стиль: {tone_style}. Додай емодзі та відповідні хештеги."
            with st.spinner("🤖 Патрік пише тексти..."):
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.warning("Вкажи опис проєкту, бро.")

elif module == "Кухня Коду":
    st.subheader("⚡ Модуль: Кухня Коду")
    st.write("Твій особистий ШІ-рев'юер коду. Знайду баги, оптимізую рефакторинг.")
    
    code_input = st.text_area("Встав свій шматок коду сюди, бро (Python, JS, HTML тощо):", height=200)
    task_type = st.radio("Що зробити з кодом?", ["Знайти баги та косяки", "Зробити красивий рефакторинг/оптимізацію", "Пояснити як це працює простими словами"])
    
    if st.button("Шеф-кухар, до столу!"):
        if code_input:
            prompt = f"Проаналізуй цей код. Завдання: {task_type}. Ось код:\n\n{code_input}"
            with st.spinner("🤖 Патрік шліфує код..."):
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.warning("Код порожній, бро. Закинь хоч щось!")
