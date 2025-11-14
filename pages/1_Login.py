import streamlit as st
import re

# إعداد الصفحة
st.set_page_config(page_title="Login", layout="centered")
st.markdown("""
<style>

.error-box {
    background-color: #ffe5e5;
    padding: 15px;
    border-left: 6px solid #d9534f;
    border-radius: 6px;
    margin-bottom: 12px;
}

.error-title {
    font-size: 18px;
    font-weight: bold;
    color: #b52b27;
    margin-bottom: 8px;
}

.error-list {
    font-size: 15px;
    color: #333;
    line-height: 1.6;
}


.warning-box {
    background-color: #fff4e5;
    padding: 15px;
    border-left: 6px solid #f0ad4e;
    border-radius: 6px;
    margin-bottom: 12px;
}

.warning-title {
    font-size: 18px;
    font-weight: bold;
    color: #d48806;
    margin-bottom: 8px;
}

.warning-list {
    font-size: 15px;
    color: #333;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
#     SESSION STATE
# -----------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# إذا مسجل دخول → تحويل للتنبؤ
if st.session_state.logged_in:
    st.switch_page("app.py")


# -----------------------------------
#     CSS بسيط للتجميل
# -----------------------------------
st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

/* عنوان الصفحة */
.login-title {
    text-align:center;
    font-size: 30px;
    font-weight: bold;
    color: #2b4c7e;
    margin-bottom: 25px;
}

/* مربعات الإدخال */
.stTextInput > div > div > input {
    border: 1.6px solid #c9d6e8 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* زر الدخول */
.stButton > button {
    width: 100%;
    background-color: #2b4c7e !important;
    color: white !important;
    padding: 10px;
    border-radius: 10px;
    font-size: 17px;
    border: none !important;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
#    دالة التحقق من اسم المستخدم
# -----------------------------------
def is_valid_username(u):
    return re.match(r'^[A-Za-z0-9_]+$', u)


# -----------------------------------
#     واجهة تسجيل الدخول
# -----------------------------------
st.markdown("<div class='login-title'>🔐 Login Page</div>", unsafe_allow_html=True)

# اسم المستخدم
username = st.text_input(
    "Username (English only)",
    placeholder="Enter username..."
)

# كلمة المرور (بدون عين)
password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter password..."
)


#        زر تسجيل الدخول

if st.button("Login"):

    username_errors = []
    password_errors = []

    # ======== شروط اسم المستخدم ==========
    if username.strip() == "":
        username_errors.append("• The username cannot be empty")
    if not re.match(r'^[A-Za-z0-9_]+$', username):
        username_errors.append("• English letters only")
        username_errors.append("• Numbers allowed")
        username_errors.append("• No Arabic characters")
        username_errors.append("• No spaces")
        username_errors.append("• No symbols (!@#$%^&*)")

    # ======== شروط كلمة المرور ==========
    if password.strip() == "":
        password_errors.append("• The password cannot be empty")
    if len(password) < 8:
        password_errors.append("• Minimum 8 characters")
    if not re.search(r'[A-Za-z]', password):
        password_errors.append("• Must contain at least one letter")
    if not re.search(r'[0-9]', password):
        password_errors.append("• Must contain at least one number")
    if ' ' in password:
        password_errors.append("• No spaces allowed")
    if re.search(r'[\u0600-\u06FF]', password):
        password_errors.append("• No Arabic characters allowed")

    # ======== عرض أخطاء اسم المستخدم (صندوق أحمر) ========
    if username_errors:
        st.markdown(
            f"""
            <div class="error-box">
                <div class="error-title">❌ Invalid Username</div>
                <div class="error-list">
                    Your username must meet the following rules:<br>
                    {'<br>'.join(username_errors)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ======== عرض أخطاء كلمة المرور (صندوق أصفر) ========
    if password_errors:
        st.markdown(
            f"""
            <div class="warning-box">
                <div class="warning-title">⚠️ Invalid Password</div>
                <div class="warning-list">
                    Your password must meet the following rules:<br>
                    {'<br>'.join(password_errors)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ======== نجاح تسجيل الدخول ========
    if not username_errors and not password_errors:
        st.success(f"🎉 Welcome, {username}!")
        st.session_state.logged_in = True
        st.switch_page("app.py")




