# Slicing exercises in Python

### haircut
Write a function haircut(aList) that chops the first and last element of the list.
So: haircut([0,1,2,3,4]) should return [1,2,3]

### slicer
Define a function slicer(aList, start, end) which takes a list and a start/end position and returns the list WITHOUT the bit between the start/end position. Use slicing operations to get the job done!
So: slicer([0, 1, 2, 3, 4, 5, 6, 7], 2, 4) should return [0, 1, 4, 5, 6, 7]

### wordSlicer
Define a function wordSlicer(aList, aWord) which takes a list and a word and returns all the elements of the list up until that word.
So: wordSlicer(["use", "the", "force", "Luke"], "force") should return ["use", "the"]

### repeatPart
Write a function repeatPart(aList, start, end) which takes a list and a start/end position and returns the list with the bit between the start/end position attached to the end. Use slicing operations to get the job done.
So: repeatPart([0,1,2,3,4,5,6], 2, 4) should return [0,1,2,3,4,5,6,2,3]
