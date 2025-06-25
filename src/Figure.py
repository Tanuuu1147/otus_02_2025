from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError(
                f"Not a Figure, need to pass here Figure object "
                f"or child Figure, actual {type(other_figure)}"
            )
        return self.area + other_figure.area
