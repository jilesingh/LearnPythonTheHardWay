# Start out with some users that need to be verified
# add an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brain', 'candace', 'Jile', 'lata']
confirmed_users = []

# Verify each user, until there are no more unconfirmed users
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
# Display all confirmed users.
print("\nThe following users ahs been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
