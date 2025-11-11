# File: ui.py (Do Dev 1 tạo ban đầu)

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Text
from knapsack_hc import HillClimbing
from knapsack_gwo import GreyWolfOptimizer
from data_handler import load_knapsack_data_from_csv

import threading
from typing import List, Tuple

class KnapsackApp:
    """Class chính quản lý giao diện người dùng và điều phối các thuật toán tối ưu."""
    def __init__(self, root):
        """Khởi tạo ứng dụng Knapsack."""
        self.root = root
        self.root.title("Knapsack Optimization - Hill Climbing & GWO Song Song")
        self.root.geometry("1400x800")

        self.data_files = [
            'dataset_500.csv',
            'dataset_1000.csv',
            'products.csv'
        ]

        self.items_data = {'names': [], 'values': [], 'weights': []}
        self.items: List[Tuple[str, int, int]] = []

        self.create_widgets()

    def create_widgets(self):
        """Thiết lập tất cả các thành phần giao diện."""
        # ========== FRAME TRÊN (Điều khiển) ==========
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(top_frame, text="Khối lượng tối đa:").pack(side="left", padx=5)
        self.max_w_entry = ttk.Entry(top_frame, width=8)
        self.max_w_entry.pack(side="left", padx=5)
        self.max_w_entry.insert(0, "5000")

        ttk.Label(top_frame, text="Số lần lặp:").pack(side="left", padx=5)
        self.iter_entry = ttk.Entry(top_frame, width=8)
        self.iter_entry.insert(0, "100")
        self.iter_entry.pack(side="left", padx=5)

        # CÁC NÚT BẤM CHƯA GÁN LỆNH (command=None)
        self.run_button = ttk.Button(top_frame, text="Chạy Song Song", command=None)
        self.run_button.pack(side="left", padx=10)

        ttk.Label(top_frame, text="Chọn Dataset:").pack(side="left", padx=(10, 5))
        self.data_combobox = ttk.Combobox(
            top_frame,
            values=self.data_files,
            state="readonly",
            width=22
        )
        self.data_combobox.set(self.data_files[0])
        self.data_combobox.pack(side="left", padx=5)

        ttk.Button(top_frame, text="Tải Dữ Liệu", command=None).pack(side="left", padx=5)
        ttk.Button(top_frame, text="Xóa kết quả", command=None).pack(side="left", padx=10)

        # ========== TABLE (Dữ liệu vật phẩm) ==========
        columns = ("Tên", "Giá trị", "Khối lượng")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
        self.tree.pack(fill="x", padx=10, pady=5)

        # ========== FRAME DƯỚI (Kết quả & Lịch sử) ==========
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(fill="both", expand=True, padx=10, pady=5)

        hc_frame = ttk.Frame(bottom_frame)
        hc_frame.pack(side="left", fill="both", expand=True, padx=5)
        ttk.Label(hc_frame, text="HILL CLIMBING", font=("Arial", 12, "bold")).pack(pady=5)
        self.hc_result = Text(hc_frame, height=8, bg="white", fg="black", font=("Consolas", 10))
        self.hc_result.pack(fill="x", pady=5)
        ttk.Label(hc_frame, text="LỊCH SỬ HC", font=("Arial", 10, "bold")).pack(pady=5)
        self.hc_history = Text(hc_frame, bg="white", fg="black", font=("Consolas", 10))
        self.hc_history.pack(fill="both", expand=True, pady=5)

        gwo_frame = ttk.Frame(bottom_frame)
        gwo_frame.pack(side="left", fill="both", expand=True, padx=5)
        ttk.Label(gwo_frame, text="GREY WOLF OPTIMIZER", font=("Arial", 12, "bold")).pack(pady=5)
        self.gwo_result = Text(gwo_frame, height=8, bg="white", fg="black", font=("Consolas", 10))
        self.gwo_result.pack(fill="x", pady=5)
        ttk.Label(gwo_frame, text="LỊCH SỬ GWO", font=("Arial", 10, "bold")).pack(pady=5)
        self.gwo_history = Text(gwo_frame, bg="white", fg="black", font=("Consolas", 10))
        self.gwo_history.pack(fill="both", expand=True, pady=5)

        try:
            self.load_data_and_populate_tree(self.data_files[0])
        except Exception as e:
            messagebox.showerror("Lỗi Tải Dữ Liệu Mặc Định", f"Không thể tải '{self.data_files[0]}'.\n{e}")
            
    def load_selected_data(self):
        pass 
    def load_data_and_populate_tree(self, filename: str):
        pass 
    def clear_results(self):
        pass 

    def _run_single_algo(self, method_name, algo_class, result_text, history_text, names, values, weights, max_w, max_iter):
        pass 

    def _update_gui(self, method_name, selected, hist, t, total_val, total_w, max_w, names, values, weights, result_text, history_text):
        pass 
    def _check_running_threads(self):
        pass 
    def start_parallel_run(self):
        pass 