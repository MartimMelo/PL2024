import sys
import re

def increment_numbers_in_data(data):
    total_sum = 0
    all_elements = re.findall(r'(on|off|=|\d+)', data, re.IGNORECASE)
    is_on = False
    print(all_elements)

    for element in all_elements:
        if element.lower() == "on":
            is_on = True
        elif element.lower() == "off":
            is_on = False
        elif element == "=":
            print(total_sum)
        elif is_on:
            total_sum += int(element)

def main():
    data = sys.stdin.read()
    increment_numbers_in_data(data)

if __name__ == "__main__":
    main()
