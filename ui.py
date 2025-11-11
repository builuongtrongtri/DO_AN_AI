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
 
        self.max_w_entry = ttk.Entry(self.root)
        self.iter_entry = ttk.Entry(self.root)
        self.run_button = ttk.Button(self.root, text="Chạy (Chưa gán lệnh)") 
        
        self.data_combobox = ttk.Combobox(self.root, values=self.data_files)
        self.tree = ttk.Treeview(self.root)
        
        self.hc_result = Text(self.root, height=8)
        self.hc_history = Text(self.root)
        self.gwo_result = Text(self.root, height=8)
        self.gwo_history = Text(self.root)
       
        try:
            self.load_data_and_populate_tree(self.data_files[0])
        except Exception as e:
            pass 
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
