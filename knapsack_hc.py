import time
import random
from typing import List, Tuple, Dict
from knapsack_base import KnapsackAlgorithmBase  

class KnapsackHillClimbing(KnapsackAlgorithmBase):
    """
    Giải bài toán Knapsack (0/1) sử dụng thuật toán Hill Climbing (Leo đồi).

    Thuật toán này cài đặt phiên bản "Steepest Ascent" (Leo đồi dốc nhất).
    Nó bắt đầu với một nghiệm ban đầu và lặp đi lặp lại việc di chuyển đến
    hàng xóm tốt nhất, cho đến khi đạt đến đỉnh cục bộ.
    """

    def __init__(self, *args, **kwargs):
        """Khởi tạo, gọi Class cơ sở."""
        super().__init__(*args, **kwargs)

    def _generate_initial_solution(self) -> List[int]:
        """
        Tạo nghiệm ban đầu. 
        Cách đơn giản nhất là bắt đầu với một cái túi rỗng (toàn số 0).
        Đây là một nghiệm hợp lệ và thuật toán sẽ "leo" từ đây.
        """
        return [0] * self._n

    def _get_neighbors(self, sol: List[int]) -> List[List[int]]:
        """
        Tạo ra tất cả các "hàng xóm" của nghiệm hiện tại.
        Một hàng xóm được định nghĩa là nghiệm có 1 bit bị lật (0->1 hoặc 1->0).
        """
        neighbors = []
        for i in range(self._n):
            neighbor = sol.copy()
            neighbor[i] = 1 - neighbor[i]  
            neighbors.append(neighbor)
        return neighbors

    def solve(self) -> Tuple[List[str], List[str], float]:
        """
        Chạy thuật toán Hill Climbing (Steepest Ascent).

        Trả về:
            Tuple[List[str], List[str], float]: 
            (Tên các vật phẩm được chọn, Tên các vật phẩm không được chọn, Tổng giá trị tốt nhất)
        """
        start_time = time.time()

        current_solution = self._generate_initial_solution()
        current_value = self._fitness_value(current_solution)

        self.best_solution = current_solution.copy()
        self.best_value = current_value
        self.history.append((0, self.best_value))

        
        for i in range(1, self._max_iterations + 1):
            neighbors = self._get_neighbors(current_solution)
            best_neighbor = None
            best_neighbor_value = -1  

            for neighbor in neighbors:
                neighbor_value = self._fitness_value(neighbor)
                if neighbor_value > best_neighbor_value:
                    best_neighbor_value = neighbor_value
                    best_neighbor = neighbor

            
            if best_neighbor is None or best_neighbor_value <= current_value:
                
                if self.history[-1][0] != i - 1:
                     self.history.append((i - 1, self.best_value))
                break
            
            current_solution = best_neighbor
            current_value = best_neighbor_value

            
            self.best_solution = current_solution.copy()
            self.best_value = current_value
            
            self.history.append((i, self.best_value))

        self.exec_time = time.time() - start_time

        
        selected_items = [self._item_names[i] for i in range(self._n) if self.best_solution[i] == 1]
        unselected_items = [self._item_names[i] for i in range(self._n) if self.best_solution[i] == 0]

        return selected_items, unselected_items, self.best_value