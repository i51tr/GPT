import tkinter as tk
from PIL import ImageTk, Image
import openai

#  API 
openai.api_key = "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"

# إنشاء نافذة الواجهة الرسومية
window = tk.Tk()
window.title("ChatGPT Bigboss Meto ")

# إضافة شعار 
logo_image = Image.open("chatgpt_logo.png")
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(window, image=logo_photo)
logo_label.pack(pady=10)

# إنشاء مربع النص لإدخال السؤال
question_entry = tk.Entry(window, width=50)
question_entry.pack(pady=10)

# إنشاء منطقة النص المتدفقة لعرض الاستجابة
response_text = tk.Text(window, width=80, height=10)
response_text.pack(pady=10)

# دالة للحصول على الاستجابة عند النقر على زر "Get Response"
def get_response():
    question = question_entry.get()
    if 'exit' in question or 'quit' in question:
        window.quit()
    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        response_text.insert(tk.END, response.choices[0].text)

# إنشاء زر "Get Response" للحصول على الاستجابة
response_button = tk.Button(window, text="Get Response", command=get_response)
response_button.pack(pady=10)

# دالة لحذف النصص
def clear_text():
    question_entry.delete(0, tk.END)

# إنشاء زر "Clear Text" لحذف النص
clear_button = tk.Button(window, text="Clear question", command=clear_text)
clear_button.pack(pady=10)

# تشغيل الواجهة 
window.mainloop()