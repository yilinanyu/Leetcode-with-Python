def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return " ".join(output)

# Remove duplicates from this list.
values = "abssbsbsbs"
result = remove_duplicates(values)
print(result)