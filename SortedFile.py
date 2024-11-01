def sort_words_in_file(Input,Output):
    try:
         open("Input.txt", 'r') as file:
            words = file.read().split()
        lower_case_words = [word.lower() for word in words]
        sorted_words = sorted(set(lower_case_words)) 
         open("Output.txt", 'w') as file:
            for word in sorted_words:
                file.write(f"{word}\n")
        print(f"Sorted words written to {Output}")
    except Exception as e:
        print(f"An error occurred: {e}")
