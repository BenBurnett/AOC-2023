import sys


def test_input() -> None:
    _input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip().split('\n')

    assert part_1(_input) == 142


def test_input_2() -> None:
    _input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip().split('\n')

    assert part_2(_input) == 281


def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f]


def score_line(line: str) -> int:
    digits = [d for d in line if d.isdigit()]
    return int(digits[0] + digits[-1])


def part_1(input_data: list[str]) -> int:
    return sum(score_line(line) for line in input_data)


def part_2(input_data: list[str]) -> int:
    digits = {
        'one': 'o1e',
        'zero': '0o',
        'four': '4',
        'five': '5e',
        'six': '6',
        'seven': '7',
        'eight': 'e8t',
        'two': 't2o',
        'three': 't3e',
        'nine': 'n9e',
    }

    def replace_digits(line: str) -> str:
        for word, replacement in digits.items():
            line = line.replace(word, replacement)
        return line

    return sum(score_line(replace_digits(line)) for line in input_data)


def main() -> None:
    input_data = read_input(sys.argv[1])
    print(f'Part 1: {part_1(input_data)}')
    print(f'Part 2: {part_2(input_data)}')


if __name__ == '__main__':
    main()
