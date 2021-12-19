
# name = input('enter your name: ')
# result = "my name is : " + name
# print(result)

# scores = [90, 87, 77, 22]
# scores.append(55)
# scores.pop()
# print(scores[len(scores) - 1])

# identity = {
#     "nama": "risky",
#     "umur": 15,
#     "isWorking": True
# }
# identity2 = {
#     "nama": "risky",
#     "umur": 15,
#     "isWorking": True
# }
# identity3 = {
#     "nama": "risky",
#     "umur": 15,
#     "isWorking": True
# }

# identity["nama"] = "ibnu"

# identity["address"] = "Jl. H. Taiman"

# result = "Hi my name is " + identity["nama"] +". umur saya " + str(identity["umur"])

# print(identity)
# print(result)


identities = [
    {
        "nama": "Risky",
        "laptop": "Macbook"
    },
    {
        "nama": "Ibnu",
        "laptop": "Asus"
    },
    {
        "nama": "Michael",
        "laptop": "Acer"
    },
]
# print(identities[1])

identities[1] = {
    "nama": ["Erno", "Nugraha"],
    "laptop": "Dell"
}
# identities.append({})
print(identities[1]["nama"][0])

products = []

#read
print(products)

#create
products.append({
        "name": "pengharum",
        "price": 20000
    })

#update
products[0] = {
    "name": "Smartphone",
    "price": 15000
}

#delete
products.pop()