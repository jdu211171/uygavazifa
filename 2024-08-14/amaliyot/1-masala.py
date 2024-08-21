class Technology:

    def __init__(self, brand: str, model: str, typeof: str):
        self.brand = brand
        self.model = model
        self.typeof = typeof

    def info(self):
        return (f'brand: {self.brand}\n'
                f'model: {self.model}\n'
                f'typeof:  {self.typeof}\n')


class Notebook(Technology):

    def __init__(self, video_card: str, ram: int, display: str):
        super().__init__(self.brand, self.model, self.typeof)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        return super().info() + (f'video_card: {self.video_card}\n'
                                 f'ram: {self.ram}\n'
                                 f'display: {self.display}\n')


class Television(Technology):

    def __init__(self, size: str, display: str):
        super().__init__(self.brand, self.model, self.typeof)
        self.size = size
        self.display = display

    def more_info(self):
        return super().info() + (f'size: {self.size}\n'
                                 f'display: {self.display}\n')


class Smartphone(Technology):

    def __init__(self, size: str, sim_count: int):
        super().__init__(self.brand, self.model, self.typeof)
        self.size = size
        self.sim_count = sim_count

    def more_info(self):
        return super().info() + (f'size: {self.size}\n'
                                 f'sim_count: {self.sim_count}\n')
