# Создать класс структуры данных Стек, Очередь. Создать класс
# комплексного числа и реализовать для него арифметические
# операции.

from collections import deque


class Stack(deque):
    def push(self, x):
        super().append(x)

    def pop(self):
        return super().pop()


class Queue(deque):
    def enqueue(self, x):
        self.append(x)

    def dequeue(self):
        return self.popleft()


s = Stack()
q = Queue()

s.push(1)
s.push(2)
s.push(4)

q.enqueue(1)
q.enqueue(3)
q.enqueue(9)

print(s)
print(q)

s.pop()
q.dequeue()

print(s)
print(q)


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, obj):
        self.sum_real = self.real + obj.real
        self.sum_imag = self.imag + obj.imag
        return self.sum_real, self.sum_imag

    def __mul__(self, obj):
        self.mult_real = self.real * obj.real - self.imag * obj.imag
        self.mult_imag = self.imag * obj.real + self.real * obj.real
        return self.mult_real, self.mult_imag

    def __str__(self):
        return f'{self.real}, {self.imag}'


x = Complex(1, 3)
y = Complex(4, 2)

sum = x + y
mult = x * y

print(f'Sum is {sum}')
print(f'Multiple is {mult}')
