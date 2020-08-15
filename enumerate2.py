def skip_elements(elements):
  elements = [v for i, v in enumerate(elements) if i % 2 == 0]

  return elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) 

# Print values with even index
# ['a', 'c', 'e', 'g']
# ['Orange', 'Strawberry', 'Peach']
