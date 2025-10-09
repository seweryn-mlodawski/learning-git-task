kaufen_list = {"piekarnii": ["chleb", "pączek","bułki"],
               "warzywniaku":["marchew", "seler", "rukola"]}

total_products = 0

for store, items in kaufen_list.items():
    print(f"Gdy będę w {store}, kupię: {items}")