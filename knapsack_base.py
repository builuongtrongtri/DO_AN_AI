import time
import csv
from typing import List, Tuple, Dict, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Item:
    """Đại diện một món: tên, giá trị và trọng lượng."""
    name: str
    value: int
    weight: int


class KnapsackAlgorithmBase(ABC):
    """
    Lớp cơ sở cho các thuật toán Knapsack 0/1, viết lại theo cấu trúc rõ ràng hơn.

    Tính năng bổ sung:
    - `Item` dataclass cho từng phần tử.
    - Validation input khi khởi tạo.
    - Helper methods: `selected_items`, `solution_summary`, `validate_solution`.
    - Thu gọn `history` thành list các dict (thuận tiện cho logging/plot).
    """

    def __init__(
        self,
        item_names: List[str],
        item_values: List[int],
        item_weights: List[int],
        knapsack_capacity: int,
        max_iterations: int = 100,
    ):
        """Khởi tạo và validate input.

        Ghi chú: các danh sách phải cùng chiều dài; giá trị/trọng lượng nên là số không âm.
        """
        self._validate_inputs(item_names, item_values, item_weights, knapsack_capacity)

        self._items: List[Item] = [
            Item(n, int(v), int(w)) for n, v, w in zip(item_names, item_values, item_weights)
        ]
        self._capacity = int(knapsack_capacity)
        self._max_iterations = int(max_iterations)
        self._n = len(self._items)

        # History: list of dicts e.g. {"iter": i, "solution": [...], "value": v}
        self.history: List[Dict[str, Any]] = []

        # Best-known solution state
        self.best_solution: List[int] = [0] * self._n
        # best_value is the (feasible) total value for best_solution
        self.best_value: int = 0
        self.exec_time: float = 0.0

    def _validate_inputs(
        self,
        names: List[str],
        values: List[int],
        weights: List[int],
        capacity: int,
    ) -> None:
        if not (len(names) == len(values) == len(weights)):
            raise ValueError("item_names, item_values and item_weights must have the same length")
        if capacity < 0:
            raise ValueError("knapsack_capacity must be non-negative")
        # optional: ensure all values/weights are ints
        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError("item_values must be numeric")
        for w in weights:
            if not isinstance(w, (int, float)):
                raise TypeError("item_weights must be numeric")

    def _calculate_fitness(self, sol: List[int]) -> Tuple[int, int]:
        """Tính (total_value, total_weight) cho một nghiệm (list 0/1).

        Nếu `sol` dài hơn `_n`, các giá trị dư sẽ bị bỏ qua; nếu ngắn hơn, coi phần thiếu là 0.
        """
        total_value = 0
        total_weight = 0
        for i in range(self._n):
            bit = int(sol[i]) if i < len(sol) else 0
            if bit:
                item = self._items[i]
                total_value += item.value
                total_weight += item.weight
        return total_value, total_weight

    def _fitness_value(self, sol: List[int]) -> int:
        """Trả về tổng giá trị nếu nghiệm hợp lệ, ngược lại trả 0.

        Lưu ý: trả về 0 cho nghiệm không hợp lệ là một chiến lược đánh giá;
        một thiết kế khác có thể trả -inf hoặc dùng penalty.
        """
        total_value, total_weight = self._calculate_fitness(sol)
        return total_value if total_weight <= self._capacity else 0

    def validate_solution(self, sol: List[int]) -> bool:
        """Kiểm tra xem `sol` có hợp lệ về mặt dạng (chứa 0/1) và trọng lượng không vượt quá capacity."""
        if not all(int(x) in (0, 1) for x in sol):
            return False
        _, total_weight = self._calculate_fitness(sol)
        return total_weight <= self._capacity

    def selected_items(self, sol: List[int]) -> List[Item]:
        """Trả về danh sách `Item` được chọn bởi `sol`."""
        return [self._items[i] for i in range(self._n) if i < len(sol) and int(sol[i])]

    def solution_summary(self, sol: List[int]) -> Dict[str, Any]:
        """Tổng hợp thông tin tóm tắt: tên mục được chọn, tổng giá trị, tổng trọng lượng."""
        total_value, total_weight = self._calculate_fitness(sol)
        names = [it.name for it in self.selected_items(sol)]
        return {"selected": names, "value": total_value, "weight": total_weight}

    @abstractmethod
    def solve(self) -> Tuple[List[int], int, float]:
        """Phương thức trừu tượng: chạy thuật toán và trả về (best_solution, best_value, exec_time).

        Lớp con phải cập nhật `self.history` khi cần và có thể sử dụng helper methods trên.
        """
        raise NotImplementedError()
