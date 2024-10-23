class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.paths = {}

    def set_paths(self, directions):
        self.paths = directions

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def describe(self):
        return f"{self.name}: {self.description}\nItems: {', '.join(self.items) if self.items else "None"}"


class Player:
    def __init__(self, start_location):
        self.current_location = start_location
        self.inventory = []

    def move(self, direction):
        if direction in self.current_location.paths:
            self.current_location = self.current_location.paths[direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way!")

    def pick_up_item(self, item):
        if item in self.current_location.items:
            self.inventory.append(item)
            self.current_location.remove_item(item)
            print(f"You picked up: {item}")
        else:
            print("Item not found!")

    def use_item(self, item):
        if item in self.inventory:
            print(f"You used the {item}.")
        else:
            print("You don't have that item.")


class Game:
    def __init__(self):
        self.locations = self.create_world()
        self.player = Player(self.locations["Start"])

    def create_world(self):
        start = Location("Start", "You are the start of your journey.")
        forest = Location("Forest", "You are surrounded by trees.")
        cave = Location("Cave", "A very dark cave is ahead.")
        treasure_room = Location(
            "Treasure Room", "You have found a hidden treasure room!"
        )

        start.set_paths({"north": forest})
        forest.set_paths({"south": start, "east": cave})
        cave.set_paths({"west": forest, "north": treasure_room})
        treasure_room.set_paths({"south": cave})

        forest.add_item("stick")
        cave.add_item("key")
        treasure_room.add_item("treasure")

        return {
            "Start": start,
            "Forest": forest,
            "cave": cave,
            "Treasure Room": treasure_room,
        }

    def play(self):
        print("=== Welcome to the Adventure Game ===")
        while True:
            print(self.player.current_location.describe())
            action = input(
                "\nWhat do you want to do? (move, pick up, use, quit): "
            ).lower()
            if action == "move":
                direction = input(
                    "Which direction? (north, south, east, west): "
                ).lower()
                self.player.move(direction)
            elif action == "pick up":
                item = input("What do you want to pick up?: ").lower()
                self.player.pick_up_item(item)
            elif action == "use":
                item = input("What item do you want to use?: ").lower()
                self.player.use_item(item)
            elif action == "quit":
                print("Thanks for playing!")
                break
            else:
                print("That is not a valid action.")


if __name__ == "__main__":
    game = Game()
    game.play()
