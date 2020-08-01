import tkinter as tk
import youtube_dl

window = tk.Tk()
window.title("유튜브 다운로드")
window.geometry("500x300")

label1 = tk.Label(window, text="다운로드 URL 입력")
label1.pack()
entry1 = tk.Entry(window, width=50)
entry1.pack()

def my_hook(d):
    global textarea
    # if d['status'] == 'downloading':
    #     textarea.delete('1.0', tk.END)
    #     textarea.insert(tk.INSERT, d['filename']+":"+d['status']+ "("+d["_percent_str"]+")")
    if d['status'] == 'finished':
        textarea.insert(tk.INSERT, d['filename'] + '\n다운로드 완료\n\n')

def download(url):
    ydl_opts = {
    'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
    'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as y:
        y.download([url])

btn1 = tk.Button(window, text="다운로드", command=lambda: download(entry1.get()))
btn1.pack()
textarea = tk.Text(window)
textarea.pack()

window.mainloop()