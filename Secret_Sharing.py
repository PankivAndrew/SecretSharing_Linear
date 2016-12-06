import random
import numpy
import time
import work_with_matrix
from Teacher import Teacher


class Secret:
    def __init__(self, secret):
        self.start_time = time.time()
        binary_string = self.convert_to_binary(secret)
        self.lst_of_vectors, self.lst_of_teachers, self.__lst_of_keys = self.encode(binary_string)
        exampl_teachers = [tea.get_code() for tea in self.lst_of_teachers[0]]
        print("Example vector", self.lst_of_vectors[0], "Example of teachers", exampl_teachers, "KEY",
              self.__lst_of_keys[0])

    def encode(self, lst_of_binaries):
        lst_of_vecotrs = []
        lst_of_keys = []
        lst_of_teachers = []
        for letter in lst_of_binaries:
            for byte_pair in range(0, len(letter) - 1, 2):
                pair = [int(letter[byte_pair]), int(letter[byte_pair + 1])]
                key, vectors = self.encode_and_get_key_and_vectors(pair)
                lst_of_vecotrs.append(vectors)
                lst_of_keys.append(key)
                lst_tmp = [Teacher(numpy.array(vectors[teacher_index][0]).dot(numpy.array(key)),
                                   numpy.array(vectors[teacher_index][1]).dot(numpy.array(key))) for teacher_index in
                           range(1, 5)]
                lst_of_teachers.append(lst_tmp)
        return lst_of_vecotrs, lst_of_teachers, lst_of_keys

    def encode_and_get_key_and_vectors(self,
                                       secret):  # Ще цю протестуй тут я підбираю вектор, який би дорівнював секретам.
        u = [1, 1, 1, 1, 1, 1]
        vectors = self.genetare_vect_a()
        while (numpy.array(vectors[0][0]).dot(numpy.array(u)) != secret[0]) or (numpy.array(
                vectors[0][1]).dot(numpy.array(u)) != secret[1]):
            u = [random.randint(0, 1) for _ in range(6)]
            elapsed_time = time.time() - self.start_time
            if elapsed_time > 1:
                import main
                print("Restarting", )
                main.main()
                quit()

        return u, vectors

    def convert_to_binary(self, string_input):
        lst_of_binaries = []
        for letter in string_input:
            lst_of_binaries.append((10 - len(bin(ord(letter)))) * '0' + bin(ord(letter))[2:])
        print(lst_of_binaries, "BINARY")
        return lst_of_binaries

    def genetare_vect_a(self, number=10, size=6):
        # while not self.check_independency(vectors):
        vectors = [[[], []], [[], []], [[], []], [[], []], [[], []]]
        while not self.check_independency(vectors):
            vectors = [[[], []], [[], []], [[], []], [[], []], [[], []]]
            for i in range(number // 2):
                for g in range(2):
                    for j in range(size):
                        vectors[i][g].append(random.randint(0, 1))
        return vectors

    def check_independency(self, matrix):
        if matrix != [[[], []], [[], []], [[], []], [[], []], [[], []]]:
            for i in range(1, len(matrix) - 2):
                for j in range(i + 1, len(matrix) - 1):
                    for k in range(j + 1, len(matrix)):
                        if self.determinant([matrix[i][0], matrix[i][1], matrix[j][0], matrix[j][1], matrix[k][0],
                                             matrix[k][1]]) == 0:
                            return False
            return True
        else:
            return False

    def determinant(self, matrix):
        return numpy.linalg.det(matrix)

# print(a.__genetare_vect_a(10, 6))#Перевір цей виклик, він повертає 1 векторів, треба забити в калькулятор і перевірити чи 2,3,4; 2,3,5; 2,4,5; 3,4,5
