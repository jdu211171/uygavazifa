class Notebook:

    def __init__(self, firma: str, model: str, cpu: str, ddr: str, price: float):
        self.firma = firma
        self.model = model
        self.cpu = cpu
        self.ddr = ddr
        self.price = price

    def info_notebook(self):
        print(f'firma: {self.firma}\n'
              f'model: {self.model}\n'
              f'cpu: {self.cpu}\n'
              f'ddr: {self.ddr}\n'
              f'price: {self.price}\n')


notebook1 = Notebook('Dell', 'XPS 13', 'Intel i7', '16GB', 1200.00)
notebook2 = Notebook('HP', 'Spectre x360', 'Intel i5', '8GB', 1000.00)
notebook3 = Notebook('Apple', 'MacBook Pro', 'M1', '16GB', 1500.00)
notebook4 = Notebook('Lenovo', 'ThinkPad X1', 'Intel i7', '16GB', 1300.00)
notebook5 = Notebook('Asus', 'ZenBook 14', 'AMD Ryzen 7', '16GB', 1100.00)

notebooklar = [notebook2, notebook1, notebook3, notebook5, notebook4]
for notebook in notebooklar:
    notebook.info_notebook()
