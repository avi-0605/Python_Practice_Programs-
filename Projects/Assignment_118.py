#Email Slicer Prompt the user for an email address, extract the username and domain, and display them.
def email_slicer():
    # Prompt the user to enter their email address
    email = input("Enter your email address: ")

    # Split the email into username and domain
    username, domain = email.split('@')

    # Display the username and domain
    print(f"Username: {username}")
    print(f"Domain: {domain}")

# Start the email slicer
email_slicer()
