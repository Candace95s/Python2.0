import os

# --- Our "database" of servers ---
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
    if server_name in servers:
        new_status = input("Enter new status: ")
        servers[server_name] = new_status
        print(f"Task: Setting {server_name} to {new_status}..")
    else:
        print(f"Error: Server '{server_name}' not found.")


def add_new_server():
    """Option 3: Asks user for a new server name and starting status."""
    server_name = input("Enter new server name: ")
    initial_state = input("Enter initial state: ")
    servers[server_name] = initial_state
    print(f"Server '{server_name}' added with status: {initial_state}")


def exit_program():
    """Option 4: Exits the program."""
    print("Exiting System. Goodbye!")


def display_menu():
    """Helper function: prints the menu to the screen."""
    print("\n" + "=" * 25)
    print(">>> SYSADMIN MENU <<<")
    print("1. View All Servers")
    print("2. Change Server Status")
    print("3. Add New Server")
    print("4. Exit")
    print("=" * 25)


# --- JUMP TABLE ---
# Instead of a long if/elif chain, we map each menu choice
# directly to the function that handles it.
# This makes runCommand() very simple and clean!
jump_table = {
    '1': view_all_servers,
    '2': change_server_status,
    '3': add_new_server,
    '4': exit_program
}


def runCommand(choice):
    """
    Looks up the user's choice in the jump table and calls
    the matching function. No if/elif needed!
    """
    if choice in jump_table:
        jump_table[choice]()          # Look up and call the function
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")


# --- The Main "Manager" Function ---

def main():
    """Controls the loop and calls runCommand() for every choice."""
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        runCommand(choice)            # runCommand handles everything now!

        if choice == '4':
            break                     # Stop the loop when user picks Exit


# --- Starting point of the program ---
if __name__ == "__main__":
    main()
