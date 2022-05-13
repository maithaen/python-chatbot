
#Create chatbot
#%%
from nltk.chat.util import Chat, reflections
#['(.*)ຄຳຖາມ(.*)', ['ຄຳຕອບ1', 'ຄຳຕອບ2', 'ຄຳຕອບອື່ນໆ']] \\(.*) ສ່ວນຕໍ່ທ້າຍ
pairs = [
['ສະບາຍດີ(.*)', ['ເຈົ້າ', 'ໂດຍ', 'ມີຫຍັງໃຫ້ຊ່ວຍບໍ່']],
['ມີຫຍັງໃຫ້ຊ່ວຍ(.*)', ['ເຈົ້າ', 'ໂດຍ', 'ມີຫຍັງໃຫ້ຊ່ວຍບໍ່']],
['ເຮັດຫຫຍັງຢູ່(.*)', ['ນອນຫຼີ້ນ']]
]
chat = Chat(pairs, reflections)
#print(reflections)
chat.converse()


# %%
