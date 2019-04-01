import Tkinter
import itertools
import SortingAlgorithms
import DecisionTree

# runs a sorting algorithm if user input is valid
def call_sorting_algorithm(algorithm, array):
    dt = DecisionTree.DecisionTree()
    array_permutations = []  # empty list to be filled with all permutations of a given list of elements
    for perm in (itertools.permutations(array)):
        # the permutations returned by itertools.permutations are tuples
        # for the purposes of sorting these permutations need to be in the form of lists
        permutation = []  # a single permutation
        for p in perm:
            permutation.append(p)
        # a permutation should only be added the the list of all permutations if it is not already in the list
        # this is possible if the list contains multiple occurrences of the same element
        if permutation not in array_permutations:
            array_permutations.append(permutation)

    results = []
    for a in array_permutations:
        if algorithm == option_list[0]:
            results = SortingAlgorithms.bubble_sort(a)
        elif algorithm == option_list[1]:
            results = SortingAlgorithms.insertion_sort(a)
        elif algorithm == option_list[2]:
            results = SortingAlgorithms.selection_sort(a)
        elif algorithm == option_list[3]:
            results = SortingAlgorithms.merge_sort(a)
        elif algorithm == option_list[4]:
            results = SortingAlgorithms.heap_sort(a)
        elif algorithm == option_list[5]:
            results = SortingAlgorithms.quick_sort(a, 0, len(a) - 1, 0)

        elements = str(a[0]) + " , " + str(a[1]) + " , " + str(a[2])
        sorted_order = results[0][1] + results[1][1] + results[2][1]

        for l in dt.leaves:
            if l.j_order == sorted_order:
                DecisionTree.append_data(l, elements)
    results_label_text.set((DecisionTree.RenderTree(dt.root)))

# checks that user has submitted valid unput
def submit_user_input():
    feedback_label_text.set("")
    user_input = user_input_entry.get()
    user_input_entry.delete(0, "end")
    user_values = user_input.split()

    # check that user input only contains number
    try:
        list_to_sort = []
        for v in user_values:
            list_to_sort.append(float(v))
        if len(list_to_sort) != 3:
            raise IndexError
        feedback_label_text.set("Success")
        call_sorting_algorithm(option_var.get(), list_to_sort)

    # if non-numeric values are given, prompt the user to try again
    except ValueError:
        feedback_label_text.set("Please enter numbers only")
        return

    # if less than three numbers are given, prompt the user to try again
    except IndexError:
        feedback_label_text.set("Please enter 3 numbers")
        return


window = Tkinter.Tk()
window.title("GUI")
window.geometry("900x500")


selection_label_text = Tkinter.StringVar()
selection_label_text.set("Select a sorting Algorithm")
selection_label = Tkinter.Label(window, textvariable=selection_label_text)
selection_label.pack()

# option list for selecting a sorting algorithm to run
option_list = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Heap Sort", "Quick Sort"]
option_var = Tkinter.StringVar()
option_var.set(option_list[0])
drop_menu = Tkinter.OptionMenu(window, option_var, *option_list)
drop_menu.grid(column=0, row=6)
drop_menu.pack()

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
