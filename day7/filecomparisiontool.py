
import difflib

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.readlines()
        text2 = f2.readlines()

    differ = difflib.Differ()
    diff = list(differ.compare(text1, text2))

    differences = [line for line in diff if line.startswith('- ') or line.startswith('+ ')]
    
    if differences:
        print("Differences will be found:")
        for line in differences:
            print(line)
    else:
        print("No differences will be  found.")


if __name__ == "__main__":
    file1 = input("Enter the your first file path: ")
    file2 = input("Enter the your second file path: ")

    compare_files(file1, file2)
