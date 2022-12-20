## Assignment
Write a program to prompt for a file name, and then read through the file and look for lines of the form:
```
X-DSPAM-Confidence: 0.8475
```

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

## Starter Code
```
file_name = input("Enter the file name: ")
```

## Desired Output
```
Enter the file name: mbox-short.txt
Average spam confidence: 0.7507185185185187
```

OR

```
Enter the file name: mbox-long.txt
Average spam confidence: 0.8941280467445736
```

## Test
When you're ready, run `pytest` in the terminal
