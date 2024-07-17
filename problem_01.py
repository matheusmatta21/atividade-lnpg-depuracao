def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def get_numbers():
    while True:
        try:
            numbers = input("Enter numbers separated by spaces: ").split()
            numbers = [
                float(num) for num in numbers
            ]  ## casting para float, assim qualquer tipo numérico pode ser digitado
            return numbers
        except ValueError:
            print(
                "Digite números."
            )  ## verificacao de tipo para apenas numeros serem digitados


def main():
    numbers = get_numbers()
    if len(numbers) == 0:  ## verificar se a lista é vazia, evitando divisão por 0
        print("Não houve entrada de dados")
    else:
        print("Average:", calculate_average(numbers))
        print("Maximum:", find_max(numbers))


if __name__ == "__main__":
    main()
