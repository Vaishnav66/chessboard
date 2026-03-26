def determine_color(s):
    col = ord(s[0]) - ord('a')  # a=0
    row = int(s[1])
    
    if (col + row) % 2 == 1:
        return "Black"
    else:
        return "White"
    pass

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the input string
    
    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()
