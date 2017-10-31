# Create Median function to calculate median of a list:
def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

#hand = input('Enter File: ')       # Open input file
#if len(fname) < 1: fname = 'Ad.txt'  (add the txt file later as an advertisement)
hand = open ('itcont1.txt')

# Create Output medianvals_by_zip.txt
clean_data = []
running_med = dict()                      # Running Median
total_dollar = dict()                     # Total Amount of Transactions
number_transaction = dict()               # Total Number of Transactions
amount_donated = dict ()                  # Individual Amount Donated

with open("medianvals_by_zip.txt", "w") as text_file:
    for line in hand:
        line=line.rstrip()
        field=line.split('|')
        # Only consider individual contributions, valid zip_code, valid recipient & valid amount:
        if field[15] == '' and len(field[10])>4 and field[0] != '' and field[14] != '':
            field = field
            field[10] = field[10][:5]      # Extract 5-digits zip-code
            clean_data = [field[0]+field[10], field[14]] # Create new list
        else:
            continue

        for d in clean_data:
            if d in number_transaction and len(d) > 6:
                number_transaction[d] = number_transaction[d] + 1
                total_dollar[d] = total_dollar[d] + int(field[14])
                amount_donated[d].append(int(field[14]))
                running_med[d] = median(amount_donated[d])
            elif len(d) > 6:
                number_transaction[d] = 1
                total_dollar[d] = int(field[14])
                amount_donated[d] = [int(field[14])]
                running_med[d] = median(amount_donated[d])
            else:
                continue
            print(d[:9],"|",d[9:],"|",round(running_med[d]),"|",number_transaction[d],"|",total_dollar[d], file=text_file)
text_file.close()

# Create Output medianvals_by_date.txt as date[13]|recipient[0]|total_number_trans|total_amount|median_contr
hand = open ('itcont1.txt')
second_data = []
total_num_trans = dict()       # Total Number of Transactions
total_amn_trans = dict()       # Total Amount of Transactions
median_con = dict()            # Running Median
med_lst = list()
with open("medianvals_by_date.txt", "w") as text_fil:
    for ln in hand:
        ln=ln.rstrip()
        fld=ln.split('|')
        if fld[15] == '' and len(fld[13])==8 and int(fld[13][:2])<13 and int(fld[13][2:4])<=31 and 2015 <= int(fld[13][4:]) <=2017 and fld[0] != '' and fld[14] != '':
            fld = fld
            second_data = [fld[0]+fld[13], fld[14]]
        else:
            continue

        for d in second_data:
            if d in total_num_trans and len(d) > 6:
                total_num_trans[d] = total_num_trans[d] + 1
                median_con[d].append(int(fld[14]))
                total_amn_trans[d] = total_amn_trans[d] + int(fld[14])
            elif len(d) > 6:
                total_num_trans[d] = 1
                total_amn_trans[d] = int(fld[14])
                median_con[d]=[int(fld[14])]
            else:
                continue
    for (k,v), (l,m), (n,p) in zip(total_num_trans.items(),total_amn_trans.items(),median_con.items()):
        print(k[:9],"|",k[9:],"|",round(median(p)),"|",v,"|",m, file=text_fil)
