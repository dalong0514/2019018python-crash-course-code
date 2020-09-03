from statistics import mean, stdev

def add_item_to_cart(new_item, shopper_name, existing_items=[]):
    existing_items.append(new_item)
    print(f"{shopper_name}'s cart has {existing_items}'")
    return existing_items

def add_item_to_cart_refactor(new_item, shopper_name, existing_items=None):
    if existing_items is None:
        existing_items = list()
    existing_items.append(new_item)
    print(f"{shopper_name}'s cart has {existing_items}'")
    return existing_items

def evaluate_test_result(scores):
    scores_mean = mean(scores)
    scores_std = stdev(scores)
    scores_s = stdev(scores)
    return scores_mean, scores_std, scores_s

if __name__ == "__main__":
    evaluate_result = evaluate_test_result([1, 2, 3, 4, 4, 7, 8])
    print(f"{evaluate_result}")