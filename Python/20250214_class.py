class Cat:
    pass

cat = Cat()
another_cat = Cat()

cat.name = "Tama"
cat.nemesis = another_cat
another_cat.name = "Jiro"

print("cat name: " + cat.name)
print("cat nemesis name: " + cat.nemesis.name)
