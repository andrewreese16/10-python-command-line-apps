import json

class Flashcard:
  def __init__(self, term, definition):
    self.term = term
    self.definition = definition

  def __str__(self):
    return f"{self.term}: {self.definition}"
  

class FlashcardApp:
  def __init__(self):
    self.flashcards = []

  def add_flashcard(self, term, definition):
    flashcard = Flashcard(term, definition)
    self.flashcards.append(flashcard)
    print("Flashcard added.")

  def view_flashcards(self):
    if not self.flashcards:
      print("No flashcards.")
      return
    for card in self.flashcards:
      print(card)

  def quiz(self):
    if not self.flashcards:
      print("No flashcards")
      return
    
    score = 0
    for card in self.flashcards:
      answer = input(f"What is the definition of '{card.term}?'")
      if answer.lower() == card.definition.lower():
        print("correct")
        score += 1
      else:
        print(f"Incorrect! The correct answer is: {card.definition}")
      print(f"Your score: {score}/{len(self.flashcards)}")

  def save_flashcards(self, filename='flashcards.json'):
    with open(filename, 'w') as f:
      json.dump([{'term': card.term, 'definition': card.definition} for card in self.flashcards], f)
    print("Flashcards saved.")

  def load_flashcards(self, filename='flashcards.json'):
    try:
      with open(filename, 'r') as f:
        cards_data = json.load(f)
        self.flashcards = [Flashcard(card['term'], card['definition']) for card in cards_data]
      print("Flashcards loaded.")
    except FileNotFoundError:
      print("No saved flashcards.")


def main():
  app = FlashcardApp()

  app.load_flashcards()

  while True:
    print("\n=== Flashcards App ===")
    print("1. Add Flashcard")
    print("2. View Flashcards")
    print("3. Quiz")
    print("4. Save Flashcards")
    print("5. Quit")
    choice = input("Select an option: ")

    if choice == '1':
      term = input("Enter the term: ")
      definition = input("Enter the definition: ")
      app.add_flashcard(term, definition)
    elif choice == '2':
      app.view_flashcards()
    elif choice == '3':
      app.quiz()
    elif choice == '4':
      app.save_flashcards()
    elif choice == '5':
      print("Goodbye!")
      break
    else:
      print("That is not a valid choice")

if __name__ == "__main__":
  main()