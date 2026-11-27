[English](README.md) | **العربية**

# ReMindly Agent

بيحوّل الشرح الخام وملاحظات المحاضرات والنصوص التقنية لملفات Markdown منظمة ونضيفة، من خلال خط معالجة بالذكاء الاصطناعي: توليد، تحقق، مراجعة، وإعادة محاولة لو لزم.

باك إند FastAPI، واجهة HTML/JS بسيطة بعرض لحظي، وبيشتغل مع أي موديل متوافق مع OpenAI.

## بيعمل إيه

- ينظّم النص العشوائي في عناوين وقوائم وجداول وكتل كود من غير ما يغيّر المعنى.
- يبث التقدم والناتج لحظيا عن طريق Server-Sent Events.
- يكتشف لغة المدخل (عربي أو إنجليزي أو مختلط) ويتأكد إن الناتج بنفس اللغة المطلوبة.
- يقسّم النصوص الطويلة لأجزاء ويعالجها بالتوازي.
- يتحقق من الـ Markdown الناتج، وبعدها مراجعة جودة منفصلة بالذكاء الاصطناعي، ومحاولة إعادة واحدة لو احتاج.
- أوضاع ومستويات تفصيل: short وmedium وdetailed وpreserve، مع تعليمات مخصصة اختيارية.
- معاينة ونسخ وتحميل كملف `.md`.

```text
نص خام -> تقسيم -> توليد -> تحقق -> مراجعة جودة -> Markdown
```

## تشغيل سريع

محتاج Python 3.12.

```bash
git clone https://github.com/Ibrahim-Al-Jid/ReMindly-Agent.git
cd ReMindly-Agent
python -m venv .venv
source .venv/bin/activate        # على ويندوز: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # ضع MODEL_API_KEY
uvicorn app.main:app --reload
```

افتح http://127.0.0.1:8000.

## الإعدادات

| المتغير | الافتراضي | الغرض |
|---|---|---|
| `MODEL_API_KEY` | لا يوجد | مفتاح مزود الذكاء الاصطناعي (مطلوب للتوليد) |
| `MODEL_BASE_URL` | `https://openrouter.ai/api/v1` | عنوان API المتوافق مع OpenAI |
| `MODEL_NAME` | `nvidia/nemotron-3-super-120b-a12b:free` | الموديل المستخدم |
| `APP_API_KEY` | فاضي | حماية اختيارية للـ API عبر الهيدر `X-API-Key` |
| `ORGANIZE_RATE_LIMIT` / `STREAM_RATE_LIMIT` | `10/minute` / `5/minute` | حدود الطلبات |

المفاتيح بتفضل على السيرفر فقط. ما ترفعش ملف `.env` أبدا. الجدول الكامل في [docs/guide.md](docs/guide.md) (بالإنجليزي).

## الـ API

| الطريقة | المسار | الوصف |
|---|---|---|
| GET | `/api/health` | حالة الخدمة |
| POST | `/api/organize` | تنظيم النص، رد JSON |
| POST | `/api/organize/stream` | نفس الشيء بالبث (`progress` و`token` و`replace` و`completed` و`error`) |

## الاختبارات

```bash
pytest          # 34 اختبار، من غير مفتاح ولا استدعاء موديل حقيقي
black --check app tests
ruff check app tests
mypy app
```

كلهم بينجحوا، وCI بيشغّلهم مع كل push.

## Docker وVercel

```bash
docker build -t remindly-agent .
docker run -p 8000:8000 --env-file .env remindly-agent
```

إعداد Vercel موجود في `vercel.json` و`index.py`.

## الهيكل

```text
app/        تطبيق FastAPI: api وcore وservices وmodels
static/     الواجهة
tests/      اختبارات pytest
docs/       الدليل الموسّع
```
