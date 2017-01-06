######
# TODO:
# 1. Change 0001 to 1
# 2. Change frame number to miliseconds
# 3. Change space between in_time and out_time to -->
# 4. Write to new file according to srt format
######
# .srt format START
'''
1
00:00:20,000 --> 00:00:24,400
Howdy!

2
00:00:24,600 --> 00:00:27,800
Why, hello there!
What's your name?

'''
# .srt format ENDS

f = open('rof.txt','r+b')
#f.read()
lines = f.readlines()

list_of_headers = []
num = []
in_time = []
out_time = []

list_of_sub_content = []

# choose only the numbers, time in and time out. Every third element. 
list_of_headers = lines[::3]

header_split = [] 
new_header = []
in_time_split = []
out_time_split = []

for item in list_of_headers:
    # WORK ON THE NUMBERS. Convert 0001 to 1 etc.       
    # split the header by space
    # result: each header is a list with 3 or 4 members
    header_split = item.split(" ")
    
    # strip the leading zeroes
    # result: number with no leader zeroes. .srt format requirement
    header_split[0] = header_split[0].rstrip(" ").lstrip('0')
    
    # remove sticky \r\n
    header_split[2] = header_split[2].rstrip("\r\n")
    
    # remove the extra \r\n member, caused by inconsistent spacing between out time and \r\n. 
    # Later will add it back when I write to file
    if len(header_split) == 4:
        header_split.pop()
    
    # work on in_time
    # convert frames to milisecond
    in_time_split = header_split[1].split(":")
    in_time_split[3] = str(int(float(in_time_split[3])/25*1000))
    #print in_time_split
    
    # put in_time_split back together again
    header_split[1] = in_time_split[0] + ":" + in_time_split[1] + ":" + in_time_split[2] + "," + in_time_split[3]
    #print header_split[1]
    
    
    # work on out_time
    # convert frames to milisecond
    out_time_split = header_split[2].split(":")
    out_time_split[3] = str(int(float(out_time_split[3])/25*1000))
    #print out_time_split
    
    # put out_time_split back together again
    header_split[2] = out_time_split[0] + ":" + out_time_split[1] + ":" + out_time_split[2] + "," + out_time_split[3]
    #print header_split[2]    
    
        
    # put everything back together again in new_header
    new_header.append(header_split)


# choose only the subtitle text itself
list_of_sub_content = lines[1::3]    


# aggregate elements from both cleaned up header and list of subtitle text
zipped = zip(new_header,list_of_sub_content)


# Writing the wrangled items to new file

f2 = open('rof_new.txt','w')   

for item in zipped:
    f2.write(item[0][0]+'\r\n')
    f2.write(item[0][1]+' --> '+ item[0][2] + '\r\n')
    f2.write(item[1]+'\r\n')
    
    
    
    