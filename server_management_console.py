import os

# --- This is our "database" of servers ---
# We use a dictionary: the KEY is the server name, the VALUE is its status
servers = {
    "Web_Alpha": "Online",
    "DB_Storage": "Offline",
    "Mail_Relay": "Online"
}


# --- Sub-functions for each menu option ---

def view_all_servers():
    """Option 1: Shows every server and its current status."""
    print("\n---- CURRENT SERVER STATUS ----")
    for server_name, status in servers.items():
        print(f"[{server_name}]: {status}")


def change_server_status():
    """Option 2: Lets the user pick a server and change its status."""
    server_name = input("Which server name?: ")

    # Check if the server actually exists in our dictionary
    if server_name in servers:
        new_status = input("Enter new status: ")
        servers[server_name] = new_status          # Update the dictionary
        print(f"Task: Setting {server_name} to {new_status}..")
    else:
        print(f"Error: Server '{server_name}' not found.")


def add_new_server():
    """Option 3: Asks user for a new server name and starting status."""
    server_name = input("Enter new server name: ")
    initial_state = input("Enter initial state: ")
    servers[server_name] = initial_state           # Add it to the dictionary
    print(f"Server '{server_name}' added with status: {initial_state}")


def display_menu():
    """Helper function: just prints the menu to the screen."""
    print("\n" + "=" * 25)
    print(">>> SYSADMIN MENU <<<")
    print("1. View All Servers")
    print("2. Change Server Status")
    print("3. Add New Server")
    print("4. Exit")
    print("=" * 25)


# --- The Main "Manager" Function ---

def main():
    """Controls the loop and calls the right function based on user choice."""

    while True:                          # Keep showing the menu until user picks 4
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            view_all_servers()
        elif choice == '2':
            change_server_status()
        elif choice == '3':
            add_new_server()
        elif choice == '4':
            print("Exiting System. Goodbye!")
            break                        # This stops the while loop
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")


# --- This is the starting point of the program ---
if __name__ == "__main__":
    main()
