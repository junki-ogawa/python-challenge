import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

list_of_votes = []
complete_list_of_candidates = {}


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        #total number of votes
        list_of_votes.append(row[2])
        
        candidate = row[2]
        if candidate in complete_list_of_candidates:
            complete_list_of_candidates[candidate] += 1
        else:
            complete_list_of_candidates[candidate] = 1
    
    def getList(dict):
        return dict.keys()

    #print the 4 names in a list, aka the count_of_candidates
    count_of_candidates = [key for key in complete_list_of_candidates]
    
    khan_count = (list_of_votes.count("Khan"))
    correy_count = (list_of_votes.count("Correy"))
    li_count = (list_of_votes.count("Li"))
    otooley_count = (list_of_votes.count("O'Tooley"))
    
    khan_avg = (khan_count)/len(list_of_votes)
    correy_avg = (correy_count)/len(list_of_votes)
    li_avg = (li_count)/len(list_of_votes)
    otooley_avg = (otooley_count)/len(list_of_votes)

    pypoll_hw = os.path.join("Resources", "pypoll_hw.csv")    

    with open(pypoll_hw, 'w') as csvfile:
        write_this = csv.writer(csvfile, delimiter=',')
        write_this.writerow(['Election Results'])
        write_this.writerow(['----------------------------'])
        write_this.writerow([(f'Total Votes: {(len(list_of_votes))}')])
        write_this.writerow(['----------------------------'])
        write_this.writerow([(f'Khan: {(khan_avg):.0%} {(khan_count)}')])
        write_this.writerow([(f'Correy: {(correy_avg):.0%} {(correy_count)}')])
        write_this.writerow([(f'Li: {(li_avg):.0%} {(li_count)}')])
        write_this.writerow([(f'OTooley: {(otooley_avg):.0%} {(otooley_count)}')])
        write_this.writerow(['----------------------------'])
        write_this.writerow([(f'Winner: Khan')])
        write_this.writerow(['----------------------------'])


