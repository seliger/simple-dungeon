
from pprint import pprint

X_AXIS = ['west', 'center', 'east']
Y_AXIS = ['north', 'mid', 'south']
CARDINALS = ['north', 'south', 'west', 'east']


def parse_command_words(command_text: str) -> list[str]:
    return [word for word in command_text.split(' ') if word]


def generate_map() -> list[list[dict]]:
    game_map = []
    for row in range(len(Y_AXIS)):
        game_map_row = []
        for col in range(len(X_AXIS)):
            game_map_row.append({
                'name': f'{Y_AXIS[row].capitalize()}-{X_AXIS[col]} Corridor',
                'description': f'A dark corridor in the {Y_AXIS[row]}-{X_AXIS[col]} section of the dungeon.',
            })
        game_map.append(game_map_row)

    return game_map


def calculate_exits(game_map: list[list[dict]], coordinates: list) -> list:
    possible_exits = []

    if coordinates[1] > 0:
        possible_exits.append(CARDINALS[0])

    if coordinates[1] < len(game_map) - 1:
        possible_exits.append(CARDINALS[1])

    if coordinates[0] > 0:
        possible_exits.append(CARDINALS[2])

    if coordinates[0] < len(game_map[coordinates[0]]) - 1:
        possible_exits.append(CARDINALS[3])

    return possible_exits


def calculate_move(command: str, coordinates: list) -> list:

    # Determine the index of our direct (e.g., north = 0)
    cardinal_index: int = CARDINALS.index(command)

    # Compute the direction based on the remainder
    # Evens subtract (north, west), odds add (south, east)
    direction: int = 1 if cardinal_index % 2 else -1

    if cardinal_index > 1:
        coordinates[0] += direction
    else:
        coordinates[1] += direction

    return coordinates


def main() -> None:

    current_position: list = [1, 1]
    game_map = generate_map()
    game_active = True

    while game_active:
        exits: list = calculate_exits(game_map, current_position)

        print(f'Possible exits are {", ".join(exits)}.')
        command = parse_command_words(input('> '))

        if command:
            if command[0].lower() in ('quit', 'exit'):
                game_active = False
            elif command[0].lower() in exits:
                current_position = calculate_move(command[0], current_position)
            else:
                print(f'Unknown command: {command[0]}')


if __name__ == '__main__':
    main()
