print("=======================")
print("    INFO DATA SALDO    ")
print("=======================")



with open('saldo.txt', 'r') as f:
    states_list = [line.strip() for line in f.readlines()]
for state in sorted(states_list):
    print(state)
