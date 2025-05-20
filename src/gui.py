import tkinter as tk
from ttkbootstrap import Style, ttk
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO
from src.queries import *
import os
import threading

class RSTreeApp:
    def __init__(self, root, rs_tree):
        self.root = root
        self.rs_tree = rs_tree
        self.root.title("RS-Tree Video Analysis")
        self.style = Style(theme="flatly")  
        self.model = YOLO("yolov8n.pt") 
        self.video_path = "data/datatest.mp4"
        self.cap = cv2.VideoCapture(self.video_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0
        self.playing = False

        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        self.video_canvas = tk.Canvas(self.main_frame, width=640, height=360, bg="black")
        self.video_canvas.pack(side="left", padx=10, pady=10)

        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(side="right", fill="y", padx=10)

        ttk.Label(self.control_frame, text="RS-Tree Video Analysis", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttk.Label(self.control_frame, text="Chọn truy vấn").pack(anchor="w")
        self.query_var = tk.StringVar()
        queries = [
            "Find Video with Object",
            "Find Video with Activity",
            "Find Video with Activity and Prop",
            "Find Video with Object and Prop",
            "Find Objects in Video",
            "Find Activities in Video",
            "Find Activities and Props in Video",
            "Find Objects and Props in Video"
        ]
        self.query_menu = ttk.Combobox(self.control_frame, textvariable=self.query_var, values=queries, state="readonly")
        self.query_menu.pack(fill="x", pady=5)
        self.query_menu.set(queries[0])

        ttk.Label(self.control_frame, text="Object Name").pack(anchor="w")
        self.object_var = tk.StringVar()
        objects = ["car", "person", "bicycle"]
        self.object_menu = ttk.Combobox(self.control_frame, textvariable=self.object_var, values=objects, state="readonly")
        self.object_menu.pack(fill="x", pady=5)
        self.object_menu.set(objects[0])

        ttk.Label(self.control_frame, text="Activity Name").pack(anchor="w")
        self.activity_var = tk.StringVar()
        activities = ["moving", "walking", "running"]
        self.activity_menu = ttk.Combobox(self.control_frame, textvariable=self.activity_var, values=activities, state="readonly")
        self.activity_menu.pack(fill="x", pady=5)
        self.activity_menu.set(activities[0])

        ttk.Label(self.control_frame, text="Property").pack(anchor="w")
        self.prop_var = tk.StringVar()
        props = ["red", "blue", "black"]
        self.prop_menu = ttk.Combobox(self.control_frame, textvariable=self.prop_var, values=props, state="readonly")
        self.prop_menu.pack(fill="x", pady=5)
        self.prop_menu.set(props[0])

        ttk.Label(self.control_frame, text="Frame Range").pack(anchor="w")
        self.frame_range = ttk.Frame(self.control_frame)
        self.frame_range.pack(fill="x", pady=5)
        self.start_frame = tk.IntVar(value=0)
        self.end_frame = tk.IntVar(value=100)
        ttk.Label(self.frame_range, text="Start:").pack(side="left")
        ttk.Entry(self.frame_range, textvariable=self.start_frame, width=10).pack(side="left", padx=5)
        ttk.Label(self.frame_range, text="End:").pack(side="left")
        ttk.Entry(self.frame_range, textvariable=self.end_frame, width=10).pack(side="left", padx=5)

        ttk.Button(self.control_frame, text="Run Query", command=self.run_query, style="primary.TButton").pack(fill="x", pady=10)

        self.video_controls = ttk.Frame(self.control_frame)
        self.video_controls.pack(fill="x", pady=10)
        ttk.Button(self.video_controls, text="Play Video", command=self.play_video, style="success.TButton").pack(side="left", padx=5)
        ttk.Button(self.video_controls, text="Pause", command=self.pause_video, style="warning.TButton").pack(side="left", padx=5)
        ttk.Button(self.video_controls, text="Restart", command=self.restart_video, style="info.TButton").pack(side="left", padx=5)

        self.time_slider = ttk.Scale(self.control_frame, from_=0, to=self.frame_count-1, orient="horizontal", command=self.seek_video)
        self.time_slider.pack(fill="x", pady=5)

        self.result_text = tk.Text(self.control_frame, height=10, width=40, wrap="word")
        self.result_text.pack(fill="both", expand=True, pady=10)

        self.update_video()

    def run_query(self):
        query = self.query_var.get()
        self.result_text.delete(1.0, tk.END)
        try:
            if query == "Find Video with Object":
                result = find_video_with_object(self.object_var.get(), self.rs_tree)
                self.result_text.insert(tk.END, f"Videos with object '{self.object_var.get()}': {result}\n")
            elif query == "Find Video with Activity":
                result = find_video_with_activity(self.activity_var.get(), self.rs_tree)
                self.result_text.insert(tk.END, f"Videos with activity '{self.activity_var.get()}': {result}\n")
            elif query == "Find Video with Activity and Prop":
                result = find_video_with_activity_and_prop(self.activity_var.get(), self.prop_var.get(), 0.0, self.rs_tree)
                self.result_text.insert(tk.END, f"Videos with activity '{self.activity_var.get()}' and prop '{self.prop_var.get()}': {result}\n")
            elif query == "Find Video with Object and Prop":
                result = find_video_with_object_and_prop(self.object_var.get(), self.prop_var.get(), 0.0, self.rs_tree)
                self.result_text.insert(tk.END, f"Videos with object '{self.object_var.get()}' and prop '{self.prop_var.get()}': {result}\n")
            elif query == "Find Objects in Video":
                result = find_objects_in_video("video1", self.start_frame.get(), self.end_frame.get(), self.rs_tree)
                self.result_text.insert(tk.END, f"Objects in video 'video1' from frame {self.start_frame.get()} to {self.end_frame.get()}: {result}\n")
            elif query == "Find Activities in Video":
                result = find_activities_in_video("video1", self.start_frame.get(), self.end_frame.get(), self.rs_tree)
                self.result_text.insert(tk.END, f"Activities in video 'video1' from frame {self.start_frame.get()} to {self.end_frame.get()}: {result}\n")
            elif query == "Find Activities and Props in Video":
                result = find_activities_and_props_in_video("video1", self.start_frame.get(), self.end_frame.get(), self.rs_tree)
                self.result_text.insert(tk.END, f"Activities and props in video 'video1' from frame {self.start_frame.get()} to {self.end_frame.get()}: {result}\n")
            elif query == "Find Objects and Props in Video":
                result = find_objects_and_props_in_video("video1", self.start_frame.get(), self.end_frame.get(), self.rs_tree)
                self.result_text.insert(tk.END, f"Objects and props in video 'video1' from frame {self.start_frame.get()} to {self.end_frame.get()}: {result}\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Lỗi: {e}\n")

    def update_video(self):
        if not self.playing:
            return
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
        ret, frame = self.cap.read()
        if ret:
            results = self.model(frame, verbose=False, conf=0.5)
            frame = results[0].plot() 
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 360))
            img = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(img)
            self.video_canvas.create_image(0, 0, anchor="nw", image=self.photo)
            self.current_frame += 1
            self.time_slider.set(self.current_frame)
            if self.current_frame < self.frame_count:
                self.root.after(int(1000/self.fps), self.update_video)
            else:
                self.playing = False
        else:
            self.playing = False

    def play_video(self):
        if not self.playing:
            self.playing = True
            self.update_video()

    def pause_video(self):
        self.playing = False

    def restart_video(self):
        self.current_frame = 0
        self.time_slider.set(0)
        self.play_video()

    def seek_video(self, value):
        self.current_frame = int(float(value))
        self.update_video()

    def __del__(self):
        self.cap.release()