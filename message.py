import pywhatkit as WA
from logo import Logo

def display_menu():
    print(Logo)
    print("Welcome to the WhatsApp Automation Tool\n")
    print("1. Send Message To Contact")
    print("2. Send Message To Group")
    print("3. Send Image To Group/Contact")
    print("4. Exit")

def msg_to_contact():
    ph = input("Enter Phone Number: ")
    msg = input("Enter your message: ")
    WA.sendwhatmsg_instantly(phone_no=ph,message=msg,tab_close=True)

def msg_to_grp():
    grp_name = input("Enter Group name: ")
    grp_msg = input("Enter message: ")
    WA.sendwhatmsg_to_group_instantly(group_id=grp_name,message=grp_msg,tab_close=True)

def send_img():
    ph = input("Enter Phone Number / Group name: ")
    img = input("Enter image path: ")
    caption = input("Enter image caption: ")
    WA.sendwhats_image(receiver=ph,img_path=img,caption=caption,tab_close=True)

while True:
    display_menu()
    choice = input("Enter Your Choice: ")
    if choice == '1':
        msg_to_contact()
    elif choice == '2':
        msg_to_grp()
    elif choice == '3':
        send_img()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
    



