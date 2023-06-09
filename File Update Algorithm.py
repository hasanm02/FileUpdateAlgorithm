# In this lab, you're working as a security analyst and you're responsible for developing an algorithm that parses a file containing IP addresses that are allowed to access restricted content and removes addresses that no longer have access.
# Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`
# and combines the steps you've written in this lab leading up to this
def update_file(import_file, remove_list):

  # Build `with` statement to read in the initial contents of the file
    with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
        ip_addresses = file.read()

  # Use `.split()` to convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()

  # Build iterative statement
  # Name loop variable `element`
  # Loop through `remove_list`
    for element in remove_list:

    # use the `.remove()` method to remove
    # elements from `ip_addresses`
        ip_addresses.remove(element)

  # Convert `ip_addresses` back to a string so that it can be written into the text file
    ip_addresses = " ".join(ip_addresses)

  # Build `with` statement to rewrite the original file
    with open(import_file, "w") as file:

    # Rewrite the file, replacing its contents with `ip_addresses`
        file.write(ip_addresses)

# Call `update_file()` and pass in "allow_list.txt" and a list of IP addresses to be removed
update_file("data/allow_list.txt", ["192.168.25.60", "192.168.90.124", "192.168.60.153"])

# Build `with` statement to read in the updated file
with open("data/allow_list.txt", "r") as file:

  # Read in the updated file and store the contents in `text`
    text = file.read()

# Display the contents of `text`
print(text)
