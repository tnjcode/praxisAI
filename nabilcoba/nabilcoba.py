import cv2
import sqlite3
import pathlib
import os
import tkinter as tk
from datetime import datetime, date
from PIL import Image, ImageTk
import numpy as np
import face_recognition

# Paths
current_dir = pathlib.Path(__file__).parent
img_dir = current_dir.joinpath('img')
db_path = current_dir.joinpath('faces.db')

# Create directories if not exist
if not img_dir.exists():
    os.makedirs(img_dir)

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table for storing face data
cursor.execute('''
CREATE TABLE IF NOT EXISTS faces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    image_path TEXT,
    encoding BLOB,
    log TEXT
)
''')
conn.commit()

def recognize_face(face_encoding):
    cursor.execute("SELECT * FROM faces")
    rows = cursor.fetchall()
    for row in rows:
        known_encoding = np.frombuffer(row[4], dtype=np.float64)
        matches = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.6)
        if True in matches:
            return row
    return None

def save_identity(name, face, role, face_encoding):
    timestamp = datetime.now().timestamp()
    img_path = img_dir.joinpath(f'{int(timestamp)}.jpg')
    cv2.imwrite(str(img_path), face)  # Convert img_path to string

    encoding_blob = face_encoding.tobytes()
    cursor.execute('''
    INSERT INTO faces (name, role, image_path, encoding, log) VALUES (?, ?, ?, ?, ?)
    ''', (name, role, str(img_path), encoding_blob, '[]'))
    conn.commit()

def register_new_face(frame, face, face_encoding):
    root = tk.Tk()
    root.title("Daftarkan Wajah")

    tk.Label(root, text='Masukkan nama:').pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text='Masukkan role:').pack()
    role_entry = tk.Entry(root)
    role_entry.pack()

    # Show the face to be saved
    face_img = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
    face_img = ImageTk.PhotoImage(image=face_img)
    tk.Label(root, image=face_img).pack()

    def save():
        name = name_entry.get()
        role = role_entry.get()
        save_identity(name, face, role, face_encoding)
        root.destroy()

    tk.Button(root, text='Simpan', command=save).pack()
    root.mainloop()

def log_attendance(entry_id):
    today = date.today().isoformat()
    now = datetime.now().isoformat()
    
    cursor.execute("SELECT log FROM faces WHERE id = ?", (entry_id,))
    log = eval(cursor.fetchone()[0])  # Convert string representation of list back to list

    if len(log) == 0 or log[-1]['date'] != today:
        log.append({
            'date': today,
            'attendance_time': now,
            'go_home_time': None
        })
    else:
        log[-1]['go_home_time'] = now

    cursor.execute("UPDATE faces SET log = ? WHERE id = ?", (str(log), entry_id))
    conn.commit()

cap = cv2.VideoCapture(0)

detected_faces = set()
running = True
while running:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        face_img = frame[top:bottom, left:right]
        
        # Generate a unique key for the detected face based on its position
        face_key = (left, top, right, bottom)
        
        if face_key not in detected_faces:
            entry = recognize_face(face_encoding)
            detected_faces.add(face_key)

            if entry:
                log_attendance(entry[0])  # Use entry ID to log attendance
                name_and_role = f"{entry[1]} ({entry[2]})"
                cv2.putText(frame, name_and_role, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
            else:
                register_new_face(frame, face_img, face_encoding)

            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

    cv2.putText(frame, 'Tekan [q] untuk keluar', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
 