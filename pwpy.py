import itertools
print(''' 
  ______         ______      
  | ___ \        | ___ \     
  | |_/ /_      _| |_/ /   _ 
  |  __/\ \ /\ / /  __/ | | |
  | |    \ V  V /| |  | |_| |
  \_|     \_/\_/ \_|   \__, |
                        __/ |
                       |___/ 
''')
print("[+] Insert the information about the victim to make a dictionary")
print("[+] If you don't know all the info, just hit enter when asked!" "\n")

key_words = ['-', '+', '_', '2015', '2016', '2017', '2018', '2019', '2020', '@', '.']
name = str(input('> Name:'))
nickname = str(input('> Nickname:'))
surname = str(input('> Surname:'))
birthday = str(input("> Birthdate (DD/MM/YYYY):"))

try:
    d, m, y = birthday.split('/')
except ValueError:
    d = ''
    m = ''
    y = ''


print("\n")
best_friend = str(input('> Girlfriend Name:'))
best_friend_nickname = str(input('> Girlfriend Nickname:'))
best_friend_birthdate = str(input('> Girlfriend Birthdate (DD/MM/YYYY):'))

try:
    d1, m1, y1 = best_friend_birthdate.split('/')

except ValueError:
    d1 = ''
    m1 = ''
    y1 = ''

print("\n")

phone_number = str(input('> Phone Number:'))
favorite_team = str(input('> Favorite Team:'))

words = [name, nickname, surname, d, m, y, best_friend, d1, m1, y1, best_friend_nickname, phone_number, favorite_team]

while("" in words):
   words.remove("")

password_list = []

print('\n')

xyz = input("Do you want to add some key words about the victim? Y/[N]:")

if xyz == 'y' or xyz == 'Y':
    password_list = words + key_words
else:
    password_list = words

min_length, max_length = 1, 4

for n in range(min_length, max_length+1):
    for xs in itertools.product(password_list, repeat=n):
        print(''.join(xs), file=open("passwords.txt", "a"))

print("\n")
print('[+] Now making a dictionary...')
print("[+] Sorting list and removing duplicates...")
print('[+] Saving dictionary to passwords.txt...')
print('[+] ! Good luck!')
