
class Categories:
    
    def __init__(self):
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]

    def view(self):
        def view(l=self._categories, depth=0):
            for item in l:
                if(type(item) == str):
                    print("  "*depth, '-', item)
                else:
                    view(item, depth+1)
        view()


    def is_valid(self, target):
        return True if self.find_subcategories(target) else False

    
    def find_subcategories(self, target):
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(category, categories[index + 1], True)
            else:
                if categories == category or found:
                    yield categories

        return list(find_subcategories_gen(target, self._categories))

