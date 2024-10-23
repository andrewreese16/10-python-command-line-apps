def calculate(expression):
  try:
    result = eval(expression)
    return result
  except ZeroDivisionError:
    return "Error: Division by zero is not allowed."
  
def calculator():
  print("=== Calculator ===")
  print("Enter your mathmatical expression (or type 'quit to exit).")

  while True:
    user_input = input("\nEnter expression: ")
    if user_input.lower() == 'quit':
      print("Goodbye!")
      break
    
    result = calculate(user_input)

    print(f"Result: {result}")


if __name__ == "__main__":
      calculator()
