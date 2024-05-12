# pip install num2words #
from num2words import num2words

number = int(input('Enter a number: '))

num_en = num2words(number, lang='en')
print(f'In english: {num_en}')

num_en_ord = num2words(number, lang='en', to='ordinal')
print(f'In english (ordinal): {num_en_ord}')

num_pt = num2words(number, lang='pt-br')
print(f'In portuguese: {num_pt}')

num_pt_ord = num2words(number, lang='pt-br', to='ordinal')
print(f'In portuguese (ordinal): {num_pt_ord}')
