import csv
import os
neg_file_dir = './Sentiment Analysis/Movie Review Dataset/tokens/neg'
pos_file_dir = './Sentiment Analysis/Movie Review Dataset/tokens/pos'  
neg_txt_files = [file for file in os.listdir(neg_file_dir) if file.endswith('.txt')]
pos_txt_files = [file for file in os.listdir(pos_file_dir) if file.endswith('.txt')]
with open('./Sentiment Analysis/movie_review.csv', 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(["Review", "Polarity"])
    #writing in the negatives
    for txt_file in neg_txt_files:
        with open(os.path.join(neg_file_dir, txt_file), 'r', encoding='ISO-8859-1') as file:
            content = file.read()
            content = content.replace(",","")
            writer.writerow([content,-1])
    #writing in the positives
    for txt_file in pos_txt_files:
        with open(os.path.join(pos_file_dir, txt_file), 'rt', encoding='ISO-8859-1') as file:
            content = file.read()
            content = content.replace(",","")
            writer.writerow([content,1])
     