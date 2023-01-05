# Créez une liste des articles disponibles dans le magasin et leur price
articles = {
    "Apple": 2.50,
    "Mangoe": 0.50,
    "Banana": 1.50,
    "Water": 3.00,
    "Yogourt": 0.75,
    "Orange": 0.75,
    "Pineapple": 0.50,
    "Papaya": 4.50,
    "Tee-Shirt": 12.8
}

# Input your wallet amount
wallet = float(input("Input your wallet amount : "))

# Create a empty list
shopping = []

for article, price in articles.items():
  if wallet >= price:
    shopping.append(article)
    wallet -= price

# Short the list of items

shopping.sort()

# Print the shopping's list
if shopping:
  print("You can buy :")
  for article in shopping:
    print(article)
else:
  print("Enough money to buy something")