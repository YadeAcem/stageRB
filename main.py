
def find_klinker(aantal,klinker):
    vraag = input("type uw zin AUB:")
    print(vraag)
    for i in range(len(vraag)):
        if vraag[i] in klinker:
            aantal += 1
    print("in uw zin zitten", aantal,"klinkers")

if __name__ == '__main__':
    klinker_lijst=["a","e","i","o","u"]
    aantal_klink = 0
    find_klinker(aantal_klink,klinker_lijst)

