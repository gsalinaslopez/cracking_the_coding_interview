import arrays_and_strings
from linked_lists import *
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(arrays_and_strings.question_1_6("aabcccccaaa"))
    print(arrays_and_strings.question_1_6("abc"))
    exit(0)
    print(arrays_and_strings.question_1_4("tact coa"))
    exit(0)
    # print(arrays_and_strings.question_1_1("unico"))
    # print(arrays_and_strings.question_1_1("unicorn"))

    # print(arrays_and_strings.question_1_2("check", "khecc"))
    # print(arrays_and_strings.question_1_2("checa", "khecc"))
    # print(arrays_and_strings.question_1_3("Mr John Smith    ", 13))
    # arrays_and_strings.question_1_3("Mr John Smith    ", 13)

    # example_ll = LinkedList()
    # example_ll.append(1)
    # example_ll.append(4)
    # example_ll.append(5)
    # example_ll.append(9)
    # example_ll.print_contents()
    #
    # print()
    # example_ll.delete(6)
    # example_ll.delete(1)
    # example_ll.delete(9)
    # example_ll.print_contents()
    #
    # print()
    # example_ll.append(6)
    # example_ll.append(7)
    # example_ll.print_contents()

    example_dll = DoublyLinkedList()
    example_dll.append(1)
    example_dll.append(4)
    example_dll.append(5)
    example_dll.append(9)
    example_dll.print_contents()
    # print()
    # example_dll.print_links()

    print()
    example_dll.delete(6)
    example_dll.delete(4)
    example_dll.delete(9)
    example_dll.print_contents()
    # print()
    # example_dll.print_links()

    print()
    example_dll.append(6)
    example_dll.append(7)
    example_dll.print_contents()
    # print()
    # example_dll.print_links()

    print()
    example_dll.delete(1)
    # example_dll.delete(5)
    # example_dll.delete(6)
    # example_dll.delete(7)
    example_dll.print_contents()
    print()
    example_dll.print_links()

    print()
    example_dll.append(6)
    example_dll.append(7)
    example_dll.print_contents()
    # print()
    # example_dll.print_links()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
