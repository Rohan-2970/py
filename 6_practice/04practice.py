username = input("Enter your username: ")

if not username:
    print("❌ Username cannot be empty.")
elif len(username) > 10:
    print("❌ Username is too long. Maximum 10 characters allowed.")
elif not username.isalpha():
    print("❌ Username should contain only letters (A-Z or a-z).")
else:
    print("✅ Username is valid:", username)
