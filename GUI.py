import Tkinter
import itertools
import string
import SortingAlgorithms
import DecisionTree


# checks that user has submitted valid input
def submit_user_input():
    feedback_label_text.set("")
    user_input = user_input_entry.get()
    user_input_entry.delete(0, "end")
    user_values = user_input.split()

    # check that user input only contains number
    try:
        list_to_sort = []
        # check that user only entered whole numbers
        for v in user_values:
            list_to_sort.append(int(v))
        # checks that user entered at least 3 numbers
        if len(list_to_sort) < 3:
            raise IOError
        if len(list_to_sort) > 3:
            combinations = []
            for combination in itertools.combinations(list_to_sort, r=3):
                c = []
                for i in combination:
                    c.append(i)
                if c not in combinations:
                    combinations.append(c)
            list_to_sort = subtree_popup(combinations)

        feedback_label_text.set("Success")
        call_sorting_algorithm(algorithm_option_var.get(), list_to_sort)

    # if non-numeric values are given, prompt the user to try again
    except ValueError:
        feedback_label_text.set("Please enter whole numbers only")
        return

    # if less than three numbers are given, prompt the user to try again
    except IOError:
        feedback_label_text.set("Please enter at least 3 numbers")
        return


def subtree_popup(array):
    index = [0]

    def select_subtree():
        index[0] = subtree_option_list.index(subtree_option_var.get())
        popup.quit()

    subtree_option_list = []
    for i in array:
        st = ""
        for j in i:
            st = st + str(j) + " "
        subtree_option_list.append(st)
    popup = Tkinter.Tk()
    popup.title("Sub-tree Selection")

    popup_label = Tkinter.Label(popup, text="Select a list to create a sub-tree from")
    popup_label.pack()

    # option list for selecting a list to make a sub-tree from
    subtree_option_var = Tkinter.StringVar()
    subtree_option_var.set(subtree_option_list[0])
    subtree_drop_menu = Tkinter.OptionMenu(popup, subtree_option_var, *subtree_option_list)
    subtree_drop_menu.grid(column=0, row=1)
    subtree_drop_menu.pack()

    select_button = Tkinter.Button(popup, text="Select", command=select_subtree)
    select_button.pack()

    popup.mainloop()
    popup.destroy()
    return array[index[0]]



# runs a sorting algorithm if user input is valid
def call_sorting_algorithm(algorithm, array):
    letters = ""
    for i in range(len(array)):
        letters = letters + string.ascii_lowercase[i]

    array_permutations = []  # empty list to be filled with all permutations of a given list of elements
    for permutation in (itertools.permutations(array)):
        # the permutations returned by itertools.permutations are tuples
        # for the purposes of sorting these permutations need to be in the form of lists
        p = []  # a single permutation
        char = 0
        for i in permutation:
            p.append((i, string.ascii_lowercase[char]))
            char += 1
        # a permutation should only be added the the list of all permutations if it is not already in the list
        # this is possible if the list contains multiple occurrences of the same element
        if p not in array_permutations:
            array_permutations.append(p)

    order = []
    for i in range(len(array)):
        order.append(string.ascii_lowercase[i])

    root = DecisionTree.TreeNode(None, order, None)

    for a in array_permutations:
        SortingAlgorithms.decisions_made[:] = []
        unsorted_array = list(a)
        if algorithm == algorithm_option_list[0]:
            SortingAlgorithms.bubble_sort(a)
        elif algorithm == algorithm_option_list[1]:
            SortingAlgorithms.insertion_sort(a)
        elif algorithm == algorithm_option_list[2]:
            SortingAlgorithms.selection_sort(a)
        elif algorithm == algorithm_option_list[3]:
            SortingAlgorithms.merge_sort(a)
        elif algorithm == algorithm_option_list[4]:
            SortingAlgorithms.heap_sort(a)
        elif algorithm == algorithm_option_list[5]:
            SortingAlgorithms.quick_sort(a, 0, len(a) - 1)

        root.add_node(order, SortingAlgorithms.decisions_made, unsorted_array)

    graphic_root = root.create_graphic_node(len(array))
    results_label_text.set((DecisionTree.RenderTree(graphic_root)))


# creating the window that contains all Tkinter widgets
window = Tkinter.Tk()
window.title("GUI")
window.geometry("700x500")

# label to prompt the user to select a sorting algorithm
selection_label_text = Tkinter.StringVar()
selection_label_text.set("Select a sorting Algorithm")
selection_label = Tkinter.Label(window, textvariable=selection_label_text)
selection_label.pack()

# option list for selecting a sorting algorithm to run
algorithm_option_list = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Heap Sort", "Quick Sort"]
algorithm_option_var = Tkinter.StringVar()
algorithm_option_var.set(algorithm_option_list[0])  # bubble sort is the default algorithm
algorithm_drop_menu = Tkinter.OptionMenu(window, algorithm_option_var, *algorithm_option_list)
algorithm_drop_menu.grid(column=0, row=6)
algorithm_drop_menu.pack()

# label to prompt for the user to enter input
entry_prompt_label_text = Tkinter.StringVar()
entry_prompt_label_text.set("Enter a list of numbers to be sorted \n Numbers must be separated by spaces")
entry_prompt_label = Tkinter.Label(window, textvariable=entry_prompt_label_text)
entry_prompt_label.pack()

# label to provide feedback on user input
feedback_label_text = Tkinter.StringVar()
feedback_label_text.set("")
feedback_label = Tkinter.Label(window, textvariable=feedback_label_text)
feedback_label.pack()

# entry element for user input
user_input_entry = Tkinter.Entry(window)
user_input_entry.pack()

# submit button
submit_user_input_button = Tkinter.Button(window, text="Submit", command=submit_user_input)
submit_user_input_button.pack()


# label to display the decision tree
results_label_text = Tkinter.StringVar()
results_label_text.set("")
results_label = Tkinter.Label(window, textvariable=results_label_text, justify="left")
results_label.pack()


window.mainloop()
