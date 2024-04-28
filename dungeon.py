
def parse_command_words(command_text: str) -> list[str]:
    return [word for word in command_text.split(' ') if word]


def main() -> None:
    game_active = True
    while game_active:
        command = parse_command_words(input('> '))

        if command[0].lower() in ('quit', 'exit'):
            game_active = False


if __name__ == '__main__':
    main()
