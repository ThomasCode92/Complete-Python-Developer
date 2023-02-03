is_magician = False
is_expert = True

# Check if magician AND expert: "You are a master magician!"
if is_expert and is_magician:
    print("You are a master magician!")

# Check if magician but not expert: "At least you're getting there!"
elif is_magician and not is_expert:
    print("At least you're getting there!")

# Not a magician: "You need magic powers!"
elif not is_magician:
    print("You need magic powers!")
