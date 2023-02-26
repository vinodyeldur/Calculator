#Calculator
#add
def add(n1 + n2):
  return add

#subtract
def subtract(n1 - n2):
  return subtract

#multiply
def multiply(n1 * n2):
  return multiply

#divide
def divide(n1 / n2):
  return divide

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What is your first number?: "))
num2 = int(input("What is your second number?: "))
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick any operation from the line above:")
calculation_symbol = operations[operation_symbol]
first_answer = calculation_symbol[num1, num2]

print(f'{num1} {operation_symbol} {num2} = {first_answer}')

operation_symbol = input("Pick any operation from the line above:")
num3 = input("what is next number")

print(f' first_answer} {operation_symbol} {num3} = {second_answer}')