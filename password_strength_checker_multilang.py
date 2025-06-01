
import re

messages = {
    "ar": {
        "welcome": "🔐 مرحباً بك في أداة تقييم قوة كلمة المرور!",
        "enter_password": "👉 أدخل كلمة المرور لتقييمها: ",
        "short": "❌ كلمة المرور قصيرة جداً. يفضل 8 أحرف أو أكثر.",
        "no_lower": "❌ يجب أن تحتوي كلمة المرور على أحرف صغيرة (a-z).",
        "no_upper": "❌ يجب أن تحتوي كلمة المرور على أحرف كبيرة (A-Z).",
        "no_digit": "❌ يجب أن تحتوي كلمة المرور على أرقام (0-9).",
        "no_special": "❌ يفضل أن تحتوي كلمة المرور على رموز خاصة (!@#$...).",
        "result": "\n🔍 النتيجة:",
        "strong": "🔒 كلمة المرور قوية جداً! ممتاز.",
        "medium": "⚠️ كلمة المرور متوسطة. حاول تحسينها أكثر.",
        "weak": "❌ كلمة المرور ضعيفة. يرجى تحسينها."
    },
    "en": {
        "welcome": "🔐 Welcome to the Password Strength Checker!",
        "enter_password": "👉 Enter the password to evaluate: ",
        "short": "❌ The password is too short. It should be at least 8 characters.",
        "no_lower": "❌ The password should contain lowercase letters (a-z).",
        "no_upper": "❌ The password should contain uppercase letters (A-Z).",
        "no_digit": "❌ The password should contain digits (0-9).",
        "no_special": "❌ The password should contain special characters (!@#$...).",
        "result": "\n🔍 Result:",
        "strong": "🔒 The password is very strong! Excellent.",
        "medium": "⚠️ The password is medium strength. Try to improve it.",
        "weak": "❌ The password is weak. Please make it stronger."
    }
}

def check_password_strength(password, lang="ar"):
   
    
    
    msg = messages[lang]
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        print(msg["short"])

    if re.search(r"[a-z]", password):
        score += 1
    else:
        print(msg["no_lower"])

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print(msg["no_upper"])

    if re.search(r"[0-9]", password):
        score += 1
    else:
        print(msg["no_digit"])

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print(msg["no_special"])

    print(msg["result"])
    if score == 5:
        print(msg["strong"])
    elif 3 <= score < 5:
        print(msg["medium"])
    else:
        print(msg["weak"])

def main():
    """
    """
    # تحديد اللغة
    lang_choice = input("🌐 اختر اللغة (ar/en): ").strip().lower()
    if lang_choice not in ["ar", "en"]:
        lang_choice = "ar"  # الافتراضية: عربي

    print(messages[lang_choice]["welcome"])
    password = input(messages[lang_choice]["enter_password"])
    check_password_strength(password, lang=lang_choice)

if __name__ == "__main__":
    main()
