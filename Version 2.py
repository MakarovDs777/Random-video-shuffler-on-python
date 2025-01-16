from moviepy.editor import VideoFileClip, concatenate_videoclips, concatenate_audioclips
import tkinter as tk
from tkinter import filedialog
import os
import random

def split_video_and_audio(video_path, duration=1):
    video_clip = VideoFileClip(video_path)
    audio = video_clip.audio
    
    # Разделение видео на 1-секундные фрагменты
    video_clips = []
    audio_clips = []

    for start in range(0, int(video_clip.duration), duration):
        end = min(start + duration, video_clip.duration)
        video_clips.append(video_clip.subclip(start, end))
        audio_clips.append(audio.subclip(start, end))

    return video_clips, audio_clips

def shuffle_video_and_audio(video_path, output_video_path):
    video_clips, audio_clips = split_video_and_audio(video_path)
    
    # Случайное перемешивание видеофрагментов и аудиофрагментов
    random.shuffle(video_clips)
    random.shuffle(audio_clips)

    # Объединение перемешанных видеоклипов в один
    final_video = concatenate_videoclips(video_clips)
    final_audio = concatenate_audioclips(audio_clips)

    # Объединение перемешанных видеоклипов с аудиотреком
    final_video = final_video.set_audio(final_audio)

    # Сохранение итогового видео
    final_video.write_videofile(output_video_path)
    print(f"Создано новое видео: {output_video_path}")

def select_video():
    file_path = filedialog.askopenfilename(title="Выберите видео файл")
    if file_path:
        output_path = os.path.join(os.path.expanduser("~"), "Desktop", "shuffled_video.mp4")
        shuffle_video_and_audio(file_path, output_path)

# Создание графического интерфейса
root = tk.Tk()
root.title("Перемешиватель видео и аудио")
root.geometry("320x120")  # Установка размера окна

select_video_button = tk.Button(root, text="Выбрать видео", command=select_video)
select_video_button.pack(pady=10)

# Запустить основной цикл интерфейса
root.mainloop()
