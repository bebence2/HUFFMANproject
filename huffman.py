import huffmanencode as en
import huffmandecode as de
import keyboard as k
import os
import time

print("Select what you want to do:")
showmenu = True

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')




def show_menu(selected_option):
    clear_console()
    options = ["Encode", "Decode"]
    for i, option in enumerate(options, start=1):
        if i == selected_option:
            print(f"> {option} <")
        else:
            print(f"  {option}")





def handle_encode(input_path, output_path):
    print("\nEncoding...")
    en.encode(input_path, output_path)
    print("Encoding complete.")
    input("\nPress Enter to return to menu.")
    time.sleep(1)

def handle_decode(input_path, output_path):
    print("\nDecoding...")
    de.decode(input_path, output_path)
    print("Decoding complete.")
    input("\nPress Enter to return to menu.")
    time.sleep(1)





def get_input_path():
    time.sleep(0.3)
    input_path = input("Insert the source file path:\n> ").strip()
    return input_path.strip()

def get_output_path():
    output_path = input("Insert the output file path:\n> ").strip()
    return output_path.strip()


selectedoption = 1
inputpath = ""
outputpath = ""



def run_menu():
    selected_option = 1
    show_menu(selected_option)
    global showmenu
    while showmenu == True:
        if k.is_pressed("down") and selected_option < 2 :
            selected_option += 1
            show_menu(selected_option)

        elif k.is_pressed("up") and selected_option > 1 :
            selected_option -= 1
            show_menu(selected_option)

        elif k.is_pressed("enter"):
            input().strip()
            clear_console()
            time.sleep(1)
            input_path=get_input_path()
            output_path = (lambda selected_option: "encoded.txt" if selected_option == 1 else "decoded.txt")(selected_option)
            

            if selected_option == 1:
                handle_encode(input_path, output_path)
            elif selected_option == 2:
                handle_decode(input_path, output_path)

            show_menu(selected_option)
        elif k.is_pressed("escape"):
            showmenu = False


if __name__ == "__main__":
    try:
        run_menu()
    except KeyboardInterrupt:
        print("\nProgram exited.")