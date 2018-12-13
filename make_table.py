from __future__ import print_function


def print_upper_bound_line(head, body):
    print("|", end='')
    for index, eye in enumerate(head):
        largest_length = len(eye)
        for element in body:
            if len(element[index]) > largest_length:
                largest_length = len(element[index])
        upper_bound_length = largest_length + 2
        print("-" * upper_bound_length, end='|')
    print()


def print_head_elements(head, body):
    print("|", end='')
    for index, eye in enumerate(head):
        largest_length = len(eye)
        for element in body:
            if len(element[index]) > largest_length:
                largest_length = len(element[index])
        upper_bound_length = largest_length + 2
        print(eye, end='')
        print(" " * (upper_bound_length - len(eye)), end='|')

    print()


def print_body_elements(head, body):
    list_of_lengths = list()
    for index, eye in enumerate(head):
        largest_length = len(eye)
        for element in body:
            if len(element[index]) > largest_length:
                largest_length = len(element[index])
        upper_bound_length = largest_length + 2
        list_of_lengths.append(upper_bound_length)

    for element in body:
        print("|", end='')
        for el in element:
            print(el, end='')
            print(" " * (list_of_lengths[element.index(el)] - len(el)), end='|')
        print()


def print_table(head, body):

    for element in body:
        if len(element) != len(head):
            return

    print_upper_bound_line(head, body)
    print_head_elements(head, body)
    print_upper_bound_line(head, body)
    print_body_elements(head, body)
    print_upper_bound_line(head, body)


def main():
    head = ["list_element_1", "list_element_2", "list_element_3"]
    body = [["vjp1", "22", "0"], ["vjp2", "23", "1"], ["vjp3 for testing making a very large line", "24", "2"], ["very big line for testing", "23", "3"]]

    print_table(head, body)


if __name__ == '__main__':
    main()
