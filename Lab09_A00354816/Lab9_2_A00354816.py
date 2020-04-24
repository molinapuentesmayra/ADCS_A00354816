
import csv
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='Lab9_A00354816_LOG.log',
                    filemode='w')

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s = %(message)s")
handler.setFormatter(formatter)
logging.getLogger('').addHandler(handler)

class Lab5:
    arr = []

    # Python program for implementation of MergeSort
    def execute_merge_sort(self):
        
        logging.info("execute merge_sort on arr %s", self.arr)
        self.merge_sort(self, self.arr)

        return (self.arr)

    def merge_sort(self, arr):
        if len(arr) > 1:
            middle = len(arr) // 2
            left = arr[:middle]
            right = arr[middle:]

            # merge is recursive, apply merge mechanism on each half
            self.merge_sort(self, left)
            self.merge_sort(self, right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Previous loop only runs if both have something in queue, must check if there are remaining on the sides
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    # This methods sets the information about the file that will be used to read the data
    # Define custom exceptions or error codes for where the parameter is incorrect
    def set_input_data(self, file_path_name, is_num):
        if not file_path_name:
            raise FileNotFoundError

        with open(file_path_name, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)

        unsorted_list = []
        # really wanted to deal with only one big list to sort
        for column in rows:
            for x in column:
                if x != " ":
                    if is_num:
                        unsorted_list.append(int(x))
                    else:
                        unsorted_list.append(x)
        self.arr = unsorted_list
        return unsorted_list

    # This methods sets the information about the file that will be used to store the data
    # Define custom exceptions or error codes for situations where the parameter is incorrect
    def set_output_data(file_path_name, sorted_list):
        with open(file_path_name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(sorted_list)


 if __name__ == '__main__':
     logging.info("MERGE SORT - reading input data from unsorted_list.csv")
     arr = set_input_data("unsorted_list.csv", True)
     logging.info("MERGE SORT PRE - array %s",arr)
     print(arr)

     logging.info("MERGE SORT - executing merge sort")
     execute_merge_sort(arr)

     logging.info("MERGE SORT - saving sorted list to sorted_list.csv")
     set_output_data("sorted_list.csv", arr)

     logging.info("MERGE SORT PRE - array %s",arr)
     print(arr)
