import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os
import random

def shuffle_video_frames(video_path, output_video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    # Извлечение всех кадров из видео
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()

    # Перемешивание кадров
    random.shuffle(frames)

    # Запись перемешанных кадров в новое видео
    height, width, layers = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()
    print(f"Создано новое видео: {output_video_path}")

def select_video():
    file_path = filedialog.askopenfilename(title="Выберите видео файл")
    if file_path:
        output_path = os.path.join(os.path.expanduser("~"), "Desktop", "shuffled_video.mp4")
        shuffle_video_frames(file_path, output_path)

# Создание графического интерфейса
root = tk.Tk()
root.title("Перемешиватель видео")
root.geometry("320x120")  # Установка размера окна

select_video_button = tk.Button(root, text="Выбрать видео", command=select_video)
select_video_button.pack(pady=10)

# Запустить основной цикл интерфейса
root.mainloop()
