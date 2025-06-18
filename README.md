# Langchain + OpenAI Basit Mesaj Projesi

Bu proje, Python ve Langchain kullanarak OpenAI API'si üzerinden basit bir chatbot projesidir.

## 📂 Dosyalar

- `simplemessage.py` : Langchain + OpenAI ile bir mesaj gönderip yanıt alır.
- `openaimodels.py` : API'ye bağlı olarak erişilebilir OpenAI modellerini listeler.
- `.env` : OpenAI API anahtarınızı gizli tutmak için ortam değişkenlerini içerir.

## 🚀 Kurulum

1️⃣ Depoyu klonlayın:
```bash
git clone https://github.com/kendi-reponuz/langchain-openai-demo.git
cd langchain-openai-demo
```

2️⃣ Sanal ortam oluşturun ve aktive edin:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

3️⃣ Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

⚙️ .env içeriği
Proje kök dizininde bir .env dosyası oluşturun ve aşağıdaki içeriği ekleyin:
```bash
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=FirstProject
```
API anahtarınızı OpenAI platformundan alabilirsiniz.

⚠️ Uyarılar
API kullanım kotanıza dikkat edin. Ücretsiz kotalar hızlıca tükenebilir.
API anahtarınızı kimseyle paylaşmayın, .env dosyanızı gizli tutun.










