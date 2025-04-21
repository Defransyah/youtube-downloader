import os
import subprocess

def download_mp3_high_quality(url, output_path='Downloads'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    print("🔽 Sedang mengunduh dengan kualitas tinggi...")

    command = [
        'yt-dlp',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '0',  # 0 = best
        '-o', f'{output_path}/%(title)s.%(ext)s',
        url
    ]

    try:
        subprocess.run(command, check=True)
        print("✅ Selesai! Lagu berhasil diunduh dalam kualitas tinggi.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error saat download: {e}")

# Jalankan
link = input("Masukkan URL YouTube:  ")
download_mp3_high_quality(link)
