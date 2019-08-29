# 'r' means read only
# file_for_reading = open('reading_file.txt', 'r')
# make sure to close!
# file_for_reading.close()

# or you can use a with block, which will close the file

lines = ''
with open('10-exercises/some_other_text_file.txt', 'r') as file:
    for line in file:
        print('next line = %s' % (line.strip()))
