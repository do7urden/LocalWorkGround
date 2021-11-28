import os

print(os.getcwd())
print("******************* Walk directory tree ******************")
# Aşağıdaki kodlar için ilgili klasörleri kendi sisteminize göre düzeltmeniz gerekir
all_file_names = []
for elm in os.walk(r"C:\Users\Core_Machine\Documents\pyCharmProjects\LocalWorkGround"):
    print(elm)
    # if ".git" not in elm[0]:
    #     all_file_names += elm[2]
    #     # all_file_names = all_file_names.union(set(elm[2]))