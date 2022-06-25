# Interactive Scientific Calculator

- We will build an interactive scientific calculator that will have a `user menu` and `11 math operations` that the user can choose from.
- Also after performing each operation the user will be asked if he or she would like to either return.
- At first we're telling the user to `choose the desired math operation` to perform and then using a different number or identifier for each operation the user has `11 options` to choose from `addition` `subtraction` `multiplication` `division` `modulo raising to a power` `square root` `logarithm sine cosign and tangent` after showing the user all the available options.
- We then ask him or her to `enter an option at the prompt`: here the user can type in any option from `0 to 10` inclusively and then hitting the enter key is required to continue.
- However if for some reason the user types in another number or in fact anything else besides `0` or `1` or `2` and `so on` then we should handle this scenario as well.
- let's say the user types in `11` by mistake. In this case he gets an error message in return `invalid option`. Then he is redirected back to the main menu.
- Now let's say that the user wants to perform a `division operation` or he has to do is type in the corresponding number. In this case `3` and hit enter. Next we're asking the user for the `first value` meaning the `numerator` or in plain English the number we want to divide.
- Let's say `five` after hitting enter. We're asking the user to input the `denominator or the number to divide 5` by let's say `two` immediately after hitting enter once again the result is printed out to the screen `2.5` which is correct.
- Finally we're asking the user if he would like to go back to the main menu and perform another math operation or simply quit the program if he types in `y` for `yes` then he agrees to return to the `main menu`. Otherwise by typing `n` for `no` the execution of the program ends.


# Turn your script to windows executable file

    ## Windows `exe` file
    
    - You will need to ensure that your scientific calculator does not have any errors
    - You will need to `pip install` the [pyinstaller](https://pyinstaller.org/en/stable/installation.html)
    - Then you will open your `cmd` by ranning as administrator
    - Navigate to the folder where you have your `script scinetific calculator`
    - You will need to ran `pyinstaller --onefile <name of your scientific calculator script>
    - After a while the `executable` will be created and it will be in the `dist folder`
    - Now you can ran your `exe` file.
