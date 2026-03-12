import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Possible choices
choices = ["Rock", "Paper", "Scissors"]

# Score tracking
user_score = 0
comp_score = 0

# Function to play a round
def play(user_choice):
    global user_score, comp_score

    # Computer choice
    comp_choice = random.choice(choices)

    # Display choices
    label_user_choice.config(text=f"You chose: {user_choice}")
    label_comp_choice.config(text=f"Computer chose: {comp_choice}")

    # Determine winner
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        comp_score += 1

    # Update result and score
    label_result.config(text=result)
    label_score.config(text=f"Score — You: {user_score}  Computer: {comp_score}")

# Labels
label_title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
label_title.pack(pady=10)

label_user_choice = tk.Label(root, text="", font=("Arial", 12))
label_user_choice.pack()

label_comp_choice = tk.Label(root, text="", font=("Arial", 12))
label_comp_choice.pack()

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_result.pack(pady=10)

label_score = tk.Label(root, text="Score — You: 0  Computer: 0", font=("Arial", 12))
label_score.pack(pady=5)

# Buttons for user to choose
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_rock = tk.Button(frame_buttons, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(frame_buttons, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(frame_buttons, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.grid(row=0, column=2, padx=5)

root.mainloop()
