import glob, re


spam_file_path = "/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/14-exercies/spam-data/*/*"
data = []

unicode_exception_counts = {
    'SPAM': 0,
    'HARD_HAM': 0,
    'EASY_HAM': 0
}

email_class_totals = {
    'SPAM': 0,
    'HARD_HAM': 0,
    'EASY_HAM': 0
}

for filename in glob.glob(spam_file_path):
    is_spam = "ham" not in filename
    is_hard_ham = "hard_ham" in filename
    is_easy_ham = "easy_ham" in filename

    if is_spam: email_class_totals['SPAM'] += 1
    if is_hard_ham: email_class_totals['HARD_HAM'] += 1
    if is_easy_ham: email_class_totals['EASY_HAM'] += 1

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("Subject:"):
                    subject = re.sub("^Subject: ", "", line).strip()
                    data.append((subject, is_spam))
    except UnicodeDecodeError:
        # print('UnicodeDecodeError thrown for file = %s' % filename)
        if is_spam: unicode_exception_counts['SPAM'] += 1
        if is_hard_ham: unicode_exception_counts['HARD_HAM'] += 1
        if is_easy_ham: unicode_exception_counts['EASY_HAM'] += 1


# print('data length = %s' % len(data))

# print('SPAM unicode_exception_count = %s' % unicode_exception_counts['SPAM'])
# print('SPAM email_class_total = %s' % email_class_totals['SPAM'])
# print('SPAM percentage_error_throwing_data = %s' % (
#     unicode_exception_counts['SPAM'] / email_class_totals['SPAM']
# ))

# print('HARD_HAM unicode_exception_count = %s' % unicode_exception_counts['HARD_HAM'])
# print('HARD_HAM email_class_total = %s' % email_class_totals['HARD_HAM'])
# print('HARD_HAM percentage_error_throwing_data = %s' % (
#     unicode_exception_counts['HARD_HAM'] / email_class_totals['HARD_HAM']
# ))

# print('EASY_HAM unicode_exception_count = %s' % unicode_exception_counts['EASY_HAM'])
# print('EASY_HAM email_class_total = %s' % email_class_totals['EASY_HAM'])
# print('EASY_HAM percentage_error_throwing_data = %s' % (
#     unicode_exception_counts['EASY_HAM'] / email_class_totals['EASY_HAM']
# ))

# for index in range(10):
    # data_tuple = data[index]
    # print('next data tuple: subject = %s, is_spam = %s', data_tuple)
