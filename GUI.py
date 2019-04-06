import Tkinter
import itertools
import string
import SortingAlgorithms
import DecisionTree


class TreeGui:
    def __init__(self, master):

        # create the GUI window
        self.window = master
        self.window.title("GUI")
        self.window.geometry("700x500")

        # label to prompt the user to select a sorting algorithm
        self.selection_label_text = Tkinter.StringVar()
        self.selection_label_text.set("Select a sorting Algorithm")
        self.selection_label = Tkinter.Label(self.window, textvariable=self.selection_label_text)
        self.selection_label.pack()

        # option list for selecting a sorting algorithm to run
        self.algorithm_option_list = \
            ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Heap Sort", "Quick Sort"]
        self.algorithm_option_var = Tkinter.StringVar()
        self.algorithm_option_var.set(self.algorithm_option_list[0])  # bubble sort is the default option
        self.algorithm_drop_menu = Tkinter.OptionMenu(self.window, self.algorithm_option_var,
                                                      *self.algorithm_option_list)
        self.algorithm_drop_menu.grid(column=0, row=6)
        self.algorithm_drop_menu.pack()

        # label to prompt for the user to enter input
        self.entry_prompt_label_text = Tkinter.StringVar()
        self.entry_prompt_label_text.set("Enter a list of numbers to be sorted \n Numbers must be separated by spaces")
        self.entry_prompt_label = Tkinter.Label(self.window, textvariable=self.entry_prompt_label_text)
        self.entry_prompt_label.pack()

        # label to provide feedback on user input
        self.feedback_label_text = Tkinter.StringVar()
        self.feedback_label_text.set("")
        self.feedback_label = Tkinter.Label(self.window, textvariable=self.feedback_label_text)
        self.feedback_label.pack()

        # entry element for user input
        self.user_input_entry = Tkinter.Entry(self.window)
        self.user_input_entry.pack()

        # submit button
        self.submit_user_input_button = Tkinter.Button(self.window, text="Submit", command=self.submit_user_input)
        self.submit_user_input_button.pack()

        # label to display the decision tree
        self.results_label_text = Tkinter.StringVar()
        self.results_label_text.set("")
        self.results_label = Tkinter.Label(self.window, textvariable=self.results_label_text, justify="left")
        self.results_label.pack()

        self.window.mainloop()

    # checks that user has submitted valid input
    def submit_user_input(self):
        self.feedback_label_text.set("")
        user_input = self.user_input_entry.get()
        self.user_input_entry.delete(0, "end")
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
            # if the user entered more than 3 numbers, allow them to choose a list to create a sub-tee from
            if len(list_to_sort) > 3:
                # create a list containing a combinations of size 3 of the user's input
                combinations = []
                for combination in itertools.combinations(list_to_sort, r=3):
                    c = []
                    for i in combination:
                        c.append(i)
                    if c not in combinations:
                        combinations.append(c)
                # create a popup window allowing users to select a combination
                list_to_sort = self.subtree_popup(combinations)

            self.feedback_label_text.set("Success")
            self.call_sorting_algorithm(self.algorithm_option_var.get(), list_to_sort)

        # if non-numeric values are given, prompt the user to try again
        except ValueError:
            self.feedback_label_text.set("Please enter whole numbers only")
            return

        # if less than three numbers are given, prompt the user to try again
        except IOError:
            self.feedback_label_text.set("Please enter at least 3 numbers")
            return

    def subtree_popup(self, array):
        # the index of the list chosen by the user
        index = [0]

        # sets index to the index of the list the user selected
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

        # prompts the user to select a list
        popup_prompt_label = Tkinter.Label(popup, text="Select a list to create a sub-tree from")
        popup_prompt_label.pack()

        # option list for selecting a list to make a sub-tree from
        subtree_option_var = Tkinter.StringVar(popup)
        subtree_option_var.set(subtree_option_list[0])  # index 0 in the list of combinations is the default
        subtree_drop_menu = Tkinter.OptionMenu(popup, subtree_option_var, *subtree_option_list)
        subtree_drop_menu.grid(column=0, row=100)
        subtree_drop_menu.pack()

        # button for submitting the users choice
        select_button = Tkinter.Button(popup, text="Select", command=select_subtree)
        select_button.pack()

        popup.mainloop()

        # destroy the popup window and return the chosen list
        popup.destroy()
        return array[index[0]]

    # runs a sorting algorithm if user input is valid
    def call_sorting_algorithm(self, algorithm, array):
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
                # append a tuple which satisfies the requirements for parameters for
                #  the sorting algorithm implementations
                p.append((i, string.ascii_lowercase[char]))
                char += 1
            # a permutation should only be added the the list of all permutations if it is not already in the list
            # this is possible if the list contains multiple occurrences of the same element
            if p not in array_permutations:
                array_permutations.append(p)

        # the initial order of elements for any list
        order = ["a", "b", "c"]

        # create the root node for the decision tree
        root = DecisionTree.TreeNode(None, order, None)

        # run the selected sorting algorithm on each permutation
        for a in array_permutations:
            SortingAlgorithms.decisions_made[:] = []  # empties the decisions_made list
            unsorted_array = list(a)
            if algorithm == self.algorithm_option_list[0]:
                SortingAlgorithms.bubble_sort(a)
            elif algorithm == self.algorithm_option_list[1]:
                SortingAlgorithms.insertion_sort(a)
            elif algorithm == self.algorithm_option_list[2]:
                SortingAlgorithms.selection_sort(a)
            elif algorithm == self.algorithm_option_list[3]:
                SortingAlgorithms.merge_sort(a)
            elif algorithm == self.algorithm_option_list[4]:
                SortingAlgorithms.heap_sort(a)
            elif algorithm == self.algorithm_option_list[5]:
                SortingAlgorithms.quick_sort(a, 0, len(a) - 1)

            # add the results to the tree
            root.add_node(order, SortingAlgorithms.decisions_made, unsorted_array)

        # create a graphic representation of the node using the anytree library
        # and display it in the GUI window
        graphic_root = root.create_graphic_node(len(array))
        self.results_label_text.set((DecisionTree.RenderTree(graphic_root)))
