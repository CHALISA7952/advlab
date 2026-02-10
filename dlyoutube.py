import yt_dlp

# รับลิงก์ YouTube จากผู้ใช้
url = input("กรุณาใส่ลิงก์ YouTube: ")

# ตั้งค่าการดาวน์โหลด
ydl_opts = {
    'format': 'best',                # ดาวน์โหลดวิดีโอคุณภาพดีที่สุด
    'outtmpl': '%(title)s.%(ext)s'   # ตั้งชื่อไฟล์ตามชื่อวิดีโอ
}

# ดาวน์โหลดวิดีโอ
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("ดาวน์โหลดวิดีโอเรียบร้อยแล้ว")
