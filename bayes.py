import sys
import os
import math

def main():

    total_spam = 0
    total_ham = 0

    p_spam = {}
    p_ham = {}

    f_spam = open('probability_spam_words.txt', 'r')
    f_ham = open('probability_ham_words.txt', 'r')

    spam_lines = f_spam.read().splitlines()
    ham_lines = f_ham.read().splitlines()

    line1_spam = spam_lines[0]
    line1_ham = ham_lines[0]

    num_spam_file = int(line1_spam.split()[1])
    num_ham_file = int(line1_ham.split()[1]) 

    for line in spam_lines[2:]:
        items = line.split()
        p_spam[items[0]] = float(items[1])
        total_spam += int(items[2])
    for line in ham_lines[2:]:
        items = line.split()
        p_ham[items[0]] = float(items[1])
        total_ham += int(items[2])


    if len(sys.argv) != 3:
        sys.exit('Usage: python bayes.py input output')

    file_in = open(sys.argv[1], 'r')
    file_out = open(sys.argv[2], 'w')

    words_in = []
    p_spam_in = []
    p_ham_in = []

    for line in file_in.read().splitlines():
        for word in line.split():
            words_in.append(word)
            if word not in p_spam:
                p_spam_in.append(1/total_spam)
            else:
                p_spam_in.append(p_spam[word])
            if word not in p_ham:
                p_ham_in.append(1/total_ham)
            else:
                p_ham_in.append(p_ham[word])

    log_p_spam = 0
    log_p_ham = 0

    file_out.write('(1)P(Spam, all words)\n')
    p_spam_file = num_spam_file / (num_spam_file+num_ham_file)
    file_out.write('   P(Spam) = {:.4f}\n'.format(p_spam_file))
    log_p_spam += math.log(p_spam_file)

    for i in range(len(words_in)):
        file_out.write("   P('{}'|Spam) = {:.4f}\n".format(words_in[i], p_spam_in[i]))
        log_p_spam += math.log(p_spam_in[i])

    file_out.write("   log P(Spam, all words) = {:.4f}\n".format(log_p_spam))

    file_out.write('(2)P(Ham, all words)\n')
    p_ham_file = num_ham_file / (num_spam_file+num_ham_file)
    file_out.write('   P(Ham) = {:.4f}\n'.format(p_ham_file))
    log_p_ham += math.log(p_ham_file)

    for i in range(len(words_in)):
        file_out.write("   P('{}'|Ham) = {:.4f}\n".format(words_in[i], p_ham_in[i]))
        log_p_ham += math.log(p_ham_in[i])

    file_out.write("   log P(Ham, all words) = {:.4f}\n".format(log_p_ham))

    file_out.write("\nConclusion: This message is classified as ")
    if log_p_spam >= log_p_ham:
        file_out.write("Spam.\n")
    else:
        file_out.wrtie("Ham.\n")



    file_out.close()




main()


