weather=input("What's the weather like today?(sunny/rainy/cold):").strip().lower()
if weather=="sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather=="rainy":
    print("Dont forget your umbrella and a raincoat.")
elif weather=="cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry. I dont have recommendations for this weather.")
