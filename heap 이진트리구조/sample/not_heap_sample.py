class DataStructure: # not heap 
    def __init__(self):
        self.data = []

    def add_element(self, element):
        self.data.append(element)

    def get_min(self):
        if not self.data:
            return None
        return min(self.data)

    def get_max(self):
        if not self.data:
            return None
        return max(self.data)

# 예시 사용법
my_data_structure = DataStructure()

# 데이터 추가
my_data_structure.add_element(5)
my_data_structure.add_element(10)
my_data_structure.add_element(3)
my_data_structure.add_element(8)

# 최소값 및 최대값 확인
min_value = my_data_structure.get_min()
max_value = my_data_structure.get_max()

print(f"최소값: {min_value}")
print(f"최대값: {max_value}")