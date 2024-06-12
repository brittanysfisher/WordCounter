# README

I cloned this repository: https://github.com/hadoop-sandbox/hadoop-sandbox.git

I modified the mapper from https://github.com/cd-public/merrer/

I used the following mapred command:
```
hdfs dfs -rm -r /user/sandbox/words
mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words \
  -mapper mapper.py \
  -reducer reducer.py \
  -file scripts/mapper.py \
  -file scripts/reducer.py
```

I tested my map reduce word count scripts on the Pride and Prejudice text from: https://raw.githubusercontent.com/cd-public/books/main/pg1342.txt

I could not figure out how to save the word counts from the sandbox connection on Cloud Shell to my local device, but upon inspecting both the head and viewing all word counts with 'cat', my new script seems to have counted the words how I wanted. 

Note: I only modified the mapper script (the reducer script was left the same).
